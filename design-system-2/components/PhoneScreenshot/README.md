# PhoneScreenshot

A screenshot shown inside a phone outline: `device` bezel, a screen with a pill-shaped camera cutout, status bar and home indicator. It's the one piece of evidence with rounded corners, because phones are. The rounding comes from the object (`radius-device`), not from the game.

- `app`: `messages` (default) or `calls`. Or pass any `children` to draw a custom screen (map, photo, banking app).
- Messages: `contact`, `messages: [{ from: 'them' | 'me', text } | { day } | { receipt }]`.
- Calls: `calls: [{ name, time, missed, kind }]`.
- `time` (status bar, 24-hour) and `battery` (0–100) are evidence too: teams can read them.
- Bubbles are neutral grey and near-black, never blue or red. The thread stays the only brand red, and nothing copies a real phone maker's look.
- Wrap in `Evidence` with `device` set, so the shadow isn't doubled.
