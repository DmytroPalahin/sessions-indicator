# Testing

Pine Script cannot be run outside TradingView, so testing has two layers: static checks that run anywhere, and a
manual matrix on real charts.

## 1. Static checks

```bash
uv run tools/check.py
```

The script needs only the Python standard library, so `python3 tools/check.py` works too. CI runs it on every push
and pull request. It checks:

- the license header, `//@version=6` and the `indicator()` call;
- the short title length (TradingView allows 10 characters);
- no tabs, no trailing whitespace, LF line endings, a final newline;
- indentation in multiples of four (the source does not wrap lines);
- balanced brackets on every line and balanced `//#region` markers;
- inline input rows with a title on their first input only (TradingView warning `CW10026`);
- every function and method has its own name (an overload cannot read globals, error `CE10182`);
- the number of plot-like calls against the limit of 64;
- the version in the script, the README badge and the changelog agree;
- every local link and picture in the documentation points at a file that exists;
- the Russian and the French README have the sections, pictures and local links of the English one.

The check script has tests of its own in `tests/test_check.py`: every check is run on input that passes and on
input for each problem it can report, and the whole script is run on this repository and on a broken copy.

```bash
uv run pytest
```

## 2. Compile check

1. Paste the script into the Pine Editor.
2. Wait a few seconds for the editor to analyse it, then press **F8** ("go to next problem"). No problem list means
   the editor found no errors and no warnings.
3. Press **Add to chart**. This runs the full compiler, which catches errors the editor's own analysis misses — for
   example an overloaded function that reads a global variable (`CE10182`).

A release must pass both steps with zero errors and zero warnings.

## 3. Chart matrix

Run before every release. Add the indicator to the chart and walk through the rows.

### Symbols

| Symbol | Why |
| -------- | ----- |
| `FX:EURUSD` | 24/5 market, pips, sessions crossing midnight |
| `FX:USDJPY` | JPY pip size |
| `BINANCE:BTCUSDT` | 24/7 market, weekends |
| `CME_MINI:ES1!` | futures day that starts at 18:00 New York |
| `NASDAQ:AAPL` | regular hours only, then with extended hours |

### Timeframes

`1`, `5`, `15`, `60` for sessions; `240` and `D` to confirm that intraday modules hide and the rest still works.

### Checks

| # | Check | Expected |
| --- | ------- | ---------- |
| 1 | Defaults on a 15-minute chart | Four session boxes per day (Asia, Frankfurt, London, New York), no labels, and the hours table with a line for each of the four |
| 2 | Change the city of a session row, then the *Clock* of the killzones, then *My timezone* | The box of that row moves and keeps its width, the other sessions stay; the killzone clock moves killzones only; *My timezone* moves nothing but rows and clocks set to `My time` and changes the *Hours* column of the dashboard |
| 3 | Weeks around the clock changes in Europe and the US (March, October – November) | Every session keeps the local hours of its city; killzones keep their New York times |
| 4 | Style `Background`, then `Box + background`, then `Hidden` | Bands, both, nothing — labels stay for all but `Hidden` caption |
| 5 | *④ Session levels* on | Two lines per finished session; a line stops and fades on the bar that trades through it |
| 6 | *Broken levels* = `Remove` | Broken lines disappear |
| 7 | *⑤ Killzones* on | Five shaded windows with names |
| 8 | *⑥ Previous day / week / month* on | `PDH`/`PDL`/`PWH`/`PWL`/`PMH`/`PML` match the previous daily, weekly and monthly candles |
| 9 | *Keep past periods* on | Earlier days keep their lines, ending at the day boundary |
| 10 | *⑦ Opening prices* on | Each line starts on the right bar and matches that bar's open |
| 11 | *⑧ Opening range* on, stock chart | Box for 09:30–10:00, lines for six hours, one triangle per side at most |
| 12 | *(reserved for the session VWAP, which is parked on the `feature/vwap` branch)* | — |
| 13 | *⑨ Time tools* on | One separator and one weekday label per day |
| 14 | *⑩ Dashboard* on | Status matches the clock; ranges match the labels on the chart |
| 15 | 4-hour chart | No sessions, killzones or opening range; previous week and month levels remain |
| 16 | Daily chart | Only previous week and month levels and week / month opens remain |
| 17 | Bar Replay | Drawings build up bar by bar and match the non-replay chart |
| 18 | *(reserved for alerts, which are parked on the `feature/alerts` branch)* | — |
| 19 | History = `0` on a 1-minute chart | The script loads without a runtime error |
| 20 | Light and dark chart themes | All text is readable: with *Label text adapts to the chart background* on, every text colour has a contrast of 4.5 : 1 or more against the chart background |
| 21 | Regular-hours chart (stock or futures, RTH) | The New York session is drawn every day, although no bar separates two days |
| 22 | *Hide levels farther than* = `2` with weekly and monthly levels on | Distant levels disappear and the price scale stops being stretched |
| 23 | Level labels on a chart with the default right margin, then *Level labels position* = `After the line` | `At the line end`: every label is complete, over its line or under it for lows. `After the line`: the text follows the line and long labels are cut off by the price scale |

## Verification log

| Date | Version | What was verified | Result |
| ------ | --------- | ------------------- | -------- |
| 2026-11-25 | 1.0.0 | Static checks (`tools/check.py`) | pass |
| 2026-11-25 | 1.0.0 | Editor analysis in the Pine Editor (Pine v6) | 0 errors, 0 warnings |
| 2026-11-25 | 1.0.0 | Full compile with **Add to chart** | pass, after fixing `CE10182` (overloaded methods read globals) |
| 2026-11-25 | 1.0.0 | Chart matrix rows 1, 5, 7, 9, 11, 13, 14, 15, 16, 21, 22 | pass — `OANDA:GBPUSD` on 30s, 5m, 15m, 30m, 1h, 4h, D; `BINANCE:BTCUSDT`, `CME_MINI:ES1!` and `NASDAQ:AAPL` on 15m. Row 21 failed first and was fixed (`windowKey`). |
| 2026-11-25 | 1.0.0 | Chart matrix rows 8, 10, 12 | drawn and plausible; values not cross-checked against the candles |
| 2026-11-25 | 1.0.0 | Chart matrix rows 2, 4, 19 | pass — `OANDA:GBPUSD` 1m with History = 0, Timezone = UTC, Style = Box + background |
| 2026-11-25 | `feature/alerts` | Alerts on `OANDA:GBPUSD` 1m with *Any alert() function call* | Session start and killzone start were delivered on the first tick of their bar, and a broken session level at the close of its bar, each with the session name. The module was then parked. |
| 2026-11-25 | 1.0.0 | Full compile and chart run after removing the alerts module | pass — `TVC:DXY` on the daily and the 15-minute timeframe, all modules on |
| 2026-11-25 | 1.1.0 | New default sessions, colours and box style | pass — `OANDA:EURUSD` 15m: full compile, and the boxes coincide edge to edge with an 08:00 – 16:00 per-city reference indicator |
| 2026-11-25 | 1.1.0 | Release build | The tagged file differs from the build run on the chart only in the `VERSION` string; static checks pass, it was not run on a chart again |
| 2026-11-25 | 1.2.0 | Labels hidden by default, timezone setting renamed | pass — `OANDA:EURUSD` 15m: full compile; boxes only, no labels, same edges as the reference indicator |
| 2026-11-25 | 1.2.0 | Frankfurt session in the defaults, slots in time order | pass — `OANDA:GBPUSD` 15m: full compile; the purple Frankfurt box sits between the Asia and London boxes, at the same place as in the reference indicator |
| 2026-11-25 | 1.2.0 | VWAP plots taken out of the status line while VWAP is off | pass — `OANDA:GBPUSD` 15m: full compile; the legend shows the indicator name with no empty values |
| 2026-11-25 | 1.2.0 | Release build | The tagged file differs from the build run on the chart only in the `VERSION` string; static checks pass, it was not run on a chart again |
| 2026-11-25 | 1.2.0 | Published build, modules switched on through the settings | pass — the script published on TradingView, on `OANDA:EURUSD` 15m and 5m: session labels, session levels, killzones, previous day levels, day and midnight opens, opening range with two projections, VWAP with bands, day separators, weekday labels and the dashboard, each without a script error; the dashboard status matched the clock. The pictures in `docs/images` come from this run. |
| 2026-11-25 | 1.2.0 | Cosmetic findings of that run | recorded in the FAQ: level labels are cut off when the right margin of the chart is narrower than the label offset; labels of two levels at one price overlap; the default yellow VWAP is faint on a light chart |
| 2026-11-25 | 1.3.0 | Level labels at the line end (new default), offset 5 | Static checks pass. Editor analysis: 0 errors, 0 warnings. Full compile with **Add to chart**: pass, twice (once with the level modules on by default, once with the released defaults). |
| 2026-11-25 | 1.3.0 | Chart matrix rows 23 and 6 | pass — `OANDA:EURUSD` 15m and 5m with TradingView's default right margin (10 bars at 6 pixels): session levels, previous day levels, day and midnight opens are labelled in full, also with *Price in level labels* on and with a 6-bar margin. On the same chart version 1.2.0 cut every one of these labels, and still did with the offset lowered to 2. `After the line` gives the old placement. *Broken levels* = `Remove` deletes the broken lines. |
| 2026-11-25 | 1.3.0 | Release build | pass — the tagged file itself was saved in TradingView and published as the update: editor analysis and compile with 0 errors and 0 warnings; on `OANDA:EURUSD` 15m the indicator shows the new input and the new defaults and reports no script error |
| 2026-11-25 | 1.3.0 | Chart matrix row 3 | pass — the published script on `OANDA:EURUSD` 60m, 830 bars from 7 October to 25 November, read bar by bar from the *Session N high* values. All 138 runs of Asia, Frankfurt, London and New York start and end at their New York times (18:00 – 02:00, 02:00 – 03:00, 03:00 – 11:00, 08:00 – 16:00). In UTC every session moves one hour later from 1 November, when the United States changed the clock, and does not move on 25 October, when Europe did. The 15m and 30m charts confirm the times after the change to the bar; their loaded history did not reach 1 November. The March change was not checked. |
| 2026-11-25 | 1.3.0 | Chart matrix row 17 | pass — `OANDA:EURUSD` 15m with every module on: Bar Replay from 24 November 10:00 UTC, 46 single-bar steps to 21:15 UTC. All 26 plot values of the 47 replayed bars equal the normal chart. Every finished drawing of the last two days is identical on both charts (10 boxes, 37 lines, 23 labels), among them the London and New York boxes, the opening range box and the killzone captions that were built during the replay. The running London box at the start had the range the normal chart shows at that bar. After leaving the replay the chart was back at its 70 boxes, 303 lines and 185 labels. |
| 2026-11-25 | 1.3.0 | Findings of the replay run | In the history before the replay start the VWAP differed from the normal chart by up to 1.1 pips in two sessions: the replay data carries another tick volume on 9 of 203 compared bars, with identical prices. Recorded in the FAQ. When reading values in a replay, let the last bar settle: for a moment it shows the values of its first tick. |
| 2026-11-25 | 1.3.0 | Chart matrix row 20 | dark: pass; light: readable, but pale — the contrast of every text colour against the chart background was measured from the drawn labels with all level types on. Dark background (`#131722`): the dashboard and the weekday labels switch to light text; the lowest ratios are Frankfurt purple 2.8 : 1 and Asia blue 3.7 : 1, everything else is 4.7 : 1 or more. White background: dashboard 21 : 1, weekday labels 8.6 : 1, Frankfurt 6.3 : 1, Asia 4.9 : 1, but 14 default colours are below 3 : 1 — `PWH` / `PWL` 1.4, `W Open` 1.5, `00:00 Open` 1.8, `PDH` / `PDL` 1.9, New York 2.2, London 2.8, the killzone captions 1.9 to 2.8. Recorded in the FAQ. The dark background was set on the chart canvas of the test layout only. |
| 2026-11-25 | 1.4.0 | Label text adapts to the chart background (new, on by default) | Static checks pass. Editor analysis: 0 errors, 0 warnings. Full compile with **Add to chart**: pass, twice. |
| 2026-11-25 | 1.4.0 | Chart matrix row 20 | pass — `OANDA:EURUSD` 15m with all level types, killzones, captions and the dashboard on; the contrast of all 20 text colours was read from the drawn labels and table cells. White background: 4.5 : 1 to 21 : 1 with the setting on (London `#357A38`, New York `#995B00`, `PWH` `#7F6A27`, `PDH` `#697276`); with it off the colours of 1.3.0 return, 15 of them below 4.5 : 1. Dark background (`#131722`): 4.7 : 1 or more with the setting on (Frankfurt `#B967C7`, Asia `#5381FF`); off, Frankfurt is at 2.8 : 1 and Asia at 3.7 : 1. Lines, boxes and backgrounds keep their colours in every case. |
| 2026-11-25 | 1.4.0 | Release build | pass — the tagged file itself was saved in TradingView, added to the chart and published as the update: editor analysis and compile with 0 errors and 0 warnings; on `OANDA:EURUSD` 15m the indicator shows the new input with its default and reports no script error |
| 2026-11-25 | 1.4.0 | The version the Indicators dialog adds | pass, with a finding — the script service lists the update as version 3.0 from the moment it was published. Added from *Indicators → Favorites* on an empty chart with a freshly loaded list, the publication comes as version 3.0: 115 inputs, the new one among them, no script error. Before that the dialog kept adding version 2.0 for more than twenty minutes, across reloads: it reads the version from its Favorites list in the browser's cache. An instance already on a chart stayed on 2.0 after reloading. *My scripts* added the saved script in its newest version at once. Recorded in the FAQ and in PUBLISHING.md. |
| 2026-11-25 | 1.4.0 | When the Indicators dialog renews its cached Favorites list | Read from TradingView's client code and confirmed on the live dialog. The list is valid for 24 hours from its last write; a favourite found in it is not requested again; opening the dialog writes the list anew. A cache entry made to look 23 hours old, holding version 2.0, was kept at 2.0 and stored with a new time. One made to look 25 hours old was dropped and rebuilt with version 3.0. Reopening the dialog twenty seconds later rewrote the entry again. The code also drops the list on sign-out; that was not run. |
| 2026-11-25 | 2.0.0 | Session VWAP taken out, later settings groups renumbered | Static checks pass. Editor analysis: 0 errors, 0 warnings. Full compile with **Add to chart**: pass. On `OANDA:EURUSD` 15m and 5m the build has 110 inputs in groups ① to ⑪ and 20 plots, none of them a VWAP, and reports no script error with sessions as a background, with the opening range, and with labels, levels, killzones, previous day levels, opens, time tools and the dashboard on together. |
| 2026-11-25 | 2.0.0 | Release build | pass — the tagged file itself was saved in TradingView, added to the chart and published as the update: editor analysis and compile with 0 errors and 0 warnings; on `OANDA:EURUSD` 15m the indicator has 110 inputs in 11 groups, all at their defaults, and reports no script error |
| 2026-11-26 | 2.1.0 | *Custom timezone* defaults to `Europe/London`; the `Custom` choice, which had not been run before | Static checks pass. Editor analysis: 0 errors, 0 warnings. Full compile with **Add to chart**: pass. On `OANDA:EURUSD` 15m the Asia window `1800-0200` falls at 23:00 – 07:00 UTC with `America/New_York`, and with `Custom` at 18:00 – 02:00 UTC for `Europe/London`, 09:00 – 17:00 UTC for `Asia/Tokyo`, 16:00 – 00:00 UTC for `Europe/Kyiv` and 15:00 – 23:00 UTC for `UTC+3`, each without a script error. |
| 2026-11-26 | 2.1.0 | Release build | pass — the tagged file itself was saved in TradingView, added to the chart and published as the update: it compiles without errors and the editor marks nothing; on `OANDA:EURUSD` 15m the indicator has 110 inputs, all at their defaults, *Custom timezone* shows `Europe/London`, and it reports no script error |
| 2026-11-26 | 2.1.1 | Timezone reminder in the headings of *② Sessions* and *⑤ Killzones* and in the tooltips of the time inputs | Static checks pass. Full compile with **Add to chart** from an unsaved draft: pass. On `OANDA:EURUSD` 15m the build has the same inputs as 2.1.0 and reports no script error. In the settings dialog both headings stay on one line (322 px of a 550 px wide dialog) and the row tooltip carries the new sentence. Not looked at in the mobile app. |
| 2026-11-26 | 2.1.1 | Release build | pass — the tagged file itself was saved in TradingView and published as the update: it compiles without errors and the editor marks nothing; on `OANDA:EURUSD` 15m the instance on the chart took the new version, shows both new headings and reports no script error |
| 2026-11-26 | 3.0.0 | Each session row has a city of its own; the settings changed order; the dashboard header lost its clock | Static checks pass. Full compile with **Add to chart** from an unsaved draft: pass, the editor marks nothing; 115 inputs, 20 plots. In the settings dialog a row of checkbox, name, hours and city stays on one line and the five colours sit on a row under them. On `OANDA:EURUSD` 60m, 1223 bars from 7 September: Asia starts at 23:00 UTC on every day (08:00 Tokyo); Frankfurt at 06:00 UTC until 23 October and at 07:00 UTC from 26 October; London at 07:00 and 08:00 UTC on the same dates; New York at 12:00 UTC until 30 October and at 13:00 UTC from 2 November. Build 2.1.1 next to it moves all four on 1 November. A row with `0300-1100` and the city `As in ①` gives the London session of 2.1.1; with *① General* on `Europe/Berlin` only that row moves. On 15m, 2051 bars from 23 October, with killzones, the opening range and three opens on: all 20 plots equal those of 2.1.1 on every bar from 1 November, the killzone plots on every bar, and the 70 boxes, 73 lines and 88 labels of the two builds are the same. Dashboard at 03:31 UTC: Asia `Open · 3h 29m left`, Frankfurt `Opens in 3h 29m`, London `Opens in 4h 29m`, New York `Opens in 9h 29m`. Not checked: the clock changes of March, the Sydney row, the mobile app. |
| 2026-11-26 | 3.0.0 | Release build | pass — the tagged file itself was saved in TradingView, added to the chart as a new instance and published as the update: it compiles without errors and the editor marks nothing; on `OANDA:EURUSD` 15m the indicator has 115 inputs, all at their defaults, and 20 plots, and reports no script error |
| 2026-11-26 | 4.0.0 | No timezone for the whole indicator: a *Clock* in the killzone, opens, opening range and time tools groups; *My timezone*; cities `Exchange` and `My time`; *Hours* column in the dashboard | Static checks pass. Full compile with **Add to chart** from an unsaved draft: pass, the editor marks nothing; 119 inputs, 20 plots. On `OANDA:EURUSD` 15m, 400 bars, with killzones, three opens, the opening range, day separators and weekday labels on: all 20 plots equal those of 3.0.0 on every bar, and the 70 boxes, 90 lines and 105 labels of the two builds are the same. A London row with `0900-1700` and the city `My time`, *My timezone* on `Paris, Berlin, Madrid`, gives the same plots as `0800-1600` `London` on all 400 bars. Dashboard with that timezone at 04:21 UTC: Asia `00:00 – 08:00` `Open · 2h 39m left`, Frankfurt `08:00 – 09:00`, London `09:00 – 17:00`, New York `14:00 – 22:00`. Not checked: a clock other than New York for killzones, opens and the opening range, the summer half of the year for a `My time` row, the mobile app. |
| 2026-11-26 | 4.0.0 | Release build | pass — the tagged file itself was saved in TradingView, added to the chart as a new instance and published as the update: it compiles without errors and the editor marks nothing; on `OANDA:EURUSD` 15m the indicator has 119 inputs, all at their defaults, and 20 plots, and reports no script error |
| 2026-11-26 | 4.1.0 | Hours table on the chart when the dashboard is off | Static checks pass. Full compile with **Add to chart** from an unsaved draft: pass, the editor marks nothing; 119 inputs, 20 plots. On `OANDA:EURUSD` 15m with every input at its default the table reads `Asia · 08:00 – 16:00 Tokyo · 23:00 – 07:00`, `Frankfurt · 08:00 – 09:00 Frankfurt · 07:00 – 08:00`, `London · 08:00 – 16:00 London · 08:00 – 16:00`, `New York · 08:00 – 16:00 New York · 13:00 – 21:00` under the heading `UTC time`, and matches the time axis of a chart set to UTC. With *My timezone* on `Paris, Berlin, Madrid` the last column becomes 00:00 – 08:00, 08:00 – 09:00, 09:00 – 17:00 and 14:00 – 22:00; with killzones on, their five lines follow (`NY AM KZ · 07:00 – 10:00 New York · 13:00 – 16:00`). With the dashboard on the table is the dashboard with its *Hours* column; with *Hours on my clock* off and the dashboard off there is no table. Not checked: the mobile app, a chart above the timeframe limit. |
| 2026-11-26 | 4.1.0 | Release build | pass — the tagged file itself was saved in TradingView and published as the update: it compiles without errors and the editor marks nothing; on `OANDA:EURUSD` 15m the instance on the chart took the new version, has 119 inputs, all at their defaults, and 20 plots, shows the hours table and reports no script error |
| 2026-11-26 | 4.2.0 | *Hours are local* under the session rows; hours table with two columns | Static checks pass. Full compile with **Add to chart** from an unsaved draft: pass, the editor marks nothing; 120 inputs, 20 plots. In the settings dialog the new line is the last one of *② Sessions*, under the colours, and fits on one line. On `OANDA:EURUSD` 15m with every input at its default the table reads `Asia 23:00 – 07:00`, `Frankfurt 07:00 – 08:00`, `London 08:00 – 16:00`, `New York 13:00 – 21:00` under `UTC time`. With *Hours are local* off, *My timezone* on `Paris, Berlin, Madrid` and the rows retyped as `0000-0800`, `0800-0900`, `0900-1700` and `1400-2200`, all 20 plots equal those of 4.1.0 at its defaults on all 401 bars. Not checked: the summer half of the year for that mode, the mobile app. |
| 2026-11-26 | 4.2.0 | Release build | pass — the tagged file itself was saved in TradingView and published as the update: it compiles without errors and the editor marks nothing; on `OANDA:EURUSD` 15m the instance on the chart took the new version, has 120 inputs, all at their defaults, and 20 plots, shows the two-column hours table and reports no script error |
