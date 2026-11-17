# Research: Screen of five more industries

Type: research
Status: resolved
Blocked by: none
Map: [chains-and-brands](../map.md)

## Question

In grocery, thrift stores, arts and crafts retail, home furnishings and casinos, what share of the top ~10 national US brands is PE-owned or a PE minority stake, counted with the engine's rules, and how many national brands does each industry have?

## Context

- Added 2026-11-16 in "Launch industries" (round 2, Q9). The clusters came from the PE consumer scan and the newsroom rebuild ([pe-consumer-scan](../research/pe-consumer-scan.md)): grocery (The Fresh Market, Cardenas and Tony's under Apollo; Erewhon, Smart & Final), thrift stores (Savers Value Village, Ares 75.83%; America's Thrift Stores), arts and crafts retail (Michaels under Apollo; the scan's worker believes JOANN closed its stores in 2025, unverified), home furnishings (At Home, The Shade Store, Brooklinen), casinos (The Venetian under Apollo).
- Left out: hotels (moved to the housing map, "Launch industries" Q13) and specialty physician practices (rollups whose locations keep local names, out under Q6).
- The bar: 20% or more at about 10 brands qualifies an industry outright; 10% to 20% earns a 30-brand audit whose cost the developer approves when it comes up; under 10% doesn't launch ("Launch industries" Round 1, Q3).
- Counting rules: "Launch industries" Round 1, Q2 (the engine's rules).
- Approved cost: about 0.55M tokens (two workers); stop and report if the total passes 0.7M.

## Find out

1. **The list:** the top ~10 national US brands per industry by a trade-press ranking (sales, stores or units), from a source that knows nothing about ownership. Brands, not companies. Where an industry has fewer than 10 national brands, say how many exist and list them all.
2. **Owners, Form ADV and share:** as in "Research: Industry screen" ([industry-screen](../research/industry-screen.md)): owner chain from primary sources, `Any PE Funds` for investment-firm owners, PE share by brand row under the engine's rules.
3. **Rollups:** owners whose locations keep local names, listed separately, not counted as rows.
4. **Verdict per industry:** qualifies (20% or more), audit candidate (10% to 20%, with the number of national brands a 30-brand audit could draw on), or no.

## Rules

- Same rules as "Research: Industry screen": public primary sources only, trade press for rankings only, no paywalled sources, competitor sites never sources; robots.txt read before the first request to each host (including after redirects); a challenge page gets one honest retry with no clicks; SEC user agent with the project's name and no email, at or under 2 requests per second. Every quote saved with its page text and re-checked.
- Findings go to `.scratch/chains-and-brands/research/industry-screen-2.md`, with worker reports under `research/industry-screen-2/`.

## Hands on

- Any industry at 20% or more joins the launch list ("Launch industries" Q10); the developer approves its label when this ticket resolves. Audit candidates go to the developer with a cost.
- "Category brand lists and checked": the lists.

## Comments

### 2026-11-17 run

- Launched as two background workers: A (grocery, thrift stores, arts and crafts retail) and B (home furnishings, casinos). Reports go to `research/industry-screen-2/`; the summary file and quote re-check follow when both finish.
- Same shared data, page cache and SEC rate (1 per second per worker) as "Research: Audits of five product industries", which runs alongside.

### Resolution rulings (2026-11-17)

- **Old deal documents** (Q1): selection counts a deal as current when no exit is found, as for every earlier industry. Michaels (2021 completion 8-K), Paper Source (sale completed 2021-05-27) and The Fresh Market (2016) go to the seeding plan as rows needing a fresh source.
- **Industries with fewer than 30 national brands** (Q5): counting every national brand replaces the 30-brand audit the bar requires under 20% ("Launch industries" amended). A complete count is stronger than a sample.
- **Arts and crafts launches** (Q3): 2 of 7 (28.6%), every national brand counted. Label "Arts and crafts stores" (`arts_and_crafts_stores`, Q4).
- **Follow-up audits** (Q6): a new research ticket, "Research: Follow-up audits of four industries" (about 1.1M tokens): grocery as a 30-banner audit (every store name is its own brand, "Brand and chain model"), home furnishings as a 30-brand audit from a ranking that covers decor chains and direct-to-consumer brands, thrift and resale stores as a count of every multi-state brand (resale franchises in scope), and casinos as a count of every brand under the glossary's definition (a name used at several locations; single-property names are locations).

## Answer

Resolved 2026-11-17 by two background workers (about 0.57M tokens) and the rulings above. Findings: [industry-screen-2](../research/industry-screen-2.md), with the worker reports in [research/industry-screen-2/](../research/industry-screen-2/).

| Industry | PE share by brand row | Outcome |
|---|---|---|
| Arts and crafts retail | 2 of 7 (28.6%), every national brand | launches as "Arts and crafts stores" |
| Thrift stores | 2 of 13 (15.4%) | follow-up count of every multi-state brand |
| Grocery | 1 of 11 (9.1%) to 2 of 14 (14.3%) by banner rule | follow-up 30-banner audit |
| Home furnishings | 1 of 10 (10%) | follow-up 30-brand audit |
| Casinos | 1 of 10 (10%) | follow-up count of every brand |

- Albertsons is a PE minority stake under the engine's rules: Cerberus holds 31.0% on a 13G filed under Rule 13d-1(d), not (b), and reports PE funds.
- The Venetian is Las Vegas Sands' licensed brand, so the Apollo-run operator doesn't make it PE.
- Quote check: every evidence quote matched; 0 of 95 altered copies matched.
- Process: one robots slip (ssvpusa.org, one request before reading its robots.txt; deleted unread).

Handed on:
- "Launch industries": arts and crafts and the fewer-than-30 rule (amended there).
- "Research: Follow-up audits of four industries": grocery, home furnishings, thrift and resale, casinos.
- "Category brand lists and checked": arts and crafts' 7 brands; waits on the follow-up ticket.
- Seeding plan (map fog): Michaels, Paper Source and The Fresh Market need a fresh source.
