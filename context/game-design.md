# Game design — rules for every case

Draft v1 · 2026-10-26 (updated 2026-10-28) · applies to **every** Red Thread case. Individual cases live in `cases/`.

## 1. Game format

| | |
| --- | --- |
| **Players** | 3–6, each on their own phone with a different role |
| **Length** | 100–120 min on foot, ending near cafés and bars (Case 001.2 tests a longer 150–180 min format) |
| **Difficulty** | Hard: escape-room level. Target finish rate ≥ 70%, median 1–2 hints |
| **Ending** | Each player privately names **who, how, why** and the case's key detail, then the group agrees a final answer. Scored in stars |
| **Play hours** | Set per case; parks and quiet areas are daylight only |

## 2. Design rules

1. **Real deduction, not riddles.** Every stop adds evidence; the case is solved by combining it, not by answering a quiz question.
2. **No player can solve a stop alone.** Each puzzle needs at least two roles' information plus something seen on site.
3. **On-site only.** Each stop has an observation step that can't be Googled from home (a feature, an inscription, a count).
4. **Durable clues.** Only permanent public features: building dates, statues, street names, architecture. No stickers, no staff, no business signs (they change).
5. **Fair play.** Every fact needed for the solution is shown to players before the accusation. No twist relies on information they never saw.
6. **Three red herrings (or more), one truth.** Each innocent suspect has a motive and a lie, and each lie is explained by the end.
7. **Nothing graphic.** The death happens off-screen; no gore, no weapons in detail.
8. **Everyone starts suspicious except the culprit.** The culprit should look cleared early and be found guilty late. *(from Case 001 notes)*

## 3. Roles (each phone shows different things)

| Role | Gets | Unique ability |
| --- | --- | --- |
| **Detective** | Case file, map, timeline board | Submits answers for the group; unlocks the next stop |
| **Forensics** | Scene photos, lab reports, physical evidence | Can "examine" an item once per stop for an extra detail |
| **Records** | Phones, emails, bank and swipe-card logs | Can request one record per stop |
| **Informant** | Witness interviews as **audio only on their phone** | Hears interrogations nobody else hears, so has to retell them |
| *Journalist* (5–6 players) | Newspaper archive, gossip, social posts | Background on suspects' pasts |
| *Rookie* (6 players) | The hint budget and the clock | Decides when the group spends a hint |

**3 players:** Detective also takes Records. **4:** core four. **5:** + Journalist. **6:** + Rookie. Material is split by role, so content is identical whatever the group size; only who holds it changes. The case must be solvable at any group size.

## 4. Scoring

| | Stars |
| --- | --- |
| Correct culprit | 2 |
| Correct motive | 1 |
| Correct key detail (set per case, e.g. where the stolen item is) | 1 |
| ≤ 2 hints used | 1 |

Cases may add items (Case 001.2 adds the weapon, 6 stars total). Individual answers are shown next to the group answer at the end ("3 of 4 of you suspected the culprit at Stop 4") to drive the post-game conversation.

## 5. Hint system

- Three levels per puzzle: **Nudge** (where to look) → **Push** (what to combine) → **Answer**.
- Hints are free to see but cost score. The group can't get permanently stuck: the answer is always available.
- Auto-offer a nudge after 15 minutes without progress at a stop.
- The final accusation has **no hints**, but each player can review all evidence the group found.
- Idea (open): "camera view".

## 6. Functional requirements

1. **Room code + role assignment:** one organiser books; players join by code on their own phones; roles dealt automatically by group size.
2. **Real-time sync:** answers, unlocked stops and hint use shared across phones within ~2 s.
3. **Per-role content:** each phone only receives its own role's material; solvable at any group size.
4. **Audio and video for one player:** Informant interrogations play only on that phone.
5. **No GPS check-in.** Each stop has a clue only available at the location; the code to continue can only be read on site. (Geofencing rejected: risk of bugs and stuck game states.)
6. **Offline-first:** all content downloaded at the start; sync when signal returns.
7. **Rejoin:** any player can rejoin on another phone without losing the role.
8. **No app install:** runs in the mobile browser.
9. **Accusation and results:** private per-player answers, one group answer, epilogue in text and audio, star score, time, hints used, share card.

## 7. Safety, access and permissions

- **Daylight only** where a route uses parks or quiet areas. Bookings end ~1–2 h before sunset.
- **Road crossings:** signalised crossings only; in-game reminder not to read while crossing.
- **Access:** every route shows a step-free alternative where one exists.
- **Public outdoor spaces only:** nobody enters a building or needs to talk to staff.
- **Real places, fictional people:** institutions appear only as public settings. No logos or names in marketing beyond the location; never imply real staff are involved.
- **Auckland Council:** check whether a self-guided commercial game in parks needs a permit or licence before launch `[verify]`.

## 8. Quality bar before any case launches

- ≥ 70% finish rate, median time within the case's target, median ≤ 2 hints, fun ≥ 8/10 across on-site playtests.
- Each case carries its own production log and playtest plan; log real build hours (they feed the business model).

## 9. Open questions

- [ ] Auckland Council rules for commercial self-guided games in parks
- [ ] Can audio-only interrogations work outdoors in a noisy CBD? Test in the tech spike
