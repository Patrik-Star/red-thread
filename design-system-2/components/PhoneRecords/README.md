# PhoneRecords

An itemised call record from a phone company: a printout in `doc` type (Arimo), so it looks like someone else's office printer rather than the game.

- `carrier` (fictional), `holder`, `number`, `period`, `footer`.
- `rows`: `[{ date, time, dir, to, duration, marked }]`. `dir` is `out`, `in`, `missed`, `sms` or `sms-in`.
- `marked: true` sets the row in bold and underlines it in `evidence-mark` pen, as if a detective had marked it before you. Use it once per document, at most.
- Write `[redacted]` in a number for a black bar. Never print a full real-looking phone number.
- Wrap in `Evidence`.
