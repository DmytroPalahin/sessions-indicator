# Settings reference

Every input of the indicator, in the order of the settings panel. Inputs without a visible title sit on the same row
as the titled input before them.

> **Tip.** Hover the ⓘ icon next to an input in TradingView to read the same explanation without leaving the chart.

## ① General

| Input | Default | What it does |
|-------|---------|--------------|
| Timezone | `America/New_York` | The timezone in which every time of this indicator is read. `Exchange` follows the symbol. Named zones follow daylight saving time automatically. |
| Custom timezone | `UTC+3` | Used only when *Timezone* is `Custom`. Accepts an IANA name (`Europe/Kyiv`) or an offset (`UTC+3`). An offset does not follow daylight saving time. |
| History, days (0 = all) | `20` | Drawings older than this many days are skipped. `0` draws the whole loaded history. |
| Hide sessions above, minutes | `60` | Sessions, killzones and the opening range are hidden on chart timeframes above this value. |
| Level labels offset, bars | `8` | How far to the right of the last bar the level lines and their labels end. |

## ② Sessions

Five rows. Each row is: checkbox · name · time window · colour.

| Slot | Name | Window | On |
|------|------|--------|----|
| 1 | Asia | `1900-0400` | yes |
| 2 | London | `0300-1200` | yes |
| 3 | New York | `0800-1700` | yes |
| 4 | Sydney | `1700-0200` | no |
| 5 | Custom | `0930-1600` | no |

A window may cross midnight and may be up to 24 hours long (`1800-1800` restarts every day at 18:00).

## ③ Session display

| Input | Default | What it does |
|-------|---------|--------------|
| Style | `Box` | `Box` frames the session range. `Background` shades the whole height of the chart. `Box + background` does both. `Hidden` keeps the session active for levels, alerts and the dashboard without drawing it. |
| Box fill transparency | `90` | 0 is solid, 100 is invisible. |
| Background transparency | `92` | Same scale, for the `Background` style. |
| Border transparency | `40` | Same scale, for the box border. |
| Border | `Solid`, `1` | Line style and width of the box border. |
| Label | `Name + range`, `Left` | What the caption above the session says, and where it sits. `Hidden` removes it. |
| Range unit | `Auto` | Unit of every range in labels and in the dashboard: `Price`, `Ticks`, `Pips` or `Percent`. `Auto` uses pips on forex and price elsewhere. |
| Open line | off | A dotted line at the opening price of the session. |
| Midline (50%) | off | A dashed line at the middle of the session range. It moves while the range grows. |

## ④ Session high / low levels

| Input | Default | What it does |
|-------|---------|--------------|
| Extend session high / low until broken | off | When a session ends, its high and low stay as lines. A high is broken by a higher high, a low by a lower low. |
| Broken levels | `Keep, faded` | `Keep, faded` stops the line at the breaking bar and dims it. `Remove` deletes it. |
| Max levels on chart | `12` | The oldest level is removed when this number is exceeded. |

## ⑤ Killzones

| Input | Default | What it does |
|-------|---------|--------------|
| Show killzones | off | Master switch for all five rows. |

| Slot | Name | Window |
|------|------|--------|
| 1 | Asia KZ | `2000-0000` |
| 2 | London KZ | `0200-0500` |
| 3 | NY AM KZ | `0700-1000` |
| 4 | NY Lunch | `1200-1300` |
| 5 | NY PM KZ | `1330-1600` |

| Input | Default | What it does |
|-------|---------|--------------|
| Style | `Background` | Same choices as for sessions. |
| Box fill transparency | `88` | Used by the `Box` styles. |
| Background transparency | `90` | Used by the `Background` styles. |
| Label | `Name`, `Left` | Caption content and position. Killzone captions sit below the zone, so they do not collide with session captions above it. |

## ⑥ Previous day / week / month

| Input | Default | What it does |
|-------|---------|--------------|
| Previous day high / low | off | Lines labelled `PDH` and `PDL`. |
| Previous week high / low | off | Lines labelled `PWH` and `PWL`. |
| Previous month high / low | off | Lines labelled `PMH` and `PML`. |
| Keep past periods | off | Keeps the lines of earlier days, weeks and months. Also applies to *⑦ Opening prices*. |

A period is shown only on chart timeframes lower than the period itself.

## ⑦ Opening prices

| Input | Default | Label on the chart |
|-------|---------|--------------------|
| Day open | off | `D Open` |
| Week open | off | `W Open` |
| Month open | off | `M Open` |
| Midnight open (00:00) | off | `00:00 Open` — the first bar of the calendar day in the indicator timezone |
| Custom open (hour, minute) | off, `8`, `30` | `08:30 Open` — the bar that opens at this time |

Day, week and month follow the trading calendar of the symbol. Midnight and the custom time follow the indicator
timezone.

## ⑧ Opening range

| Input | Default | What it does |
|-------|---------|--------------|
| Show opening range | off | Master switch. |
| Window | `0930-1000` | The window in which the range is measured. |
| Colour | cyan | Colour of the box, the lines and the markers. |
| Extend for, hours | `6.0` | How long the lines keep extending after the window closes. |
| Midline | on | A dashed line at the middle of the range. |
| Projection 1 × | `1.0` | Lines at one range above the high and below the low. `0` turns them off. |
| Projection 2 × | `0.0` | A second pair of projections. |
| Breakout markers | on | A triangle on the first bar that closes outside the range, once per side. |

## ⑨ Session VWAP

| Input | Default | What it does |
|-------|---------|--------------|
| Show VWAP | off | Master switch. Needs a symbol with volume. |
| Anchor | `Each session start` | Where the calculation restarts: every enabled session, or each day, week or month. |
| Colour, width | yellow, `1` | Look of the line. |
| Bands × | `0.0` | Standard-deviation multiplier of the bands. `0` hides them. |

## ⑩ Time tools

| Input | Default | What it does |
|-------|---------|--------------|
| Day separators | off | A dotted vertical line at the first bar of each calendar day in the indicator timezone. |
| Weekday labels | off | `Mon`, `Tue`, … below that bar. |

## ⑪ Dashboard

| Input | Default | What it does |
|-------|---------|--------------|
| Show dashboard | off | Master switch. |
| Position | `Top right` | Corner or side of the chart. |
| Text size | `Small` | Size of the table text. |
| Average length | `20` | Number of completed sessions and days behind the `Avg` column. |
| Day range row | on | Adds the day range and its share of the average daily range. |

Columns: session name · status (`Open · 2h 05m left` or `Opens in 5h 03m`) · current or latest range · average
range.

## ⑫ Style

| Input | Default | What it does |
|-------|---------|--------------|
| Text size | `Small` | Size of every label on the chart. |
| Dashboard text follows the chart theme | on | Dark text on light charts, light text on dark charts. |
| Dashboard text colour | light grey | Used when the option above is off. |
| Level lines | `Solid`, `1` | Style and width of session levels, previous highs and lows, and opening prices. |
| Level labels | on | Text at the right end of each level line. |
| Price in level labels | off | Appends the price to the label. |
| Hide levels farther than, × ADR (0 = never) | `0.0` | Levels farther from the last price than this many average daily ranges are not drawn. Use it when a distant weekly or monthly level squeezes the candles. Session levels fold back to the bar where they formed. |
