# Red Thread — project context for Claude

Red Thread is a phone-run **outdoor escape room** for groups of friends: solve a real Auckland crime (murder or theft) on foot, each player holding different clues on their own phone. Auckland first, then the rest of NZ. Domain: redthread.co.nz.

- **Stage:** idea → building Case 001. Solo side project by Patrik, started 2026-10-26.
- **Launch target:** soft launch of Case 001 in Auckland CBD, early Feb 2027.
- **Promise:** "An escape room the size of Auckland."

## Where things live

| Path | What |
| --- | --- |
| `context/overview.md` | One-page summary, timeline, current status |
| `context/game-design.md` | Rules that apply to **every** case (format, roles, scoring, hints, functional requirements, safety) |
| `context/business-model.md` | Lean canvas, unit economics, scenarios, kill numbers |
| `context/gtm.md` | Positioning, messaging, channels, pricing, launch plan |
| `cases/NNN-slug/case.md` | One case: story, suspects, stops, scoring, production and playtest plan |
| `cases/NNN-slug/solution.md` | Spoilers. Kept separate so the case file can be shared with playtesters |
| `decisions/log.md` | Dated decisions and why (append-only) |
| `playtests/` | One file per playtest session |
| `templates/` | Starting points for new cases and playtest logs |
| `design-system/` | Brand and UI design system: brand book (`README.md`), `Colour.md`, `tokens.json`, React components. Mirror of the live Design System artifact: https://claude.ai/artifact/HTSicb4XPKRxgkqMbbGGxx. **To view it, open `design-system/preview.html`** (self-contained). The `components/*/preview.html` files are fragments and show nothing on their own. After changing tokens or components, rerun `python3 design-system/scripts/build_preview.py` to regenerate `preview.html` and `tokens.css`. |
| `design-system-2/` | Design system **v2**, a copy of v1 plus the two-layer rule: game notes and UI are rounded, flat and off-white; physical evidence is square, white and shadowed. Adds GameNote, Evidence (manila tag + object), Receipt, PhoneScreenshot, PhoneRecords, BankStatement, Ticket, HandwrittenNote, CctvStill and Printout, plus a Case 001 examples card. Open `design-system-2/preview.html`; rebuild with `python3 design-system-2/scripts/build_preview.py`. Not yet mirrored to the live artifact. |
| `.claude/skills/` | Project skills (see below) |

Notion is the original home of these documents (page IDs in `context/overview.md`). The repo is now the source of truth; use the `notion-sync` skill to push updates back.

## Skills

- `new-case` — design a new case that follows the game-design rules
- `review-case` — audit a case for fair play, logic holes and rule breaks
- `log-playtest` — record a playtest and turn findings into case fixes
- `notion-sync` — pull from / push to the Red Thread pages in Notion

## Working rules

1. **Game-design rules are binding.** Every case must satisfy `context/game-design.md` §2 (real deduction, no solo stops, on-site only, durable clues, fair play, red herrings explained, nothing graphic).
2. **No GPS / geofencing.** Stops unlock with a code or word only readable on site (decision 2026-10-28).
3. **On-site facts are unverified until walked.** Anything a puzzle depends on is tagged `[verify]` until checked in person. Never remove the tag without a photo or a confirmed source.
4. **Spoilers stay in `solution.md`.** Don't put the culprit or answer chain in `case.md`.
5. **Real places, fictional people.** No real businesses, staff or people named or implied. Avoid the words "Clue"/"Cluedo" (Hasbro trademark), "sleuth", "AI-powered", "treasure hunt", "for all ages".
6. **Mark assumptions.** Business numbers are hypotheses until interviews/playtests back them; label them as such.
7. **Log decisions** in `decisions/log.md` with the date and reason.
8. Use NZ English and NZ\$.
