# Changelog

All notable changes to this project are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

How versions are counted for an indicator:

- **Major** — a setting was removed or renamed, so saved settings stop applying.
- **Minor** — a new module, a new setting or a changed default. Changed defaults are listed under *Changed*.
- **Patch** — a fix that does not add settings.

## [Unreleased]

### Added

- **Initial balance.** A second range next to the opening range, in *⑧ Opening range and initial balance*, off by
  default: the first hour of the session — 09:30 to 10:30 New York, with a window and a city of its own — as a
  box, the lines `IBH`, `IBL` and `IB 50%` extended to the New York close, up to three pairs of extensions (half a
  range and a whole range by default) and breakout markers. A label over the box gives the size of the first hour
  and its share of the average of the last days: `IB  42.0 p · 78% of avg`. Earlier days keep the box, the high
  and the low.
- Labels on the lines of the opening range: `ORH`, `ORL`, `OR 50%`, `OR ×1`. They follow *⑪ Style → Level labels*
  and carry the price with *Price in level labels*. A high or a low that the opening range and the initial balance
  share gets one label, `ORH · IBH`.
- *⑧ Size label* for the opening range, off by default: `OR  12.0 p · 85% of avg` under its box.
- A dashboard row for the opening range and one for the initial balance when they are on: `Forming · 23m left`
  while the window runs, then `Inside`, `Broken up`, `Broken down` or `Broken both ways` while the lines extend,
  with the size of the range and its average.

### Changed

- The group *⑧ Opening range* is now *⑧ Opening range and initial balance*. No setting moved: the new inputs are
  declared after all older ones, so saved settings keep applying.
- While the lines of the opening range extend, they end *① General → Level labels offset, bars* to the right of
  the last bar, like the other level lines, so their labels have room.

### Fixed

- The opening range is measured only on bars that fit its window. On a stock chart with 1-hour bars the
  30-minute window used to give the range of the whole first hour; on such a chart, and on one whose bars do not
  start where the window starts, nothing is drawn now.

## [4.4.0] - 2026-11-27

A new page on TradingView, with the code open and a description that matches the script.

### Changed

- The indicator is published again, as an open-source script named
  `Sessions, Killzones, Opening Range and Dashboard with Auto DST`:
  <https://www.tradingview.com/script/aK5XyDPb-Sessions-Killzones-Opening-Range-and-Dashboard-with-Auto-DST/>.
  The description of the first page could not be edited and no longer matched the script; that page stays at
  4.3.1 and gets no more updates. Add the indicator from the new page to keep getting them: the settings are the
  same.
- The script declares that title. The short title on the chart stays `Sessions`, and no setting moved.
- The header of the script no longer carries a link: TradingView does not allow links to other sites in
  published code.

## [4.3.1] - 2026-11-27

The same chart in about half the time.

### Changed

- The script does less work on every bar. Session and killzone rows that are off, the opening range, the
  opening prices and the previous day / week / month are no longer followed while nothing shows them, and a
  session label is formatted only when it is on the chart. With the settings the indicator starts with, the Pine
  profiler shows 406 ms on 10 290 bars of `OANDA:EURUSD` 15m where 4.3.0 took 815 ms. Nothing on the chart
  changes: plots, boxes, lines, labels and the dashboard are the same.

## [4.3.0] - 2026-11-26

A clean chart by default again.

### Changed

- *⑩ Dashboard → Hours on my clock* is off by default, so the hours table is no longer on the chart until it is
  asked for. To get it back after the update, tick that checkbox.
- *① General → My timezone* starts at `Paris, Berlin, Madrid` instead of `UTC`. It is only a starting value for
  the hours table and for clocks set to `My time`; sessions do not depend on it.

## [4.2.0] - 2026-11-26

The answer to "why does every session start at 08:00?" now sits under the session rows.

### Added

- *② Sessions → Hours are local: 08:00 is 8 o'clock in the row's city*, a checkbox under the session rows, on by
  default. Its title says how the rows are read. Unticked, every row is read in *① General → My timezone*
  instead, whatever its city says, so the hours can be typed as the chart shows them.

### Changed

- The hours table has two columns, the session and its hours on your clock. The column that repeated the hours of
  the settings is gone: the new line in the settings says the same where the question comes up.
- The heading of *② Sessions* is short again.

## [4.1.0] - 2026-11-26

The hours of the sessions are on the chart from the start, on your own clock.

### Changed

- *⑩ Dashboard → Hours on my clock* no longer needs the dashboard. With the dashboard off it shows a small table of
  its own, and since the setting is on by default, so is the table: one line per session with its name, its hours
  as they are written in the settings and the same hours in *① General → My timezone*. Enabled killzones are
  listed under the sessions. Picking another timezone changes the last column at once; until now it changed
  nothing that could be seen while the dashboard was off.
- The default look therefore has a table in the top right corner. Untick *Hours on my clock* to hide it.

### Added

- FAQ entries: why the hours in the settings still start at 08:00 after you picked your timezone, and how to hide
  the hours table.

## [4.0.0] - 2026-11-26

No timezone for the whole indicator any more: every window has its clock next to it, and the one timezone you set
is your own. The settings changed order again, so settings saved for 3.0.0 do not carry over.

### Added

- *① General → My timezone*: the timezone your own chart shows. TradingView does not tell an indicator which one
  it is, so it is picked once from a list of cities. Sessions are drawn in the right place whatever is chosen.
- Dashboard column *Hours*: the hours of every session on your own clock, with the timezone named in the first
  line. *⑩ Dashboard → Hours on my clock* switches it off.
- City `My time` for a session row: its hours are read in *My timezone*, typed as you see them on your chart.
- City `Exchange`, the timezone of the symbol.

### Changed

- **Breaking.** *① General → Killzones and opens timezone* is gone. The killzones, the midnight and custom opens,
  the opening range and the day separators each have a *Clock* in their own group, with the same list of cities as
  a session row. All of them start at `New York`, so nothing moves on the chart.
- **Breaking.** The city `As in ①` is replaced by `My time`.
- **Breaking.** The settings changed order. Settings saved for an older version are applied by position and no
  longer fit: press *Defaults → Reset settings* after the update.
- The heading of *⑤ Killzones* is short again; the clock above the rows says what the heading used to say.

### Removed

- *① General → Custom timezone*, the free-text timezone. Every clock is now picked from a list.

## [3.0.0] - 2026-11-26

Sessions are written in the local time of their own city. The settings changed order, so settings saved for 2.x
do not carry over.

### Changed

- **Breaking.** Every session row has a city, and its hours are the local time of that city: Asia `0800-1600`
  Tokyo, Frankfurt `0800-0900` Frankfurt, London `0800-1600` London, New York `0800-1600` New York, Sydney
  `0800-1600` Sydney. Until now every row was read in one timezone, New York by default. While all these cities
  are on winter time the default sessions stay where they were. In the rest of the year each session follows the
  clock changes of its own city instead of New York's: Asia starts at 08:00 Tokyo all year, and London at 08:00
  London also in the weeks when Europe and the United States are out of step.
- **Breaking.** The settings changed order: the city sits in the session row, the five session colours moved to a
  row of their own, and the timezone fields moved to the end of *① General*. Settings saved for an older version
  are applied by position and no longer fit: press *Defaults → Reset settings* after the update.
- *① General → Timezone of session times* is now *Killzones and opens timezone*. It sets the clock of the
  killzones, the opening range window, the midnight and custom opens and the day labels. A session reads it only
  on a row with the city `As in ①`.
- The dashboard header no longer shows a clock in the indicator timezone.

### Added

- City `As in ①` for a session row: its hours are read in the timezone of *① General*. This keeps custom zones,
  the exchange timezone and the old way of writing hours available.
- FAQ entries: why London `0800-1600` is drawn at another time on your chart, what the timezone in *① General* is
  for, and what to do after the update to 3.0.0.

## [2.1.1] - 2026-11-26

The settings dialog now says in which timezone the times are written. Only texts change.

### Changed

- The headings of *② Sessions* and *⑤ Killzones* in the settings dialog end with "times in the timezone set in
  ① General", and the tooltips of the session rows, the killzone rows, *⑦ Custom open* and *⑧ Window* say that the
  time is written in that timezone, not in your own. Only texts change: no setting moves and saved settings keep
  applying.

### Added

- FAQ entry: why the session times are in New York time and not in yours.

## [2.1.0] - 2026-11-26

A clearer *Custom timezone* field, and a French README. Charts that keep the default timezone do not change.

### Changed

- *① General → Custom timezone* shows `Europe/London` by default instead of `UTC+3`. The field is used only when
  *Timezone of session times* is `Custom`; the old example looked like a setting to adjust and, being an offset,
  did not follow daylight saving time. Its tooltip says so now.

### Added

- FAQ entry: what the *Custom timezone* field is for.
- A French README, `README.fr.md`, next to the English and the Russian one.
- `tools/check.py` checks that every translated README has the sections, pictures and local links of
  `README.md`.

## [2.0.0] - 2026-11-25

A major release. Taking the session VWAP out removes five inputs, and TradingView stores settings
by input position: what you changed in *Time tools*, *Dashboard* or *Style* will not carry over. After updating,
use *Settings → Defaults → Reset settings* and set those groups again. Sessions, levels, killzones, previous
periods, opening prices and the opening range keep their settings.

### Removed

- **Session VWAP** — the line, its anchors and its bands — is taken out for now. The code is kept on the
  `feature/vwap` branch.

### Added

- Tests for `tools/check.py` (`tests/test_check.py`): every check on passing input and on each problem it
  reports.
- `pyproject.toml` and `uv.lock`: the Python tools — ruff, pytest and coverage — are installed and run with uv.
- FAQ and publishing guide: when the Indicators dialog renews its cached Favorites list — after 24 hours without
  being opened, on sign-out, or when the site data is cleared.

### Changed

- The settings groups after the opening range are renumbered: *⑨ Time tools*, *⑩ Dashboard*, *⑪ Style*. Earlier
  entries of this file use the numbers of their time.
- CI installs uv, lints and format-checks the Python tools, runs their tests and then checks the indicator.
- `tools/check.py` follows the ruff rules of the project; what it checks is unchanged.

### Fixed

- The FAQ and the publishing guide said that an indicator added from the publication follows its updates. It
  does not: it stays on the version it was added with until it is added again, and the Indicators dialog can add
  the previous version from its cached Favorites list.

## [1.4.0] - 2026-11-25

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
  <https://www.tradingview.com/script/ticv4Yo6-Custom-Sessions-Indicator/>
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

[Unreleased]: https://github.com/DmytroPalahin/sessions-indicator/compare/v4.4.0...HEAD
[4.4.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v4.3.1...v4.4.0
[4.3.1]: https://github.com/DmytroPalahin/sessions-indicator/compare/v4.3.0...v4.3.1
[4.3.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v4.2.0...v4.3.0
[4.2.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v4.1.0...v4.2.0
[4.1.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v4.0.0...v4.1.0
[4.0.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v3.0.0...v4.0.0
[3.0.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v2.1.1...v3.0.0
[2.1.1]: https://github.com/DmytroPalahin/sessions-indicator/compare/v2.1.0...v2.1.1
[2.1.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v1.4.0...v2.0.0
[1.4.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/DmytroPalahin/sessions-indicator/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/DmytroPalahin/sessions-indicator/releases/tag/v1.0.0
