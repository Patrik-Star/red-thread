# Button

Actions are 44px tall so they work with cold fingers on a phone in the street.

- **`primary`**: a `thread` fill with `on-thread` text. Use it **once per screen** for the action the screen is for ("Open the case file", "Submit your accusation"). It counts as that screen's red.
- **`ghost`** (default): a `line-strong` outline with `ink` text. Use it for everything else.
- `size="sm"` (36px) for dense toolbars only.
- Labels start with a verb, in sentence case, with no exclamation marks.
- Consumer provides: the label (children) and `onClick`. Other button attributes pass through.
