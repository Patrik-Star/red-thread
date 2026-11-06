# Business model

Iteration 1 · 2026-10-26 · original model script: `street-sleuth/06-model/model.py` (not yet in repo).

> **Bottom line:** each sale is very profitable and very little cash is at risk (~NZ\$125/month). The real risk is **how many games sell**, and founder time. Verdict: **promising, not yet validated.**

## Summary

- ~97% of a direct sale is kept after card fees; cash costs ~NZ\$125/month. Money isn't at risk; time is.
- **Base case:** ~NZ\$28k revenue and ~NZ\$22k cash profit in 18 months with 3 games ≈ **NZ\$72/founder hour**. Repays game-2 build time by Nov 2027.
- **Pessimistic:** ~NZ\$7/hour; never repays build time.
- **Kill number:** a game needs ~45 paid plays (~2/month over 2 years) to repay ~80 build hours. Under ~5/month after 6 months → change channel or price, or stop.
- **Validate next:** paid games per month.

## Lean canvas

| Cell | Content |
| --- | --- |
| **Problem** | Walk-around mystery games are too easy for adults (riddles, not investigation); players stare at one shared screen; stories are generic and clues go missing. *Alternatives:* Seekers Code, Questo, City Game, escape rooms (\$39–45 pp), drinks/dinner/pub quiz |
| **Customer segments** | Auckland friend groups 22–40 whose organiser already pays for escape rooms. Early adopters: people who found Seekers Code/Questo too easy; puzzle and board-game regulars *(hypothesis)* |
| **UVP** | The outdoor escape room that's actually hard: solve a real Auckland crime on foot in under 2 hours, each player with different clues on their own phone |
| **Solution** | Hard on-location puzzles ending in real deduction; per-player roles and private info; stories written for real places; digital clues; offline |
| **Channels** | Own site + SEO, Bookme and Fever, ~\$100/mo ads, reviews and word of mouth |
| **Revenue** | One-off purchase per game per group. Test NZ\$60–100, base NZ\$80. Repeat purchases on new games |
| **Costs** | ~NZ\$125/mo fixed (hosting + ads) + domain. Stripe 2.7% + \$0.30; ~20% marketplace commission. Biggest: founder time, ~80 h/game + ~2 h/mo upkeep |
| **Key metrics** | Paid games/month/game · completion rate and rating · repeat rate · direct vs marketplace · hours to build |
| **Unfair advantage** | None yet. Build from Auckland-specific stories, a catalogue of local games, early reviews (rivals have ~38 in Auckland combined) |

**Riskiest cell:** segments and channels — will friend groups find and buy at ~\$80? Cheapest test: interviews, then a Bookme listing for a playtested game.

## Inputs (Pess / Base / Opt)

| Input | Value | Label |
| --- | --- | --- |
| Price per group | \$60 / \$80 / \$100 | assumption, med |
| Mature sales/month, 1 game | 8 / 20 / 50 | assumption, low |
| Months to mature | 6 | assumption, low |
| Extra demand per additional game | +15% / +30% / +50% | assumption, low |
| Hours to build a game | 150 / 80 / 40 | assumption, low |
| Share via Bookme/Fever | 70% / 50% / 30% | assumption, low |
| Marketplace commission | 20% | assumption — check terms |
| Stripe fee | 2.7% + \$0.30 | Stripe NZ pricing — verify |
| Hosting / ads / domain | \$25/mo · \$100/mo · ~\$30/yr | |
| Founder time | \$40/h | assumption |
| Upkeep per live game | 2 h/mo | assumption |
| Seasonality | Jan 1.3× … Jun–Jul 0.5× | assumption |
| Launch | Feb 2027; new games Aug 2027, Feb 2028 | |

GST not modelled (threshold NZ\$60k/12 months; only the optimistic case reaches it). Income tax not modelled.

## Unit economics (base)

- Contribution, direct = 80 − (0.027×80 + 0.30) = **\$77.54**
- Contribution, marketplace = 80 × 0.8 = **\$64.00**; blended (50/50) **\$70.77**
- Gross margin **97%** · CAC (blended) **\$13.00** (excl. founder time) · LTV **\$100.80** · LTV:CAC **7.8**
- Build cost per game 80 h × \$40 = **\$3,200** → **kill number 45 sales/game**

| | Pess | Base | Opt |
| --- | --- | --- | --- |
| Blended contribution | \$51.02 | \$70.77 | \$91.90 |
| CAC | \$20.90 | \$13.00 | \$8.00 |
| LTV:CAC | 3.2 | 7.8 | 18.2 |
| Sales to repay a build | 118 (4.9/mo) | 45 (1.9/mo) | 17 (0.7/mo) |

## Scenarios (Feb 2027 – Jul 2028)

| | Pess | Base | Opt |
| --- | --- | --- | --- |
| Revenue | \$7,200 | \$27,920 | \$102,600 |
| Cash profit | \$3,813 | \$22,389 | \$91,979 |
| Founder hours | 522 | 312 | 192 |
| Profit / founder hour | \$7 | \$72 | \$479 |
| Repays founder time by | not in 18 mo | Nov 2027 | Mar 2027 |

**Sensitivity:** sales/month matters most (±20% → ±\$4.9k base profit), then price, then build hours. Base case first reaches ~\$2k/month revenue in Nov 2027.

## What must be true

1. Groups pay ~\$80 per game.
2. One game reaches ~20 paid plays/month within 6 months.
3. A game can be built in ~80 hours (Case 001.2 is budgeted at ~110 — watch this).
4. New games bring back past groups (+30%).

## Next steps

- [ ] Customer interviews: price and outing frequency
- [ ] Log hours while building Case 001
- [ ] Get Bookme and Fever commission terms; replace the 20% assumption
