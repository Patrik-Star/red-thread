# Red Thread

**Red Thread** is a real-world mystery game. Teams of 3–6 people walk the streets of Auckland CBD (Tāmaki Makaurau) with a case file, following evidence from stop to stop until together they can name who did it, how and why.

The name comes from the investigator's corkboard: photos, notes and places, joined by one red string. The brand works the same way. **A single red thread runs through everything** (posters, the app, evidence cards, the case box) and links each piece to the next.

The feel is **dark, mysterious and modern**: night streets, wet pavement, a city keeping secrets. It is a contemporary game you play with your phone in hand, not a Victorian pastiche. Think minimal noir, not magnifying glasses and deerstalkers.

> This is a first system, built from the brief alone. There is no existing logo, photography or code yet. Everything here is a proposal to react to. Colours, type and components are starting points; the thread rule is the part to keep.

---

## 1. The thread rule

The red thread is the brand's signature. Treat it like a logo.

1. **One thread per composition.** A single continuous line in `thread`. It never splits, never runs as two parallel strands, and never becomes a pattern.
2. **It connects things.** It runs from one element to the next: headline to evidence, evidence to map pin, chapter to chapter. A thread with nothing at either end is decoration. Cut it.
3. **It enters and leaves.** Let it bleed off the edge of the page or screen, so it seems to come from the previous piece and carry on to the next. On a multi-page layout, line its exit up with the next page's entry.
4. **It is the only red.** On any surface the thread, the primary button and pins share the one red. No red photos, no red backgrounds behind red thread, and no second accent colour.
5. **It's string, not a vector line.** Straight runs between pins with a slight sag, or a loose curve. No zig-zags, arrows or perfect geometric arcs. Width is `thread-width` (2px) in UI and `thread-width-hero` (3px) at poster scale.
6. **It's tied off at pins.** Where it changes direction it passes a pin: a small disc in `brass` (or `manila-thread` on manila). Pins use `radius-pill`, and they're the only round thing in the system.

**Do:** run the thread from a case title, under a paragraph, to a map location. **Don't:** underline every heading in red, use red for errors, or draw the thread as a dashed "route" line. Dashed lines belong to tear-offs on paper (`manila-line`).

## 2. Voice: content fundamentals

Red Thread speaks like a **calm case officer briefing a capable team**: precise, a little dry, never breathless. The mystery does the work. The copy doesn't need to shout.

- **Short, declarative sentences.** Facts first, and let the gaps create the suspense.
- **Second person, plural.** "You have ninety minutes." The team is the detective, not "players" or "users".
- **Specific Auckland places**, named the way locals say them: Britomart, the Ferry Building, Vulcan Lane, Albert Park, Sky Tower. Use te reo Māori names with macrons (Tāmaki Makaurau, Waitematā).
- **New Zealand English:** colour, organise, centre, licence (noun), metres.
- **Evidence in mono.** Times, coordinates and transcripts go in `evidence` style, written as records: `23:40`, `-36.8442, 174.7676`.
- **No exclamation marks, no emoji, and never the words "clue", "Cluedo", "sleuth" or "treasure hunt".** Gore and violence stay off the page. We imply the crime and never show it.

| Instead of | Write |
| --- | --- |
| "Get ready for an EPIC murder mystery adventure!!" | "A body was found at the Ferry Building at 23:40. You have ninety minutes." |
| "Awesome! You found item 3 🎉" | "Evidence 03 recovered. The ticket was bought with cash." |
| "Oops, wrong answer, try again!" | "That doesn't hold. Look at the timestamp again." |
| "Click here to start your game" | "Open the case file" |

**Case titles** go "The ___ Affair / Case / Ledger": *The Ferry Building Affair*, *The Vulcan Lane Ledger*. **Buttons** start with a verb and use sentence case: "Open the case file", "Submit your accusation", "Ask for a hint".

## 3. Visual foundations

**Colour.** The default theme is **Night**: `ground` is almost black with a warm cast, text is `ink` (a bone white, never pure #fff) and there's exactly one accent, `thread`. **Paper** inverts to a soft near-white (`ground` #FBFAF7, not pure #FFF, which glares) for daylight play, printed matter and anyone who finds dark mode hard to read outdoors. Its body text sits at 17:1. `thread` is a vivid signal red (#E4142C), bright enough to carry on a phone in sunlight and at night. `manila` is evidence paper. It's the same colour in both themes, the way a real folder doesn't change colour when the lights go out. `brass` is the hardware: pins, tags, case numbers. `solved` appears only when a case or answer is confirmed.

Ratio by area, roughly: **85% ground and surface · 10% ink · 4% manila and brass · 1% thread.** If a layout looks red, there's too much red.

**Type.** Three voices:
- **Instrument Serif** (`display-xl`, `display-l`, `heading`) is the narrator: case names and evidence titles. It's tall and narrow, with a modern editorial cut. Use the italic (`heading-italic`) for one phrase of emphasis only.
- **Inter** (`title`, `body`, `small`) carries instructions and evidence text. It has to stay readable on a phone in drizzle at 11pm. Body never goes below 16px.
- **IBM Plex Mono** (`label`, `evidence`) is the file. Uppercase labels are tracked at 0.14em, and records, times and coordinates are set in it.

All three are on Google Fonts; `components/bundle.css` loads them.

**Space and shape.** The grid is 4px (`space-1` … `space-16`). Corners are nearly square (`radius-sm`, 2px), like paper and card. Round shapes are reserved for pins and knots (`radius-pill`). Depth comes from layering paper on dark, with `shadow-card` used on evidence (evidence cards, folders) only. Everything else is flat and divided by `line` hairlines.

**Imagery** (direction, none shot yet): Auckland CBD after dark. Wet streets, sodium and neon light, long shadows, empty laneways, the harbour at night. Grade images cool and desaturated so that the thread is the only saturated red in frame. Show places, never victims. Hands, backs and silhouettes are fine; faces only when they're part of the story.

**Motion** (when it exists): slow and deliberate. The thread *draws on* along its path (600–900ms, ease-out) as new evidence connects, and nothing bounces.

## 4. Iconography

There's no icon set yet. Until one is drawn, use a thin-stroke outline set at a **1.5px stroke** in `ink-muted`, sized 20–24px. Lucide is a reasonable stand-in, and that choice is an assumption. Icons are functional only (map, clock, hint, team). The magnifying glass, fingerprint and footprints are clichés: don't use them as decoration.

## 5. Logo

**No logo exists yet.** Until one is designed, set the name as a wordmark: "Red Thread" in Instrument Serif, `ink`, with a single thread passing under it from the left, tied off at a pin on the right. See the **Wordmark** component. It's a placeholder lockup, not a final mark.

## 6. Components

| Component | Use |
| --- | --- |
| `Wordmark` | The provisional name lockup with its thread. |
| `Button` | `primary` (thread fill) once per screen for the main action; `ghost` for the rest. 44px tall for cold fingers. |
| `CaseTag` | Mono status label: `open`, `solved`, `neutral`. |
| `EvidenceCard` | A piece of evidence as a pinned manila card: number, title, text, location. `locked` blurs the text until reached. |
| `ThreadDivider` | The thread as a section break, with an optional chapter label on a knot. |

Components are React 18, exported as `window.RedThread`, and styled with the tokens via `components/bundle.css`.

## 7. Accessibility, outdoors

The game is played **on foot, at night, on a phone**:
- Body text is 16px+, and all text meets 4.5:1 in both themes (see each token's note). Red text uses `thread-text`, never `thread`.
- Tap targets are at least 44px.
- Never rely on red alone. "Open" and "solved" also differ in label and lightness.
- Use the Paper theme in daylight. Phones are hardest to read outdoors in sun, and a near-white ground with near-black ink wins there. Turn the screen brightness up rather than lightening the text.
- Keep instructions physical and unambiguous: "Stand under the clock at Britomart, facing the harbour."
