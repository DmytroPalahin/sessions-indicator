"""Tests for tools/check.py.

Each check is a pure function from source lines to a list of problems, so the tests
feed it a few lines and look at what comes back. The last tests run the whole
script: once against this repository, which must pass, and once against a broken
copy, which must not.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from tools import check

if TYPE_CHECKING:
    from pathlib import Path

GOOD_HEADER = [
    check.LICENSE_LINE,
    "// © someone",
    "",
    "//@version=6",
    'indicator("Some Indicator", "Short", overlay = true)',
]


# -----------------------------------------------------------------------------
# strip_code
# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ("x = 1 // a comment", "x = 1 "),
        ('s = "a (b" // tail', 's = "    " '),
        ("s = 'it // stays'", "s = '           '"),
        (r's = "a \" b"', 's = "      "'),
        ("// only a comment", ""),
        ("plain(code)", "plain(code)"),
    ],
)
def test_strip_code_blanks_strings_and_drops_comments(line: str, expected: str):
    assert check.strip_code(line) == expected


# -----------------------------------------------------------------------------
# header and titles
# -----------------------------------------------------------------------------
def test_header_accepts_a_complete_header():
    assert check.check_header(GOOD_HEADER) == []


@pytest.mark.parametrize(
    ("lines", "fragment"),
    [
        (["// something else", *GOOD_HEADER[1:]], "license notice"),
        ([GOOD_HEADER[0], "// no copyright", *GOOD_HEADER[2:]], "copyright notice"),
        ([GOOD_HEADER[0]], "copyright notice"),
        ([*GOOD_HEADER[:3], "//@version=5", GOOD_HEADER[4]], "//@version=6"),
        (GOOD_HEADER[:4], "must call indicator()"),
        (
            [*GOOD_HEADER[:3], GOOD_HEADER[4], GOOD_HEADER[3]],
            "must come before indicator()",
        ),
    ],
)
def test_header_reports_what_is_missing(lines: list[str], fragment: str):
    assert any(fragment in problem for problem in check.check_header(lines))


def test_header_of_an_empty_file_lists_every_problem():
    assert len(check.check_header([])) == 4


def test_titles_accept_a_short_title_within_the_limit():
    assert check.check_titles(['indicator("Long Enough Title", "TenLetters")']) == []


def test_titles_reject_a_short_title_over_the_limit():
    problems = check.check_titles(['indicator("Title", "ElevenChars")'])
    assert problems == ['short title "ElevenChars" is 11 characters, the limit is 10']


@pytest.mark.parametrize("lines", [[], ['indicator("Only a title")']])
def test_titles_need_a_title_and_a_short_title(lines: list[str]):
    assert check.check_titles(lines) == [
        "indicator() must have a title and a short title"
    ]


# -----------------------------------------------------------------------------
# whitespace, indentation, brackets, regions
# -----------------------------------------------------------------------------
def test_whitespace_accepts_clean_text():
    assert check.check_whitespace("a\n    b\n", ["a", "    b"]) == []


def test_whitespace_reports_every_kind_of_problem():
    raw = "a\r\n\tb \nc"
    problems = check.check_whitespace(raw, ["a\r", "\tb ", "c"])
    assert "the file must use LF line endings" in problems
    assert "the file must end with a newline" in problems
    assert "line 2: tab character" in problems
    assert "line 2: trailing whitespace" in problems


def test_indentation_allows_multiples_of_four_and_blank_lines():
    assert check.check_indentation(["a", "    b", "        c", "", "   "]) == []


def test_indentation_rejects_a_wrapped_line():
    problems = check.check_indentation(["call(a,", "     b)"])
    assert len(problems) == 1
    assert problems[0].startswith("line 2: indentation of 5 spaces")


@pytest.mark.parametrize(
    "line",
    [
        "f(a[1], {b})",
        'label.new(x, y, "text with ) and [")',
        "x = 1 // a comment with ( in it",
    ],
)
def test_brackets_accept_balanced_lines(line: str):
    assert check.check_brackets([line]) == []


@pytest.mark.parametrize(
    ("line", "problem"),
    [
        ("f(a, b", "line 1: missing ')' (lines are not wrapped in this project)"),
        ("a + b)", "line 1: unexpected ')'"),
        ("f(a]", "line 1: unexpected ']'"),
    ],
)
def test_brackets_report_the_first_mismatch(line: str, problem: str):
    assert check.check_brackets([line]) == [problem]


def test_regions_accept_closed_regions():
    lines = ["//#region A", "x = 1", "//#endregion", "//#region B", "//#endregion"]
    assert check.check_regions(lines) == []


@pytest.mark.parametrize(
    ("lines", "problem"),
    [
        (
            ["//#region A", "//#region B", "//#endregion"],
            "line 2: region opened inside the region of line 1",
        ),
        (["//#endregion"], "line 1: //#endregion without //#region"),
        (["x = 1", "//#region A"], "line 2: region is never closed"),
    ],
)
def test_regions_report_broken_markers(lines: list[str], problem: str):
    assert check.check_regions(lines) == [problem]


# -----------------------------------------------------------------------------
# inputs, names, plots
# -----------------------------------------------------------------------------
def test_inline_inputs_allow_one_title_per_row():
    lines = [
        'bool a = input.bool(true, "Show", inline = "row", group = G_ONE)',
        'int  b = input.int(1, "", inline = "row", group = G_ONE)',
        'bool c = input.bool(true, "Show", inline = "row", group = G_TWO)',
        'bool d = input.bool(true, "No row at all", group = G_ONE)',
    ]
    assert check.check_inline_inputs(lines) == []


def test_inline_inputs_reject_a_second_title_in_a_row():
    lines = [
        'bool a = input.bool(true, "Show", inline = "row", group = G_ONE)',
        'int  b = input.int(1, "Width", inline = "row", group = G_ONE)',
    ]
    problems = check.check_inline_inputs(lines)
    assert len(problems) == 1
    assert 'line 2: input "Width" is not first in inline row "row"' in problems[0]


def test_unique_names_accept_distinct_functions_and_methods():
    lines = [
        "fmtSpan(float span) =>",
        "method advance(Tracker this) =>",
        "x = 1",
    ]
    assert check.check_unique_names(lines) == []


def test_unique_names_reject_a_second_definition():
    lines = ["method place(Marker this) =>", "", "place(int x) =>"]
    problems = check.check_unique_names(lines)
    assert len(problems) == 1
    assert problems[0].startswith("line 3: 'place' is already defined on line 1")


def test_unique_names_reject_the_name_of_a_builtin_method():
    problems = check.check_unique_names(["method put(Level this) =>"])
    assert len(problems) == 1
    assert "'put' is the name of a built-in method" in problems[0]


def test_plot_budget_counts_calls_but_not_comments():
    lines = ["plot(close)"] * check.PLOT_LIMIT + ["// plot(open)", "x = plot_count"]
    assert check.check_plot_budget(lines) == []


def test_plot_budget_rejects_one_call_too_many():
    lines = ["plot(close)"] * check.PLOT_LIMIT + ["    bgcolor(color.red)"]
    assert check.check_plot_budget(lines) == [
        f"{check.PLOT_LIMIT + 1} plot-like calls, the limit is {check.PLOT_LIMIT}"
    ]


# -----------------------------------------------------------------------------
# version
# -----------------------------------------------------------------------------
@pytest.fixture
def release_files(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """A README and a changelog that agree on version 1.2.3, in a temporary folder."""
    readme = tmp_path / "README.md"
    readme.write_text("![v](https://img.shields.io/badge/version-1.2.3-blue)\n")
    changelog = tmp_path / "CHANGELOG.md"
    changelog.write_text("# Changelog\n\n## [1.2.3] - 2026-01-01\n")
    monkeypatch.setattr(check, "README_FILES", (readme, tmp_path / "README.ru.md"))
    monkeypatch.setattr(check, "CHANGELOG", changelog)
    return tmp_path


def test_version_agrees_across_the_script_readme_and_changelog(release_files: Path):
    assert check.check_version(['const string VERSION   = "1.2.3"']) == []


def test_version_must_be_declared_in_the_script(release_files: Path):
    assert check.check_version(["x = 1"]) == [
        'the script must declare: const string VERSION = "X.Y.Z"'
    ]


def test_version_reports_a_stale_badge(release_files: Path):
    problems = check.check_version(['const string VERSION = "1.2.4"'])
    assert "README.md: the version badge does not show 1.2.4" in problems
    assert "CHANGELOG.md has no entry for 1.2.4" in problems


def test_version_may_wait_under_unreleased(release_files: Path):
    (release_files / "README.md").write_text("badge/version-1.2.4-blue\n")
    (release_files / "CHANGELOG.md").write_text("## [Unreleased]\n\n## [1.2.3]\n")
    assert check.check_version(['const string VERSION = "1.2.4"']) == []


def test_version_needs_a_changelog_with_headings(release_files: Path):
    (release_files / "CHANGELOG.md").write_text("# Changelog\n")
    assert check.check_version(['const string VERSION = "1.2.3"']) == [
        "CHANGELOG.md has no version headings"
    ]
    (release_files / "CHANGELOG.md").unlink()
    assert check.check_version(['const string VERSION = "1.2.3"']) == [
        "CHANGELOG.md is missing"
    ]


# -----------------------------------------------------------------------------
# documentation links
# -----------------------------------------------------------------------------
def test_doc_links_resolve_relative_targets(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    (tmp_path / "docs" / "images").mkdir(parents=True)
    (tmp_path / "docs" / "images" / "chart.png").write_bytes(b"png")
    (tmp_path / "docs" / "GUIDE.md").write_text(
        "![chart](images/chart.png) and [the readme](../README.md#top)\n"
    )
    (tmp_path / "README.md").write_text(
        "[guide](docs/GUIDE.md), [site](https://example.com), [top](#top),\n"
        '<img src="docs/images/chart.png"> <a href="mailto:a@example.com">mail</a>\n'
    )
    monkeypatch.setattr(check, "ROOT", tmp_path)
    assert check.check_doc_links() == []


def test_doc_links_report_missing_targets(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    (tmp_path / "README.md").write_text(
        'first line\n[gone](docs/GONE.md)\n<img src="missing.png">\n'
    )
    monkeypatch.setattr(check, "ROOT", tmp_path)
    assert check.check_doc_links() == [
        "README.md:2: link target not found: docs/GONE.md",
        "README.md:3: link target not found: missing.png",
    ]


# -----------------------------------------------------------------------------
# report and the script as a whole
# -----------------------------------------------------------------------------
def test_report_counts_and_prints_each_check(capsys: pytest.CaptureFixture[str]):
    report = check.Report()
    report.check("first", [])
    report.check("second", ["something is wrong"])
    output = capsys.readouterr().out
    assert report.passed == 1
    assert report.failures == ["second"]
    assert "ok    first" in output
    assert "FAIL  second" in output
    assert "something is wrong" in output


def test_report_shortens_a_long_list_of_problems(capsys: pytest.CaptureFixture[str]):
    problems = [f"problem {n}" for n in range(check.PROBLEMS_SHOWN + 5)]
    check.Report().check("many", problems)
    output = capsys.readouterr().out
    assert f"problem {check.PROBLEMS_SHOWN - 1}" in output
    assert f"problem {check.PROBLEMS_SHOWN}" not in output
    assert "... and 5 more" in output


def test_main_passes_on_this_repository(capsys: pytest.CaptureFixture[str]):
    assert check.main() == 0
    assert "checks passed" in capsys.readouterr().out


def test_main_fails_on_a_broken_source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
):
    broken = tmp_path / "broken.pine"
    broken.write_text("//@version=5\nplot(close")
    monkeypatch.setattr(check, "SOURCE", broken)
    assert check.main() == 1
    output = capsys.readouterr().out
    assert "FAIL  header" in output
    assert "FAIL  brackets" in output
    assert "the file must end with a newline" in output
    assert "check(s) failed" in output


def test_main_fails_when_the_source_is_missing(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
):
    monkeypatch.setattr(check, "SOURCE", tmp_path / "nowhere.pine")
    assert check.main() == 1
    assert "source file not found" in capsys.readouterr().out
