---
name: log-playtest
description: Record a Red Thread playtest (paper or on-site) from the founder's notes, compare results to the launch quality bar, and turn findings into concrete case fixes. Use when the founder shares playtest notes, results, timings, quotes or feedback.
---

# Log playtest

1. Create `playtests/YYYY-MM-DD-case-NNN-vX-<paper|onsite>-<group>.md` from `templates/playtest-template.md`. Fill only what the founder gave; mark unknowns `?` rather than inventing numbers.
2. Compare against the quality bar in `context/game-design.md` §8 (finish ≥ 70%, median hints ≤ 2, time within target, fun ≥ 8/10). If there are several playtests for the case, compute running medians across all files in `playtests/` for that case.
3. Turn each issue into a fix with severity. Rule: if it's too hard, add a nudge first; **never remove the deduction itself**.
4. Ask before editing `case.md`. When applying fixes, bump the version note and add a line to `decisions/log.md` for anything structural.
5. Pull out quotes usable in marketing (with permission) and words customers use — add notable ones to `context/gtm.md` → words bank.
6. If actual build hours were reported, update the "Actual h" column in the case's production plan.
