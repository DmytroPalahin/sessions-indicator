## What changes

<!-- One or two sentences. Link the issue: "Closes #12". -->

## Why

<!-- The problem this solves, in terms of what a trader sees on the chart. -->

## How it was tested

- [ ] `uv run tools/check.py` passes
- [ ] `uv run ruff check` and `uv run pytest` pass, if `tools/` or `tests/` changed
- [ ] The Pine Editor shows no errors and no warnings
- [ ] Rows of `docs/TESTING.md` I ran: <!-- for example 1, 5, 6, 17 -->
- Symbols and timeframes: <!-- for example FX:EURUSD 15m, BINANCE:BTCUSDT 1m -->

## Screenshots

<!-- Before and after, for anything visible. -->

## Checklist

- [ ] `CHANGELOG.md` is updated under **Unreleased**
- [ ] `docs/SETTINGS.md` is updated if an input was added or changed
- [ ] New modules are off by default
- [ ] No value from the future is used (higher-timeframe data has a one-bar offset)
