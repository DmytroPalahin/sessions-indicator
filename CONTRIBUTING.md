# Contributing

Thank you for helping. This guide tells you how to report a problem, propose an idea and send a change.

## Ways to contribute

| You want to | Do this |
| ------------- | --------- |
| Report a bug | [Open a bug report](https://github.com/DmytroPalahin/sessions-indicator/issues/new/choose). Include the symbol, the timeframe and a screenshot. |
| Propose a feature | [Open a feature request](https://github.com/DmytroPalahin/sessions-indicator/issues/new/choose). Describe the trading need first, the solution second. |
| Fix or build something | Open an issue first if the change is larger than a small fix, then send a pull request. |
| Improve the docs | Send a pull request directly. |

## Development setup

You need a TradingView account (the free plan is enough) and [uv](https://docs.astral.sh/uv/) for the tools.

```bash
git clone https://github.com/DmytroPalahin/sessions-indicator.git
```

```bash
cd sessions-indicator
```

```bash
uv sync
```

`uv sync` installs the Python version named in `pyproject.toml` and the tools pinned in `uv.lock` into `.venv`.
Then:

```bash
uv run tools/check.py
```

The check script uses the standard library only, so `python3 tools/check.py` works without uv as well.

The loop while developing:

1. Edit [src/custom_sessions_indicator.pine](src/custom_sessions_indicator.pine) in your editor.
2. Run `uv run tools/check.py`.
3. Paste the file into the TradingView Pine Editor and press **Add to chart**.
4. Walk through the relevant rows of [docs/TESTING.md](docs/TESTING.md).

Read [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) before the first change. It is short and it explains why the code
looks the way it does.

## Code style

The file follows the [Pine Script style guide](https://www.tradingview.com/pine-script-docs/writing/style-guide/)
with these project rules.

**Naming**

| Thing | Style | Example |
| ------- | ------- | --------- |
| Constants | `UPPER_SNAKE` | `MS_DAY`, `G_SESSIONS` |
| Inputs | `i_` + camelCase | `i_lookback` |
| Types and enums | `PascalCase` | `Tracker`, `ZoneStyle` |
| Functions, methods, variables | camelCase | `runZones`, `barEnd` |

**Structure**

- Put new code in the region it belongs to. A region may only use what the regions above it define.
- State goes into a type. Drawing goes into a method of the Engine region. Helpers stay pure.
- Every dropdown is an `enum`. Do not compare strings.
- Every input belongs to a group and, when its meaning is not obvious, has a tooltip.
- In an inline row only the first input has a title.
- New modules are off by default.
- Declare a new input after the last one. TradingView stores settings by input position, so an input added in the
  middle shifts the saved settings of everyone who uses the indicator.

**Formatting**

- Four spaces per level, no tabs.
- Do not wrap lines. Pine gives wrapped lines special indentation rules; this project avoids them.
- Document every type and function with `// @type`, `// @function`, `// @param`, `// @returns`.
- A comment says *why*. The code already says *what*.

**Behaviour**

- Never read the future. Higher-timeframe values need a one-bar offset.
- Nothing new may be drawn on a bar outside `inWindow`.
- Respect the timeframe gates: if a module cannot be right on a timeframe, it must draw nothing.
- Count your drawings. The budget is 500 lines, 500 labels and 500 boxes for the whole script.
- Print text in `inkOf(colour)`, not in the colour itself, so it stays readable on light and dark charts.

## Python tools

The only Python in the repository is [tools/check.py](tools/check.py) and its tests in
[tests/test_check.py](tests/test_check.py). When you change either, run:

```bash
uv run ruff check
```

```bash
uv run ruff format
```

```bash
uv run pytest
```

The settings of ruff, pytest and coverage are in `pyproject.toml`. The script writes its output with `say()`:
the ruff rules keep `print` for tests. A new check comes with tests: one input that
passes and one for every problem it can report. CI runs the same commands on every push and pull request.

## Screenshots

The pictures in the READMEs and in `docs/SETTINGS.md` live in [docs/images](docs/images). Retake them when a
change alters what they show.

- Use a chart with this indicator only: no other indicators, no drawings, the light theme.
- Symbol `OANDA:EURUSD`: 15 minutes for the session pictures and the dashboard, 5 minutes for killzones and the
  opening range.
- Keep TradingView's default right margin, so the pictures show what a new user sees.
- Take the picture with TradingView's own snapshot (the camera icon → *Download image*), so the symbol, the
  timeframe and the time are part of it.
- Keep the file names, and name the settings you switched on in the caption.

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<emoji> <type>(<scope>): <summary in the imperative, lower case, no full stop>
```

Every commit starts with the emoji of its type, so the history can be read at a glance:

| Emoji | Type | Use it for |
| ------- | ------ | ----------- |
| ✨ | `feat` | a new module or setting |
| 🐛 | `fix` | a bug fix |
| ⚡ | `perf` | the same result with less work |
| ♻️ | `refactor` | a change that neither fixes a bug nor adds a feature |
| 📝 | `docs` | documentation only |
| ✅ | `test` | tests only |
| 👷 | `ci` | the workflow or the check script |
| 🔧 | `chore` | repository housekeeping |
| 🚀 | `chore(release)` | a release commit |

One emoji per commit; a breaking change adds 💥 after it. Commits made before 2026-11-27 have none, and the
history is not rewritten for it.

Scopes are the modules: `sessions`, `killzones`, `levels`, `periods`, `opens`, `range`, `vwap`, `dashboard`,
`alerts`, `style`.

Examples: `✨ feat(killzones): add a sixth slot`, `🐛 fix(levels): keep the label when a level is faded`.

## Pull requests

- Branch from `main`. Name the branch `feat/…`, `fix/…` or `docs/…`.
- Keep one topic per pull request.
- Update `CHANGELOG.md` under **Unreleased**.
- Update `docs/SETTINGS.md` when you add or change an input.
- Change `README.ru.md` and `README.fr.md` together with `README.md`. The check script compares their sections,
  pictures and links with the English file.
- Attach before / after screenshots for anything visible.
- Fill in the pull request template, including the test rows you ran.

## Releases (maintainers)

1. Move the **Unreleased** entries of `CHANGELOG.md` under a new version heading with today's date.
2. Set `VERSION` in the script, and the version badge and the status line in every README (`README.md`,
   `README.ru.md`, `README.fr.md`).
3. Run the full matrix of [docs/TESTING.md](docs/TESTING.md) and add a line to its verification log.
4. Commit as `🚀 chore(release): vX.Y.Z`, tag `vX.Y.Z`, push with tags.
5. Create the GitHub release from the tag with the changelog section as notes.
6. Update the script on TradingView as described in [docs/PUBLISHING.md](docs/PUBLISHING.md).
7. Retake the screenshots if the release changes how the chart looks.

## License

By contributing you agree that your contribution is licensed under the
[Mozilla Public License 2.0](LICENSE).
