# Research: Full category audit (ten remaining candidates)

Type: research
Status: resolved
Map: [chains-and-brands](../map.md)

## Question

In each of ten remaining candidate categories, what share of the top ~30 US brands is owned or backed by private equity today, which of those brands or their parents borrow from public BDCs, and which have brand-direct affiliate programs? Use the same method as "Research: Category audit pilot", so the numbers line up with restaurants, gyms and eyewear.

## Context

- Graduated from the map's "Not yet specified" on 2026-11-07. The developer ruled to run the full audit in the background while grilling continues, and to count shares by brand row as the pilot did until they rule on how to count (pilot findings §9).
- The categories are the candidates named in `.scratch/pivot-handoff-2026-11-02.md` §5 that the pilot didn't cover, with the two compound ones split:
  1. pharmacies (drugstores)
  2. dollar and discount stores
  3. car washes
  4. pet stores
  5. women's apparel
  6. mattresses
  7. cookware
  8. vitamins and supplements
  9. dental chains
  10. veterinary chains

  Appliances stay out (handoff: PE is probably rare there).
- Model to copy: [research/category-audit-pilot.md](../research/category-audit-pilot.md), the tables in §2–§4, the Form ADV check in §5, the BDC overlap in §6 and the method in §8.
- **From "Brand and chain model"** (2026-11-06): a brand is a name a consumer sees on a storefront, menu board or product label. A rollup whose practices keep their own names is a company, not a brand, and isn't a list entry. That matters for the dental and vet lists. A brand page reports the owner of the brand's US business.
- **From engine "Owner kind"** (2026-11-07): Form ADV `Any PE Funds = Y` marks a PE firm, even one that calls itself something else, and `N` proves nothing.

## Find out

Per category:
- **The brand list:** the top ~30 US brands (or every national chain, if fewer exist), the public source of the ranking (sales, units or revenue) and its date. Rollups with locally named practices go in a separate short list, not in the 30.
- **Per brand:** the current owner as a primary source states it; whether that owner is a PE firm or a PE-held company; the acquisition date; a ticker if public; franchised or company-operated (where it applies); brand-direct affiliate program (yes/no, URL); a source URL and verbatim quote for each fact. "Not found" rather than a guess.
- **Category share:** PE-owned or PE minority stake, by brand row. Also report the strict count (a public company whose 5%+ holder's Form ADV reports PE funds counts as PE minority stake) and, where easy, the share by parent company and by sales.
- **BDC overlap** (assembler): whether the brand, its operating company or its parent is a borrower in the latest DERA BDC data set.
- **Method and cost:** time, requests and tokens per category, and what made brands slow.

## Rules

- Public primary sources only (CLAUDE.md): SEC filings, company and sponsor press releases, sponsor portfolio pages, Form ADV, official registries. Trade press may supply the ranking only. No PitchBook, Preqin, CB Insights or any paywalled secondary source.
- Competitor sites (Buy'r, Worse on Purpose, Grass, ShopFair, Ethos) are never sources. Never fetch WhoIsMyDentist, Private Equity Vet or Reddit.
- Owner kinds here are research notes for a human decision, not engine classifications (ADR 0001 governs the product).
- Respect robots.txt. SEC requests use the user agent `EvidenceEngine ownership-research bot (category audit)` with no email or contact detail, and stay at or under 2 per second per worker.
- About 5 fetches per brand, then "not found".

## How to resolve

AFK, the same way the pilot ran:
- **Workers:** one per category, at most four at a time. Each invokes the `research` skill and writes `.scratch/chains-and-brands/research/category-audit/<category>.md`.
- **Assembler:** after the workers finish, one agent runs the Form ADV and DERA BDC matching and re-checks every quote with a script, including a negative control. It then writes `.scratch/chains-and-brands/research/category-audit-full.md` and appends `## Answer` here.
- No branches, commits or pushes.

## Answer

Findings: [research/category-audit-full.md](../research/category-audit-full.md) (assembled 2026-11-07; the ten worker files are in [research/category-audit/](../research/category-audit/)). Shares count by brand row, after the Form ADV pass. Strict means a public company whose 5%+ holder's Form ADV reports PE funds counts as PE minority stake; index and asset managers are left out, as in the pilot.

| Category | Rows | PE-owned plus PE minority | Upper bound | Strict |
|---|---|---|---|---|
| Pharmacies | 30 | 1 (3.3%); 30.7% of ranked Rx sales | 1 | 2 (6.7%) |
| Dollar and discount | 25 (13 core) | 2 (8.0%); core 1/13 | 2 | 4 (16.0%) |
| Car washes | 30 | 16 (53.3%); 70.5% of sites | 17 (56.7%) | 16 |
| Pet stores | 26 ranked | 5 (19.2%); 61.0% of locations | 7 (26.9%) | 5 |
| Women's apparel | 32 | 12 (37.5%) | 14 (43.8%) | 12 |
| Mattresses | 30 | 8 (26.7%) | 9 (30.0%) | 9 (30.0%) |
| Cookware | 30 | 4 (13.3%) | 4 | 4 |
| Vitamins and supplements | 30 | 3 (10.0%); 5 if the Yellow Wood sale closes | 5 (16.7%) | 3 |
| Dental chains | 30 | 15 (50.0%); 64.5% of offices | 19 (63.3%) | 15 |
| Veterinary chains | 21 | 11 (52.4%); 26.3% of hospitals | 16 (76.2%) | 11 |

- **Form ADV** changed car washes (10 to 16) and dollar and discount (0 to 2), the strict counts for pharmacies and mattresses (+1 each) and the vet upper bound (14 to 16). The decisive flags were Brigade, Arbour Lane, Freeman Spogli, Access Holdings, Point72, Wildcat, Cerberus, Coliseum, Deerfield and D1, all `Any PE Funds = Y`. Susquehanna Private Capital and OpCapita are not in the files; Anchorage reports N.
- **BDC overlap:** 66 of 284 brand rows (23.2%), through 43 borrower groups held by 88 BDCs at the latest DERA period (mostly 2026-06-30). 45 of the 77 PE or PE-minority rows overlap. By category: pharmacies 3, dollar 1, car washes 11, pet stores 6 (plus Chewy), women's apparel 8, mattresses 6, cookware 1, supplements 2 (plus 2 added rows), dental 22, vet 6. All five named worker leads were confirmed: FS KKR's dental equity, HPS and Knitwell, Churchill and Thorne, WhiteHorse and ClearWater, OHA and MedVet.
- **Quote check:** 1,022 quotes and HTML fields re-checked against re-downloaded pages. 943 matched the page text, 25 the raw HTML and 5 a worker copy; 48 were not checkable and 1 failed (CW10, a meta-description quote that is not on the cited page). 29 of 29 altered quotes failed in the negative control.
- **Cost:** workers 3,419,427 tokens in all (about 342k per category, against the pilot's 260k to 280k). The assembler took about 46 minutes and about 800 requests.
- **Open questions** are listed in the findings file, §7, as numbers only.
