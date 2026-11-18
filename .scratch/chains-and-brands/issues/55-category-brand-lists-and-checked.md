# Category brand lists and brand-level "checked"

Type: grilling
Status: resolved
Blocked by: 54, 64, 81, 91, 92, 93, engine/28  (Product categories: vocabulary and assignment; USPTO trademark data: adopt as a source?; Launch industries; Research: Audits of five product industries; Research: Screen of five more industries; Research: Follow-up audits of four industries; What "checked" means and coverage states)
Map: [chains-and-brands](../map.md)

## Question

How is an industry's brand list chosen and kept current, and what does the industry page promise about coverage?

(Narrowed 2026-11-17, round 1 Q0: what a brand needs before it counts as checked moved to "Brand-level checked: required sources and freshness"; the v1 licensee gap moved to "Licensed names in v1".)

## Context

- Pivot proposal, **not decided**: "Every major brand in this category is checked" replaces launch states as the coverage promise.
- The brand list needs a public, repeatable source (rankings by sales, units or revenue); the pilot audit records which sources worked.
- Engine "What 'checked' means and coverage states" fixes the engine meaning; this is the brand and category level: which sources must have run (SEC, sponsor portfolio pages, press, Form ADV, USPTO if adopted), and how long a check stays fresh.
- `no_evidence_found` is publishable (CLAUDE.md): "No PE evidence found (checked {date})", never "Not PE-owned" (GLOSSARY).
- **From "Brand and chain model"** (2026-11-06): a category's list holds consumer-facing brand names only. Groups of brands (Luxottica Retail, Inspire Brands, Xponential Fitness) are companies and never list entries; a brand and a same-named company are two rows. Brands whose stores another company runs under license (BJ's Optical) count like any brand. A share counted "by parent company" (audit §9 question 1) would count companies, which exist as rows.
- **From engine "Entity lifecycle"** (2026-11-06): a discontinued brand leaves the launch lists; nothing sets `status = closed` on brands at launch.
- **From "Research: Full category audit (ten remaining candidates)"** (2026-11-07; findings in research/category-audit-full.md): each category file lists its brands with cited owners, a separate list of rollups that aren't brands (dental, vet), and owner-not-found rows (from 1 in car washes and vet to 13 in pet stores). Several rankings are composites, and 2026 deals make public rankings stale; findings §7 lists the open counting questions.
- **From engine "What 'checked' means and coverage states"** (2026-11-07; ADR 0001 amended): the engine side is settled. A brand is checked when every source on its required list has finished a run (finding nothing counts); its checked date is the oldest run's; a failed or robots-blocked source leaves it unchecked. Shared sources (sponsor pages, press feeds, Form ADV, BDC Schedules) count through their latest complete pass after the brand was added. A check is judged against the list in force when it ran. Before a check completes, a brand shows only PE-owned or PE minority stake, else "not yet checked". Which sources make up the brand list, and how long a check stays fresh, are this ticket's.
- **From engine "Press and EDGAR full-text connectors"** (2026-11-08): press as a required source for a brand means the wire feeds going forward (releases stored from issuers' own sites) plus the historical route, which "Retrieval fan-out, tracked entities and refresh cadence" decides after "Research: Web search APIs for finding a brand's past coverage".
- **From engine "EDGAR full-text search and ownership filings"** (2026-11-08): EDGAR full-text search per brand (exact-phrase query per brand and company name over deal, prospectus, annual-report, proxy and merger forms since 2001) is a candidate required source for a brand's check.
- **From "Product categories: vocabulary and assignment"** (2026-11-16): a brand's industries come only from the industry brand lists that include it (nothing else assigns one), so the list is the assignment; rollups whose locations keep local names are never list entries; a brand can sit on several lists. Open here: whether brands outside the launch industries get seeded at all (for example Walgreens, Sycamore-owned since 2025, while pharmacies may not launch).
- **From "Launch industries"** (2026-11-16): 27 industries launch, at 10% or more PE by brand row (under 20% only on a 30-brand audit); labels and code values are in its Answer. Lists here must come from sources blind to ownership (never built from PE portfolios). Open here: what eyewear covers (retailers or frame brands, pilot §9 Q4); industries with fewer than 30 national brands (vet 21, dollar and discount 13 core, pet stores 26, rental homes 8, golf 7); cookware launches, so the licensee gap (a licensee's brand list that never says "licensed", Meyer and KitchenAid) is live for its list. "Research: Audits of five product industries" and "Research: Screen of five more industries" may add industries.
- **From "Research: Audits of five product industries" and "Research: Screen of five more industries"** (2026-11-17): six more launch industries (33 in all; labels in "Launch industries", amended): clothing and shoes, beauty products, personal care (sun care in, oral care out), arts and crafts stores (7 national brands, all counted), and, as named exceptions, sporting goods and outdoor gear and pet food and supplies. Sporting goods' launch list must not reuse the audit's Walmart-shelf list (it leaves out Weber, Traeger and Yeti; 11 owners not found). Pet food's Nestlé Purina brands blocked the bot, so their sources need another route before they can be checked. Clothing and shoes is licensing-heavy (Authentic Brands Group). "Research: Follow-up audits of four industries" (grocery, home furnishings, thrift and resale, casinos) may add more.
- **From "Research: Follow-up audits of four industries"** (2026-11-17): three more launch industries (36 in all): grocery stores (each banner a brand; the audit sized banners by store-weighted sales, and Kroger's banner counts rest on leads), thrift and resale stores (23 multi-state brands, 11 more unconfirmed; Savers' four store names are four rows), and home furnishings as a named exception (no free ranking of direct-to-consumer home brands exists, so its list leaves out The Shade Store, Visual Comfort and Brooklinen). Casinos don't launch.
- **From "USPTO trademark data: adopt as a source?"** (2026-11-17): USPTO is not a v1 source, so it is not on any brand's required list. The v1 licensee gap (a licensee's "our brands" list that never says "licensed" gives the licensee as owner: Meyer and KitchenAid) is live for cookware and clothing and shoes and needs a v1 fix without USPTO, here or as a change to engine "Extraction prompt rules" (a prompt change the developer approves).

## Comments

### Round 1 (2026-11-17)

- **Split** (Q0): this ticket keeps the lists and the coverage promise. New "Brand-level checked: required sources and freshness" takes the required source list and freshness, blocked by engine "Retrieval fan-out, tracked entities and refresh cadence" (which decides the connectors, including the press history route). New "Licensed names in v1" takes the licensee gap.
- **List size** (Q1): 30 brands per industry; every national brand where fewer than 30 exist (vet 21, arts and crafts 7, rental homes 8, golf 7). Lists can grow later through operator batches guided by the demand log.
- **Sources and method** (Q2): every list comes from a ranking blind to ownership (trade-press sales or unit rankings, NRF, YouGov, a retailer's category pages); a composite is allowed when no single source reaches 30, with its method recorded. Each industry page shows the method in one line ("The 30 largest US grocery banners by 2025 sales (NRF Top 100), each banner a brand"). Audit lists are reused where they meet the rule; new lists are built for the 15 industries measured only by screens, for sporting goods (the Walmart-shelf list missed Weber, Traeger and Yeti) and for pet food (a 2021 survey plus a capped company table).
- **Keeping lists current** (Q3, revised after the developer asked why a brand with its analysis done would leave the industry page): lists only grow. A list is refreshed when its source republishes; new entrants join and read "not yet checked" until checked; a brand that drops out of the new top 30 stays on the list and stays checked, leaving only when discontinued or when it no longer operates in the industry. The industry page shows the current ranking's 30 first, then "also checked". Reason: the list is the industry assignment ("Product categories"), so dropping a brand would strip its industry for falling a rank, against the glossary's meaning of industry.
- **PE brands outside launch industries** (Q4): one extra operator batch seeds the PE-owned brands the research found in industries that don't launch (Bally's and similar); they get brand pages and search, no industry page. Everything else waits for the demand log.
- **Eyewear** (Q5, option b): retailers, online sellers (Warby Parker, Zenni, GlassesUSA) and frame brands (Ray-Ban, Oakley), from rankings blind to ownership.
- **Pharmacies** (Q6; the developer added them "despite the pe influence being low"): launch as a named exception, label "Pharmacies" (`pharmacies`), 37 launch industries. Walgreens (Sycamore) is now inside a launch industry. The audit list (8 ranked by prescription sales plus 22 franchise networks and regional grocers) meets Q2 with its method recorded.

### Round 2 (2026-11-17)

- **Coverage promise** (Q7): an industry goes live only when every brand on its list is checked. Its page shows the method line, the current top 30 first, then "also checked", and a count that may read "31 brands, 29 checked" after launch while new entrants are being checked; each brand row shows its own checked date. Wording goes to "Website pages and shareable cards".
- **No hand cross-listing** (Q8): a brand appears on an industry's list only when that list's source puts it there; it lands in several industries only when several sources include it. Nobody picks rows after seeing who owns them.
- **When lists are built** (Q9): the remaining lists (the 15 screened industries, sporting goods, pet food, eyewear's online sellers and frame brands, thrift's 11 unconfirmed brands) are built as a step in the seeding plan, close to seeding, because rankings republish yearly. The work is ranking only, with no ownership research, so the workers stay blind to ownership by design; rough estimate 1.2M to 1.6M tokens. The audits' lists are reused at that step where they qualify. Nothing runs now.
- **Refresh** (Q10): each list records its source and the month that source usually republishes; the operator report flags a list once its source has republished or 13 months after it was built, whichever comes first. A flagged list is rebuilt and goes in as an operator batch.

## Answer

Resolved 2026-11-17 in a grilling session (two rounds, recorded under Comments). Split before round 1 into this ticket (lists and the coverage promise), "Brand-level checked: required sources and freshness" and "Licensed names in v1". Pharmacies added to the launch list during round 1 (37 industries).

- **Size:** 30 brands per industry at launch; every national brand where fewer than 30 exist.
- **Sources:** rankings blind to ownership; composites allowed with the method recorded; each industry page shows its method in one line. Rows are never picked by ownership, and no brand is cross-listed by hand.
- **Lists only grow:** refreshed when the source republishes; new entrants read "not yet checked" until checked; a brand leaves only when discontinued or out of the industry. The page shows the current top 30 first, then "also checked".
- **Promise:** an industry goes live only when every brand on its list is checked; the page shows a count of brands and how many are checked, and each brand's checked date.
- **Extra batch:** the PE-owned brands the research found outside launch industries (Bally's and similar) are seeded with brand pages and no industry.
- **Eyewear:** retailers, online sellers and frame brands.
- **Building the lists:** a seeding-plan step, close to seeding; ranking-only workers; about 1.2M to 1.6M tokens.
- **Refresh flags:** on the operator report when a source republishes or after 13 months.
- Docs: `evidence_layer_plan.md` §4 notes (`source_runs` now points to the new required-sources ticket; industry assignment notes lists only grow). No ADR, no glossary change.

Handed on:
- "Brand-level checked: required sources and freshness" (new): the required list per brand and freshness.
- "Licensed names in v1" (new): the licensee gap.
- "Website pages and shareable cards": the industry page's method line, top 30 then "also checked", the checked count, per-brand checked dates.
- Seeding plan (map fog): the list-building step and its estimate, the extra batch of PE brands outside launch industries.
- engine "API conventions, internal auth and operator surface": the list refresh flags.
- "Alternatives and affiliate links": eyewear covers online sellers and frame brands (where its affiliate programs sit).
