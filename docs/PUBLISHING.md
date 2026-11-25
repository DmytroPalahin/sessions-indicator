# Publishing on TradingView

How a release goes from this repository to the TradingView community library.

## What is published now

| | |
| --- | --- |
| Page | <https://www.tradingview.com/script/ticv4Yo6-Custom-Sessions-Indicator/> |
| Author | [dmitry_plhn](https://www.tradingview.com/u/dmitry_plhn/) |
| Access | Public, protected: everyone can add it to a chart, TradingView does not show the code. The code is open here. |
| Code | Version 1.4.0 — the file at the tag `v1.4.0` |
| First published | 2026-11-25, from version 1.2.0 |
| Latest update | 2026-11-25, version 1.4.0; the page carries the release notes of 1.3.0 and 1.4.0 |
| Categories | Multi-timeframe · Pivot points and levels |
| Tags | `sessions`, `killzones`, `forex` |
| Picture | `OANDA:EURUSD`, 15 minutes, default settings |

The description on that page is the text in [Description](#description) below; the release notes of each update
follow it there.

## Before you publish

- [ ] `python3 tools/check.py` passes.
- [ ] The compile check shows zero errors and zero warnings (see [TESTING.md](TESTING.md)).
- [ ] The chart matrix in [TESTING.md](TESTING.md) is complete and logged.
- [ ] `VERSION` in the script, the README badges and `CHANGELOG.md` show the new version.
- [ ] The release is tagged in git: `git tag -a vX.Y.Z -m "vX.Y.Z"`.

## The chart is the picture

TradingView takes the publication picture from the chart that is open when you press **Publish script**, and it
takes a new one with every update. Prepare the chart first:

- one symbol, this indicator only, no other indicators and no drawings — moderators reject cluttered pictures;
- a liquid symbol and an intraday timeframe on which the sessions are easy to read (`OANDA:EURUSD`, 15 minutes);
- default settings, so the picture shows what a new user gets;
- two or three days on screen.

Keeping a separate chart layout for this makes the picture repeatable.

## First publication

1. Open the script in the Pine Editor and **Save** it as `Custom Sessions Indicator`.
2. Open the prepared chart and add the saved script to it.
3. Press **Publish script** and choose **Public**, then the visibility: **Open-source** shows the code to everyone,
   **Protected** hides it. This indicator is published as protected; the same code stays open here.
4. Fill in the form with the texts below, tick the House Rules box and publish.

### Title

```
Custom Sessions Indicator
```

### Description

TradingView's House Rules ask a description to explain what the script does, how it does it and how to use it, in
your own words and without links that advertise. The description field is plain text. The text of the publication:

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

The text is final on TradingView and still lists the session VWAP. That module is parked on the `feature/vwap`
branch; the release notes of the update that removes it have to say so.

### Category and tags

- Categories: **Multi-timeframe** and **Pivot points and levels**.
- Tags: `sessions`, `killzones`, `forex`.

## Updating a published script

1. Open the saved script in the Pine Editor (**Open → My scripts**).
2. Replace its code with the new version and **Save**.
3. Open the prepared chart, so the update gets a clean picture. The saved script itself must be on it: an
   indicator added from the publication does not count, and TradingView then offers to add the saved one. Remove
   the other copy, so the picture shows the indicator once.
4. Press **Publish script → Update existing script**.
5. Choose `Custom Sessions Indicator` in the list of published scripts and leave *Don't update the chart*
   unticked.
6. Write the release notes: the version, then the changes of the matching `CHANGELOG.md` section in plain text.
7. On the next page keep **Public** and **Protected**, tick the House Rules box and press **Publish new version**.

An update must describe what changed; the matching `CHANGELOG.md` section does that. Publish an update when the code
changes, not to edit the page: the release notes are added under the first description, which stays as it is.

An update does not change charts by itself. An indicator that is already on a chart, added from the publication
or from the saved script, stays on the version it was added with until it is removed and added again. The new
version is the one that gets added from then on — with one catch: the Indicators dialog keeps its Favorites list
in the browser's cache, version included, so a browser that opened the dialog before the update can go on adding
the previous version. A favourite already in that cache is not requested again, and the cache is written anew at
every opening of the dialog; it is dropped only after 24 hours without being written, on sign-out, or when the
site data is cleared. Someone who opens the dialog every day therefore keeps getting the old version from
*Favorites* until one of those happens. To check what the service itself serves, read
`https://pine-facade.tradingview.com/pine-facade/versions/<pine id>`; the pine id of this publication starts with
`PUB;550e`. A copy pasted from this
repository into someone's own Pine Editor does not change until they paste the new file.

## Rules worth remembering

- A publication can be edited or deleted for 15 minutes. After that the title and the description are final, and
  only updates with release notes are possible.
- A public open-source script cannot be made private later.
- The description may not contain links that sell or advertise. For that reason the publication does not link to
  this repository, while the repository links to the publication.
- Moderators hide scripts that duplicate existing ones without adding anything; the description should say what is
  different here.
- The copyright line of a published script names the TradingView account that publishes it.

Read the current [House Rules](https://www.tradingview.com/house-rules/) and
[Script Publishing Rules](https://www.tradingview.com/support/solutions/43000590599/) before publishing — they change.
