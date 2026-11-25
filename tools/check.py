#!/usr/bin/env python3
"""Static checks for the indicator source.

Pine Script can only be compiled by TradingView, so this script cannot prove that the code compiles.
It catches what can be caught offline: the mistakes that are cheap to make and that TradingView
reports as errors or warnings, plus the conventions of this repository.

Usage:
    python3 tools/check.py

Exit code 0 means every check passed. Only the Python standard library is used.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "src" / "custom_sessions_indicator.pine"
README_FILES = (ROOT / "README.md", ROOT / "README.ru.md")
CHANGELOG = ROOT / "CHANGELOG.md"

LICENSE_LINE = (
    "// This Pine Script® code is subject to the terms of the Mozilla Public License 2.0 "
    "at https://mozilla.org/MPL/2.0/"
)
SHORT_TITLE_MAX = 10  # TradingView warns above this (SHORT_TITLE_TOO_LONG)
PLOT_LIMIT = 64  # maximum number of plot-like outputs of one script
PLOT_CALLS = ("plot", "bgcolor", "plotshape", "plotchar", "plotarrow", "hline", "fill", "barcolor", "alertcondition")

BRACKETS = {"(": ")", "[": "]", "{": "}"}

# Names of built-in Pine methods. A user function with one of these names is an overload of the built-in.
BUILTIN_METHODS = frozenset(
    "abs avg binary_search clear concat contains copy covariance delete every fill first get includes indexof insert "
    "join keys last lastindexof max median min mode percentrank pop push put put_all range remove reverse set shift "
    "size slice some sort sort_indices standardize stdev sum unshift values variance".split()
)


class Report:
    """Collects failures and prints one line per check."""

    def __init__(self) -> None:
        self.failures: list[str] = []
        self.passed = 0

    def check(self, name: str, problems: list[str]) -> None:
        if problems:
            print(f"FAIL  {name}")
            for problem in problems[:20]:
                print(f"        {problem}")
            if len(problems) > 20:
                print(f"        ... and {len(problems) - 20} more")
            self.failures.append(name)
        else:
            print(f"ok    {name}")
            self.passed += 1


def strip_code(line: str) -> str:
    """Returns the line with string contents blanked and the trailing comment removed."""
    out: list[str] = []
    quote = ""
    i = 0
    while i < len(line):
        ch = line[i]
        if quote:
            if ch == "\\":
                out.append("  ")
                i += 2
                continue
            if ch == quote:
                quote = ""
                out.append(ch)
            else:
                out.append(" ")
        elif ch in "\"'":
            quote = ch
            out.append(ch)
        elif line.startswith("//", i):
            break
        else:
            out.append(ch)
        i += 1
    return "".join(out)


def check_header(lines: list[str]) -> list[str]:
    problems = []
    if not lines or lines[0] != LICENSE_LINE:
        problems.append("line 1 must be the MPL-2.0 license notice")
    if len(lines) < 2 or not lines[1].startswith("// ©"):
        problems.append("line 2 must be the copyright notice (// © ...)")
    version_at = next((n for n, text in enumerate(lines) if text.startswith("//@version=")), None)
    indicator_at = next((n for n, text in enumerate(lines) if text.startswith("indicator(")), None)
    if version_at is None or lines[version_at] != "//@version=6":
        problems.append("the script must declare //@version=6")
    if indicator_at is None:
        problems.append("the script must call indicator()")
    elif version_at is not None and indicator_at < version_at:
        problems.append("//@version=6 must come before indicator()")
    return problems


def check_titles(lines: list[str]) -> list[str]:
    problems = []
    call = next((text for text in lines if text.startswith("indicator(")), "")
    strings = re.findall(r'"([^"]*)"', call)
    if len(strings) < 2:
        return ["indicator() must have a title and a short title"]
    if len(strings[1]) > SHORT_TITLE_MAX:
        problems.append(f'short title "{strings[1]}" is {len(strings[1])} characters, the limit is {SHORT_TITLE_MAX}')
    return problems


def check_whitespace(raw: str, lines: list[str]) -> list[str]:
    problems = []
    if "\r" in raw:
        problems.append("the file must use LF line endings")
    if not raw.endswith("\n"):
        problems.append("the file must end with a newline")
    for number, text in enumerate(lines, 1):
        if "\t" in text:
            problems.append(f"line {number}: tab character")
        if text != text.rstrip():
            problems.append(f"line {number}: trailing whitespace")
    return problems


def check_indentation(lines: list[str]) -> list[str]:
    problems = []
    for number, text in enumerate(lines, 1):
        if not text.strip():
            continue
        indent = len(text) - len(text.lstrip(" "))
        if indent % 4:
            problems.append(f"line {number}: indentation of {indent} spaces (use multiples of 4, do not wrap lines)")
    return problems


def check_brackets(lines: list[str]) -> list[str]:
    problems = []
    for number, text in enumerate(lines, 1):
        stack: list[str] = []
        for ch in strip_code(text):
            if ch in BRACKETS:
                stack.append(BRACKETS[ch])
            elif ch in BRACKETS.values():
                if not stack or stack.pop() != ch:
                    problems.append(f"line {number}: unexpected '{ch}'")
                    stack = []
                    break
        if stack:
            problems.append(f"line {number}: missing '{stack[-1]}' (lines are not wrapped in this project)")
    return problems


def check_regions(lines: list[str]) -> list[str]:
    problems = []
    open_at = 0
    for number, text in enumerate(lines, 1):
        if text.startswith("//#region"):
            if open_at:
                problems.append(f"line {number}: region opened inside the region of line {open_at}")
            open_at = number
        elif text.startswith("//#endregion"):
            if not open_at:
                problems.append(f"line {number}: //#endregion without //#region")
            open_at = 0
    if open_at:
        problems.append(f"line {open_at}: region is never closed")
    return problems


def check_inline_inputs(lines: list[str]) -> list[str]:
    """In an inline row only the first input may have a title (TradingView warning CW10026)."""
    rows: dict[tuple[str, str], list[tuple[int, str]]] = defaultdict(list)
    pattern = re.compile(r"=\s*input\.\w+\(\s*[^,]+,\s*\"([^\"]*)\"")
    for number, text in enumerate(lines, 1):
        code = text.split("//")[0] if text.lstrip().startswith("//") else text
        match = pattern.search(code)
        inline = re.search(r'inline\s*=\s*"([^"]*)"', code)
        group = re.search(r"group\s*=\s*(\w+)", code)
        if match and inline:
            rows[(group.group(1) if group else "", inline.group(1))].append((number, match.group(1)))
    problems = []
    for (group, inline), members in rows.items():
        for number, title in members[1:]:
            if title:
                problems.append(f'line {number}: input "{title}" is not first in inline row "{inline}" and must have an empty title')
    return problems


def check_unique_names(lines: list[str]) -> list[str]:
    """An overloaded function may not read global variables (TradingView error CE10182)."""
    seen: dict[str, int] = {}
    problems = []
    for number, text in enumerate(lines, 1):
        match = re.match(r"(?:method\s+)?(\w+)\(.*\)\s*=>", text)
        if not match:
            continue
        name = match.group(1)
        if name in seen:
            problems.append(f"line {number}: '{name}' is already defined on line {seen[name]} (overloads cannot read globals)")
        elif name in BUILTIN_METHODS:
            problems.append(f"line {number}: '{name}' is the name of a built-in method, which makes this an overload")
        seen.setdefault(name, number)
    return problems


def check_plot_budget(lines: list[str]) -> list[str]:
    count = 0
    for text in lines:
        code = strip_code(text).lstrip()
        if any(code.startswith(name + "(") for name in PLOT_CALLS):
            count += 1
    if count > PLOT_LIMIT:
        return [f"{count} plot-like calls, the limit is {PLOT_LIMIT}"]
    return []


def check_version(lines: list[str]) -> list[str]:
    problems = []
    declared = next((re.search(r'"(\d+\.\d+\.\d+)"', text) for text in lines if text.startswith("const string VERSION")), None)
    if not declared:
        return ['the script must declare: const string VERSION = "X.Y.Z"']
    version = declared.group(1)
    for readme in README_FILES:
        if readme.exists() and f"version-{version}-" not in readme.read_text(encoding="utf-8"):
            problems.append(f"{readme.name}: the version badge does not show {version}")
    if CHANGELOG.exists():
        headings = re.findall(r"^## \[([^\]]+)\]", CHANGELOG.read_text(encoding="utf-8"), flags=re.MULTILINE)
        if not headings:
            problems.append("CHANGELOG.md has no version headings")
        elif version not in headings and headings[0] != "Unreleased":
            problems.append(f"CHANGELOG.md has no entry for {version}")
    else:
        problems.append("CHANGELOG.md is missing")
    return problems


def main() -> int:
    if not SOURCE.exists():
        print(f"FAIL  source file not found: {SOURCE}")
        return 1
    raw = SOURCE.read_bytes().decode("utf-8")
    lines = raw.split("\n")
    if lines and lines[-1] == "":
        lines.pop()

    report = Report()
    report.check("header: license, copyright, //@version=6, indicator()", check_header(lines))
    report.check("titles: short title within the TradingView limit", check_titles(lines))
    report.check("whitespace: LF endings, no tabs, no trailing spaces", check_whitespace(raw, lines))
    report.check("indentation: multiples of four, no wrapped lines", check_indentation(lines))
    report.check("brackets: balanced on every line", check_brackets(lines))
    report.check("regions: every //#region is closed", check_regions(lines))
    report.check("inputs: inline rows have one title", check_inline_inputs(lines))
    report.check("names: every function and method has its own name", check_unique_names(lines))
    report.check("plots: within the limit of plot-like calls", check_plot_budget(lines))
    report.check("version: script, README badges and changelog agree", check_version(lines))

    print()
    if report.failures:
        print(f"{len(report.failures)} check(s) failed, {report.passed} passed.")
        return 1
    print(f"All {report.passed} checks passed ({len(lines)} lines).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
