# FAQ and troubleshooting

## Nothing is drawn

Check these in order.

1. **Timeframe.** Sessions are hidden above *① General → Hide sessions above, minutes* (60 by default). Switch to
   a lower timeframe or raise the limit.
2. **History.** Only the last *History, days* are drawn. Scroll to recent bars or raise the value.
3. **The slot is off.** In *② Sessions* the checkbox of the row must be ticked.
4. **The market does not trade then.** A stock chart without extended hours has no bars at 03:00, so there is no
   London session to draw.

## I set the timezone to my own and every session moved

*① General → Timezone of session times* is the timezone in which the session times are **written**, not the timezone
you live in. The default times (`1800-0200`, `0200-0300`, `0300-1100`, `0800-1600`) are New York times. Select Berlin and the
same numbers are read as Berlin times, six hours away from where they should be.

Two ways to fix it:

- set the timezone back to `America/New_York` — recommended, the chart still shows your own clock;
- or keep your timezone and retype the windows in it. For Central European winter time: Asia `0000-0800`, Frankfurt
  `0800-0900`, London `0900-1700`, New York `1400-2200`.

## Sessions are shifted by an hour

The session times are read in the timezone from *① General → Timezone of session times*. Two common causes:

- You entered times for one timezone while another is selected.
- You use a fixed offset such as `UTC+3`. Offsets do not follow daylight saving time. Use a named zone instead.

## Why does the Asia session start at 18:00?

Because the default timezone is New York. 18:00 in New York is 08:00 in Tokyo while New York is on winter time. If
you prefer to think in another timezone, select it and enter the windows in that time.

## London and New York are "wrong" for a few weeks in March and November

The United States and Europe change their clocks on different dates. For two or three weeks a year the gap between
London and New York is four hours instead of five. With one timezone for all sessions, the session defined in the
other city's time shifts for those weeks. This is real: the markets do open at a different New York time then.

## The box does not start exactly at the session time

A session starts on the first bar that opens inside the window. On a 1-hour chart a 09:30 start can only be shown
from the 10:00 bar. Use a timeframe that divides the session time evenly.

## The candles got squeezed after I switched on weekly or monthly levels

TradingView fits every line an indicator draws into the price scale. A monthly high far above price therefore
compresses the candles. Two ways out:

- *⑫ Style → Hide levels farther than, × ADR* — set it to `2` or `3` and distant levels are not drawn;
- right-click the price scale and tick **Scale price chart only** — the scale then ignores all indicators.

## The level labels are cut off at the right edge

By default a level label sits at the right end of its line — over it, or under it for a low — and that end is
*① General → Level labels offset, bars* after the last bar (5 by default). The label is complete as long as the right
margin of the chart is at least that wide; TradingView's default margin is 10 bars. If you made the margin
narrower, drag the chart to the left or lower the offset.

With *⑫ Style → Level labels position* set to `After the line` the text follows the line instead. It then needs
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

## VWAP is not plotted

VWAP needs volume. Some indices and some forex feeds have none. With the anchor *Each session start* the VWAP also
hides above the session timeframe limit.

## The VWAP line is hard to see

The default VWAP colour is yellow. It reads well on a dark chart and is faint on a light one. Pick a darker colour
in *⑨ Session VWAP → Colour*.

## The dashboard says a session is open on Saturday

The status follows the clock and the session schedule. It does not know the exchange calendar, so weekends and
holidays are not excluded.

## The dashboard countdown does not move

A script runs when the chart receives a tick. On a closed market there are no ticks, so the table shows the last
computed values.

## The "Avg" column is empty

The average needs at least one completed session on the chart. On timeframes above the session limit there are no
sessions to average.

## Can I use a 24-hour session?

Yes. A window such as `1800-1800` restarts every day at its start time. The same logic keeps sessions correct on
charts with regular trading hours only, where the last bar of one day is followed directly by the first bar of the
next.

## Does it repaint?

Previous day, week and month values do not: they are read with a one-bar offset. The high and low of the session
that is *still running* move while the session makes new extremes — that is what a running range is. Opening range
breakout markers appear only after a bar has closed.

## I updated the script but the chart still shows the old version

An indicator that is already on a chart keeps the version it was added with. After saving a new version in the Pine
Editor, either press **Update on chart** in the editor (the button next to the script name), or remove the
indicator from the chart and add it again from *Indicators → My scripts*. Settings you changed by hand stay as you
set them; *Settings → Defaults → Reset settings* brings back the defaults of the new version.

## Can I rename "Asia" to something else?

Yes. The name field in each row is free text, and the new name is used in labels and in the dashboard.

## Pips look wrong on my symbol

`Pips` is defined for forex pairs: 0.0001, or 0.01 for JPY pairs. On other markets it falls back to the minimum tick.
Choose `Price`, `Ticks` or `Percent` in *③ Session display → Range unit* instead.

## Where do I get the indicator?

From its [page on TradingView](https://www.tradingview.com/script/ticv4Yo6-Custom-Sessions-Indicator/): press **Use on chart**. The publication is protected, so TradingView does
not show its code there; the same code is open in this repository, in
[src/custom_sessions_indicator.pine](../src/custom_sessions_indicator.pine). An indicator added from the
publication follows its updates; reload the chart if a new version does not show up.

## Still stuck?

See [SUPPORT.md](../SUPPORT.md).
