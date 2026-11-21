# Task: Estimate local-business costs for New York, the tri-state area and the US

Type: task
Status: resolved
Blocked by: none
Map: [local-businesses](../map.md)

## Question

What would the parked local-businesses product add in cost on top of the chains-and-brands v1, for three scopes: New York alone, the tri-state area (all of New York, New Jersey and Connecticut, with Pennsylvania as an extra line), and the whole US? For each scope: build, one seeding pass, and a typical month, with low and high figures, plus whether the scope is feasible at all with free public data.

## Context

- Requested by the developer on 2026-11-20. The map stays parked (ADR 0004). This task estimates costs only. It doesn't unpark the map or decide any open local ticket; it assumes ranges where those tickets are open and names them.
- **Plan:** the developer pays for Claude Code on the $100 a month Max plan. Price Claude Code work (build, registry research, upkeep) as months of that plan, and check whether the pace fits the plan's limits; show API-equivalent dollars only as a secondary column.
- **Scope, from the parked plan** (`docs/pre-launch-seeding.md` §2, decisions.md §11):
  - national census plus rosters for dental practices, physician groups and urgent care, dermatology, ophthalmology and optometry, and ABA therapy (NPPES census);
  - national rosters only for vets, funeral homes, car washes and HVAC (no census);
  - deep research (the full connector fan-out) on every dental and vet practice in each launch state. For the tri-state and US scopes, treat every state in scope as a launch state.
  - On-demand research is gone (decisions.md §15), so there is no per-search research cost.
- **Decided facts:** New York is launch state 1 ("Launch states and metros"). NPPES is a free monthly 1.1 GB zip; the API caps at 1,200 results per query ("Research: NPPES bulk file and API"). New York's SoS data is free on data.ny.gov, with no officers for LLCs; New York licenses only individual vets, so its vet census needs a FOIL request; Florida publishes a free weekly CSV of about 2,500 vet establishments; Colorado's data is public domain; Texas and Arizona are paid or search-only ("Research: SoS and vet license boards in the launch states"). A rough figure on record: "a full NY run could be ~$1k of extraction" ("Launch-state run budget and the NYC-area counties").
- **Prices and unit costs:** take them from engine "Task: Estimate build, seeding and monthly running costs" (`.scratch/engine/research/cost-estimate.md`): about $0.003 per page and $0.019 per long filing on DeepSeek off-peak, DeepSeek Search $0.75 per 1,000, hosting options, Google Places prices. Google Places is lazy and on-demand only, never bulk (CLAUDE.md; decisions.md: used for a national census it "would be the project's largest bill").
- **Open tickets to assume ranges for:** "NPPES census load and census match" (31; the match is code, no LLM), "SoS and vet license board connectors" (33), "Pick the second launch state" (47), "Research: Rollup rosters for omitted medical specialties" (48), "Local business identity and resolution" (49, including geocoding), "Local fan-out and refresh cadence" (50: documents per business and how often the census-scale no-evidence set refreshes), "Launch-state run budget and the NYC-area counties" (51), "IRS exempt-org file and nonprofit owners" (79). Also the parked plan's registry work W1 (300 to 500 DSO, rollup and consolidator domains).
- **Counts:** nothing in the repo counts local businesses per state. Use the Census Bureau's County Business Patterns (latest year, by NAICS, for NY, NJ, CT, PA and the US) for establishment counts, plus published NPPES or professional-body counts where they help. Don't download the full NPPES file.
- **States beyond the researched five:** check NJ's and CT's SoS bulk data and vet license data, and for the US scope sample the ten most populous states, so the US figure rests on a stated sample.
- **Output:** `.scratch/local-businesses/research/cost-estimate.md`.
- **Rules:** no paid API calls; vendor and government pages as sources, each with the date read; bot rules as in CLAUDE.md, and stop and report on any permission refusal; never fetch whoismydentist.com, privateequityvet.org or Reddit; no paywalled data; no OpenAI models.

## Answer

Resolved 2026-11-20 by a background agent (about 290k tokens, three research workers, no paid API calls). Findings: `.scratch/local-businesses/research/cost-estimate.md`. Counts from the Census Bureau's County Business Patterns 2023 files (the Census API refused the request). The map stays parked.

| | New York | Tri-state (NY, NJ, CT) | US |
|---|---|---|---|
| Build, Max plan months | 3.3 to 6.7 ($330 to $670) | 3.6 to 7.4 ($360 to $740) | 8.1 to 22 ($810 to $2,220) |
| Developer hours | 80 to 250 | 90 to 290 | 210 to 780 |
| One seeding pass | $335 to $5,760 | $1,470 to $45,660 ($550 to $8,660 without New Jersey's registry file) | $13,900 to $153,700 |
| A typical month | $8 to $2,000 | $17 to $3,560 | $830 to $26,750 |
| Free public data enough? | Yes, apart from the vet census | Mostly | No |

- Every scope shares the national NPPES census (about 363,000 dental, physician and optometry sites) and national rosters; scopes differ in which states get deep research (9,485 dental and vet practices in New York, 16,716 tri-state, 169,961 US) and their own registry and vet board connectors.
- New York: free except the vet census (FOIL or NYSED's bulk verification files). Connecticut's registry is free; New Jersey sells its registry at $0.0185 a record (up to about $37,000), which the census doesn't need; none of the three licenses vet premises. US sample of 14 states: 6 sell their registry or offer search or records requests only; 3 have a vet premises list (Florida, California, North Carolina); extrapolated, 15 to 30 states need paid data or records requests.
- Biggest drivers: pages read per practice (mostly search results kept per query); paid state data; EDGAR full-text hits on practice names read whole; Google Places on demand after launch; the no-evidence refresh ($10,000 to $140,000 a pass at census scale, kept outside the totals).
- Figures assume today's rules. The cuts under discussion in engine "Cost cuts before revenue" (EDGAR filtering and windows, fewer search results, no scheduled refreshes) would lower the reading rows.
- Outside the cost question: Cloudflare Pages Free holds 20,000 files (100,000 paid), far below the census's 360,000-plus sites; and under the engine's stricter "checked" rule only deep-researched dental practices would read "No PE evidence found".
- Blocks and slips: Census API, Ohio, Georgia, Illinois and Michigan registry hosts, NJ consumer affairs and others refused or blocked (listed in the file); one research worker fetched one page on www.pacodeandbulletin.gov before reading its robots.txt (disallow all), recorded in the file.
- **Revised 2026-11-21** for engine "Cost cuts before revenue" (findings §11): seeding New York $150 to $3,043, tri-state $250 to $4,657 without New Jersey's file ($1,175 to $41,657 with it), US $11,197 to $122,629 ($2,347 to $38,269 on free data only); a month with no pass $5 to $27, $5 to $28 and $7 to $75; each pass priced when run.
