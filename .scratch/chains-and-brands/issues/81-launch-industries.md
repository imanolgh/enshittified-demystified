# Launch industries

Type: grilling
Status: resolved
Blocked by: 80, 82  (Research: Industry screen; Research: Where PE owns consumer brands)
Map: [chains-and-brands](../map.md)

## Question

Which industries launch in version 1, which wait for a second batch, and what is each industry's label?

## Context

- Split off "Product categories: vocabulary and assignment" on 2026-11-16 (round 1 Q2 revised): the thirteen audited industries came from the pivot proposal's candidate list, so the launch list waits on a screen of twelve more ("Research: Industry screen") and full audits of any that look like about 20% PE or higher.
- Numbers so far (PE-owned plus PE minority stake by brand row, strict rule): car washes 53%, veterinary care 52% (21 rows), dental care 50%, restaurants 40%, women's apparel 38%, gyms 33%, mattresses 30%, pet stores 19% (61% of locations), dollar and discount 16%, eyewear 13% (20.5% of sales), cookware 13% (five licensed-name rows), supplements 10%, pharmacies 7% (30.7% of ranked prescription sales). Brand-direct affiliate programs on brands that are not PE-owned: mattresses 5 to 6, women's apparel 4, eyewear 4, cookware 9, supplements 2, pet stores 1, pharmacies 1. Findings: [category-audit-pilot](../research/category-audit-pilot.md), [category-audit-full](../research/category-audit-full.md).
- Claude's first proposal (before the split, not decided): car washes, veterinary care, dental care, restaurants, women's apparel, gyms, mattresses and pet stores; eyewear, cookware, supplements, dollar and discount, and pharmacies as second-batch candidates. Cookware's licensed names were the extra reason against it.
- Selection test from the pivot proposal (a proposal, not decided): about 20% PE or higher, at least three industries with affiliate income; about 8 to 10 industries and roughly 1,000 brands.
- Landlord brands are in the screen; property managers are ruled out ("Product categories", Q6).
- Settled in "Product categories": the word is **industry** everywhere, and the site's browse pages are industry pages; a brand can sit in several industries.
- **From "Research: Industry screen"** (2026-11-16; [findings](../research/industry-screen.md)): PE share by brand row in twelve more industries: collision repair 90%, urgent care 80%, physical therapy 80%, home services franchises 69% (composite), child care 60%, oil change and auto service 50%, bowling and family entertainment 45% (64% if Atairos counted), hair salons 30%, golf 29%, landlord brands 25% strict, ski resorts 12.5%, funeral homes 0%. Seven were judged worth a full audit (about 340k tokens each by the full audit's figure); golf only as an operator audit. Open here: whether to run those audits before choosing, and the workers' five questions: owners whose Form ADV says no PE funds (Atairos, Meritage), a public holding company as a holder (Icahn Enterprises), real estate funds as landlords (the engine's `real_estate` kind), industries where PE sits in local-name rollups, and home services' size measure.
- **From "Product categories"** (2026-11-16, Q11): the launch list also waits on "Research: Where PE owns consumer brands", a bottom-up scan of PE portfolio pages and BDC borrower sectors, because both candidate lists so far were guesses. Q7 there: if cookware or another licensing-heavy industry makes the list, revisit the known gap (a licensee's brand list that never says "licensed" can still give a claim that the licensee owns the brand).
- **From "Research: Where PE owns consumer brands"** (2026-11-16, steps 1 and 3; [findings](../research/pe-consumer-scan.md)): a bottom-up scan of 73 PE firms' current portfolios (about 735 consumer-facing companies) confirmed the measured industries and screened twelve new ones: med spas and beauty services 100%, behavioral health 77%, education and youth activities 58%, home care and hospice 43% (all judged worth a full audit); primary care 25%, pet food 20%, sporting goods 10%, apparel 7%, beauty, personal care, packaged food and beverages 0% at top 10 with dozens of PE brands in the long tail. Open here: how to count product industries (long tail vs top 10), and seven more counting questions: PE partners at clinic level (Humana and WCAS), creditor groups of hedge funds (Cano), BayMark's trade-press-only lender takeover, PE founders holding personally (3G founders in AB InBev), owners with no PE funds on Form ADV (Strategic Value Partners, alongside Atairos and Meritage), a self-described PE firm with no Form ADV (Susquehanna Private Capital), preferred equity under a founder majority (Bass Pro).
- **From the newsroom rebuild** (2026-11-16, same research ticket): the five biggest firms without a portfolio list hold, by their own newsrooms, 51 current US consumer companies (Blackstone 15, Apollo 12, Bain 20, Ares 4, Brookfield 0; an overcount since exits are rarely announced). Unmeasured clusters it adds: grocery (The Fresh Market, Cardenas, Tony's, Smart & Final, Erewhon), thrift stores (Savers Value Village, Ares 75.83%; America's Thrift Stores), arts and crafts retail (Michaels, JOANN), casinos. Whether to screen these before choosing is open here.

## Comments

### Round 1 (2026-11-16)

- **Split** (Q1): kept whole. The counting questions are answered by settled engine rules, so what remains is one choice: the bar, the list, the second batch and the labels.
- **Counting questions** (Q2, revised after the developer asked what the landlord 25% and mattress 30% figures meant): selection numbers use the engine's own rules (ADR 0001 as amended through 2026-11-16), the "strict" counts. Form ADV `Any PE Funds = Y` makes a firm PE, including VC and growth investors (vet rises from 52% to 71%, 15 of 21) and a single-family office (Wildcat, already in car washes' 53%). Not PE: owners whose ADV says N without a mapped self-description (Atairos, Meritage, Strategic Value Partners: bowling stays 45%), a public holding company's 13D (Icahn Enterprises at Monro), passive 13d-1(b) holders (index managers), BDC-held equity (Serta Simmons' four mattress rows: mattresses stays 30%, 43% if counted), real estate funds (Tricon: landlord brands stay 25%, 38% if counted), PE founders holding personally (family), the Humana CenterWell clinics in the WCAS partnership (Humana's brand). Counted: 13D or non-passive 13G PE holders of public companies (3G, Trian), lender groups whose advisers report PE funds (Gabe's, Cano), a self-described PE firm with no ADV (Susquehanna Private Capital, reported), trade-press-only takeovers (BayMark, reported). Preferred equity under a founder majority (Bass Pro) is minority only where a document states the stake. Pending deals count on closing; licensed names belong to the licensor. No rule moves an industry across the bar.
- **The bar** (Q3, revised: the developer asked about 15% and proposed 10%, "if we can support more industries, the better"): PE-owned plus PE minority stake by brand row, 10% or higher. An industry under 20% qualifies only on a full 30-brand audit, because in a 10-brand screen 10% is a single brand. Location and sales shares are noted, never decisive. Counts by bar: 22 industries at 20%, 24 at 15% (pet stores 19.2%, dollar and discount 16%), 27 at 10% (eyewear 13.3%, cookware 13.3%, supplements 10.0%, all audited). Ski resorts 12.5%, pet food 12.5% (by consumer brand; 20% by company) and sporting goods 10% are screens only and fail the audit rule.
- **Launch size** (Q4, revised): no fixed industry count. Every qualifying industry launches; if the seeding plan can't check them all before launch, the rest form the second batch in a ranking order set in round 2. About 27 industries with top-30 lists is about 800 brands; extraction costs about $0.0045 per document on DeepSeek, so the limit is readying each industry (brand list, registry entries, a completed check of every brand), not compute.
- **Affiliate requirement** (Q5, revised): kept, at least three launch industries with brand-direct affiliate programs. Six qualify under the 10% bar (mattresses, women's apparel, eyewear, cookware, supplements, pet stores), so no exception is needed.
- **Industries v1 can't show** (Q6, updated for the 10% bar; corrected: pet food is 12.5%, not 0 to 10%): rollup industries (funeral homes, ski resorts, specialty physician practices) are out of the launch list and the second batch and wait for the store map or local businesses, because a rollup is a company, never an industry page entry. Whether to audit product industries (beauty, personal care, apparel other than women's, sporting goods, pet food, beverages, packaged food) at 30 brands moved to round 2.

### Round 2 (2026-11-16)

- **Screened candidates** (Q7): no full audits for the 15 industries that qualify on their screens (lowest: primary care and landlord brands 25%, golf 29%, hair salons 30%). Their lists come from "Category brand lists and checked", and seeding computes every brand's verdict. Saves about 5.1M tokens.
- **Product industries** (Q8, revised twice: the developer asked about 100 brands per industry, then kept 30 after the cost, about 4 to 6M for five product industries at 100, against 1.7M at 30): 30-brand audits of beauty and cosmetics, apparel other than women's, personal care, pet food and products, and sporting goods and outdoor. The 30 brands come from a source blind to ownership (a sales ranking, a retailer's category pages), never from the PE brands the scan found, so the share isn't high by construction. Beverages and packaged food are skipped (packaged food measured 0 of 20; beverages' top 30 holds one PE minority, Primo). About 1.7M tokens, stop at 2M.
- **New clusters** (Q9, revised): about 10-brand screens of grocery, thrift stores, arts and crafts retail, home furnishings and casinos, about 0.55M tokens. 20% or more qualifies; 10% to 20% earns a 30-brand audit whose cost the developer approves when it comes up. Specialty physician practices are rollups (out under Q6).
- **Hotels** (Q13, the developer asked whether hotels belong with housing or local businesses): the parked housing map. A hotel's PE sits in who owns the building (KSL resorts, Blackstone real estate funds), separate from the brand on the sign (Marriott) and the company running it; that needs housing's building-to-owner role and property records, while local businesses works from provider sources (NPPES, Secretary of State, vet boards). Adding hotels widens housing's destination; whoever unparks it decides whether they stay there.
- **Sequencing** (Q10): this ticket resolves now; Q8 and Q9 are new research tickets, any industry they find that passes the bar joins the launch list, and the developer approves its label when that research ticket resolves. "Category brand lists and checked" waits on both.
- **Order if seeding can't check everything before launch** (Q11): three affiliate industries are guaranteed, then PE share by brand row, highest first. No demand data exists before launch.
- **Labels** (Q12): the 27 below; the code value is the label in snake case (`car_washes`); synonyms go in each industry's search word list ("Product categories", Q4).

## Answer

Resolved 2026-11-16 in a grilling session (two rounds, recorded under Comments).

- **The bar:** an industry launches when PE-owned plus PE minority stake is 10% or more by brand row, counted with the engine's rules (ADR 0001 as amended through 2026-11-16, the "strict" counts). Under 20% it needs a full 30-brand audit; a 10-brand screen isn't enough. Location and sales shares are noted, never decisive.
- **No fixed count:** every qualifying industry launches. If the seeding plan can't check them all before launch, the rest form the second batch: three affiliate industries are guaranteed first, then PE share by brand row, highest first.
- **Affiliate requirement:** at least three launch industries with brand-direct affiliate programs. Met six times over: mattresses, women's clothing, eyewear, cookware, vitamins and supplements, pet stores.
- **The launch list (27), with labels and PE share by brand row:**

| # | Label | Code value | PE share | Measured by |
|---|---|---|---|---|
| 1 | Beauty services and med spas | `beauty_services_and_med_spas` | 100% (10 of 10) | scan screen |
| 2 | Collision repair | `collision_repair` | 90% (9 of 10) | industry screen |
| 3 | Urgent care | `urgent_care` | 80% (8 of 10) | industry screen |
| 4 | Physical therapy | `physical_therapy` | 80% (8 of 10) | industry screen |
| 5 | Behavioral health | `behavioral_health` | 77% (10 of 13) | scan screen |
| 6 | Veterinary care | `veterinary_care` | 71% (15 of 21) | full audit, engine rules |
| 7 | Home services | `home_services` | 69% (9 of 13) | industry screen |
| 8 | Child care | `child_care` | 60% (6 of 10) | industry screen |
| 9 | Car washes | `car_washes` | 53% (16 of 30) | full audit |
| 10 | Dental care | `dental_care` | 50% (15 of 30) | full audit |
| 11 | Oil change and auto repair | `oil_change_and_auto_repair` | 50% (6 of 12) | industry screen |
| 12 | Bowling and family entertainment | `bowling_and_family_entertainment` | 45% (5 of 11) | industry screen |
| 13 | Home care and hospice | `home_care_and_hospice` | 43% (6 of 14) | scan screen |
| 14 | Tutoring and kids' activities | `tutoring_and_kids_activities` | 42% strict (5 of 12) | scan screen |
| 15 | Restaurants | `restaurants` | 40% (12 of 30) | pilot audit |
| 16 | Women's clothing | `womens_clothing` | 38% (12 of 32) | full audit |
| 17 | Gyms and fitness studios | `gyms_and_fitness_studios` | 33% (10 of 30) | pilot audit |
| 18 | Mattresses | `mattresses` | 30% (9 of 30) | full audit |
| 19 | Hair salons | `hair_salons` | 30% (3 of 10) | industry screen |
| 20 | Golf | `golf` | 29% (2 of 7) | industry screen |
| 21 | Rental homes | `rental_homes` | 25% (2 of 8) | industry screen |
| 22 | Primary care | `primary_care` | 25% (2 of 8) | scan screen |
| 23 | Pet stores | `pet_stores` | 19.2% (5 of 26) | full audit |
| 24 | Dollar and discount stores | `dollar_and_discount_stores` | 16% (4 of 25) | full audit |
| 25 | Eyewear | `eyewear` | 13.3% (4 of 30) | pilot audit |
| 26 | Cookware | `cookware` | 13.3% (4 of 30) | full audit |
| 27 | Vitamins and supplements | `vitamins_and_supplements` | 10.0% (3 of 30) | full audit |

- **Counting questions:** all answered by the engine's rules (Round 1, Q2); none moves an industry across the bar.
- **Not launching:** rollup industries (funeral homes, ski resorts, specialty physician practices), which wait for the store map or local businesses; pharmacies (6.7%), beverages and packaged food (0%); hotels go to the housing map. Ski resorts, pet food and sporting goods fail the audit-under-20% rule as screens.
- **Pending research:** "Research: Audits of five product industries" and "Research: Screen of five more industries" may add industries under the same bar.
- Docs: none changed beyond the maps; no glossary change (industry labels are values, not terms); no ADR (the bar is easy to change).

Handed on:
- "Category brand lists and checked": the 27 industries and their labels, the list-source rule from Q8 (blind to ownership), the eyewear question (retailers or frame brands, pilot §9 Q4), lists shorter than 30 (vet 21, dollar and discount 13 core, pet stores 26, landlords 8, golf 7), and the two research tickets.
- "Alternatives and affiliate links": six affiliate industries (program counts on brands that aren't PE-owned: cookware 9, mattresses 5 to 6, women's clothing 4, eyewear 4, supplements 2, pet stores 1), and cookware's licensing gap.
- Seeding plan (map fog): the second-batch order (Q11).
- Housing map: hotels (Q13).
- The licensee gap: cookware launches, so the gap from "Product categories" Q7 (a licensee's brand list that never says "licensed") is live for v1. Its v1 handling falls to "Category brand lists and checked" (cookware's list) and engine "Extraction prompt rules"; the full fix is the parked non-PE owners map's "Brand licensors and licensees on the brand page".

### Amended 2026-11-17 (from "Research: Audits of five product industries" and "Research: Screen of five more industries")

- **Six more launch industries, 33 in all:**

| # | Label | Code value | PE share | Measured by |
|---|---|---|---|---|
| 28 | Clothing and shoes | `clothing_and_shoes` | 23.3% (7 of 30) | product audit |
| 29 | Beauty products | `beauty_products` | 20.0% (6 of 30) | product audit |
| 30 | Personal care | `personal_care` | 13.3% (4 of 30) | product audit |
| 31 | Arts and crafts stores | `arts_and_crafts_stores` | 28.6% (2 of 7, every national brand) | screen |
| 32 | Sporting goods and outdoor gear | `sporting_goods_and_outdoor_gear` | 10.0% (3 of 30) | product audit; named exception |
| 33 | Pet food and supplies | `pet_food_and_supplies` | 6.7% (2 of 30) | product audit; named exception |

- **Named exceptions:** pet food (under the bar) and sporting goods (on it, falling to 6.7% on 2026-12-02) launch by the developer's decision. The 10% bar stays for every other industry; a 5% bar was turned down because it would also admit pharmacies (6.7%).
- **Fewer than 30 national brands:** counting every national brand replaces the 30-brand audit under 20% (arts and crafts 7, thrift about 13 to 15, casinos about 15 to 20).
- **Old deal documents:** selection counts a deal as current when no exit is found, for every industry; the site applies the 18-month rule itself.
- **Pending:** "Research: Follow-up audits of four industries" (grocery, home furnishings, thrift and resale stores, casinos) may add more under the same bar.
