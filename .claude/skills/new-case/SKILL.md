---
name: new-case
description: Design a new Red Thread case (murder, theft or disappearance) for an Auckland/NZ route, following the project's game-design rules. Use when asked to create, brainstorm, outline or draft a new case, route or mystery, or a new version of an existing case.
---

# New case

Produce a complete case design in `cases/NNN-slug/` that passes `review-case`.

## Before writing
1. Read `CLAUDE.md`, `context/game-design.md` (binding rules), and the latest case in `cases/` as a quality reference.
2. Read `decisions/log.md` so you don't reverse a past decision.
3. Ask the founder only for what you can't infer: area/route, crime type, target length. Otherwise pick sensible defaults and state them.

## Design order (work backwards from the truth)
1. **Truth first.** Write `solution.md`: culprit, method, motive, key detail (e.g. weapon or item location), and the full key chain.
2. **Red herrings.** At least 3 innocent suspects (aim for 5), each with a motive, a lie, and the stop where the lie is explained. Culprit starts *Not suspicious*; everyone else starts *Suspicious*.
3. **Evidence map.** Assign each key-chain fact to a stop and a role. Every stop needs **≥ 2 roles' info + 1 on-site observation**.
4. **Route.** Pick durable public landmarks only (building dates, plaques, statues, architecture). No business signage, stickers or staff. Tag every puzzle-critical feature `[verify]`. Avoid areas competitors already use (e.g. Auckland waterfront). Prefer signalised crossings; note step-free alternatives.
5. **Unlock codes.** Each stop's **Look for** → **Enter** must be readable only on site. No GPS.
6. **Pacing.** Suspect statuses should swing: at least one "turn" where a cleared suspect becomes suspicious again. The culprit becomes the main suspect late (final third).
7. **Scoring + accusation** questions with plausible distractors for each.
8. **Production plan** with hour budget (business model assumes ~80 h; flag if over) and a **playtest plan**.

## Output
- `cases/NNN-slug/case.md` from `templates/case-template.md` (no culprit reveal outside status lines).
- `cases/NNN-slug/solution.md` with key chain and a red-herring table (motive / lie / cleared by).
- Add the case to the table in `context/overview.md` and a line to `decisions/log.md`.
- Finish by running the `review-case` checklist on your own draft and fixing what fails.

## Style
NZ English, NZ$. Real places, fictional people. Nothing graphic. Avoid "Clue/Cluedo", "sleuth", "treasure hunt".
