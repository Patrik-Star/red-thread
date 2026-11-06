# Case 001: "The Dusk Painting"

**Version:** 001.2 (draft v2, 2026-10-29) · **Status:** design, not playtested · follows [`context/game-design.md`](../../context/game-design.md)
**Previous version:** v1 (2026-10-26, 6 stops / 4 suspects / ~2 km) — Notion page `405f4a71-d350-8169-a20d-c7f024623a30`.

> ⚠️ Every on-site detail (plaque wording, building dates, column counts, clock faces, steps) is **written from memory and must be checked on site**. Items tagged `[verify]` are ones a puzzle depends on. The solution is in [`solution.md`](solution.md) — keep it away from playtesters. This design file still contains suspect-status progressions, so don't share it with playtesters either.

## What changed from v1

- **9 stops** (was 6): Stops 0–8. New: Art Gallery forecourt, Customs Street, Town Hall.
- **6 suspects** (was 4): new Tessa Lowe (conservator) and Gideon Hart (former partner).
- **Everyone but the killer starts Suspicious.** Dr Helen Park starts Not suspicious.
- **Nina can return to the city.** A second taxi (Stop 5) puts her on Customs Street at 11:48pm. She's cleared at Stop 7 by forensics, not by a timestamp.
- **A murder weapon thread runs through every stop.**
- **No GPS.** Each stop unlocks only with a code or word read on site.
- **Route ~5 km** (was ~2 km); time budget 150–180 min (was 100–120).
- **Stop 2 is a Word Lock** (Wordle-style).

## 1. At a glance

| | |
| --- | --- |
| **Case** | A well-known art dealer is found dead in Albert Park at dawn, and the painting he was about to sell is missing. Murder **and** theft |
| **Length** | 150–180 min: 9 stops, ~5 km, finishing at Britomart near cafés and bars |
| **Route** | Britomart → Vulcan Lane → Chancery Square → Auckland Art Gallery → Albert Park → Customs Street → Town Hall → University Clock Tower → Britomart |
| **Play hours** | Daylight only |

> Note: the v2 route list in Notion names Freyberg Place, but Stop 2 is set in Chancery Square. Resolve which square Stop 2 uses (Sam's alibi is "a gig in Freyberg Place"). `[decide]`

## 2. The case

**Victim:** **Julian Ashby**, 61, Auckland art dealer. Found 6:10am at the edge of the Albert Park fountain by a jogger. Briefcase open and empty.

**Time of death:** 11:50pm – 12:30am (scene temperature, CCTV at Stop 2).

**Missing:** *Evening, Waitematā* by the fictional painter **Eliza Crane**, due to sell at 7am for \$240,000 to Marcus Reid. Its **gilt oak frame** is also missing.

All characters are fictional. No real businesses, institution staff or people are named or implied.

## 3. The weapon thread

"What did the killer use?" is asked at Stop 0 and answered in pieces. Players keep a **Weapon board** on their phone.

| Candidate | Evidence | Result |
| --- | --- | --- |
| Silver-topped walking cane (Gideon's) | Stop 3: knob is round, 3 cm | Ruled out (wound is square) |
| Bronze paperweight (Julian's desk) | Stop 1: office inventory shows it on the desk | Ruled out |
| Fountain edge stone | Stop 0: no grit or stone in the wound | Ruled out |
| Gilt picture frame (oak, ~9 kg, four brass corner pins) | Stops 0, 3, 4, 7 | See solution |

**Stop 0 wound report (verbatim, Forensics):** "Single blow to the left temple. Edge is square, not rounded. Two parallel indentations, about 4 cm apart, each with a small dark ring. Not a stone. Not a cane tip."

## 4. Suspects

Start: first five **Suspicious**; Dr Helen Park **Not suspicious**.

| Suspect | Who | Their story |
| --- | --- | --- |
| **Nina Ashby** | Daughter; inherits everything. Had dinner with Julian | "I took a taxi home to Ponsonby after dinner and stayed in." |
| **Marcus Reid** | Rival dealer; the 7am buyer. Texted "You'll regret this" | "I was at the charity auction all night, then waited at Britomart." |
| **Sam Tupou** | Assistant; carried the painting. Heavy debts | "I was at a gig in Freyberg Place until 1am." |
| **Gideon Hart** | Former business partner; owed ~\$180,000 | "I was at the charity auction, and I haven't spoken to Julian in a year." |
| **Tessa Lowe** | Independent conservator hired last week | "I'd never seen the painting before last week." |
| **Dr Helen Park** | University art historian who authenticated the painting | "I was home by 10pm." |

## 5. Stops

Each stop has a **Look for** (find on site) and an **Enter** (code to unlock). No location check.

### Stop 0 — Te Komititanga, Britomart (briefing, 15 min)
- **Look for:** four-digit year carved on the old Chief Post Office facade `[verify]`. **Enter:** that year → unlocks Julian's phone.
- **Detective:** case file, timeline, Weapon board. **Forensics:** wound report. **Informant:** Marcus's voice note: "He never turned up. He's never late."
- **Unlocks:** dinner booking for two at 9:30pm in Vulcan Lane, under "Ashby".

### Stop 1 — Vulcan Lane (15 min)
- **Look for:** number on the Vulcan Lane heritage plaque `[verify]`. **Enter:** that number → taxi record.
- **Informant (waiter):** Julian argued with a younger woman in a green silk wrap: "It's not yours to sell, and it's not what you think it is."
- **Forensics:** receipt, two meals, paid 9:55pm. **Records:** Nina's taxi, High St 10:05pm → Ponsonby 10:20pm (only this ride shown).
- **Detective note:** the painting may not be what it seems. **Office inventory:** paperweight on desk → ruled out.
- **Status after:** Nina → Partly cleared.
- 🔧 **Founder note:** Nina is cleared too early. Idea: Nina left her car in Ponsonby.

### Stop 2 — Chancery Square: Word Lock (20 min)
- **Look for:** seven-letter word COLUMNS carved on a plinth `[verify]`. **Enter:** the Word Lock answer.
- **Word Lock:** Sam's phone is locked with Julian's word game. Six guesses at a seven-letter word; starting word COLUMNS (from the plinth). Answer **GALLERY** → opens Julian's planner: "Tessa, gallery forecourt, lab report" → Stop 3.
- **Records:** Sam's bank: \$3,000 from Marcus two weeks ago. **Forensics:** CCTV stills at 11:30pm, 12:15am, 12:50am.
- **Look for (CCTV):** number of bronze benches visible `[verify]` → proves camera direction, so the figure is Sam, all night.
- **Informant:** Sam admits telling Marcus when the painting would move, "but that's all."
- **Status after:** Sam → Cleared. Marcus → Suspicious.

### Stop 3 — Auckland Art Gallery forecourt (20 min)
- **Look for:** number of steps up to the forecourt `[verify]`. **Enter:** that number → interviews.
- **Informant (Tessa):** "Nine kilos, 1890s oak, four brass pins at the corners. Julian never let it leave without the frame. I measured it myself."
- **Forensics (Tessa's lab note):** paint contains **titanium white**, not sold as artists' paint until ~1920s → forgery, can't be 1893.
- **Informant (Gideon):** owed money; leans on a silver-topped cane. **Forensics:** cane knob round, 3 cm → ruled out.
- **Status after:** Tessa → Suspicious (her "never seen it" is a lie). Gideon → Suspicious.

### Stop 4 — Albert Park, the crime scene (25 min, centrepiece)
- **Look for:** number on the memorial plaque by the park's statue `[verify]`. Use it to decode the landline digits. **Enter:** the landline number → call log.
- **Forensics:** scuff at the fountain edge; gilt wood splinters in the grass; **dark-green tweed fibres** on Julian's sleeve.
- **Records:** last call **11:42pm**, 2 min, to an unsaved landline → decodes to the University art history department.
- **Informant (groundskeeper):** "Someone in a long coat, around midnight, walking from the fountain toward Princes Street with something flat under their arm."
- **Journalist (5+):** Marcus and Julian "haven't spoken in years."
- **Status after:** Helen Park → Suspicious. Nina's fibre question stays open.
- 🔧 **Founder note:** "What do you mean decode? How?" → the decode mechanic needs designing. `[decide]`

### Stop 5 — Customs Street (15 min)
- **Look for:** year on the Old Customs House facade `[verify]`. **Enter:** that year → full taxi record.
- **Records:** Nina's second taxi: Ponsonby **11:25pm** → Customs Street **11:48pm**.
- **Informant (driver):** "She had a handbag. Nothing else. She asked me to wait while she made a phone call."
- **Detective note:** Customs St → Albert Park is ~15–20 min on foot; Nina could reach the fountain before 12:30am.
- **Status after:** Nina → Suspicious again (the turn).

### Stop 6 — Auckland Town Hall, Queen Street (20 min)
- **Look for:** number of columns on the Queen Street facade `[verify]`. **Enter:** that number → auction livestream.
- **Records:** Marcus and Gideon both on camera bidding until **12:30am**.
- **Informant (staffer):** "Marcus left the room for ten minutes at 11:40. He came back with his coat on. Gideon never left his seat."
- **Status after:** Marcus → Cleared. Gideon → Cleared.

### Stop 7 — University Clock Tower (25 min)
- **Look for:** number of clock faces `[verify]`. **Enter:** that number → building log.
- **Records (swipe log):** Dr Park in at **12:18am** (said "home by ten"). Tessa in 9:40pm, out 9:52pm, didn't return; a lab sign-in from two years ago shows she viewed the painting in Dr Park's lab → Tessa Cleared.
- **Records:** Dr Park's signed report: "genuine, c. 1893."
- **Informant (Dr Park):** "Home by ten. I was wearing my old green tweed."
- **Informant (night cleaner):** "Around half twelve, a woman came in with a long flat roll under a tweed throw. Then I heard a snap, like wood."
- **Forensics:** fibres are dark-green **tweed**; Nina's wrap is **silk** → Nina Cleared.
- **Status after:** Dr Park → Main suspect.

### Stop 8 — Britomart: the accusation (20 min)
Each player answers privately, then the group agrees:
1. **Who?** (six suspects) 2. **Weapon?** (four candidates) 3. **Why?** (money / reputation / the forgery's cover-up) 4. **Where is the painting?** (Dr Park's office / the university / Customs Street / the Town Hall)

No hints. Ending: epilogue (text + audio), star score, time, hints, share card ("We cracked Case 001.2 in 2:37, 4★").

## 6. Suspect tracker

| Suspect | Appears at stops |
| --- | --- |
| Nina Ashby | 0, 1, 5, 7 |
| Marcus Reid | 0, 2, 4, 6 |
| Sam Tupou | 0, 2 |
| Gideon Hart | 3, 6 |
| Tessa Lowe | 3, 7 |
| Dr Helen Park | 0, 4, 7 |

## 7. Scoring (6 stars)

| | Stars |
| --- | --- |
| Correct killer | 2 |
| Correct weapon | 1 |
| Correct motive | 1 |
| Correct painting location | 1 |
| ≤ 2 hints used | 1 |

## 8. Route safety and access `[verify on site]`

- Signalised crossings only; in-game reminder not to read while crossing.
- Albert Park and the climb to Princes Street have slopes and steps — show a step-free alternative.
- University, gallery, Town Hall and Customs House are public settings only; nobody enters a building or talks to staff.
- Daylight only; bookings end 1–2 h before sunset.

## 9. Production plan (~110 h)

| Task | Budget h | Actual h |
| --- | --- | --- |
| Walk the 5 km route; photograph and verify every clue | 12 | |
| Finish story; write role material and audio scripts | 22 | |
| Record audio | 8 | |
| Build case content in the engine (9 stops, Word Lock) | 28 | |
| Paper playtest (2 groups) + fixes | 12 | |
| On-site playtests (5 groups) + fixes | 18 | |
| Final route check and launch prep | 10 | |
| **Total** | **110** | |

Log real hours here — build time is a key business-model input (base assumption 80 h).

## 10. Playtest plan

- **Paper (Dec 2026):** 2 friend groups, printed role cards, founder as GM. Is the deduction fair? Do the Look-for lines work? Does the weapon thread land? Where do people get stuck?
- **On-site (Jan 2027):** 5 groups. Measure finish rate, time, hints per stop, stars, fun 1–10. Ask whether anyone suspected Nina after Stop 5 and whether they cleared her.
- **Targets:** finish ≥ 70%, median ≤ 2 hints, median time 150–180 min.
- **Too hard?** Add a nudge at Stop 4 or 7 first. Never remove the deduction.

## 11. Open questions

- [ ] Walk the route; confirm every `[verify]` item, the 5 km distance, a step-free path
- [ ] Stop 1: Nina cleared too early — rework (car-in-Ponsonby idea)
- [ ] Stop 2: Chancery Square vs Freyberg Place
- [ ] Stop 4: design the landline decode mechanic
- [ ] Word Lock fairness: do groups guess GALLERY from the story alone?
- [ ] Is 9 stops / 150–180 min too long for 22–40s?
- [ ] Auckland Council rules for parks; event calendar at Town Hall / Customs House
- [ ] Murder vs pure theft for the first game? (ask in interviews)
