# FAQ and troubleshooting

## Nothing is drawn

Check these in order.

1. **Timeframe.** Sessions are hidden above *① General → Hide sessions above, minutes* (60 by default). Switch to
   a lower timeframe or raise the limit.
2. **History.** Only the last *History, days* are drawn. Scroll to recent bars or raise the value.
3. **The slot is off.** In *② Sessions* the checkbox of the row must be ticked.
4. **The market does not trade then.** A stock chart without extended hours has no bars at 08:00 London time, so
   there is no London session to draw.

## London is set to 08:00 – 16:00 but my chart shows it at another time

The hours of a session row are the local time of the city on that row, not the time on your chart. London
`0800-1600` is 8 to 16 o'clock in London. A chart set to Paris or Berlin time shows that session from 09:00 to
17:00, a chart set to New York time from 03:00 to 11:00 — the same eight hours, read on another clock. With the
defaults a Paris or Berlin chart shows Asia at 00:00 – 08:00, Frankfurt at 08:00 – 09:00, London at 09:00 – 17:00
and New York at 14:00 – 22:00.

Nothing has to be converted and no timezone has to be selected for this. A script cannot see where you are or
which timezone your chart uses, so every row names its own city instead.

## What is the timezone in *① General* for?

*Killzones and opens timezone* is the clock of every time that is not a session row: the killzones, the opening
range window, the midnight and custom opens and the day labels. Those are New York conventions, so the default is
`America/New_York`. It is not your own timezone, and there is no need to change it to the place you live in.

Sessions ignore it, unless a row has the city `As in ①`: that row is read in this timezone. Use it for the exchange
timezone, or for a zone that is not in the list of cities — select `Custom` and type the zone into
*Custom timezone*.

## What is the *Custom timezone* field for?

Only for the case when *① General → Killzones and opens timezone* is set to `Custom`: then the killzones, the
opens and the session rows with the city `As in ①` are read in the zone typed there. With any other choice the
field is ignored. The value it shows is an example, not your location and not a setting you need to match to the
season.

## A session is shifted by an hour

- The city of the row is not the one you mean: `Frankfurt` and `London` are an hour apart.
- The row has the city `As in ①` and *① General* holds a fixed offset such as `UTC+3`. Offsets do not follow
  daylight saving time. Use a named zone instead.
- The city changed its clocks and yours did not, or the other way round — see the next entry.

## The sessions move on my chart for a few weeks in spring and autumn

Every session follows the clock of its own city. The United States, Europe and Australia change their clocks on
different dates, and Tokyo does not change them at all. So for a few weeks a year the distance between two sessions
on the chart is an hour shorter or longer than usual, and Asia moves by an hour against a European or American
chart twice a year. This is real: the markets do open at another time on your clock then.

## After the update to 3.0.0 my sessions are in the wrong place

Up to 2.1.1 the hours of every session were read in one timezone, New York by default. From 3.0.0 on they are the
local time of the city on the row, and the settings changed order. Three things to know:

- An indicator that is already on a chart keeps the version it was added with, so nothing moves until you add it
  again.
- Settings saved as your defaults for an older version are applied by position and no longer fit. Open the
  settings and press **Defaults → Reset settings**.
- Hours you used to type in New York time are now read on the clock of the row's city. Either type them in the
  local time of that city, or set the city of the row to `As in ①`: then the hours are read in the timezone of
  *① General*, as before.

## The box does not start exactly at the session time

A session starts on the first bar that opens inside the window. On a 1-hour chart a 09:30 start can only be shown
from the 10:00 bar. Use a timeframe that divides the session time evenly.

## The candles got squeezed after I switched on weekly or monthly levels

TradingView fits every line an indicator draws into the price scale. A monthly high far above price therefore
compresses the candles. Two ways out:

- *⑪ Style → Hide levels farther than, × ADR* — set it to `2` or `3` and distant levels are not drawn;
- right-click the price scale and tick **Scale price chart only** — the scale then ignores all indicators.

## The level labels are cut off at the right edge

By default a level label sits at the right end of its line — over it, or under it for a low — and that end is
*① General → Level labels offset, bars* after the last bar (5 by default). The label is complete as long as the right
margin of the chart is at least that wide; TradingView's default margin is 10 bars. If you made the margin
narrower, drag the chart to the left or lower the offset.

With *⑪ Style → Level labels position* set to `After the line` the text follows the line instead. It then needs
room for the whole text after the line end, which the default margin does not give to longer labels such as
`London High`.

## Two level labels are printed over each other

Two levels share one price — for example London and New York made the same high. Every level has its own label,
and two labels at one price overlap. Nothing is wrong with the levels themselves. One label for such levels is on
the roadmap.

## A session label is crossed by candles

The label sits above the high of its session. After a short session such as Frankfurt, which lasts one hour, price
often keeps moving through that spot and the next candles cross the text. A shorter label helps: choose `Name` or
`Range` in *③ Session display → Label*.

## Some old sessions are missing

TradingView keeps the newest 500 boxes, 500 lines and 500 labels of a script and deletes the oldest. Lower
*History, days* or switch off modules you do not use.

## The text of a label is a shade darker than its line

That is on purpose. A label takes the colour of its line or zone, and most default colours are chosen for dark
charts: on a white background yellow, orange, light green and grey text is hard to read. With *⑪ Style → Label
text adapts to the chart background* on, which is the default, such a colour is darkened on a light chart and
lightened on a dark one until the text reads well. Lines and zones keep the colour you chose. Switch the setting
off to print text in the exact colour.

A thin line in a pale colour can still be faint on a white chart. Pick a darker colour for it in the input next
to the line it belongs to.

## The dashboard says a session is open on Saturday

The status follows the clock and the session schedule. It does not know the exchange calendar, so weekends and
holidays are not excluded.

## The dashboard countdown does not move

A script runs when the chart receives a tick. On a closed market there are no ticks, so the table shows the last
computed values.

## The "Avg" column is empty

The average needs at least one completed session on the chart. On timeframes above the session limit there are no
sessions to average.

## Can a session fill the whole height of the chart?

Yes. Set *③ Session display → Style* to `Background`: every session shades the chart from top to bottom, like a
classic session-highlight indicator. `Box + background` draws the range box on top of the band. *Background
transparency* sets how strong the shade is.

## Where did the session VWAP go?

It is taken out of the indicator for now. The code is kept on the `feature/vwap` branch of the repository and may
return in a later release.

## Can I use a 24-hour session?

Yes. A window such as `1800-1800` restarts every day at its start time. The same logic keeps sessions correct on
charts with regular trading hours only, where the last bar of one day is followed directly by the first bar of the
next.

## Does it repaint?

Previous day, week and month values do not: they are read with a one-bar offset. The high and low of the session
that is *still running* move while the session makes new extremes — that is what a running range is. Opening range
breakout markers appear only after a bar has closed.

## I updated the script but the chart still shows the old version

An indicator that is already on a chart keeps the version it was added with. That holds for a script you saved in
the Pine Editor and for the publication alike: reloading the chart does not move it to a newer version.

- **Your own saved script.** After saving a new version, press **Update on chart** in the editor (the button next
  to the script name), or remove the indicator and add it again from *Indicators → My scripts*.
- **The publication.** Remove the indicator from the chart and add it again.

If the indicator you just added from *Favorites* is still the old version, the Indicators dialog is the reason. It
keeps its Favorites list in the browser's cache, versions included. A favourite that is already in that list is not
asked for again, and each time the dialog opens the list is stored anew — so the old version stays for as long as
you open the dialog at least once a day. The list is dropped, and the current version loaded, in three cases:

- the dialog has not been opened in that browser for 24 hours;
- you sign out of TradingView;
- you clear the cached data of the TradingView site.

Each browser and the desktop app keep their own copy. Adding your own saved script from *My scripts* gave the
newest version at once.

Settings you changed by hand stay as you set them; *Settings → Defaults → Reset settings* brings back the defaults
of the new version.

## Can I rename "Asia" to something else?

Yes. The name field in each row is free text, and the new name is used in labels and in the dashboard.

## Pips look wrong on my symbol

`Pips` is defined for forex pairs: 0.0001, or 0.01 for JPY pairs. On other markets it falls back to the minimum tick.
Choose `Price`, `Ticks` or `Percent` in *③ Session display → Range unit* instead.

## Where do I get the indicator?

From its [page on TradingView](https://www.tradingview.com/script/ticv4Yo6-Custom-Sessions-Indicator/): press **Use on chart**. The publication is protected, so TradingView does
not show its code there; the same code is open in this repository, in
[src/custom_sessions_indicator.pine](../src/custom_sessions_indicator.pine).

## Still stuck?

See [SUPPORT.md](../SUPPORT.md).
