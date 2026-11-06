# CaseTag

A mono, uppercase file label for status: case number, open/solved, team size.

- `open`: `thread-text`. The case is live.
- `solved`: `solved`. Confirmed correct. It differs from open in lightness and label, not hue alone.
- `neutral` (default): `ink-muted`, a hollow dot. Use it for facts like "Team of 4".
- Keep it to 1–4 words. Use `·` as a separator: "Case 07 · Open".
- Consumer provides: the text.
