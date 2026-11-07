# GameNote

The game talking to the team: instructions, hints, unlock prompts and briefings. A `note` off-white panel with `radius-note` corners, edged with `note-line` and **no shadow**. Rounded and flat means "this is the game", never something found in the story.

- `kind`: `instruction` (default), `hint` (a 2px dashed edge in `note-ink-muted`, visible in sun, so a hint never passes for an instruction), `unlock` (adds code cells: `codeLength`, `numeric`, `codeLabel`, `codeMessage`, `codeState="wrong" | "right"`, `onCode(value)`). Code cells accept a pasted code, move with the arrow keys, and lock in place once `codeState` is `right`. Wrong thickens the cell borders and keeps the message in words. Never red.
- `title` in Inter 20/600: an action ("Head to the Ferry Building"), not a label. `meta` / `metaEnd` sit in a mono footer (stop number, walking time, hint cost).
- Wrap one word in `<em>` for `note-accent` red. Once per note.
- Never white, never square, never `shadow-object`: those belong to evidence.
- Consumer provides: `title`, body (children), and optionally `kind`, `meta`, `metaEnd` and the unlock props.
