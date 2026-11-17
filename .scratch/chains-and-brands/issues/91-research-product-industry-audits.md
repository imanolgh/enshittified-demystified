# Research: Audits of five product industries

Type: research
Status: resolved
Blocked by: none
Map: [chains-and-brands](../map.md)

## Question

In beauty and cosmetics, apparel other than women's, personal care, pet food and products, and sporting goods and outdoor, what share of the top 30 brands is PE-owned or a PE minority stake, counted with the engine's rules, and which of those brands run brand-direct affiliate programs?

## Context

- Added 2026-11-16 in "Launch industries" (round 2, Q8). The launch bar is 10% or more PE-owned plus PE minority stake by brand row; under 20% an industry qualifies only on a full 30-brand audit (Round 1, Q3). So each industry here qualifies at 3 or more PE brands of 30.
- Why these five: the scan's top-10 screens found 0 to 12.5% PE, with the PE in the long tail: beauty 36 PE brands outside the top 10 (Olaplex, Orveon, Milani, IL MAKIAGE), apparel 23 (Authentic Brands Group, Vuori, PacSun), personal care 17 (DUDE Wipes, Every Man Jack), pet food 14 (Open Farm, Stella & Chewy's), sporting goods Weber and Traeger under PE control ([pe-consumer-scan](../research/pe-consumer-scan.md) step 3; worker reports [s3-a](../research/pe-consumer-scan/s3-a-beauty-personal-care.md), [s3-c](../research/pe-consumer-scan/s3-c-food-beverages-pet.md), [s3-d](../research/pe-consumer-scan/s3-d-education-apparel-sporting.md)).
- The developer considered 100 brands per industry and kept 30 after the cost (about 4 to 6M tokens at 100, against about 1.7M at 30).
- Counting rules: "Launch industries" Round 1, Q2 (the engine's rules: Form ADV `Any PE Funds = Y` makes a firm PE; BDC-held equity, real estate funds, passive 13d-1(b) holders and ADV `N` owners without a mapped self-description don't count; a public company counts only through a PE holder's 13D or non-passive 13G, or a PE majority).
- Licensing: a brand's owner is whoever owns the name, never a licensee (GLOSSARY "Brand"). Apparel is licensing-heavy (Authentic Brands); record every licensed row and its licensor and licensee, as the cookware audit did.
- Approved cost: about 1.7M tokens (about 340k per industry); stop and report if the total passes 2M.

## Find out

1. **The list:** the top 30 consumer-facing brands in each industry, from a source that knows nothing about ownership: a trade-press sales ranking, a public brand ranking, or a retailer's category pages (where robots.txt allows). Never build the list from PE portfolios or from the scan's PE brands, or the share is high by design. Where no single source reaches 30, build a composite and say exactly how. Brands, not companies: each consumer-facing name is its own row ("Brand and chain model").
2. **Owners:** each row's owner chain from primary sources, with the PE firm and stake where stated, as in [category-audit-full](../research/category-audit-full.md).
3. **Form ADV:** `Any PE Funds` for every investment-firm owner, from the SEC's latest monthly adviser files.
4. **Share:** PE-owned plus PE minority stake by brand row under the engine's rules, plus owner-not-found rows.
5. **Affiliate programs:** brand-direct affiliate programs on each row, split by PE and non-PE brands.
6. **BDC overlap:** which rows appear in the latest SEC BDC data set, as in the full audit.

## Rules

- Same rules as "Research: Full category audit": public primary sources only, trade press for rankings only, no PitchBook, Preqin, CB Insights or paywalled sources, competitor sites never sources, never fetch WhoIsMyDentist, Private Equity Vet or Reddit; robots.txt read before the first request to each host (including after redirects); a challenge page gets one honest retry with no clicks; SEC user agent with the project's name and no email, at or under 2 requests per second. Every quote saved with its page text and re-checked.
- Findings go to `.scratch/chains-and-brands/research/product-industry-audits.md`, with one worker report per industry under `research/product-industry-audits/`.

## Hands on

- Any industry at 10% or more joins the launch list ("Launch industries" Q10); the developer approves its label when this ticket resolves.
- "Category brand lists and checked": the five lists and how they were built.
- "Alternatives and affiliate links": affiliate program counts.

## Comments

### 2026-11-17 run

- Launched as five background workers, one per industry (beauty and cosmetics, personal care, apparel other than women's, pet food and products, sporting goods and outdoor). Reports go to `research/product-industry-audits/<industry>.md`; the summary file and the quote re-check follow when all five finish.
- Shared data downloaded once by the parent session (SEC, user agent `EvidenceEngine ownership-research bot (launch industries)`): Form ADV November 2026 files (`ia110226-registered.zip`, `ia11022026-exempt.zip`, still the latest posted) and the BDC data sets `2026_07` to `2026_10` (`2026_08` holds the Q2 holdings, 186,669 `soi.tsv` lines). Workers read them locally.
- SEC rate lowered to 1 request per second per worker, because seven workers run at once (this ticket's five plus "Research: Screen of five more industries") and the SEC allows 10 per second in all. Every fetched page is saved with an index so quotes can be re-checked.

### Resolution rulings (2026-11-17)

- **Old deal documents** (Q1): selection counts a deal as current when no exit is found, the method used for all 27 earlier launch industries. The site applies the engine's 18-month rule itself once it checks brands. Rows resting only on documents older than 18 months go to the seeding plan: Revlon (2023-05-02), Wellness (2020-11-18), Wilson's FountainVest 13D/A (2025-06-02, stale from 2026-12-02), plus Michaels, Paper Source and The Fresh Market from "Research: Screen of five more industries".
- **YouGov "Load More" rows** (Q2): counted. yougov.com's robots.txt allows the ratings pages for `*` and the API host (api-test.yougov.com) has no robots.txt. The apparel worker's route, a browser click after the session's permission check had refused its direct request to that host, is recorded as a process slip, and research workers gain a rule: a refused request means stop and report, never reach the same host another way.
- **What launches** (Q3, then Q7 after the developer added pet food and sporting goods): apparel other than women's, beauty and cosmetics, personal care (sun care in scope, oral care out), and, as named exceptions to the 10% bar by the developer's decision, pet food and products (6.7%) and sporting goods and outdoor (10.0%, falling to 6.7% on 2026-12-02). The bar stays 10% for every other industry; lowering it to 5% was turned down because it would also admit pharmacies (6.7%).
- **Labels** (Q4, Q8): "Clothing and shoes" (`clothing_and_shoes`), "Beauty products" (`beauty_products`), "Personal care" (`personal_care`), "Pet food and supplies" (`pet_food_and_supplies`), "Sporting goods and outdoor gear" (`sporting_goods_and_outdoor_gear`).
- **CDPQ** (apparel's open question): not counted. The adviser reporting PE funds is tied to CDPQ by name only, which the audits' match rule treats as no match.

## Answer

Resolved 2026-11-17 by five background workers (about 1.74M tokens) and the rulings above. Findings: [product-industry-audits](../research/product-industry-audits.md), with the worker reports in [research/product-industry-audits/](../research/product-industry-audits/).

| Industry | PE share by brand row | Outcome | Label |
|---|---|---|---|
| Apparel other than women's | 7 of 30 (23.3%) | launches | Clothing and shoes |
| Beauty and cosmetics | 6 of 30 (20.0%) | launches | Beauty products |
| Personal care | 4 of 30 (13.3%) | launches | Personal care |
| Sporting goods and outdoor | 3 of 30 (10.0%) | launches, named exception | Sporting goods and outdoor gear |
| Pet food and products | 2 of 30 (6.7%) | launches, named exception | Pet food and supplies |

- Licensing drove apparel: five of its seven PE rows are Authentic Brands Group names.
- Quote check: every evidence quote matched its saved page, BDC record or Form ADV row; 0 of 447 altered copies matched.
- Process: one robots slip (tasteofthewildpetfood.com, one request before reading its robots.txt; nothing used) and the YouGov route above.

Handed on:
- "Launch industries": five more launch industries (amended there).
- "Category brand lists and checked": the five lists and how each was built; sporting goods' launch list must not reuse the audit's Walmart-shelf list (it leaves out Weber, Traeger and Yeti; 11 owners not found); pet food's Nestlé Purina brands blocked the bot, so their sources need another route; personal care's scope (sun care in, oral care out).
- "Alternatives and affiliate links": brand-direct programs found: apparel 6 (1 PE), personal care 3 (1 PE), sporting goods 2, pet food 1, beauty 0 confirmed.
- Seeding plan (map fog): the rows resting on documents older than 18 months.
- engine "Operational identity, budgets and guardrail values": the two robots slips across both research tickets and the proposed shared fetcher; the refused-request rule.
