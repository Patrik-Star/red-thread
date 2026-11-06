---
name: review-case
description: Audit a Red Thread case for fair play, logic holes, timeline contradictions and breaches of the game-design rules, and return a prioritised fix list. Use when asked to review, check, critique, stress-test or "find holes in" a case, or before any playtest.
---

# Review case

Read `context/game-design.md`, then the target `cases/NNN-slug/case.md` and `solution.md`. Play it as a sharp, sceptical group would.

## Checklist
**Rules (game-design §2)**
- [ ] Solved by deduction (combining evidence), not quiz answers
- [ ] Every stop needs ≥ 2 roles' info + an on-site observation; none solvable by one player
- [ ] Every unlock code is only readable on site (not Googleable / Street-View-able if possible)
- [ ] Clues use durable public features only; puzzle-critical ones tagged `[verify]`
- [ ] Fair play: every fact in the key chain is shown before the accusation
- [ ] ≥ 3 red herrings; each has a motive **and** a lie, and each lie is explained
- [ ] Nothing graphic; real places, fictional people; no forbidden words
- [ ] Solvable at 3, 4, 5 and 6 players (Journalist/Rookie content isn't required to solve)

**Logic**
- [ ] Build a minute-by-minute timeline for every suspect across the death window; flag any alibi gap that isn't closed, and any alibi that clears someone too early
- [ ] Physical feasibility: walking times, distances, who could carry what
- [ ] Each accusation question has exactly one defensible answer; distractors are tempting but ruled out by shown evidence
- [ ] Culprit isn't obvious before the final third; at least one suspect "turns"

**Experience**
- [ ] Time per stop adds up to the target length incl. walking
- [ ] Each role has something meaningful at most stops
- [ ] Hint ladder (Nudge → Push → Answer) is writable for every puzzle
- [ ] Safety: daylight, signalised crossings, step-free alternative, no building entry

## Output
A table: **Severity** (blocker / major / minor) · **Stop** · **Problem** · **Concrete fix**. Blockers first. Then list open `[verify]` items. Don't edit the case unless asked; offer to apply fixes. Include any founder notes (🔧) already in the case as findings.
