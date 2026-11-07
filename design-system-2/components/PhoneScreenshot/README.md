# PhoneScreenshot

A screenshot shown inside a phone outline: `device` bezel, a screen with a pill-shaped camera cutout, status bar and home indicator. It's the one piece of evidence with rounded corners, because phones are. The rounding comes from the object (`radius-device`), not from the game.

- `app`: `messages` (default) or `calls`. Or pass any `children` to draw a custom screen (map, photo, banking app).
- Messages: `contact`, `messages: [{ from: 'them' | 'me', text } | { day } | { receipt }]`.
- Calls: `calls: [{ name, time, missed, kind, duration }]`.
- Screen readers get every message, each prefixed with who sent it (`contact` or "Me"), inside a group labelled with `label`. A long thread scrolls inside the screen instead of being cut off. Contacts without a name ("09 [redacted]") get a blank avatar, not stray initials.
- `time` (status bar, 24-hour) and `battery` (0–100) are evidence too: teams can read them.
- Bubbles are neutral grey and near-black, never blue or red. The thread stays the only brand red, and nothing copies a real phone maker's look.
- Wrap in `Evidence` with `device` set, so the shadow isn't doubled.
