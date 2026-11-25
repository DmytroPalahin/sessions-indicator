# Security policy

## Scope

This repository contains a TradingView indicator and a small check script. The indicator runs inside TradingView's
sandbox: it cannot read files, reach the network, place orders or see your account. It handles no credentials.

Things that still count as security problems here:

- code in this repository that could run something unexpected on a contributor's machine or in CI;
- a workflow change that could leak repository secrets;
- an indicator behaviour that misleads on purpose, such as using future data to look better than it is.

## Supported versions

Only the latest release receives fixes.

## Reporting

Please do not open a public issue for a security problem. Use
[private vulnerability reporting](https://github.com/DmytroPalahin/sessions-indicator/security/advisories/new)
instead. You can expect a first answer within a week.

## A note on copies

The only official sources of this indicator are this repository and the
[TradingView publication](https://www.tradingview.com/script/ticv4Yo6-Custom-Sessions-Indicator/) by `dmitry_plhn`. Be careful with copies from elsewhere, and never give your TradingView password or broker access to anyone
offering a "premium" version.
