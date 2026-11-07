# Evidence

The wrapper for every piece of physical evidence: a manila tag from the game, clipped to a white, square object from the story.

It pairs two layers:

1. **The EvidenceTag** (game layer): a `manila` tag with a punched hole, `radius-tag` corners, the number, status, title and where it was found. This is the game's filing, so it's rounded.
2. **The object** (story layer): any evidence component as children (Receipt, Ticket, PhoneRecords…). Square, white and lifted with `shadow-object`.

- `number`, `title`, `found`: shown on the tag. With no `number` the tag says "Evidence" alone. Leave all three out for a bare object.
- `status`: `new`, `found` (shown as "Filed") or `locked`. Locked blurs the object inside its own edges, hides it from screen readers and lays a small GameNote over it with `lockedText`, so the game's voice explains the lock. The blur is a look, not a lock. In production, pass a decoy object (same component, `[redacted]` text) while locked, and send the real contents only after the code is entered, or teams can read them in the page source.
- `device`: set it when the child is a `PhoneScreenshot`, which carries its own shadow.
- `caption`: optional text for screen readers describing the object.
- In a sequence, run the red thread between tags, never between objects (one thread, see the thread rule).
