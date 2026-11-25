# Alerts

The indicator offers alerts in two ways. Both need a TradingView alert created by you — a script cannot create one.

## Option A — one alert for everything (recommended)

Dynamic events carry your own session names: `EURUSD · Session started: London`.

1. In the indicator settings open **⑫ Alerts** and tick the events you want.
2. Press **Alt + A** (or the alarm-clock button) to open *Create alert*.
3. Set **Condition** to `Custom Sessions Indicator`, then choose **Any alert() function call**.
4. Choose how to be notified and press **Create**.

One alert now delivers every event you ticked.

> An alert keeps the settings the indicator had when the alert was created. After changing the indicator settings,
> delete the alert and create it again.

| Event | Message | Fires |
|-------|---------|-------|
| Session start | `Session started: London` | on the first tick of the session |
| Session end | `Session ended: London` | on the first tick after the session |
| Killzone start | `Killzone started: NY AM KZ` | on the first tick of the killzone |
| Session level broken | `Broken above: Asia High` / `Broken below: Asia Low` | when price trades through the level |
| Previous high / low broken | `Previous D high broken` (`D`, `W` or `M`) | when price trades through the level |
| Opening range breakout | `Opening range breakout up` / `down` | when a bar closes outside the range |

With **Wait for bar close** on (the default), level and previous high / low alerts are sent when the bar closes. Turn
it off to be notified on the first tick that crosses. Opening range breakouts always wait for the close, because a
breakout is defined by it.

## Option B — one alert per condition

Use this when you want a different sound or message for one specific event.

In *Create alert* set **Condition** to `Custom Sessions Indicator` and pick one of:

| Condition | Needs |
|-----------|-------|
| Session started | — |
| Session ended | — |
| Killzone started | ⑤ Killzones on |
| Session high broken | ④ Session high / low levels on |
| Session low broken | ④ Session high / low levels on |
| Previous day high broken | — |
| Previous day low broken | — |
| Opening range breakout up | ⑧ Opening range on |
| Opening range breakout down | ⑧ Opening range on |

For these conditions choose the trigger yourself: **Once per bar** for the first crossing tick, **Once per bar close**
to wait for the close.

## Build your own

The running high and low of every session slot are published to the Data Window as `Session 1 high`, `Session 1 low`
and so on. In *Create alert* you can compare price with them directly, for example *Price crossing Session 2 high*.
The value exists while the session is open.

## Troubleshooting

| Symptom | Cause |
|---------|-------|
| No alerts at all | No TradingView alert was created, or **Enable alert() events** is off. |
| Session alerts never fire on a 4-hour chart | Sessions are hidden above the timeframe set in *① General*. |
| The alert uses old session times | The alert was created before the settings changed. Recreate it. |
| No "session level" alerts | *④ Session high / low levels* is off, so there are no levels to break. |
