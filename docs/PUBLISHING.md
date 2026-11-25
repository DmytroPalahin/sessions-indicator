# Publishing on TradingView

How a release goes from this repository to the TradingView community library.

The indicator is published at https://www.tradingview.com/script/ticv4Yo6-Custom-Sessions-Indicator/
as a public, protected script by `dmitry_plhn` (first published 2026-11-25 from version 1.2.0 of the code, with the
author line changed to the TradingView account name).

## Before you publish

- [ ] `python3 tools/check.py` passes.
- [ ] The compile check shows zero errors and zero warnings (see [TESTING.md](TESTING.md)).
- [ ] The chart matrix in [TESTING.md](TESTING.md) is complete and logged.
- [ ] `VERSION` in the script, the README badge and `CHANGELOG.md` show the new version.
- [ ] The release is tagged in git: `git tag -a v1.0.0 -m "v1.0.0"`.

## First publication

1. Open the script in the Pine Editor and **Save** it as `Custom Sessions Indicator`.
2. Prepare a clean chart: one symbol, the indicator only, no other drawings. TradingView uses the chart as the
   publication picture, and moderators reject cluttered ones.
3. Press **Publish script** and choose **Public**, then the visibility: **Open-source** shows the code to everyone,
   **Protected** hides it. The first publication of this indicator is protected; the same code stays open here.
4. Fill in the form with the texts below.

### Title

```
Custom Sessions Indicator
```

### Description

TradingView's House Rules ask a description to explain what the script does, how it does it and how to use it, in
your own words and without links that advertise. A text that fits:

```
Custom Sessions Indicator maps the trading day on an intraday chart. Out of the box it draws the Asia, Frankfurt, London and New York sessions as soft colour boxes; everything else is switched on module by module.

WHAT IT SHOWS
- Sessions: 5 slots. Name, time window and colour are editable. Drawn as a box, a background band, both or hidden, with an optional label that shows the name and the range in price, ticks, pips or percent.
- Session high / low levels: when a session ends, its high and low stay on the chart until price trades through them.
- Killzones: 5 more slots with their own style.
- Previous day / week / month high and low.
- Opening prices: day, week, month, midnight and one custom time.
- Opening range: the range of a chosen window, its extended lines, midline, projections and breakout markers.
- Session VWAP: re-anchored at each session, day, week or month, with optional bands.
- Dashboard: which session is open, time left or time to open, current range against its average, day range against the average daily range.

HOW IT WORKS
A session is the set of bars whose opening time falls inside its window; its high and low are tracked bar by bar. The default sessions are the 08:00-16:00 working day of each city, and Frankfurt is the hour before London opens. A new run of a session is detected by its calendar date, so sessions are also correct on regular-hours charts and can be up to 24 hours long. A session level is broken when a later bar trades beyond it. Previous day, week and month values are requested from the higher timeframe with a one-bar offset, so historical bars never use data from their future. An opening range breakout is a bar that closes outside the range.

HOW TO USE IT
Add the indicator to a chart of 60 minutes or lower. The session times are written in New York time: keep "Timezone of session times" on America/New_York unless you retype the times for another zone - the chart still shows your own clock. Then switch on the modules you need. Everything except the four main sessions is off by default.

LIMITATIONS
Sessions need an intraday chart. VWAP needs volume. Levels far from price can squeeze the price scale; "Hide levels farther than" removes them. The dashboard follows the clock and does not know about weekends and holidays.

This script is a charting tool, not financial advice.
```

### Category and tags

- Category: **Trend analysis** or **Chart patterns** — pick the closer one in the form.
- Tags: `sessions`, `killzones`, `liquidity`, `vwap`, `openingrange`.

## Updating a published script

1. Open the published script from the Pine Editor (**Open → My scripts**).
2. Replace its code with the new version and **Save**.
3. Press **Publish script → Update existing**.
4. Paste the changelog section of the release as the release notes.

An update must describe what changed. The text of the matching `CHANGELOG.md` section does that.

## Rules worth remembering

- A script can be edited freely for 15 minutes after publication; after that only updates are possible.
- A public open-source script cannot be made private later.
- The description may not contain links that sell or advertise.
- Moderators hide scripts that duplicate existing ones without adding anything; the description should say what is
  different here.

Read the current [House Rules](https://www.tradingview.com/house-rules/) and
[Script Publishing Rules](https://www.tradingview.com/support/solutions/43000590599/) before publishing — they change.
