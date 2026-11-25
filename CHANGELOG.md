# Changelog

All notable changes to this project are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

How versions are counted for an indicator:

- **Major** — a setting was removed or renamed, or a default changed in a way that alters an existing chart.
- **Minor** — a new module or a new setting; existing charts look the same.
- **Patch** — a fix that does not add settings.

## [Unreleased]

Nothing yet.

## [1.0.0] - 2026-11-25

The first release. What was checked on live charts before it, and what was not, is recorded in the verification log
of [docs/TESTING.md](docs/TESTING.md).

### Added

- **Sessions** — five slots (Asia, London, New York, Sydney, Custom) with editable name, time window and colour.
  A window may cross midnight, may last up to 24 hours and works on regular-hours charts.
- **Session display** — box, background, both or hidden; label with name and range; open line; 50% midline;
  range in price, ticks, pips or percent.
- **Session high / low levels** — highs and lows that stay on the chart until price trades through them, with a
  limit on how many are kept and a choice of fading or removing broken levels.
- **Killzones** — five slots with their own style, preset to the usual Asia, London and New York windows.
- **Previous day / week / month** — high and low of the previous period, with optional history.
- **Opening prices** — day, week, month, midnight and one custom time of day.
- **Opening range** — range box, extended high / low / mid lines, two projections and breakout markers.
- **Session VWAP** — anchored to each session start, day, week or month, with optional bands.
- **Time tools** — day separators and weekday labels.
- **Dashboard** — open / closed status with countdown, current range, average range and day range against ADR.
- **Style** — text size, level line style, level labels and a distance filter that hides levels far from price so
  they do not squeeze the price scale.
- **Data Window values** — running high and low of every session slot, usable in user-made alerts.
- Project documentation, contribution guide, issue and pull request templates.
- `tools/check.py` and a CI workflow that run static checks on the script.

[Unreleased]: https://github.com/DmytroPalahin/sessions-indicator/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/DmytroPalahin/sessions-indicator/releases/tag/v1.0.0
