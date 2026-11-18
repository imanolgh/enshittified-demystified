# Research: Follow-up audits of four industries

Type: research
Status: resolved
Blocked by: none
Map: [chains-and-brands](../map.md)

## Question

In grocery, home furnishings, thrift and resale stores, and casinos, what share of the industry's brands is PE-owned or a PE minority stake, counted with the engine's rules, on a 30-brand audit or, where fewer than 30 national brands exist, a count of every national brand?

## Context

- Added 2026-11-17 in "Research: Screen of five more industries" (Q6). The screens put all four between 9% and 15%, so each needs a fuller count before it can launch ("Launch industries": 10% or more by brand row; under 20% only on a 30-brand audit, or a count of every national brand where fewer than 30 exist).
- Screen results and leads: [industry-screen-2](../research/industry-screen-2.md), worker reports [a](../research/industry-screen-2/a-grocery-thrift-crafts.md) and [b](../research/industry-screen-2/b-home-furnishings-casinos.md). Reuse their sourced rows and quotes where still valid.
- Counting rules: "Launch industries" Round 1, Q2 (the engine's rules). A deal counts as current when no exit is found; note rows resting only on documents older than 18 months.
- Approved cost: about 1.1M tokens; stop and report if the total passes 1.3M.

## Find out

1. **Grocery: a 30-banner audit.** Every store name a shopper sees is its own brand ("Brand and chain model"), so each banner is a row: Albertsons' Safeway, Vons and Jewel-Osco are three rows. Take the 30 largest multi-state banners from a ranking blind to ownership (NRF, Progressive Grocer, Supermarket News), and say how banners were ordered where the ranking is by company. Albertsons' banners are a PE minority stake under the engine's rules (Cerberus 31.0%, 13G under Rule 13d-1(d)); re-confirm from the latest filing.
2. **Home furnishings: a 30-brand audit** from a ranking that covers furniture, decor chains and direct-to-consumer brands, not only furniture and bedding sales (the screen's HNN 125 missed The Shade Store, Visual Comfort and World Market). Mattress brands are out (their own industry).
3. **Thrift and resale stores: every multi-state brand,** donation stores and buy-sell resale franchises both (Goodwill, The Salvation Army, Savers Value Village, Plato's Closet, Uptown Cheapskate, Clothes Mentor and so on). Nonprofit names run by independent members are rows like any brand; note how each is run.
4. **Casinos: every brand under the glossary's definition,** a name used at several locations (Harrah's, Horseshoe, Hollywood Casino, Hard Rock, Golden Nugget and so on); single-property names (Bellagio, Borgata) are locations, not rows. Record the operator that owns each name, and whether the name is licensed (The Venetian is Las Vegas Sands' licensed brand). Non-SEC operators count.
5. **Per industry:** PE share by brand row, owner not found, how the list was built, and brand-direct affiliate programs where they exist.

## Rules

- Same rules as "Research: Audits of five product industries" (its brief and the workers' process notes): public primary sources for ownership, rankings from sources blind to ownership, no paywalled sources, competitor sites never sources; robots.txt read before the first request to every host, including redirect targets; no 401, 403 or 429 retried; one honest browser retry on a challenge page with no clicks; SEC at or under 1 request per second per worker when several run at once; every page saved and every quote re-checked.
- **New (2026-11-17):** when the session's permission check refuses a request, the worker stops and reports. It never reaches the same host another way.
- Findings go to `.scratch/chains-and-brands/research/follow-up-audits.md`, with worker reports under `research/follow-up-audits/`.

## Hands on

- Any industry that passes the bar joins the launch list ("Launch industries"); the developer approves its label when this ticket resolves.
- "Category brand lists and checked": the four lists.

## Comments

### 2026-11-17 run

- Launched as four background workers: grocery (30 banners, about 340k), home furnishings (30 brands, about 340k), thrift and resale stores (every multi-state brand, about 150k), casinos (every multi-location name, about 250k). Reports go to `research/follow-up-audits/`; the summary and quote re-check follow when all four finish.
- Same shared SEC data and page cache as tickets 91 and 92; workers reuse the screen workers' saved pages. SEC kept at 1 request per second per worker.
- Briefs tightened after the two robots slips: a host may be requested only after its robots.txt was read and parsed in an earlier, separate command; a refused request means stop and report.

### Resolution rulings (2026-11-17)

- **Grocery and thrift launch** (Q9): "Grocery stores" (`grocery_stores`), 6 of 30 banners (20.0%, all Albertsons banners as PE minority stakes); "Thrift and resale stores" (`thrift_and_resale_stores`), 5 of 23 (21.7%), every multi-state brand. Savers' four store names count as four rows under "Brand and chain model" (each runs stores in two or more states); as one brand the share is 10.0%, still passing. Resale franchises stay in scope (Q6 of "Research: Screen of five more industries").
- **Home furnishings** (Q10): launches as a named exception by the developer's decision, the same call as pet food at the same share (6.7%). Label "Home furnishings" (`home_furnishings`).
- **Casinos** (Q11): don't launch (2 of 64, 3.1%; 5.5% by location); no exception.
- **Budget:** the run used 1,371,017 tokens by harness count, over the approved 1.3M stop; workers can't see the harness count and their own estimates ran low. Future worker budgets carry a margin against the harness count.

## Answer

Resolved 2026-11-17 by four background workers (1.37M tokens) and the rulings above. Findings: [follow-up-audits](../research/follow-up-audits.md), with the worker reports in [research/follow-up-audits/](../research/follow-up-audits/).

| Industry | PE share by brand row | Outcome | Label |
|---|---|---|---|
| Thrift and resale stores | 5 of 23 (21.7%), every multi-state brand | launches | Thrift and resale stores |
| Grocery | 6 of 30 banners (20.0%) | launches | Grocery stores |
| Home furnishings | 2 of 30 (6.7%) | launches, named exception | Home furnishings |
| Casinos | 2 of 64 (3.1%), every multi-location name | doesn't launch | none |

- Quote check: every evidence quote matched; 0 of 343 altered copies matched.
- Process: one robots slip (a browser retry followed a redirect to svdpseattle.org before reading its robots.txt; it disallows nothing). The brief's separate-command rule doesn't cover a browser's own redirects.

Handed on:
- "Launch industries": three more launch industries (amended there; 36 in all).
- "Category brand lists and checked": the grocery banner list and its sizing method (store-weighted sales; Kroger's banner counts rest on leads), thrift's 23 brands and 11 unconfirmed candidates, home furnishings' list (no free ranking of direct-to-consumer home brands exists).
- engine "Operational identity, budgets and guardrail values": the shared-fetcher proposal must also stop redirects inside a browser before they're followed.
- Seeding plan (map fog): Kroger's Giant Eagle purchase is pending (closing expected 2027).
