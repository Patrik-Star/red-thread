# Receipt

A thermal till receipt: `evidence` white, square, set in `receipt` (Share Tech Mono, uppercase) with a torn bottom edge.

- `heading` ("Tax invoice", printed above the merchant), `merchant`, `address`, `gstNumber`, `date`, `time`, `serial` (table or docket number), `server`.
- `lines`: `[{ qty, item, price }]`. `total`, `gst` (15% inclusive amount), `paid` (`Cash`, `EFTPOS`, `Visa`…), `tendered`, `card`, `footer`, `subtotal`. `extra`: `[[label, value]]` for EFTPOS slip lines (Acct, Auth, Approved). Leave `total` out and no TOTAL line prints.
- `stamp`: an `evidence-mark` ink stamp ("Void", "Refunded", "Received"). Use it only where someone in the story would stamp paper. A restaurant till slip has no stamp.
- Card numbers print as asterisks only. Never print the last four digits.
- Write `[redacted]` in any string for a black bar.
- Merchants are fictional. Streets are real (working rule 5). Prices in NZ$, dates DD/MM/YYYY, times 24-hour.
- Wrap in `Evidence` for the tag and shadow.
