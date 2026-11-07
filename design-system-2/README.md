# Red Thread

**Red Thread** is a real-world mystery game. Teams of 3–6 people walk the streets of Auckland CBD (Tāmaki Makaurau) with a case file, following evidence from stop to stop until together they can name who did it, how and why.

The name comes from the investigator's corkboard: photos, notes and places, joined by one red string. The brand works the same way. **A single red thread runs through everything** (posters, the app, evidence cards, the case box) and links each piece to the next.

The feel is **dark, mysterious and modern**: night streets, wet pavement, a city keeping secrets. It is a contemporary game you play with your phone in hand, not a Victorian pastiche. Think minimal noir, not magnifying glasses and deerstalkers.

> **Version 2.** This copy builds on the first system (still in `design-system/`) and adds one structural rule: **the game and the evidence look different.** Game notes are rounded, flat and off-white. Physical evidence is square, pure white and casts a shadow. See section 2. There is still no final logo, photography or production code. The thread rule and the two-layer rule are the parts to keep.

---

## 1. The thread rule

The red thread is the brand's signature. Treat it like a logo.

1. **One thread per composition.** A single continuous line in `thread`. It never splits, never runs as two parallel strands, and never becomes a pattern.
2. **It connects things.** It runs from one element to the next: headline to evidence, evidence to map pin, chapter to chapter. A thread with nothing at either end is decoration. Cut it.
3. **It enters and leaves.** Let it bleed off the edge of the page or screen, so it seems to come from the previous piece and carry on to the next. On a multi-page layout, line its exit up with the next page's entry.
4. **It is the only red.** On any surface the thread, the primary button and pins share the one red. No red photos, no red backgrounds behind red thread, and no second accent colour.
5. **It's string, not a vector line.** Straight runs between pins with a slight sag, or a loose curve. No zig-zags, arrows or perfect geometric arcs. Width is `thread-width` (2px) in UI and `thread-width-hero` (3px) at poster scale.
6. **It's tied off at pins.** Where it changes direction it passes a pin: a small disc in `brass` (or `manila-thread` on manila). Pins use `radius-pill`: they're the only full circles in the system.
7. **It runs between tags, not objects.** In a line-up of evidence the thread goes pin to pin across the manila tags. It never crosses a receipt or a screenshot: the thread belongs to the game, and the objects belong to the story.

**Do:** run the thread from a case title, under a paragraph, to a map location. **Don't:** underline every heading in red, use red for errors, or draw the thread as a dashed "route" line. Dashed lines belong to tear-offs on paper (`manila-line`).

## 2. Two layers: the game and the evidence

Everything on a Red Thread screen comes from one of two places, and the team must be able to tell which at a glance.

| | **The game** (talking to you) | **The evidence** (found in the story) |
| --- | --- | --- |
| What | Instructions, hints, unlock prompts, briefings, buttons, tags, panels | Receipts, tickets, phone screenshots, phone records, statements, handwritten notes, CCTV stills |
| Corners | **Rounded.** `radius-note` 16px for notes and panels, `radius-control` 10px for buttons, `radius-tag` 6px for tags and inputs | **Square.** `radius-evidence` 0. The only exception is a phone, because phones are (`radius-device`) |
| Background | `note` #F3EFE6, an off-white (on screens it sits on `ground`) | `evidence` #FFFFFF, pure white, in both themes |
| Depth | **Flat.** A `note-line` hairline edge, never a shadow | **Lifted.** `shadow-object`: objects on the table cast shadows |
| Type | Inter for instructions, IBM Plex Mono for file labels, Instrument Serif for titles | The document's own type: `receipt` (Share Tech Mono), `doc` (Arimo), `hand` (Caveat, in `evidence-pen` blue-black), the phone's system font |
| Red | `thread`, `thread-text`, `note-accent` | `evidence-mark` only: ink stamps and pen marks |

**The manila tag joins them.** Each object arrives with an `EvidenceTag` clipped to its top edge: a manila tag with the evidence number, status, title and where it was found. The tag is the game's filing, so it's rounded. The object under it is the story, so it's square. See the **Evidence** component.

Three tests:
1. **Cover the words.** From shape and shadow alone, can you tell which pieces are the game and which are evidence? If not, something is the wrong shape.
2. **No white notes, no off-white evidence.** The game never uses #FFF; evidence never uses `note`.
3. **The game never writes by hand.** Handwriting, thermal print and someone else's printer are evidence. The game speaks in Inter.

## 3. Voice: content fundamentals

Red Thread speaks like a **calm case officer briefing a capable team**: precise, a little dry, never breathless. The mystery does the work. The copy doesn't need to shout.

- **Short, declarative sentences.** Facts first, and let the gaps create the suspense.
- **Second person, plural.** "You have ninety minutes." The team is the detective, not "players" or "users".
- **Specific Auckland places**, named the way locals say them: Britomart, the Ferry Building, Vulcan Lane, Albert Park, Sky Tower. Use te reo Māori names with macrons (Tāmaki Makaurau, Waitematā).
- **New Zealand English:** colour, organise, centre, licence (noun), metres.
- **Records in mono.** In the game's own voice, times, coordinates and transcripts go in the `evidence` type style, written as records: `23:40`, `-36.8442, 174.7676`.
- **Evidence is written by the people in the story, not by us.** A receipt says what a till prints; a text says what a nervous person types. Don't let the case officer's voice leak into an object. Use fictional businesses, carriers and banks on real streets, and redact numbers instead of printing real-looking ones.
- **No exclamation marks, no emoji, and never the words "clue", "Cluedo", "sleuth" or "treasure hunt".** Gore and violence stay off the page. We imply the crime and never show it.

| Instead of | Write |
| --- | --- |
| "Get ready for an EPIC murder mystery adventure!!" | "A body was found at the Ferry Building at 23:40. You have ninety minutes." |
| "Awesome! You found item 3 🎉" | "Evidence 03 recovered. The ticket was bought with cash." |
| "Oops, wrong answer, try again!" | "That doesn't hold. Look at the timestamp again." |
| "Click here to start your game" | "Open the case file" |

**Case titles** go "The ___ Affair / Case / Ledger": *The Ferry Building Affair*, *The Vulcan Lane Ledger*. **Buttons** start with a verb and use sentence case: "Open the case file", "Submit your accusation", "Ask for a hint".

## 4. Visual foundations

**Colour.** The default theme is **Night**: `ground` is almost black with a warm cast, text is `ink` (a bone white, never pure #fff) and there's exactly one accent, `thread`. **Paper** inverts to a soft near-white (`ground` #FBFAF7, not pure #FFF, which glares) for daylight play, printed matter and anyone who finds dark mode hard to read outdoors. Its body text sits at 17:1. `thread` is a vivid signal red (#E4142C), bright enough to carry on a phone in sunlight and at night. `note` is the game's off-white paper and `evidence` is the story's pure white (section 2). `manila` is the filing: evidence tags and folders. All three are the same colour in both themes, the way a real folder doesn't change colour when the lights go out. `brass` is the hardware: pins, tags, case numbers. `solved` appears only when a case or answer is confirmed.

Ratio by area, roughly: **80% ground and surface · 10% ink · 9% note, evidence, manila and brass · 1% thread.** If a layout looks red, there's too much red.

**Type.** Three voices:
- **Instrument Serif** (`display-xl`, `display-l`, `heading`) is the narrator: case names and evidence titles. It's tall and narrow, with a modern editorial cut. Use the italic (`heading-italic`) for one phrase of emphasis only.
- **Inter** (`title`, `body`, `small`) carries instructions and evidence text. It has to stay readable on a phone in drizzle at 11pm. Body never goes below 16px.
- **IBM Plex Mono** (`label`, `evidence`) is the file. Uppercase labels are 12px, tracked at 0.12em (11px and wider tracking washed out in sun), and records, times and coordinates are set in it.

All three are on Google Fonts; `components/bundle.css` loads them.

Evidence brings its own type, so it never looks like the game: **Share Tech Mono** (`receipt`) for thermal receipts and tickets, **Arimo** (`doc-body`) for printouts such as phone records and statements, **Caveat** (`hand`, 24px, never below 22px) for handwritten notes, and the phone's system font inside screenshots. None of these is used for the game's own words.

**Space and shape.** The grid is 4px (`space-1` … `space-16`). Shape carries meaning (section 2): game elements are rounded (`radius-tag` 6px, `radius-control` 10px, `radius-note` 16px), evidence is square (`radius-evidence` 0), and full circles are pins and knots only (`radius-pill`). Depth is reserved for objects: `shadow-object` (or `shadow-object-drop` for torn edges) on evidence and the phone, and nothing else. The game is flat and divided by `line` and `note-line` hairlines.

**Imagery** (direction, none shot yet): Auckland CBD after dark. Wet streets, sodium and neon light, long shadows, empty laneways, the harbour at night. Grade images cool and desaturated so that the thread is the only saturated red in frame. Show places, never victims. Hands, backs and silhouettes are fine; faces only when they're part of the story.

**Motion** (when it exists): slow and deliberate. The thread *draws on* along its path (600–900ms, ease-out) as new evidence connects, and nothing bounces.

## 5. Iconography

There's no icon set yet. Until one is drawn, use a thin-stroke outline set at a **1.5px stroke** in `ink-muted`, sized 20–24px. Lucide is a reasonable stand-in, and that choice is an assumption. Icons are functional only (map, clock, hint, team). The magnifying glass, fingerprint and footprints are clichés: don't use them as decoration.

## 6. Logo

**No logo exists yet.** Until one is designed, set the name as a wordmark: "Red Thread" in Instrument Serif, `ink`, with a single thread passing under it from the left, tied off at a pin on the right. See the **Wordmark** component. It's a placeholder lockup, not a final mark.

## 7. Components

| Component | Use |
| --- | --- |
| `Wordmark` | The provisional name lockup with its thread. |
| `Button` | Game. `primary` (thread fill) once per screen for the main action; `ghost` for the rest. 44px tall for cold fingers, `radius-control`. |
| `CaseTag` | Game. Mono status label: `open`, `solved`, `neutral`. `radius-tag`. |
| `ThreadDivider` | Game. The thread as a section break, with an optional chapter label on a knot. |
| `GameNote` | Game. The game talking: `instruction`, `hint` or `unlock` (with code cells). Off-white, rounded, flat. |
| `Evidence` | Wrapper. A manila `EvidenceTag` (number, status, title, where found) clipped to any evidence object, with shadow and the `locked` state. Replaces v1's `EvidenceCard`. |
| `Receipt` | Evidence. Thermal till receipt with a torn edge, GST line and optional stamp. |
| `PhoneScreenshot` | Evidence. Messages or recent calls inside a phone outline. |
| `PhoneRecords` | Evidence. A carrier's itemised call record, with redaction and a marked row. |
| `BankStatement` | Evidence. A statement page for money trails. |
| `Ticket` | Evidence. Ferry/bus/event ticket with a stub, or `torn` without it. |
| `HandwrittenNote` | Evidence. A ruled notebook page or a plain scrap, in handwriting. |
| `CctvStill` | Evidence. A greyscale still with camera, place and time burned in. |
| `Printout` | Evidence. Any other printed log (taxi trips, door swipes, inventories) with your own columns. |

Any evidence string can contain `[redacted]` to print a black bar.

Components are React 18, exported as `window.RedThread`, and styled with the tokens via `components/bundle.css`.

## 8. Accessibility, outdoors

The game is played **on foot, at night, on a phone**:
- Body text is 16px+, and all text meets 4.5:1 in both themes (see each token's note). Red text uses `thread-text`, never `thread`.
- Tap targets are at least 44px.
- Never rely on red alone. "Open" and "solved" also differ in label and lightness.
- Never rely on colour alone for game vs evidence either. White and `note` are only 1.15:1 apart, so shape (rounded vs square) and depth (flat vs shadow) carry the difference. Evidence components expose their text to screen readers; a phone screenshot is labelled as one.
- Evidence text stays readable: the data on receipts and documents (names, times, amounts) is 13px minimum on screen, and handwriting 22px minimum. Uppercase column heads, field labels and system small print may go to 11px, because real paper does, but they never carry the clue. Teams can pinch to zoom on any object.
- Every evidence object fits a 360px-wide phone. Documents reflow when their printable width drops below 360px rather than clipping a column, so the column with the clue is never the one off-screen.
- Use the Paper theme in daylight. Phones are hardest to read outdoors in sun, and a near-white ground with near-black ink wins there. Turn the screen brightness up rather than lightening the text.
- Keep instructions physical and unambiguous: "Stand under the clock at Britomart, facing the harbour."
