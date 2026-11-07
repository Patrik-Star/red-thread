# Printout

Any other printed log from someone else's system: a taxi company's trip record, a building's door-swipe log, an office inventory. Same paper as PhoneRecords and BankStatement, with your own columns.

- `org` (fictional), `title` (right of the header: "Trip record", "Access log"), `info`: `[[label, value]]`.
- `columns`: `[{ label, align: 'right', wrap: true }]`. `rows`: arrays of cells, or `{ cells, marked }` to underline a row in pen.
- Cells don't wrap unless the column has `wrap`. Give the free-text column `wrap` so the table fits a phone.
- `footer`: the small print the system adds ("Times are NZDT").
- Wrap in `Evidence`.
