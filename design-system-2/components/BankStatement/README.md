# BankStatement

A page of a bank statement in `doc` type, with tabular figures so the columns line up.

- `bank` (fictional), `holder`, `account`, `period`, `footer`.
- `rows`: `[{ date, details, out, in, balance, marked }]`. Amounts are strings in NZ$ ("2,000.00").
- `marked` underlines a row in pen. `[redacted]` gives a black bar.
- Good for money trails: a transfer that comes back, a payment at a time someone says they weren't there.
- Wrap in `Evidence`.
