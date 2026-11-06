# Receipt

A thermal till receipt: `evidence` white, square, set in `receipt` (Share Tech Mono, uppercase) with a torn bottom edge.

- `merchant`, `address`, `gstNumber`, `date`, `time`, `serial` (table or docket number), `server`.
- `lines`: `[{ qty, item, price }]`. `total`, `gst` (15% inclusive amount), `paid` (`Cash`, `EFTPOS`, `Visa`…), `tendered`, `card`, `footer`.
- `stamp`: an `evidence-mark` ink stamp ("Paid", "Void").
- Write `[redacted]` in any string for a black bar.
- Merchants are fictional. Streets are real (working rule 5). Prices in NZ$, dates DD/MM/YYYY, times 24-hour.
- Wrap in `Evidence` for the tag and shadow.
