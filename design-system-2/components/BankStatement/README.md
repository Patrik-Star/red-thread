# BankStatement

A page of a bank statement in `doc` type, with tabular figures so the columns line up.

- `bank` (fictional), `holder`, `account`, `period`, `footer`.
- `rows`: `[{ date, details, out, in, balance, marked }]`. Columns print as Debit, Credit and Balance. Start with a `Balance brought forward` row, and write card and transfer details the way a bank does: `EFTPOS HALFMOON NOODLE BAR AKL`, `TRANSFER FROM M REID`.
- Account numbers: redact the bank and branch (`[redacted]-0047-00`). A real two-digit NZ bank prefix names a real bank. Amounts are strings in NZ$ ("2,000.00").
- `marked` underlines a row in pen. `[redacted]` gives a black bar.
- Good for money trails: a transfer that comes back, a payment at a time someone says they weren't there.
- On a phone (under 360px of printable width) the table tightens and wraps Details instead of clipping the amount columns.
- Wrap in `Evidence`.
