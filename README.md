<div align="center">

# Custom Sessions Indicator

**Sessions, killzones, liquidity levels, opening prices, opening range, session VWAP and a dashboard — one TradingView overlay, every part of it configurable.**

[![Pine Script](https://img.shields.io/badge/Pine%20Script-v6-2962FF)](https://www.tradingview.com/pine-script-docs/)
[![Platform](https://img.shields.io/badge/platform-TradingView-131722?logo=tradingview&logoColor=white)](https://www.tradingview.com/)
[![Version](https://img.shields.io/badge/version-1.0.0-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MPL--2.0-brightgreen)](LICENSE)
[![CI](https://github.com/DmytroPalahin/sessions-indicator/actions/workflows/ci.yml/badge.svg)](https://github.com/DmytroPalahin/sessions-indicator/actions/workflows/ci.yml)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-FE5196?logo=conventionalcommits&logoColor=white)](https://www.conventionalcommits.org/)
[![Keep a Changelog](https://img.shields.io/badge/changelog-Keep%20a%20Changelog-E05735)](https://keepachangelog.com/en/1.1.0/)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

**English** · [Русский](README.ru.md)

</div>

---

## What it is

A single Pine Script v6 indicator that maps the trading day on your chart. Out of the box it draws the Asia, London
and New York sessions as boxes with their names and ranges. Everything else is one checkbox away and off by default,
so the chart stays clean until you ask for more.

| # | Module | What you get |
|---|--------|--------------|
| ① | **General** | One timezone for the whole indicator (DST-aware), history depth, timeframe limit |
| ② | **Sessions** | 5 slots: Asia, London, New York + 2 spare. Name, time window and colour are yours to change |
| ③ | **Session display** | Box, background, both or hidden · label with name and range · open line · 50% midline |
| ④ | **Session high / low levels** | Highs and lows stay on the chart until price trades through them |
| ⑤ | **Killzones** | 5 more slots with their own look, preset to the usual Asia / London / New York windows |
| ⑥ | **Previous day / week / month** | PDH/PDL, PWH/PWL, PMH/PML |
| ⑦ | **Opening prices** | Day, week, month, midnight and one custom time of day |
| ⑧ | **Opening range** | Range box, extended lines, midline, projections and breakout markers |
| ⑨ | **Session VWAP** | Re-anchored at each session, day, week or month, with optional bands |
| ⑩ | **Time tools** | Day separators and weekday labels |
| ⑪ | **Dashboard** | Which session is open, time left or time to open, current range against its average, day range against ADR |
| ⑫ | **Style** | Text size, line style and width, label options, a filter for distant levels |

## Quick start

1. Open [src/custom_sessions_indicator.pine](src/custom_sessions_indicator.pine) and copy the whole file.
2. On TradingView open any chart, then the **Pine Editor**.
3. Replace the editor content with the copied code and press **Add to chart**.
4. Open the indicator **Settings** to switch modules on. Start with *① General → Timezone*.

The indicator needs an intraday chart for sessions (60 minutes or lower by default).

## Default sessions

All times are in the timezone selected in *① General* — `America/New_York` by default.

| Slot | Name | Window | On |
|------|------|--------|----|
| 1 | Asia | 18:00 – 02:00 | yes |
| 2 | London | 03:00 – 11:00 | yes |
| 3 | New York | 08:00 – 16:00 | yes |
| 4 | Sydney | 16:00 – 00:00 | no |
| 5 | Custom | 09:30 – 16:00 | no |

Each default session is the 08:00 – 16:00 working day of its city, written in New York time. Asia is blue, London
green and New York orange, drawn as soft boxes without a border.

Killzone presets: Asia 20:00 – 00:00, London 02:00 – 05:00, NY AM 07:00 – 10:00, NY Lunch 12:00 – 13:00,
NY PM 13:30 – 16:00. These are conventions, not rules: every window is editable.

## Documentation

| Document | Read it when you want to |
|----------|--------------------------|
| [docs/SETTINGS.md](docs/SETTINGS.md) | know what every input does and what its default is |
| [docs/FAQ.md](docs/FAQ.md) | fix "nothing is drawn" or "sessions are an hour off" |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | understand or change the code |
| [docs/TESTING.md](docs/TESTING.md) | test a change before sending it |
| [docs/PUBLISHING.md](docs/PUBLISHING.md) | publish a release on TradingView |
| [CHANGELOG.md](CHANGELOG.md) | see what changed between versions |

## How it behaves

- **No repainting from the future.** Previous day / week / month values are read with a one-bar offset, so a
  historical bar shows exactly what was known when it closed.
- **Session levels break on a trade-through.** A high is broken by a higher high, a low by a lower low.
- **Opening range breakouts need a close.** The marker appears when a bar closes outside the range.
- **Live levels cannot disappear.** TradingView keeps only the newest 500 lines, labels and boxes. Current levels are
  redrawn on the last bar, so the limit only ever removes old history.

## Limitations

These come from how Pine Script and TradingView work. They are listed so that nothing surprises you.

- Sessions, killzones and the opening range are intraday tools. They hide above the timeframe set in *① General*.
- Levels far from price squeeze the candles, because TradingView fits every level of an indicator into the price
  scale. *⑫ Style → Hide levels farther than* removes them; so does *Scale price chart only* in the price-scale menu.
- Session VWAP needs volume. On symbols without volume nothing is plotted.
- The dashboard clock follows the schedule, not the exchange calendar: it does not know about weekends and holidays.
  Like every script, it refreshes when the chart receives a tick.
- Session averages are computed from the bars loaded on the chart.
- A custom opening price needs a bar that opens at that time (or within one bar after it).

## Project status

Version 1.0.0 compiles and runs on TradingView with no errors and no warnings. It has been run on forex, crypto,
futures and stock charts from 30 seconds to daily. The verification log in [docs/TESTING.md](docs/TESTING.md) lists
what has been checked and what is still open.

## Roadmap

- Per-session timezones, so Asia can follow Tokyo time while New York follows New York time
- Standard-deviation projections of a chosen session range
- Session volume profile
- Statistics: how often one session breaks the range of another
- Alerts for session starts, broken levels and opening range breakouts — built and tried on a live chart, kept on
  the `feature/alerts` branch until a later release

Have an idea? [Open a feature request](https://github.com/DmytroPalahin/sessions-indicator/issues/new/choose).

## Contributing and support

Bug reports, ideas and pull requests are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md).
For help see [SUPPORT.md](SUPPORT.md). Please follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

[Mozilla Public License 2.0](LICENSE). You may use, modify and share the script; changes to its files stay open
under the same license.

## Disclaimer

This indicator is a charting tool. It is not financial advice and it does not predict the market. Trading involves
risk; you are responsible for your own decisions.
