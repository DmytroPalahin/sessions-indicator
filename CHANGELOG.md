# Changelog

All notable changes to this project are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

How versions are counted for an indicator:

- **Major** — a setting was removed or renamed, so saved settings stop applying.
- **Minor** — a new module, a new setting or a changed default. Changed defaults are listed under *Changed*.
- **Patch** — a fix that does not add settings.

## [Unreleased]

Label text that reads on a white chart as well as on a dark one.

### Added

- *⑫ Style → Label text adapts to the chart background*, on by default. Text in a colour that would be hard to read
  on the chart background is darkened on a light chart and lightened on a dark one, up to a contrast of 4.5 : 1.
- FAQ entries: why label text can be a shade darker than its line, and VWAP in Bar Replay.
- The verification log covers the last open rows of the chart matrix: the US clock change, Bar Replay, light and
  dark charts.

### Changed

- Captions, level labels and the session names of the dashboard are printed in the adjusted colour. Lines, boxes
  and backgrounds are unchanged. Switch the new setting off to get the exact colours back.

### Fixed

- On a white chart most default label colours were too pale to read comfortably (`PWH` 1.4 : 1, `PDH` 1.9 : 1, New
  York 2.2 : 1, London 2.8 : 1); on a dark chart Frankfurt purple was at 2.8 : 1.

## [1.3.0] - 2026-11-25

Level labels that stay readable with TradingView's default right margin, plus the publication, pictures and
documentation. If you prefer the labels where they were, set *⑫ Style → Level labels position* to `After the line`
and *① General → Level labels offset, bars* to `8`.

### Added

- *⑫ Style → Level labels position*: `At the line end` (the new default) or `After the line` (the placement of 1.2.0).
- The indicator is published on TradingView as a public, protected script:
  https://www.tradingview.com/script/ticv4Yo6-Custom-Sessions-Indicator/
- Screenshots of the default look and of the modules in both READMEs and in the settings reference
  (`docs/images`).
- A links section in both READMEs, and the roadmap in the Russian README.
- FAQ entries: where to get the indicator, level labels cut off at the right edge, two labels at one price, a
  session label crossed by candles, a faint VWAP line on a light chart.
- `tools/check.py` checks that every local link and picture in the documentation resolves.

### Changed

- Level labels sit at the right end of their line — over it, under it for lows — instead of after it.
- *① General → Level labels offset, bars* defaults to `5` (was `8`).
- The copyright line of the script names the TradingView account of the author, `dmitry_plhn`.
- `docs/PUBLISHING.md` describes the publication as it is: categories, tags, picture and what can still be
  changed after publishing.

### Fixed

- Level labels were cut off by the price scale on a chart with the default right margin (`London Hi…`, `D Ope…`).

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

[Unreleased]: https://github.com/DmytroPalahin/sessions-indicator/compare/v1.3.0...HEAD
[1.3.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/DmytroPalahin/sessions-indicator/releases/tag/v1.0.0
