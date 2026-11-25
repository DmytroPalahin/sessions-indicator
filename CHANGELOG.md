# Changelog

All notable changes to this project are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

How versions are counted for an indicator:

- **Major** — a setting was removed or renamed, so saved settings stop applying.
- **Minor** — a new module, a new setting or a changed default. Changed defaults are listed under *Changed*.
- **Patch** — a fix that does not add settings.

## [Unreleased]

### Changed

- The copyright line of the script names the TradingView account of the author, `dmitry_plhn`.

## [1.2.0] - 2026-11-25

A Frankfurt session and a cleaner default chart. The session rows changed places: values you typed into rows 2 to 5
by hand stay in those rows, so check the *② Sessions* group after updating, or use *Defaults → Reset settings*.

### Added

- A **Frankfurt** session, on by default: the hour before London opens, `0200-0300` in New York time, purple.

### Changed

- The default slots are in time order: Asia, Frankfurt, London, New York, Sydney. The `Custom` preset is gone;
  every slot can still be renamed and retimed.
- Session labels are hidden by default. Switch them on in *③ Session display → Label*.
- The *Timezone* setting is now called *Timezone of session times*, and its tooltip says that it is the timezone the
  times are written in, not the timezone of the user.

### Fixed

- The legend no longer shows three empty values (`∅ ∅ ∅`) next to the indicator name while VWAP is off.

## [1.1.0] - 2026-11-25

A new default look. Charts that use the default settings change with this update; anyone who prefers the previous
look can set the old values by hand: windows `1900-0400`, `0300-1200`, `0800-1700`, fill transparency 90, border
transparency 40.

### Changed

- Default sessions are now the 08:00 – 16:00 working day of each city in New York time: Asia `1800-0200`,
  London `0300-1100`, New York `0800-1600`, Sydney `1600-0000` (were nine-hour windows).
- Default colours: Asia blue, London green, New York orange, Sydney purple; the first two killzones follow.
- Session boxes are softer by default: fill transparency 95 and no border (were 90 and a visible border).

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

[Unreleased]: https://github.com/DmytroPalahin/sessions-indicator/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/DmytroPalahin/sessions-indicator/releases/tag/v1.0.0
