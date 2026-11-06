# Colour

Every colour token, what it's for, and what it may sit on. Ratios are WCAG contrast. **Text** needs 4.5:1, or 3:1 at 24px+ (and 18.5px+ bold). **Graphics** (thread lines, pins, control borders, focus rings, icons) need 3:1. **Decorative** pairs carry no meaning and may go below 3:1.

The live **Colours** card under Foundations shows every pairing below in whichever theme you have selected, with its ratio calculated live.

## The palette by role

| Role | Token | Night | Paper | Use it for | Never |
| --- | --- | --- | --- | --- | --- |
| Ground | `ground` | #0B0B0D | #FBFAF7 | The page itself | Pure #000 or #FFF |
| Ground | `surface` | #141417 | #F2F0EB | Panels, sheets, the case brief | Text colours other than those listed below |
| Ground | `surface-raised` | #1D1D22 | #E9E6DF | Inputs, menus, a step above surface | Large areas (it's for small raised parts) |
| Ink | `ink` | #ECE8E1 | #16140F | Headlines, body text, wordmark | — |
| Ink | `ink-muted` | #9A958D | #58534A | Secondary text, captions, mono labels | Instructions the team must act on |
| Thread | `thread` | #E4142C | #E4142C | The thread line, primary button fill, pins on ground | Small text on Night; backgrounds behind other red; errors |
| Thread | `thread-text` | #FF5A6A | #C20F2B | Red words: "Open" tags, one emphasised word | Fills, the thread line |
| Thread | `thread-deep` | #A00C22 | #A00C22 | Hover / pressed state of thread fills | Resting state of anything |
| Thread | `on-thread` | #FFFFFF | #FFFFFF | Text and icons on `thread` / `thread-deep` | Anywhere else (white never goes on ground) |
| Thread | `focus` | #FF5A6A | #C20F2B | Keyboard focus ring, 2px, 2px offset | Decoration |
| Evidence | `manila` | #D6C8A8 | #D6C8A8 | Evidence cards, folders, tamper strips | Page backgrounds, buttons |
| Evidence | `manila-ink` | #1A1714 | #1A1714 | All text on manila | Text on ground |
| Evidence | `manila-thread` | #8F0D22 | #8F0D22 | Red stamps, numbers **and pins** on manila | Text on ground |
| Evidence | `manila-line` | #A8987A | #A8987A | Dashed tear lines on manila | Anything that must be seen |
| Supporting | `brass` | #B8935A | #7D5F2E | Case numbers, pins on ground, evidence tags | Buttons, a second accent, anything on manila |
| Supporting | `solved` | #6CC4AE | #1F6F5C | "Solved" tags, the confirmed-answer state | Generic success, links, decoration |
| Lines | `line` | #2A2A31 | #DCD8CF | Hairline dividers between list rows | The only edge of a control |
| Lines | `line-strong` | #70707B | #857F74 | Borders of ghost buttons and inputs | Text |

## Approved pairings

| Foreground | On | Night | Paper | Allowed as | Example |
| --- | --- | --- | --- | --- | --- |
| `ink` | `ground` | 16.1 | 17.6 | Text, any size | Case title, evidence text |
| `ink` | `surface` | 15.1 | 16.2 | Text, any size | Case brief panel |
| `ink` | `surface-raised` | 13.8 | 14.8 | Text, any size | Answer input |
| `ink-muted` | `ground` | 6.6 | 7.3 | Text, any size | "Allow 90 minutes." |
| `ink-muted` | `surface` | 6.2 | 6.7 | Text, any size | Captions in panels |
| `ink-muted` | `surface-raised` | 5.6 | 6.1 | Text, any size | Placeholder text |
| `thread-text` | `ground` | 6.5 | 5.9 | Text, any size | `CASE 07 · OPEN` |
| `thread-text` | `surface` | 6.1 | 5.4 | Text, any size | An open tag in a panel |
| `thread-text` | `surface-raised` | 5.5 | 5.0 | Text, any size | Inline validation word |
| `brass` | `ground` | 6.9 | 5.7 | Text, any size; pins | `CASE 07`, map pins |
| `brass` | `surface` | 6.4 | 5.2 | Text, any size | Case number in a panel |
| `solved` | `ground` | 9.5 | 5.8 | Text, any size | `CASE 03 · SOLVED` |
| `solved` | `surface` | 8.9 | 5.3 | Text, any size | Confirmed answer |
| `on-thread` | `thread` | 4.7 | 4.7 | Text 15px medium and up | Primary button label |
| `on-thread` | `thread-deep` | 8.2 | 8.2 | Text, any size | Pressed primary button |
| `thread` | `ground` | 4.2 | 4.5 | Graphics; text 24px+ | The thread line, pins, a red display word |
| `thread` | `surface` | 3.9 | 4.2 | Graphics; text 24px+ | Thread divider inside a panel |
| `focus` | `ground` | 6.5 | 5.9 | Focus ring | Keyboard focus |
| `line-strong` | `ground` | 4.0 | 3.8 | Control borders | Ghost button outline |
| `line-strong` | `surface` | 3.8 | 3.5 | Control borders | Input outline in a panel |
| `manila-ink` | `manila` | 10.8 | 10.8 | Text, any size | Evidence text |
| `manila-thread` | `manila` | 5.6 | 5.6 | Text, any size; pins | `EVIDENCE 04 · NEW`, the card's pin |
| `line` | `ground` | 1.4 | 1.4 | Decorative only | Row hairlines |
| `manila-line` | `manila` | 1.7 | 1.7 | Decorative only | Tear line |

## Pairings that fail

| Pair | Night | Paper | Why not | Use instead |
| --- | --- | --- | --- | --- |
| `thread` as small text on `ground` | 4.2 | 4.5 | Fails under 24px on Night, and is borderline on Paper | `thread-text` |
| `thread` on `manila` | 2.9 | 2.9 | Too weak even for a pin | `manila-thread` |
| `brass` on `manila` | 1.7 | 3.6 | Vanishes on Night | `manila-thread` or `manila-ink` |
| `thread` on `thread-deep` | 1.7 | 1.7 | Red on red: the thread disappears | Keep the thread off red fills |
| `manila` card on Paper `ground` | — | 1.6 | The card edge vanishes | Always give manila cards `shadow-card` |
| `on-thread` (white) on `ground` | — | 1.0 | Never put white on ground | `ink` |

## Proportions

On any screen or page, by area: about **85% ground and surface, 10% ink, 4% manila and brass, and 1% thread**. Three checks:

1. **One red thing.** If you can count more than one red element apart from the thread itself (thread, primary button, open tag), remove one. The primary button counts.
2. **No colour carries meaning alone.** "Open" and "Solved" differ in label and lightness, not just hue. An incorrect answer is written in words ("That doesn't hold"), never just turned red.
3. **Paper outdoors.** In daylight on a phone, use Paper. Its body text is at 17.6:1.
