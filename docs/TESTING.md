# Testing

Pine Script cannot be run outside TradingView, so testing has two layers: static checks that run anywhere, and a
manual matrix on real charts.

## 1. Static checks

```bash
python3 tools/check.py
```

The script needs only the Python standard library. CI runs it on every push and pull request. It checks:

- the license header, `//@version=6` and the `indicator()` call;
- the short title length (TradingView allows 10 characters);
- no tabs, no trailing whitespace, LF line endings, a final newline;
- indentation in multiples of four (the source does not wrap lines);
- balanced brackets on every line and balanced `//#region` markers;
- inline input rows with a title on their first input only (TradingView warning `CW10026`);
- the number of plot-like calls against the limit of 64;
- the version in the script, the README badge and the changelog agree.

## 2. Compile check

1. Paste the script into the Pine Editor.
2. Wait a few seconds for the editor to analyse it.
3. Press **F8** ("go to next problem"). No problem list means no errors and no warnings.

A release must have zero errors and zero warnings.

## 3. Chart matrix

Run before every release. Add the indicator to the chart and walk through the rows.

### Symbols

| Symbol | Why |
|--------|-----|
| `FX:EURUSD` | 24/5 market, pips, sessions crossing midnight |
| `FX:USDJPY` | JPY pip size |
| `BINANCE:BTCUSDT` | 24/7 market, weekends |
| `CME_MINI:ES1!` | futures day that starts at 18:00 New York |
| `NASDAQ:AAPL` | regular hours only, then with extended hours |

### Timeframes

`1`, `5`, `15`, `60` for sessions; `240` and `D` to confirm that intraday modules hide and the rest still works.

### Checks

| # | Check | Expected |
|---|-------|----------|
| 1 | Defaults on a 15-minute chart | Three session boxes per day with name and range, nothing else |
| 2 | Change *Timezone* to `UTC` | Boxes move; their width stays the same |
| 3 | A week with a US clock change (March, November) | Sessions keep their New York times |
| 4 | Style `Background`, then `Box + background`, then `Hidden` | Bands, both, nothing — labels stay for all but `Hidden` caption |
| 5 | *④ Session levels* on | Two lines per finished session; a line stops and fades on the bar that trades through it |
| 6 | *Broken levels* = `Remove` | Broken lines disappear |
| 7 | *⑤ Killzones* on | Five shaded windows with names |
| 8 | *⑥ Previous day / week / month* on | `PDH`/`PDL`/`PWH`/`PWL`/`PMH`/`PML` match the previous daily, weekly and monthly candles |
| 9 | *Keep past periods* on | Earlier days keep their lines, ending at the day boundary |
| 10 | *⑦ Opening prices* on | Each line starts on the right bar and matches that bar's open |
| 11 | *⑧ Opening range* on, stock chart | Box for 09:30–10:00, lines for six hours, one triangle per side at most |
| 12 | *⑨ VWAP* on with each anchor | The line restarts at the anchor and matches the built-in anchored VWAP |
| 13 | *⑩ Time tools* on | One separator and one weekday label per day |
| 14 | *⑪ Dashboard* on | Status matches the clock; ranges match the labels on the chart |
| 15 | 4-hour chart | No sessions, killzones or opening range; previous week and month levels remain |
| 16 | Daily chart | Only previous week and month levels and week / month opens remain |
| 17 | Bar Replay | Drawings build up bar by bar and match the non-replay chart |
| 18 | Alerts: *Any alert() function call* on a 1-minute chart | One message per event, with the session name |
| 19 | History = `0` on a 1-minute chart | The script loads without a runtime error |
| 20 | Light and dark chart themes | All text is readable |

## Verification log

| Date | Version | What was verified | Result |
|------|---------|-------------------|--------|
| 2026-11-25 | 1.0.0 | Static checks (`tools/check.py`) | pass |
| 2026-11-25 | 1.0.0 | Compile check in the TradingView Pine Editor (Pine v6) | 0 errors, 0 warnings |
| — | 1.0.0 | Chart matrix | pending |
