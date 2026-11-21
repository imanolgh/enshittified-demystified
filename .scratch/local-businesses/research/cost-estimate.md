# Task: Estimate local-business costs for New York, the tri-state area and the US

Ticket: [123-task-estimate-local-business-costs](../issues/123-task-estimate-local-business-costs.md) · Estimated 2026-11-20 by a background agent · Sources: the parked plan and the local tickets (cited by name), engine "Task: Estimate build, seeding and monthly running costs" ([cost-estimate.md](../../engine/research/cost-estimate.md), called "the chains estimate" below) for every price, unit cost and the pace measured so far, the Census Bureau's County Business Patterns 2023, and state and vendor pages read on 2026-11-20. No paid API calls were made.

The local product is parked (ADR 0004). This file estimates only what it would add on top of the chains-and-brands v1 engine. It decides nothing and unparks nothing. Where a local or engine ticket is open, it assumes a range and names the ticket.

## Summary

| | New York | Tri-state (NY, NJ, CT) | US (all 50 states) |
|---|---|---|---|
| Build: Claude Code on the $100 Max plan | 3.3 to 6.7 months ($330 to $670) | 3.6 to 7.4 months ($360 to $740) | 8.1 to 22 months ($810 to $2,220) |
| Build: API-equivalent (secondary) | $1,350 to $6,600 | $1,475 to $7,320 | $3,350 to $22,000 |
| Build: developer hours | 80 to 250 | 90 to 290 | 210 to 780 |
| One seeding pass, real spend | $335 to $5,760 | $1,470 to $45,660 ($550 to $8,660 without New Jersey's registry file) | $13,900 to $153,700 |
| A typical month, real spend plus any plan step-up | $8 to $2,000 | $17 to $3,560 | $830 to $26,750 |
| Can it be done with free public data? | Yes, apart from the vet census | Mostly | No |

- New York: yes, apart from vets. NPPES, data.ny.gov and the rosters are free. New York licenses only individual vets, so a vet census needs NYSED's bulk verification files or a FOIL request, which cost little or nothing but whose fields are unconfirmed.
- Tri-state: mostly. Connecticut's registry is free and complete. New Jersey sells its registry ($0.0185 a record, up to about $37,000 for the whole register), though the census and rosters don't need it. None of the three states licenses vet premises, so the scope has no vet premises census beyond what New York's FOIL list might give.
- US: no. In the 14-state sample, 6 states sell their registry or offer it only through search or records requests, 8 don't license vet premises, and only 3 have a list of premises with addresses. Extrapolated, 15 to 30 states would need paid data or records requests, and most states would have no vet census.

Bottom line: New York alone costs little in money. Its build is about 3.5 to 7 months of the Max plan and 80 to 250 developer hours, its seeding pass is a few hundred to a few thousand dollars, and its month runs from almost nothing to about $2,000, depending mostly on choices still open. The tri-state scope costs about the same plus New Jersey's registry, if it is bought. The US scope multiplies deep research by about 18 and adds dozens of state connectors and paid data: up to two years of the Max plan at the measured pace, and five- to six-figure seeding. Every scope shares the national census and rosters, so the census-backed "No PE evidence found" layer is about the same in all three (section 10). The build months leave out registry research (210 to 550 entries, 0.1 to 1.2 months of the plan), which sits in each seeding table, and they assume the local build follows the chains build rather than running beside it.

The five biggest cost drivers (not strictly ranked, since some are one-time and some monthly):

1. Pages read per practice in deep research, mostly search results kept per query (ticket 50, engine 118): $228 to $2,274 a pass in New York, $4,079 to $40,368 in the US.
2. Paid state data in the tri-state and US scopes: New Jersey's register up to $37,000 once; across the US $8,900 to $84,000 once and $750 to $11,870 a month.
3. EDGAR full-text hits on practice names, each read whole (ticket 70, engine 42): up to $20,388 a pass in the US, where generic practice names hit landlords' and lenders' filings.
4. Google Places on demand after launch, if search pays for Places on misses (engine 40): up to $800, $1,760 and $8,160 a month.
5. The no-evidence refresh (ticket 50): up to $296, $523 and $5,267 a month for a quarterly full fan-out on launch-state practices, and $10,000 to $140,000 a pass if it ran at census scale.

In the build, the US scope's state connectors (69 to 230 active days) outweigh everything else.

Fetch method note: before the first request to each host I or the three research workers read its robots.txt, including redirect targets. The Census Bureau's API host, api.census.gov, answered the robots.txt request with a firewall "Request Rejected" page, so I made no further requests there and used the published CBP files on www2.census.gov, whose robots.txt has no rule for `*`; www.census.gov's allows the datasets page. developers.cloudflare.com allows the pages read. The workers recorded these refusals and made no further requests to them: www.ohiosos.gov and businesssearch.ohiosos.gov (403 even for robots.txt), codes.ohio.gov (robots.txt disallows everything), ovmlb.ohio.gov (404 for every page), sos.ga.gov, ecorp.sos.ga.gov, verify.sos.ga.gov and goals.sos.ga.gov (403 for robots.txt), www.ilsos.gov and apps.ilsos.gov (Akamai 403), ilga.gov (TLS failure), online-dfpr.micropact.com (robots.txt disallows Claude agents), www.michigan.gov (Akamai 403), mibusinessregistry.lara.state.mi.us (403 page; robots.txt disallows Claude-User), data.michigan.gov (robots.txt disallows everything), cofs.lara.state.mi.us (no connection), leginfo.legislature.ca.gov and govt.westlaw.com (Cloudflare challenge), dca.njoag.gov (Incapsula 403 for robots.txt), file.dos.pa.gov/data-requests (Cloudflare challenge), www.cga.ct.gov (TLS failure; the official mirror prdext2.cga.ct.gov was used), nj.accessgov.com (robots.txt served as a script-only page, skipped) and one sosnc.gov search path (403). Paths disallowed by robots.txt were not fetched on service.ct.gov, search.dca.ca.gov, data.ca.gov and app.box.com and dca.box.com (folder listings only, no file downloads). rules.sos.ga.gov names ClaudeBot as blocked but allows `*` on `/gac/700`, the one page read. One slip: a worker fetched one page on www.pacodeandbulletin.gov (the table of contents of 49 Pa. Code Ch. 31) before noticing that its robots.txt disallows everything for `*`, and made no further requests there. Facts that came only from search-engine snippets of official pages, mostly for Ohio, Georgia, Michigan and Illinois, are tagged as such in the source list and should be treated as unconfirmed. Nothing was bought, no account was opened and no form was sent.

Sources:
- [CHAINS] Engine "Task: Estimate build, seeding and monthly running costs", [cost-estimate.md](../../engine/research/cost-estimate.md), 2026-11-20. Every DeepSeek, Places, hosting, storage and Claude price below comes from it unless another tag is given.
- [CBP-DS] Census Bureau, County Business Patterns datasets page (lists "County Business Patterns: 2023, June 26, 2025" as the latest release): https://www.census.gov/programs-surveys/cbp/data/datasets.html, read 2026-11-20
- [CBP-ST] CBP 2023 state file: https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23st.zip, read 2026-11-20
- [CBP-US] CBP 2023 US file: https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23us.zip, read 2026-11-20
- [CF-PAGES-LIM] Cloudflare Pages limits (20,000 files a site on Free, 100,000 on paid plans; page updated 2026-11-19): https://developers.cloudflare.com/pages/platform/limits/, read 2026-11-20
- [CF-WORKERS] Cloudflare Workers pricing (Workers Paid from $5 a month per account, 10 million requests included, $0.30 per extra million): https://developers.cloudflare.com/workers/platform/pricing/, read 2026-11-20
- [NPPES] Local "Research: NPPES bulk file and API", [nppes.md](nppes.md), 2026-10-26
- [SOS5] Local "Research: SoS and vet license boards in the launch states", [sos-vet-boards.md](sos-vet-boards.md), 2026-10-29
- [PLACES] Engine "Research: Google Places terms, pricing and a free geocoder", [places-geocoder.md](../../engine/research/places-geocoder.md)
- [TX-BULK] Texas SoS, Business Filings Bulk Order: https://www.sos.state.tx.us/corp/bulk-order.shtml, read 2026-10-29 (cited through [SOS5])
- [NJ-FEES] New Jersey Division of Revenue and Enterprise Services, fees (bulk status reports $0.0185 a record; page updated 2026-07-01): https://www.nj.gov/treasury/revenue/fees.shtml, read 2026-11-20
- [NJ-PORTAL] New Jersey business records, status reports and principal search: https://www.njportal.com/DOR/BusinessRecords/EntityDocs/BusinessStatCopies.aspx, read 2026-11-20
- [NJ-OPRA] New Jersey Open Public Records Act text: https://www.nj.gov/grc/laws/act/, read 2026-11-20
- [NJ-DCA] New Jersey Division of Consumer Affairs standard licensee files, folder listing only: https://app.box.com/v/DCAStandardFiles, read 2026-11-20 (the DCA list page itself refused automated requests and was seen only as a search snippet)
- [NJ-REG] N.J.A.C. 13:44 (veterinary rules), on Cornell LII as a third-party pointer: https://www.law.cornell.edu/regulations/new-jersey/title-13/chapter-44, read 2026-11-20
- [CT-MASTER] data.ct.gov, Business Master n7gp-d28j, Principals ka36-64k6, Agents qh2m-n44y, Name Change History enwv-52we, Business Filing History ah3s-bes7, metadata at https://data.ct.gov/api/views/n7gp-d28j.json and siblings; portal terms https://data.ct.gov/terms; read 2026-11-20
- [CT-LIC] data.ct.gov, State Licenses and Credentials ngch-56tr: https://data.ct.gov/api/views/ngch-56tr.json, read 2026-11-20
- [CT-STAT] Connecticut General Statutes Chapter 384: https://prdext2.cga.ct.gov/2025/pub/chap_384.htm, read 2026-11-20
- [PA-DATA] data.pa.gov, Registered Businesses in PA Current by County xvd7-5r2c: https://data.pa.gov/api/views/xvd7-5r2c.json, read 2026-11-20
- [PA-FAQ] Pennsylvania DOS business FAQ (no registered agents): https://www.pa.gov/agencies/dos/resources/business-resources/frequently-asked-questions, read 2026-11-20
- [PA-FEES] Pennsylvania DOS business fees: https://www.pa.gov/agencies/dos/programs/business/fees-and-payments, read 2026-11-20
- [PA-RTK] Pennsylvania DOS Right-to-Know policy: https://www.pa.gov/content/dam/copapwp-pagov/en/dos/programs/professional-licensing/rtk_notice_for_web.pdf, read 2026-11-20
- [PA-VET] Pennsylvania State Board of Veterinary Medicine: https://www.pa.gov/agencies/dos/department-and-offices/bpoa/boards-commissions/veterinary-medicine, read 2026-11-20
- [PA-LIST] Pennsylvania licensee list requests: https://www.pa.gov/agencies/dos/programs/professional-licensing/list-requests, read 2026-11-20
- [CA-MANUAL] California bizfile Online Portal Manual (April 2022), §19.1 bulk orders: https://bpd.cdn.sos.ca.gov/ucc/ucc-online-help.pdf, read 2026-11-20
- [CA-SOS] California SoS business entity records: https://www.sos.ca.gov/administration/public-records-act-requests/business-entity-records; bizfile terms of use: https://www.sos.ca.gov/business-programs/bizfile/privacy-warning-terms-and-conditions-use/; both read 2026-11-20
- [CA-VMB] California Veterinary Medical Board, premises application and premises regulation document: https://www.vmb.ca.gov/forms_pubs/premise_initial_app.pdf and https://www.vmb.ca.gov/laws_regs/alt_vet_premises_isr.pdf, read 2026-11-20
- [CA-DCA] California DCA licensee lists: https://www.dca.ca.gov/consumers/public_info/index.shtml, and the vet folder listing https://dca.box.com/s/oss6hf8jys2bmgxqd2gdz7w4oepm2il9, read 2026-11-20
- [IL-SOS] Illinois SoS Data Transparency Act files and procedures (https://www.ilsos.gov/data/bus-serv-home.html, proc_llc_data.pdf, proc_corp_data.pdf), seen through search snippets on 2026-11-20 because the host refused automated requests; Public Act 102-0049
- [IL-LIC] data.illinois.gov, Professional Licensing pzzh-kp68 (ODbL): https://data.illinois.gov/d/pzzh-kp68, and IDFPR veterinary page https://idfpr.illinois.gov/profs/vet.html, read 2026-11-20
- [MI-FOIA] Michigan FOIA fees, MCL 15.234: https://www.legislature.mi.gov/documents/mcl/pdf/mcl-15-234.pdf, read 2026-11-20
- [MI-VET] Michigan Public Health Code Part 188: https://www.legislature.mi.gov/documents/mcl/pdf/mcl-368-1978-15-188.pdf, read 2026-11-20; LARA "License Lists and Reports" seen only as a search snippet
- [OH-SOS] Ohio SoS business reports (ohiosos.gov/business/business-reports), seen only through search snippets on 2026-11-20; ORC 4741.28 and OAC 4741-2-01 likewise
- [GA-BULK] Georgia bulk corporations data: https://georgia.gov/bulk-corporations-data, https://services.georgia.gov/gta/odi-innovations/corporationsDataHome.do and the sales agreement https://georgia.gov/document/document/bulk-corporations-data-sales-agreement/download, read 2026-11-20
- [GA-RULES] Georgia State Board of Veterinary Medicine rules, Department 700: https://rules.sos.ga.gov/gac/700, read 2026-11-20
- [GA-ROSTER] Georgia SoS roster request forms (sos.ga.gov), seen only through search snippets on 2026-11-20
- [NC-FEES] North Carolina SoS data subscriptions: https://www.sosnc.gov/fees/by_title/_data_subscriptions and data dictionaries https://www.sosnc.gov/online_services/data_subscriptions/data_dictionaries, read 2026-11-20
- [NC-VMB] North Carolina Veterinary Medical Board data requests: https://www.ncvmb.org/professional.php?section=requests, and G.S. 90-187.10: https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_90/GS_90-187.10.html, read 2026-11-20

## 1. Prices and unit costs used

All taken from [CHAINS] section 1, unchanged:

- DeepSeek V4.1 Flash reads, off-peak: about $0.003 per ordinary page, $0.0044 as the measured average, and $0.010 to $0.025 per EDGAR filing read whole (short exhibits and 8-Ks at the low end, long 10-Ks read in windows at the high end). Bulk seeding runs off-peak; single reads made at once cost up to 1.21 times as much on average. Treat page costs as about ±30%.
- DeepSeek Search: $0.75 per 1,000 successful requests.
- Google Places (New): Text Search IDs-only free and unlimited; Text Search Pro $32 per 1,000 after 5,000 free a month, $25.60 from 100,000 to 500,000, $19.20 from 500,000 to 1 million; Place Details Pro $17 per 1,000 after 5,000 free [PLACES].
- Hosting: Hetzner CPX42 (8 vCPU, 16 GB, 320 GB) €59.49, about $65; DigitalOcean managed PostgreSQL 8 GiB $122.10 with extra storage at $0.215 per GiB, 16 GiB Droplet $96; Backblaze B2 $6.95 per TB a month with Object Lock.
- Claude Code: the developer's Max plan, $100 a month. The measured pace is 19 active days in 35 calendar days, about 3.8 active days a week or about 16.5 a month. One measured planning day processed about 100 million tokens, $39 at Opus 5.5 list prices; build days are priced at $25 to $60 of API-equivalent usage, as in [CHAINS] section 3. Research workers cost $28 to $35 per million harness tokens.

New prices read for this estimate:

- Cloudflare Pages holds 20,000 files a site on the Free plan and 100,000 on paid plans [CF-PAGES-LIM]. Workers Paid costs at least $5 a month per account, with 10 million requests included and $0.30 per extra million; Pages Functions bill as Workers [CF-WORKERS].

## 2. Establishment counts

Source: County Business Patterns 2023, the latest release (June 26, 2025) [CBP-DS]. The Census Bureau's API host, api.census.gov, rejected the first request (its robots.txt returned a "Request Rejected" firewall page), so I stopped using it and read the published state and US files instead [CBP-ST, CBP-US]. Counts are establishments (physical locations with paid employees) for all legal forms (`lfo` = "-"). CBP leaves out businesses with no paid employees and government-run sites.

| Vertical | NAICS code (title) | NY | NJ | CT | Tri-state | PA (extra) | US | Fit |
|---|---|---|---|---|---|---|---|---|
| Dental practices | 621210 Offices of dentists | 8,001 | 4,511 | 1,625 | 14,137 | 4,649 | 135,665 | Close. Includes specialists; dental labs are elsewhere. |
| Physician groups (incl. dermatology and ophthalmology) | 621111 Offices of physicians (except mental health specialists) | 12,412 | 7,335 | 2,648 | 22,395 | 7,854 | 204,617 | Loose. See below. |
| Urgent care (part) | 621493 Freestanding ambulatory surgical and emergency centers | 421 | 296 | 79 | 796 | 252 | 10,042 | Loose. Also holds surgery centers; many urgent care sites sit in 621111. |
| Optometry | 621320 Offices of optometrists | 941 | 617 | 239 | 1,797 | 812 | 22,501 | Close. |
| ABA therapy (no code; nearest) | 621330 Offices of mental health practitioners (except physicians) | 2,864 | 1,062 | 444 | 4,370 | 1,387 | 46,513 | Very loose. ABA is a small, unknown share. |
| Veterinary clinics | 541940 Veterinary services | 1,484 | 717 | 378 | 2,579 | 1,270 | 34,296 | Close. See the Florida check below. |
| Funeral homes | 812210 Funeral homes and funeral services | 1,027 | 447 | 193 | 1,667 | 966 | 15,183 | Close. Crematories sit in 812220 with cemeteries (US 5,049). |
| Car washes | 811192 Car washes | 964 | 661 | 218 | 1,843 | 628 | 19,807 | Close. |
| HVAC and plumbing | 238220 Plumbing, heating, and air-conditioning contractors | 7,061 | 3,454 | 1,318 | 11,833 | 4,154 | 111,207 | Close. |
| Electrical | 238210 Electrical contractors and other wiring installation contractors | 5,232 | 2,641 | 1,204 | 9,077 | 2,750 | 83,342 | Close. |

Where the mapping is loose:

- Physician groups versus single offices. 621111 counts every physician office site, from a one-doctor office to each site of a large group, and every specialty. The plan's NPPES taxonomy list reaches only family medicine, internal medicine, general practice, pediatrics, emergency medicine, multi-specialty group codes, dermatology and ophthalmology [NPPES]; specialties such as cardiology or orthopedics are in 621111 but not in the census until ticket 48 and ticket 49 say so. So 621111 overstates the physician census. Size classes give a rough split: 6,450 of New York's 12,412 sites (52%) and 107,858 of the US's 204,617 (53%) have fewer than 5 employees, which is roughly the single-doctor office.
- Dermatology and ophthalmology have no code of their own; they are inside 621111.
- Urgent care has no code. Sites appear in 621111 or 621493, and 621493 also holds ambulatory surgery centers.
- ABA therapy has no code. Providers file under 621330, 621340 (therapists), 621498 (other outpatient centers) or 624120 (services for persons with disabilities). 621330 is shown as the nearest, and it is an upper bound only.
- Vets: Florida licenses vet premises, and its DBPR file listed 2,489 establishments with a Florida address in October 2026 [SOS5]. CBP counts 2,585 Florida 541940 establishments, so CBP tracks the premises count within about 4% there.

NPPES counts will differ from CBP. NPPES carries Type 1 sole proprietors with no employees, several NPIs for one practice, and practices whose taxonomy codes miss the filter [NPPES]. Whether Type 1 records join the census is open in ticket 49. For deep research, this estimate uses CBP for the low case and CBP plus 25% for dental in the high case (Type 1 sole proprietors and extra NPIs). For vets it uses CBP in both cases.

## 3. How the local work is sized

### What every scope shares

The parked plan builds two layers nationally whatever the launch states are (`docs/pre-launch-seeding.md` §2; decisions.md §11): the NPPES census with rosters for the 2A verticals (dental, physician groups and urgent care, dermatology, ophthalmology and optometry, ABA), and rosters only for the 2B verticals (vets, funeral homes, car washes, HVAC). Rosters are national because each DSO or rollup publishes one list for all its sites, and NPPES is one national file. So the national layer costs the same in all three scopes. The scopes differ in which states get deep research and their own SoS and vet board connectors. If the census were cut to New York alone, the cost would barely change (the load and match are code), but the coverage in section 10 would shrink.

The chains-and-brands v1 already covers part of the national layer. Its launch industries include urgent care, veterinary care, car washes and dental care, about 30 brands each ("Launch industries"), so the large DSOs, vet consolidators and car-wash chains will already have registry entries, EDGAR full-text search and DeepSeek Search runs. The local layer adds the long tail: the parked plan's W1 list of 300 to 500 DSO, rollup and consolidator domains, of which this estimate assumes 20 to 40% are already in the chains registry, leaving 180 to 400 new rollup entries plus 30 to 150 new investment-firm entries (210 to 550 in all). It also adds roster selectors, which chains v1 doesn't build (engine 74 keeps only the status-only selector on the launch path).

### Documents per practice (deep research)

Documents per local business are open ("Local fan-out and refresh cadence", 50). The parked plan's fan-out for one practice is: the practice's own site, SoS records, press found through DeepSeek Search, EDGAR full-text search on the practice and owner names, and NPPES and board records (research_flows.md A1; pre-launch-seeding.md §2C). Google Places is out of seeding (CLAUDE.md), so the practice's own site has to come from the search results.

| Read | Who reads it | Low case | High case |
|---|---|---|---|
| DeepSeek Search queries (name and town; name with "acquired", "joins" or "partners") | Search API | 2 per practice | 4 per practice |
| Search results fetched and read (local news, releases, rollup pages; directory listings dropped by a domain filter in the low case) | DeepSeek | 3 per query, 6 per practice | 10 per query, 40 per practice |
| The practice's own site (home, about, team) | DeepSeek | 2 pages | 5 pages |
| EDGAR full-text search on the practice's legal name, DBA and other names, every hit read whole (ticket 70) | Code to search, DeepSeek to read | 0.3 hits per practice on average (most have none) | 4 hits per practice on average (generic names such as "Family Dental" hit landlords' tenant lists and lenders' schedules, up to the 100-hit cap) |
| NPPES record, census match, SoS bulk record, vet board list, FOIL list | Code parsers | no LLM cost | no LLM cost |
| Owner names | | A practice owned by a DSO is covered by the DSO's own runs; an independent's owner is a person, and the product keeps no profiles of individual people, so no per-person search | same |

Per practice that is $0.029 (8 pages at $0.003, 0.3 filings at $0.010, 2 queries, 3% retries) to $0.33 (45 pages at $0.0044, 4 filings at $0.025, 4 queries, 10% retries). The New York figure on record, "a full NY run could be ~$1k of extraction" ("Launch-state run budget and the NYC-area counties"), falls inside the New York range below ($270 to $3,460 for the three deep-research rows, before retries).

### Claude Code on the Max plan

Build work is sized in active days per part, as in [CHAINS] section 3, and converted to months of the $100 Max plan at the measured 3.8 active days a week (about 16.5 a month). The API-equivalent column prices the same days at $25 to $60, for comparison only.

Whether this fits the plan: the measured planning ran at about $640 of API-equivalent usage per 30 days, all of it on the developer's current plan [CHAINS] section 2. A local build at the same daily intensity and the same number of active days a week should fit too, since it is the same kind of work. Two things could break that. First, if the local build ran while the chains product needs its own upkeep (3 to 12 active days a month in [CHAINS] section 5), the two together would pass the measured pace, and the plan's weekly limit may start to bind. Second, the US scope's upkeep alone (section 6) could reach 20 active days a month, above the measured pace. Anthropic states limits only as multiples of Pro, so no exact check is possible; the `/usage` bars are the real test. Upkeep is priced at $0 extra inside the Max plan, up to $100 a month more if the step up to the Ultra plan ($200) is needed.

## 4. New York

New York is launch state 1 ("Launch states and metros"). Deep research covers 8,001 to 10,001 dental practices and 1,484 vet practices, 9,485 to 11,485 in all. NY vets can be deep-researched in full only once a vet list exists (FOIL or NYSED's bulk verification files); until then only roster-known vets can be reached, so the vet half of the work may run later or smaller.

### Build

| Item | Low | High | API-equivalent | How it was derived | Source |
|---|---|---|---|---|---|
| Remaining local decisions and the local spec | 6 days | 12 days | $150 to $720 | Open local tickets 31, 33, 47, 49, 50, 51 and 79, the coverage-state mapping and seeding runbooks from the map's "Not yet specified", then `.scratch/local-businesses/spec.md` | local map |
| Research ticket 48 (rollup rosters for omitted medical specialties) | 1 day | 2 days | $56 to $140 | 2 to 4 million harness tokens at $28 to $35 per million, by the size of earlier research tickets | ticket 48; [CHAINS] section 2 |
| NPPES census load: monthly zip, weekly files, deactivation XLSX, other-names and practice-location files, streaming with polars | 3 days | 6 days | $75 to $360 | 10.8 GB CSV with 330 columns; file names change monthly and the index page can go down | ticket 31; [NPPES] |
| Local identity and resolution: location versus company, the `npi` scheme, Type 1 versus Type 2, taxonomy mapping, the census and NPPES API in the lookup order | 5 days | 10 days | $125 to $600 | | ticket 49; engine 19 (open) |
| Geocoding: Census Geocoder batch client (10,000 rows a batch), retries for its run-to-run match drift, a fallback for no-match business addresses | 2 days | 4 days | $50 to $240 | The Census FAQ lists commercial addresses as a no-match cause | ticket 49; [PLACES] |
| Census match: roster locations to census entities, address normalization, many-to-one cases, `operated_by` claims, no-evidence derivation, coverage states | 5 days | 10 days | $125 to $600 | Code, no LLM | ticket 31; map "Coverage states" |
| Selector producers for rosters: config schema, shape check, item-set diffs, the closing rule | 5 days | 10 days | $125 to $600 | The general selector work chains v1 leaves out | engine 74 (open) |
| Roster entries in the registry crawler (roster page role, location detail pages, gap report for rollups) | 2 days | 4 days | $50 to $240 | | engine "Rosters, portfolio pages and the registry" |
| Launch-state deep batch: intake of a state's census slice, per-practice routing, practice-site discovery from search results, EDGAR search on practice names, the per-batch spend cap | 6 days | 12 days | $150 to $720 | | research_flows.md A1; tickets 50, 51 |
| Local Beat jobs: NPPES monthly reload, census re-match after each roster crawl, vet board refresh, the no-evidence refresh | 2 days | 5 days | $50 to $300 | | ticket 50; engine 119 (open) |
| IRS exempt-org file for nonprofit owners: where EINs come from, matching, cadence | 2 days | 5 days | $50 to $300 | NPPES suppresses EINs | ticket 79; [NPPES] |
| Read API for local: geographic queries, local cards, coverage states | 3 days | 6 days | $75 to $360 | | engine 39, 41, 69 |
| Website: map (MapLibre with open tiles, decisions.md §6), local business pages, vertical pages, search by place, and pages served on request because the census can't fit Pages' file limit | 8 days | 15 days | $200 to $900 | 20,000 files on Pages Free, 100,000 on paid plans; the national census is 360,000 or more sites | [CF-PAGES-LIM] |
| Operations for the bigger corpus: database sizing, more workers, backups | 1 day | 3 days | $25 to $180 | | engine 43 (open) |
| New York connectors: SoS from data.ny.gov (active entities, name history, merger constituents, daily filings), plus a loader for the FOIL or NYSED vet list | 3 days | 6 days | $75 to $360 | Each with 2 or 3 real fixtures and one live lookup | [SOS5]; ticket 33 |
| Model test spend (golden runs on practice pages, live lookups) | $5 | $30 | | Real DeepSeek spend, as in [CHAINS] | [CHAINS] |
| Build total, Claude Code | 54 days | 110 days | $1,350 to $6,600 | | sum |
| On the Max plan | 3.3 months, $330 | 6.7 months, $670 | | 54 to 110 active days at 3.8 a week | [CHAINS] section 2 |
| Developer hours | 80 h | 250 h | | Grilling and spec review 15 to 40 h; reviewing and committing build work at 1 to 1.5 h per build day, 47 to 144 h; approving 210 to 550 registry entries by commit at 1.5 to 4 minutes each (roster entries carry selectors, so slower than chains' 1 to 2.5 minutes), 5 to 37 h; the FOIL request and follow-up 2 to 6 h; operating the seeding pass 10 to 25 h | CLAUDE.md; engine "Rosters, portfolio pages and the registry" |

### One seeding pass

| Item | Low | High | How it was derived | Source |
|---|---|---|---|---|
| Deep research: DeepSeek Search queries | $14 | $34 | 9,485 to 11,485 practices × 2 to 4 queries (19,000 to 46,000) × $0.75 per 1,000 | section 3; [CHAINS] |
| Deep research: pages read (search results and the practice's own site) | $228 | $2,274 | 8 to 45 pages per practice = 75,900 to 516,800 pages × $0.003 to $0.0044 | section 3 |
| Deep research: EDGAR hits read whole | $28 | $1,148 | 0.3 to 4 hits per practice = 2,800 to 45,900 filings × $0.010 to $0.025 | section 3; ticket 70 |
| Code reads: NPPES, census match, NY SoS records, the vet list, Form ADV and IAPD PDFs for new firms | $0 | $0 | No LLM | tickets 31, 33; engine "Form ADV and IRS exempt-org ingestion" |
| National: roster pages read by DeepSeek where no selector exists | $12 | $352 | 40,000 to 80,000 roster locations nationally ("tens of thousands", decisions.md §11); 10% read by DeepSeek in the low case, all of them in the high case | engine 74 (open) |
| National: newsroom first crawls for new local entries | $9 | $387 | 210 to 550 new entries, 50 to 80% with a newsroom, 30 to 200 releases each (3,150 to 88,000 releases) | [CHAINS] section 4 method |
| National: about, portfolio and detail pages of new entries | $2 | $48 | 3 to 20 pages per entry | [CHAINS] section 4 method |
| National: EDGAR full-text search for new tracked rollups | $23 | $675 | 180 to 400 rollups × 1.2 to 1.5 names × 15 to 60 hits (smaller than chains' 40 to 80, since long-tail rollups are less often named in filings) × 70 to 75% unique = 2,300 to 27,000 filings | ticket 70; engine 37 (full-text search on every tracked company) |
| National: DeepSeek Search for new tracked rollups | $9 | $178 | 3 to 5 queries each, 5 to 20 results read per query | engine 118 (open) |
| Retries and the daily unreadable sweep | $10 | $510 | 3 to 10% of the rows above | engine "Extraction execution" |
| DeepSeek and search subtotal | $335 | $5,607 | | |
| Geocoding | $0 | $0 | 360,000 to 900,000 census addresses through the Census Geocoder in 36 to 90 batches of 10,000; free, no key | [PLACES] |
| Google Places | $0 | $0 | Lazy only, never bulk | CLAUDE.md |
| Records requests | $0 | $150 | One FOIL request to NYSED for the vet licensee list with addresses. NY law allows only actual cost for electronic records and no fee under two hours of staff time (POL §87(1)(c)); $150 assumes about five hours at a clerk's wage, which wasn't read | [SOS5]; ticket 47 |
| Registry research (Claude writes 210 to 550 entries with roster selectors) | 2 days | 20 days | 3.2 to 22 million harness tokens (15,000 to 40,000 per entry, above chains' 8,000 to 25,000 because rosters need selectors) × $28 to $35 per million = $90 to $770 API-equivalent, or 0.1 to 1.2 months of the Max plan at the measured pace | [CHAINS] section 2 |
| Seeding total, real spend | $335 | $5,760 | Plus the registry research inside the plan fee | |

Throughput: 517,000 pages at 50 parallel reads and a 13-second median answer take about a day and a half of DeepSeek time. Fetching is slower where search results cluster on a few domains, since each domain has its own token bucket, and directory sites often disallow bots in robots.txt; those results are skipped, which pulls the real page count toward the low case.

### A typical month

| Item | Low | High | How it was derived | Source |
|---|---|---|---|---|
| New releases in local registry newsrooms | $1 | $23 | 105 to 440 newsrooms × 3 to 10 releases × $0.003 to $0.0044, times up to 1.21 for reads at once | [CHAINS] section 5 method |
| Changed roster pages re-read by DeepSeek | $1 | $639 | Low: 4,000 DeepSeek-read pages × 4 passes × 2% changed. High: 80,000 pages × 30 passes × 5% = 120,000 re-reads. Only a changed extracted text triggers a read | engine 119 (open); engine "Document storage, fetch log and last-confirmed" |
| New EDGAR filings for tracked rollups and practice names | $1 | $47 | Rollups: 216 to 600 names × 0.5 to 2 new hits. Practices: 0.001 to 0.03 new hits a month each, which is the seeding hit rate spread over 25 years of filings. × $0.010 to $0.025, times up to 1.21 | ticket 70 |
| No-evidence refresh | $0 | $296 | Low: roster re-match only, which is code. High: a quarterly full fan-out on the New York practices: every query again, with a quarter of the pages and hits new or changed, spread over three months | ticket 50 (open) |
| Google Places, on demand after launch | $0 | $800 | 10,000 to 100,000 local searches a month (unmeasured). Low: IDs-only Text Search, free and unlimited, matched against stored place IDs. High: Text Search Pro on 30% of searches (30,000 calls, 5,000 free) at $32 per 1,000 | engine 40 (open); [PLACES] |
| Model and API subtotal | $3 | $1,806 | | |
| Hosting, added | $0 | $65 | Low: fits on the chains host (Hetzner CPX42, 320 GB), since the national census, NY SoS tables and NY's documents are tens of GB. High: a second CPX42 for workers and the database | [CHAINS] section 1; engine 43 (open) |
| Object storage, added | $0 | $2 | 76,000 to 517,000 pages at 0.1 to 0.3 MB, 2,800 to 46,000 EDGAR filings at about 1 MB, and NPPES zips at 1.1 GB a month: about 10 to 200 GB on B2 at $6.95 per TB | [CHAINS] section 1 |
| Website: pages on request and map tiles | $5 | $25 | Workers Paid minimum $5, which includes 10 million requests. Open map tiles hosted as files cost storage and bandwidth only, $0 to $20 assumed (not priced from a vendor page) | [CF-WORKERS]; decisions.md §6 |
| Claude Code upkeep (roster selectors that break, two state connectors, registry gaps) | $0 | $100 | 2 to 6 active days a month, 12 to 37% of the measured pace: inside the existing Max plan, or $100 more for Ultra if chains and local upkeep together pass the limits. API-equivalent $50 to $360 | section 3 |
| Monthly total | $8 | $2,000 | | |

Contingencies outside the totals: each new prompt or model version re-reads the local corpus, another $335 to $5,600 (the seeding subtotal); and if ticket 50 chose a full fan-out at census scale for the no-evidence refresh, each pass over the national 2A census would cost $10,000 to $140,000 (360,000 to 470,000 sites at $0.029 to $0.30 each).

## 5. Tri-state (New York, New Jersey and Connecticut)

All three states are launch states. Deep research covers 14,137 to 17,671 dental practices and 2,579 vet practices, 16,716 to 20,250 in all. The national layer is the same as in New York. What the two extra states add (section 7 has the sources):

- Connecticut publishes its whole registry free on data.ct.gov, updated daily, with principals (officers, members and managers), registered agents and name history, mostly marked Public Domain. It licenses only individual vets; its free daily licensee list has a street address of record (which may be a home address) and almost no practice names.
- New Jersey sells its registry in bulk at $0.0185 per record, without officers. It licenses only individual vets; the Division of Consumer Affairs offers free licensee lists, but they sit in a Box folder whose robots.txt lets a bot read only the listing page, so the files would have to be downloaded by hand, and their fields are unconfirmed.
- Neither state licenses vet premises, so neither gives a vet premises census. A census of practice sites could only be derived from licensees' addresses, which this estimate doesn't assume.

### Build

| Item | Low | High | API-equivalent | How it was derived | Source |
|---|---|---|---|---|---|
| Everything in the New York build | 54 days | 110 days | $1,350 to $6,600 | Section 4 | section 4 |
| Decisions for two more states (whether to buy New Jersey's file, how to treat individual-only vet lists) | 1 day | 3 days | $25 to $180 | | ticket 33 |
| New Jersey connectors: parser for the bought bulk file and its monthly updates; loader for the hand-downloaded DCA vet list | 2 days | 5 days | $50 to $300 | Fields of the vet list unconfirmed | [NJ-FEES]; [NJ-DCA] |
| Connecticut connectors: data.ct.gov master, principals, agents, name history and filing history; the eLicensing vet list | 2 days | 4 days | $50 to $240 | Socrata, like New York | [CT-MASTER]; [CT-LIC] |
| Build total, Claude Code | 59 days | 122 days | $1,475 to $7,320 | | sum |
| On the Max plan | 3.6 months, $360 | 7.4 months, $740 | | at 3.8 active days a week | [CHAINS] section 2 |
| Developer hours | 90 h | 290 h | | Grilling and spec review 18 to 48 h; build review 51 to 158 h; registry approvals 5 to 37 h; the FOIL request and the New Jersey purchase 3 to 10 h; operating the seeding pass 15 to 35 h | |

### One seeding pass

| Item | Low | High | How it was derived | Source |
|---|---|---|---|---|
| Deep research: DeepSeek Search queries | $25 | $61 | 16,716 to 20,250 practices × 2 to 4 queries | section 3 |
| Deep research: pages read | $401 | $4,010 | 133,700 to 911,300 pages | section 3 |
| Deep research: EDGAR hits read whole | $50 | $2,025 | 5,000 to 81,000 filings | section 3 |
| National layer (rosters, new registry entries, rollups' EDGAR and search) | $55 | $1,640 | Same rows as New York | section 4 |
| Retries | $16 | $774 | 3 to 10% | |
| DeepSeek and search subtotal | $547 | $8,509 | | |
| New York FOIL request | $0 | $150 | As in section 4 | [SOS5] |
| New Jersey registry bulk file | $925 | $37,000 | $0.0185 per record. Low: only professional corporations, about 50,000 records (assumed). High: the whole register, about 2 million records, scaled from New York's 4.3 million and Pennsylvania's 2.4 million active entities per resident, since New Jersey's own count wasn't read. Dental and vet practices are mostly professional corporations or LLCs, and the file can be selected only by entity type and filing date, so finding every practice needs most of the register. Skipping New Jersey's registry is also possible (ticket 33): NPPES and the rosters don't need it. | [NJ-FEES] |
| Connecticut data | $0 | $0 | Free | [CT-MASTER] |
| Registry research (Claude) | 2 days | 20 days | Same as New York | section 4 |
| Seeding total, real spend | $1,472 | $45,660 | Without New Jersey's file: $547 to $8,660 | |

### A typical month

| Item | Low | High | How it was derived | Source |
|---|---|---|---|---|
| New releases, changed roster pages | $2 | $662 | Same as New York | section 4 |
| New EDGAR filings for tracked rollups and practice names | $1 | $55 | As in New York, with 16,716 to 20,250 practices | section 4 |
| No-evidence refresh | $0 | $523 | Low: re-match only. High: quarterly full fan-out on the tri-state practices | ticket 50 (open) |
| Google Places, on demand | $0 | $1,760 | 20,000 to 200,000 local searches a month; high case 60,000 Pro calls, 5,000 free, at $32 per 1,000 | engine 40 (open); [PLACES] |
| New Jersey registry updates | $9 | $370 | New filings selected by date at $0.0185: 500 professional corporations a month (low) to 20,000 records (high), both assumed | [NJ-FEES] |
| Model, API and data subtotal | $12 | $3,370 | | |
| Hosting, added | $0 | $65 | As in New York | section 4 |
| Object storage, added | $0 | $3 | About 20 to 350 GB | |
| Website: pages on request and map tiles | $5 | $25 | As in New York | [CF-WORKERS] |
| Claude Code upkeep | $0 | $100 | 2.5 to 7 active days a month (four state connectors instead of two): inside the Max plan, or Ultra. API-equivalent $60 to $420 | section 3 |
| Monthly total | $17 | $3,560 | | |

Contingencies outside the totals: a version re-read of the local corpus ($550 to $8,500), and the census-scale fan-out pass if ticket 50 picks it ($10,000 to $140,000).

### Pennsylvania as an extra line

Adding Pennsylvania as a fourth launch state adds 5,919 to 7,081 practices (4,649 dental, 1,270 vet). Pennsylvania publishes active registrations free on data.pa.gov (Public Domain, monthly, with officers and members, no status history, mergers or name changes); fuller bulk data is sold at a price it doesn't publish. It licenses only individual vets and sells the list with city and county only ($71 plus $0.005 a name). Its code-and-bulletin site disallows all bots in robots.txt.

| Item | Low | High | How it was derived | Source |
|---|---|---|---|---|
| Build: Pennsylvania connectors | 2 days | 5 days | data.pa.gov plus the vet list; $50 to $300 API-equivalent, about 0.1 to 0.3 months of the Max plan | [PA-DATA]; [PA-LIST] |
| Seeding: deep research | $174 | $2,344 | 5,919 to 7,081 practices at $0.029 to $0.33 | section 3 |
| Seeding: vet licensee list | $75 | $110 | $71 setup plus $0.005 per licensee; the licensee count wasn't read, so 1,000 to 8,000 names assumed | [PA-LIST] |
| A typical month | $0 | $670 | Refresh $0 to $183, EDGAR $0 to $6, and Places $0 to $480 more if local searches grow by 50,000 | sections 3 and 4 |

## 6. US

Every state is a launch state. Deep research covers 135,665 to 169,581 dental practices and 34,296 vet practices, 169,961 to 203,877 in all, and every state needs its own SoS and vet board connectors. Section 7 has the 14-state sample behind the per-state figures.

### Build

| Item | Low | High | API-equivalent | How it was derived | Source |
|---|---|---|---|---|---|
| Everything in the tri-state build | 59 days | 122 days | $1,475 to $7,320 | Section 5 | section 5 |
| Pennsylvania connectors | 2 days | 5 days | $50 to $300 | Section 5 | section 5 |
| Survey of the 35 states not sampled, and decisions on paid and blocked states | 4 days | 9 days | $100 to $540 | The three state workers for this estimate used 371,000 harness tokens for 9 states, about $10 to $13 at $28 to $35 per million; the decisions take longer than the reading | ticket 33 |
| Connectors for the other 46 states | 69 days | 230 days | $1,725 to $13,800 | 1.5 to 5 days a state for SoS and vet board together. Low: states that share Socrata portals or licensing vendors reuse code. High: paid files in their own formats, search-only states, and sites that block bots (in 6 of the 14 sampled states an official host refused automated requests, often robots.txt itself), which need hand downloads or records requests | section 7 |
| Build total, Claude Code | 134 days | 366 days | $3,350 to $21,960 | | sum |
| On the Max plan | 8.1 months, $810 | 22.2 months, $2,220 | | at 3.8 active days a week | [CHAINS] section 2 |
| Developer hours | 210 h | 780 h | | Grilling and spec review 30 to 80 h; build review 122 to 510 h; registry approvals 5 to 37 h; data purchases, records requests and hand downloads across 15 to 30 states 15 to 50 h; operating the seeding pass 40 to 100 h | |

### One seeding pass

| Item | Low | High | How it was derived | Source |
|---|---|---|---|---|
| Deep research: DeepSeek Search queries | $255 | $612 | 169,961 to 203,877 practices × 2 to 4 queries (340,000 to 815,000) | section 3 |
| Deep research: pages read | $4,079 | $40,368 | 1.36 to 9.17 million pages | section 3 |
| Deep research: EDGAR hits read whole | $510 | $20,388 | 51,000 to 816,000 filings | section 3; ticket 70 |
| National layer | $55 | $1,640 | Same rows as New York | section 4 |
| Retries | $147 | $6,301 | 3 to 10% | |
| DeepSeek and search subtotal | $5,045 | $69,308 | | |
| Registry and vet data in the sampled states | $4,350 | $46,560 | Texas master file $1,350; Georgia whole database $1,000; North Carolina setup $750 (its yearly fee is in the monthly table); New Jersey $925 to $37,000; California master unload $100; Arizona, Michigan and an Ohio snapshot through records requests at $0 to $1,000, $0 to $1,000 and $0 to $500 (labor-rate fees, no quote); vet lists: New York FOIL $0 to $150, North Carolina facility list $52 to $100, Pennsylvania $75 to $110, Georgia roster $100 to $3,000, Texas public-information request $0 to $500 | section 7 |
| Registry and vet data in the other 36 states | $4,500 | $37,800 | Low: 9 paid states at $500. High: 18 paid states at $2,000 plus $100 vet lists. Rates from the sample (4 of 14 states sell their registry, at $1,000 to $2,750 for the first year) | section 7 |
| Registry research (Claude) | 2 days | 20 days | Same as New York | section 4 |
| Seeding total, real spend | $13,900 | $153,700 | | |

Throughput: 9 million pages at 500 parallel reads take about 3 days of DeepSeek time; at 50 they take about 28 days. EDGAR searches on 340,000 to 610,000 practice names take 10 to 17 hours at the SEC's 10 requests a second. DeepSeek Search's own rate limit wasn't read.

### A typical month

| Item | Low | High | How it was derived | Source |
|---|---|---|---|---|
| New releases, changed roster pages | $2 | $662 | Same as New York | section 4 |
| New EDGAR filings for tracked rollups and practice names | $3 | $221 | As in New York, with 169,961 to 203,877 practices | section 4 |
| No-evidence refresh | $0 | $5,267 | Low: re-match only. High: quarterly full fan-out on every US practice | ticket 50 (open) |
| Google Places, on demand | $0 | $8,160 | 100,000 to 1 million local searches a month; high case 300,000 Pro calls: 95,000 at $32 per 1,000 after the free 5,000, then 200,000 at $25.60 | engine 40 (open); [PLACES] |
| Paid registry updates | $750 | $11,870 | Low: re-buying paid files once a year instead of updates (Texas $113, Georgia $83, North Carolina $167, New Jersey $9 and 9 other paid states at $500 a year, all per month). High: Texas daily files at $60 a day ($1,830), Georgia monthly delivery $500, North Carolina $167, New Jersey $370 and 18 other paid states at $500 | [TX-BULK]; [GA-BULK]; [NC-FEES]; [NJ-FEES] |
| Model, API and data subtotal | $755 | $26,180 | | |
| Hosting, added | $65 | $400 | Low: a second Hetzner CPX42 for workers and a database of 50 to 300 GB. High: DigitalOcean managed PostgreSQL 8 GiB ($122) with 300 GB more storage ($65) and two 16 GiB Droplets ($192) | [CHAINS] section 1; engine 43 (open) |
| Object storage, added | $2 | $25 | 0.2 to 3.6 TB of pages and filings on B2 | [CHAINS] section 1 |
| Website: pages on request and map tiles | $5 | $50 | Workers Paid minimum plus requests beyond 10 million at $0.30 per million, and tile bandwidth | [CF-WORKERS] |
| Claude Code upkeep (about 100 state connectors plus the roster selectors) | $0 | $100 | 6 to 20 active days a month, 36 to 120% of the measured pace. The high end passes the pace measured on the developer's plan, so Ultra is the likely step. API-equivalent $150 to $1,200 | section 3 |
| Monthly total | $830 | $26,750 | | |

Contingencies outside the totals: a version re-read of the local corpus ($5,000 to $69,000), and the census-scale fan-out pass if ticket 50 picks it ($10,000 to $140,000; in the US scope the dental practices are already deep-researched and are about a third of the 2A census, so this mostly adds physicians, optometry, urgent care and ABA).

## 7. State data feasibility

The sample is 14 states: the ten most populous (California, Texas, Florida, New York, Pennsylvania, Illinois, Ohio, Georgia, North Carolina, Michigan), the other two researched launch candidates (Colorado, Arizona) and the tri-state pair (New Jersey, Connecticut). They hold 66% of US dental establishments and 58% of vet establishments in CBP 2023. New York, Florida, Colorado, Texas and Arizona come from [SOS5] (2026-10-29); the other nine were read on 2026-11-20 by three research workers for this estimate, whose sources are listed at the top.

| State | Registry bulk data | Price | Officers or managers | Vet premises licensed | Vet list | Price |
|---|---|---|---|---|---|---|
| New York | Free (data.ny.gov SODA; OPEN-NY terms, whose bot clause sits under "Public Participation") | $0 | Corporate chair only; none for LLCs | No | None to download; NYSED bulk verification files on request (unconfirmed) or FOIL | FOIL at actual cost, none under 2 hours of staff time |
| Florida | Free (Sunbiz SFTP daily and quarterly; the site terms say "personal, non-commercial use only", an open conflict) | $0 | Up to 6 | Yes, §474.215 | Free weekly CSV, about 2,489 establishments with street address and DBA | $0 |
| Colorado | Free (data.colorado.gov, Public Domain, daily) | $0 | No (agent only) | No | Free, individuals, city and zip only | $0 |
| Texas | Paid | $1,350 master; $60 a day daily or $20 a week new formations; $1 a search | Yes | Not yet; facility registration with owners and MSOs due by 2027-09-01 (SB 2155) | None to download; public-information request | Unconfirmed |
| Arizona | Search only (reCAPTCHA on documents) | Commercial records requests at "the value of the reproduction on the commercial market", $30 an hour labor, $0.30 a page | Shown online | Yes, §32-2272 | Unconfirmed (board site returned 403) | Unconfirmed |
| New Jersey | Paid bulk status reports | $0.0185 a record; $5 plus $1.25 per single status report | Not in the bulk fields | No | Free DCA standard lists in a Box folder; the folder's robots.txt allows bots only the listing, and the DCA site itself returned a bot block | $0 (custom CD $55) |
| Connecticut | Free (data.ct.gov, daily, Public Domain for master, principals and name history) | $0 | Yes (principals) | No (Chapter 384 licenses individuals only) | Free daily list, individuals, street address of record | $0 |
| Pennsylvania | Partly free (data.pa.gov active registrations, monthly, Public Domain; no status history or mergers); fuller bulk sold at an unpublished price | $0; new-filing list $0.25 a name | Yes, as filed; no registered agents in PA | No | Paid, individuals, city and county only | $71 plus $0.005 a name |
| California | Partly free: weekly files free, full master unload $100, both behind a bizfile account whose terms bar using the data "for advertising or commercial purposes" and any robot | $100 (from a 2022 manual) | Online, yes; in the bulk file unconfirmed | Yes, B&P §4853 (premises registration) | Free monthly DCA file with street address; premises rows likely, unconfirmed; Box download path closed to bots | $0 |
| Illinois | Free daily full files (Business Data Transparency Act, P.A. 102-0049); the SoS site refused automated requests | $0 | LLC managers and members yes; corporate officers unconfirmed | No | Free (data.illinois.gov, ODbL), individuals, city and zip only | $0 |
| Ohio | Partly free: monthly reports of new entities and amendments only, no full snapshot found; the SoS site refused automated requests | $0 | No (Ohio filings carry none) | Partly: only facilities not majority-owned by Ohio vets (ORC 4741.28), about 900 by an older estimate | None found | n/a |
| Georgia | Paid (sold through the Georgia Technology Authority) | $1,000 whole database; $100 setup plus $500 per delivery | CEO, CFO and secretary | No (board rules) | Paid roster, individuals, city and zip only | $3,000 for all rosters; vet alone unconfirmed ($100 in 2022) |
| North Carolina | Paid subscription, weekly CSV; search pages ban scripted searches | $750 setup plus $2,000 a fiscal year | Yes, with previous names | Yes, G.S. 90-187.10 (facility permit) | Sold on request with facility name and address, Excel, about 6 weeks | $0.06 a listing, $52 minimum |
| Michigan | Search only; no bulk product found | FOIA at the lowest-paid capable employee's wage plus up to 50% fringe, 10 cents a sheet, media at cost (MCL 15.234) | Unconfirmed | No (Part 188 has no premises provision) | Account-only MiPLUS report, individuals | Unconfirmed |

Totals in the sample:

- Registry: free in full in 5 states (New York, Florida, Colorado, Connecticut, Illinois), partly free in 3 (Pennsylvania, California, Ohio), paid in 4 (Texas, New Jersey, Georgia, North Carolina) and search-only in 2 (Arizona, Michigan). Two of the free ones carry terms questions for the developer (Florida's site terms, California's account terms barring commercial use and robots), and Illinois's and Ohio's free files sit on hosts that refused this estimate's automated requests.
- Vet premises: licensed in 4 (Florida, Arizona, California, North Carolina), partly in Ohio, and from 2027 in Texas; not licensed in the other 8. A list of premises with street addresses exists for Florida (free), California (free, premises rows unconfirmed) and North Carolina (paid, cheap). Those three states hold 7,275 vet establishments, 21% of the US.

Extrapolation to 50 states, as a stated range rather than a measurement: the sample is the largest states, which are more likely than small states to run open-data portals, so the free share is probably lower elsewhere. Applying the sample's shares with that tilt gives free registry data in full in 12 to 20 states, partly free in 6 to 12, paid in 10 to 18, and search-only or records-request-only in 5 to 12. Vet premises licensing in 10 to 22 states, with a usable premises list in 4 to 12. The low ends set the low cost rows in section 6 and the high ends the high rows. Section 9 names the survey that would replace this.

States where registry or vet data costs money, or only a records request gets it, with published fees:

- Texas: registry $1,350 master, $60 a day or $20 a week for updates, $1 a search [TX-BULK]. Vet list by public-information request, fee unconfirmed.
- Georgia: registry $1,000 once, or $100 setup plus $500 per delivery; vet roster $3,000 for all rosters (vet alone $100 in a 2022 schedule); open-records fees up to 10 cents a page plus staff time at the lowest-paid qualified employee's rate, first quarter hour free [GA-BULK; GA-ROSTER].
- North Carolina: registry $750 setup plus $2,000 a fiscal year; vet facility list $0.06 a listing, $52 minimum [NC-FEES; NC-VMB].
- New Jersey: registry $0.0185 a record in bulk, $5 plus $1.25 per single report; OPRA electronic records free apart from supplies, with a commercial-purpose certification and penalties for not making it [NJ-FEES; NJ-OPRA].
- Pennsylvania: fuller registry bulk data at an unpublished price; new-filing list $0.25 a name; vet list $71 plus $0.005 a name; Right-to-Know copies $0.25 a page, prepayment above $100 [PA-FEES; PA-LIST; PA-RTK].
- California: registry master unload $100 (2022 manual; live price unconfirmed) [CA-MANUAL].
- Arizona: registry only by records request, commercial requests priced at commercial market value, $30 an hour and $0.30 a page, and "may be denied" [SOS5].
- Michigan: registry only by FOIA at labor plus media cost, charged when the estimate reaches $20 [MI-FOIA].
- Ohio: no full registry snapshot found and no records-request schedule found; a snapshot would need a request at an unpublished cost.
- New York: vet list by FOIL at actual cost, none under two hours of staff time [SOS5].

## 8. Assumptions and open tickets

Figures that rest on open local tickets, so the estimate can be re-run when each settles:

- 50 "Local fan-out and refresh cadence" moves the numbers most. It sets documents per practice (assumed 2 to 4 searches, 6 to 40 result pages, 2 to 5 site pages and 0.3 to 4 EDGAR hits), which is most of every seeding pass: $270 to $3,460 of New York's deep-research rows and $4,840 to $61,400 of the US's. It also sets the no-evidence refresh: roster re-match only ($0) or a quarterly full fan-out on launch-state practices ($296 a month in New York, $5,267 in the US at the high end). The contingency of a full fan-out at census scale ($10,000 to $140,000 a pass) exists only if this ticket picks it.
- 49 "Local business identity and resolution": whether NPPES Type 1 sole proprietors join the census (the +25% on dental in the high case), the taxonomy mapping (the physician census is far smaller than CBP's 621111 if only the plan's codes are kept), and the geocoder (the Census Geocoder is assumed, at $0).
- 31 "NPPES census load and census match": the census size and what a match publishes. The match is assumed to be code with no LLM, as the ticket says. It moves 8 to 16 build days and the coverage counts in section 10.
- 33 "SoS and vet license board connectors": what each connector reads, and whether a state's registry is loaded whole or only for matched entities. It moves the per-state build days and the database size behind the hosting rows.
- 47 "Pick the second launch state": the New York scope assumes New York alone. Florida as a second state would add 11,624 to 13,884 practices, about $340 to $4,600 of deep research per pass, plus 2 to 5 connector days (free Sunbiz files, with the terms question still open, and the free vet premises CSV). The ticket also settles whether New York's vet census needs the FOIL request.
- 48 "Research: Rollup rosters for omitted medical specialties": each specialty added grows the registry (more roster entries to research and approve) and the census.
- 51 "Launch-state run budget and the NYC-area counties": the per-batch cap splits a run into batches but doesn't change its total cost.
- 79 "IRS exempt-org file and nonprofit owners": 2 to 5 build days, depending on where EINs come from.
- The parked plan's W1 registry size (300 to 500 domains) and its overlap with the chains registry (20 to 40% assumed).

Open engine tickets that move local numbers:

- 74 "Selector producers": whether roster pages are read by selectors (code) or by DeepSeek. Seeding $12 to $352, monthly $1 to $639, and 5 to 10 build days.
- 119 "Refresh schedule and next-check date": roster pass cadence (4 to 30 a month assumed) and EDGAR refresh cadence.
- 118 "Past coverage through DeepSeek Search": results kept per query, which sets the 6-to-40 range of search pages per practice.
- 42 "Operational identity, budgets and guardrail values": the per-batch cap mechanism, and whether EDGAR full-text noise is filtered before reading (the EDGAR rows assume every hit is read whole, per ticket 70).
- 40 "Search and the demand log": whether and how search uses Places (the Places rows).
- 43 "Hosting, storage and deployment": the hosting rows.
- 19 "Entity resolution algorithm", 39/41/69 (card shapes, API conventions, graph endpoint) and 106 (prompt p10, which sets when a version re-read happens).

Assumptions no ticket has measured:

- Practice counts: CBP 2023 establishments for the low case, plus 25% on dental for the high case.
- Search results kept per query, pages per practice site and EDGAR hits per practice name. A pilot would measure all three (section 9).
- Roster locations nationally (40,000 to 80,000) and the share read by DeepSeek (10 to 100%).
- New registry entries (210 to 550), harness tokens per entry (15,000 to 40,000) and approval minutes per entry (1.5 to 4).
- Local search traffic a month (New York 10,000 to 100,000; tri-state 20,000 to 200,000; US 100,000 to 1 million) and the share that needs a paid Places call (0 to 30%).
- Build days per part and per state connector (1.5 to 5 days for each state beyond the four named), and that a build day costs what a planning day did.
- Map tile hosting ($0 to $20 a month, not priced from a vendor page) and the NY FOIL fee ($0 to $150, the clerk wage not read).

## 9. What would sharpen each estimate

New York:

- A pilot deep-research run on about 100 New York practices (dental and vet, the NYC-area counties first), with no publishing. Record per practice: searches run, results kept after the domain filter and robots.txt, site pages, EDGAR hits on the practice's names and their sizes, and DeepSeek tokens. At $0.03 to $0.33 a practice it costs $3 to $33, and it fixes the rows that set most of the seeding range.
- Filing the NYSED FOIL request and the bulk verification form, which settles whether New York gets a vet census, its fields and its fee.
- Counting New York's Type 1 and Type 2 NPPES records by taxonomy in one monthly file (code, free). That replaces CBP with the real census size once ticket 49 rules on Type 1.
- Ticket 50's refresh choice, then the roster location count from the first 20 rollup registry entries.
- For the build, the same step as [CHAINS] section 8: time one local connector (New York's SoS) end to end and sum its transcript tokens.

Tri-state:

- The same pilot, with New Jersey and Connecticut practices in the sample.
- New Jersey's active-entity count and a quote for a selection by entity type from the Division of Revenue, which turns the $925-to-$37,000 range into one figure, and the developer's ruling on whether the local product needs New Jersey's registry at all (ticket 33).
- Downloading New Jersey's and Connecticut's vet licensee lists by hand once, to see whether practice addresses can be told apart from home addresses.

US:

- A survey of the 35 states not sampled here, in the same format as section 7. The US connector days (69 to 230) and the data purchases rest on 15 states.
- Written quotes or published fee schedules for every paid state, and the developer's ruling on whether paid data is acceptable at all (ticket 33).
- Whether every state is a launch state. Deep research scales with practices, so each state costs about its share of the $5,000 to $69,000.
- Engine 42 on EDGAR noise: filtering generic practice names before reading would cut the high EDGAR row ($20,400 a pass) most.
- Engine 40 on Places: the high Places row ($8,160 a month) exists only if search pays for Places on misses.

## 10. What the money buys

This section counts outcomes under the parked plan's own coverage rules (pre-launch-seeding.md §1 and §2), with CBP 2023 establishments standing in for census entities. It recommends nothing.

The rules: in the 2A verticals, each census entity is either matched to a roster (roster-confirmed, labeled `reported` until a second source) or published as "No PE evidence found (checked {date})". In the 2B verticals there is no census, so each business is roster-confirmed or unknown, and none can read "No PE evidence found", except vets in a launch state that has a vet census. Deep research adds the full fan-out on top, turning roster-confirmed practices into verified chains where a second source exists.

The national layer is the same in every scope:

- 2A census: about 363,000 sites (135,665 dental, 204,617 physician offices, 22,501 optometry), 373,000 with the urgent-care and surgery-center code, plus ABA, which CBP can't count. The physician figure overstates the plan's census, since the plan's taxonomy list leaves many specialties out (section 2). How many of these are roster-confirmed rather than "No PE evidence found" is unknown until the roster crawl runs.
- 2B, roster-only: about 264,000 sites nationally (34,296 vets, 15,183 funeral homes, 19,807 car washes, 111,207 HVAC and plumbing, 83,342 electrical). Everything not on a roster stays unchecked.

| | New York | Tri-state | US |
|---|---|---|---|
| Practices given deep research (dental and vet) | 9,485 | 16,716 | 169,961 |
| 2A sites with a census-backed outcome, nationally | about 363,000 | about 363,000 | about 363,000 |
| of which in the scope's own states | 21,354 | 38,329 | about 363,000 |
| Vets with a census, so able to read "No PE evidence found" | 0 until the FOIL or NYSED list arrives, then up to 1,484 | the same 0 to 1,484 (New Jersey and Connecticut list individuals only) | 7,275 in the 3 sampled states with premises lists (Florida, California, North Carolina), plus New York's if its list arrives; perhaps 4 to 12 states in all |
| 2B sites unchecked unless on a roster | about 264,000 nationally, 15,768 of them in New York | about 264,000, 26,999 of them in the three states | about 257,000 (264,000 less the vets in states with a census) |

A stricter reading changes these counts. The engine's rule is that a business shows "No PE evidence found" only after every source the product requires for it has finished a run (engine "What 'checked' means and coverage states"). How the local coverage states map onto that rule is open (the local map's "Not yet specified"). If the local product made the deep-research sources required for every 2A entity, only deep-researched dental practices would read "No PE evidence found": up to 8,001 in New York, 14,137 in the tri-state and 135,665 in the US. The rest of the national census would read "not yet checked".

## 11. Revised for "Cost cuts before revenue" (2026-11-21)

Engine "Cost cuts before revenue" (ticket 124) changed rules this estimate assumed. This section re-prices the tables above under the new rules, row by row. The build sections don't change.

What changes for the local product:

- EDGAR full-text search: a hit is read whole only when the brand's company or a tracked owner filed it, and every other hit is read as windows around the name. Practices and long-tail rollups are private, so nearly all their hits are third-party filings: priced at $0.003 (short filings, no saving) to $0.0073 (long filings, windowed) instead of $0.010 to $0.025 (`.scratch/engine/research/edgar-third-party-windows.md`).
- Page price: the newsroom test measured $0.00136 per release on DeepSeek off-peak (`.scratch/engine/research/newsroom-filter-test.md`). Practice sites and search results are assumed to cost about the same: the low case uses $0.00136 and the high case keeps $0.003 (was $0.003 to $0.0044). Release rows use $0.00136 at both ends.
- No timers before revenue: recurring rows cost nothing between operator passes; each pass is priced when run. The no-evidence refresh runs only when the developer chooses.
- No automatic version re-reads: the version re-read contingency is $0 unless chosen.
- Hosting before revenue: the engine runs on the developer's machine, so no host is added. The local pages still exceed Cloudflare Pages' file limits, so the Workers line ($5 to $50 a month) stays. Search is built into the site, so no Google Places calls happen before revenue.
- Unchanged: paid state data, the FOIL request, DeepSeek Search query counts, and build time on the Max plan.

### One seeding pass, revised

| Row | New York | Tri-state | US |
|---|---|---|---|
| Deep research: DeepSeek Search queries | $14 to $34 | $25 to $61 | $255 to $612 |
| Deep research: pages read | $103 to $1,550 | $182 to $2,734 | $1,850 to $27,510 |
| Deep research: EDGAR hits, windowed | $8 to $335 | $15 to $591 | $153 to $5,957 |
| National layer: roster pages ($5 to $240), newsroom first crawls ($4 to $120), about and portfolio pages ($1 to $33), rollups' EDGAR windowed ($7 to $197), rollups' DeepSeek Search ($4 to $121) | $21 to $711 | $21 to $711 | $21 to $711 |
| Retries, 3 to 10% | $4 to $263 | $7 to $410 | $68 to $3,479 |
| DeepSeek and search subtotal | $150 to $2,893 | $250 to $4,507 | $2,347 to $38,269 |
| Records requests and paid data | $0 to $150 (NY FOIL) | $925 to $37,150 (NY FOIL plus New Jersey's registry file) | $8,850 to $84,360 (sampled and other states, as in section 6) |
| Seeding total, real spend | $150 to $3,043 (was $335 to $5,760) | $1,175 to $41,657 (was $1,472 to $45,660); without New Jersey's file $250 to $4,657 (was $547 to $8,660) | $11,197 to $122,629 (was $13,900 to $153,700); free data only $2,347 to $38,269, without SoS data in 15 to 30 states |

### Between passes, revised (a typical month with no pass run)

| Row | New York | Tri-state | US |
|---|---|---|---|
| Hosting, added | $0 (developer's machine) | $0 | $0, but see the storage note below |
| Website: local pages on Workers and map tiles | $5 to $25 | $5 to $25 | $5 to $50 |
| Backups of documents and the database (Backblaze B2) | $0 to $2 | $0 to $3 | $2 to $25 |
| Google Places | $0 (search is built into the site) | $0 | $0 |
| Claude Code upkeep | inside the Max plan | inside the Max plan | inside the Max plan; the high end may need Ultra (+$100) |
| Month with no pass | $5 to $27 (was $8 to $2,000) | $5 to $28 (was $17 to $3,560) | $7 to $75 (was $830 to $26,750) |

### Each pass, when run

- A routine pass (new releases, changed roster pages, new EDGAR filings for rollups and practices, staleness sweep, recompute): about $1 to $20 for New York, $1 to $30 for the tri-state, $5 to $250 for the US.
- A full no-evidence refresh of the launch-state practices, only when chosen: $0 for a roster re-match (code), up to about $500 for New York, $880 for the tri-state and $9,000 for the US with every query run again and a quarter of the pages and hits new.
- Paid registry updates, only when bought: New Jersey $9 to $370 an update; in the US, re-buying paid files once a year comes to about $9,000 a year at the low end.
- A prompt or model version: $0 unless a re-read is chosen.

### Trade-offs: the research behind these cuts and what they give up

The same cuts apply to the local product, and the same research backs them. The shared detail first, then what is specific to local businesses.

#### The research behind the cuts

Four measurements, all on 2026-11-20 and 2026-11-21, with $1.37 of DeepSeek in total:

1. Where SEC filings state ownership (`.scratch/engine/research/edgar-quote-distance.md`, code only). In 33 SEC filings from the extraction tests, all filed by the brand's company, its owner or as deal filings, DeepSeek's whole reads found 677 facts. 84% of quotes contain the subject's name and 98% sit within about 2,000 tokens of it. The 12 far facts (2%, in 5 filings) are all a company describing its own controlling owner as "we" or "our Principal Stockholder" (Petco: "We are currently indirectly controlled by certain funds (the "CVC Funds")"; Mister Car Wash: "LGP has more than 50% of the voting power"; Chewy; Unilever on TMICC).
2. Windows on third-party filings (`.scratch/engine/research/edgar-third-party-windows.md`, $1.13). 10 brands, 2,274 full-text hits: 664 from the brand's company or an owner, 566 deal-type, 532 third party, 512 BDC. 44 third-party filings were read by hand and by DeepSeek, whole and as windows. 7 of 44 (16%) state an owner of the brand and 3 (7%) an investor in its company (KKR and Ontario Teachers' for Heartland Dental in a mortgage-pool prospectus, Align's stake in Heartland's holding company, Sentinel as MB2 Dental's former owner); none of 14 landlord or 3 lender filings does. Every statement sits within 391 characters of a brand mention. Windowed reads missed no brand fact a whole read found (0 of 44); whole reads found 13 brand facts and windowed reads 19, a gap about the size of two reads of the same text. Cost per read $0.0200 whole against $0.0057 windowed; long filings $0.030 against $0.0073. 299 of the 566 deal-type hits came from landlords, REITs and mortgage trusts.
3. Older 10-Qs (`.scratch/engine/research/ten-q-deals-missing-from-ten-k.md`, code plus reading). In two test pairs (Chewy, Tractor Supply), a 10-Q's only new ownership facts were the quarter's acquisitions (Modern Animal, VIP Petcare). Across 22 consumer companies, 734 10-Qs and 261 10-Ks from 2015 to 2026, about 420 real deals were named in 10-Qs, and the next 10-K named all but one (about 0.2%): Driven Brands' Clearwater Car Wash, about $24 million, folded into "All Other Car Wash", with no 8-K or press release naming it. No brand bought and sold within a year went missing (Hershey's Tyrrells is in the 10-K). Smucker and Clorox restate deals only in the 10-K's Exhibit 13 or 99.1.
4. Newsroom first-crawl filter (`.scratch/engine/research/newsroom-filter-test.md`, $0.24). 176 releases from Blackstone, TSG Consumer, Serta Simmons Bedding, Pharmavite and Ocean State Job Lot, plus 171 known releases from the research. 37 of the 97 fact-yielding releases state ownership only in the closing About paragraph. The best filters skipped 6% to 25% of releases while losing 3% to 12% of ownership pairs. A release cost $0.00136.

#### What each cut gives up, and how much it matters

**1. Third-party EDGAR filings read as windows** (Q1).

- Evidence: measurements 1 and 2. A company's own filings stay whole reads because that's where the 2% of far facts sit.
- What could be missed:
  - An ownership statement in a third-party filing far from every mention of the name. None was found in 44 filings, but only 9 of them held any brand fact, so the sample bounds the miss rate only loosely: up to about 7% of third-party filings, or about a third of the fact-bearing ones, at 95% confidence.
  - Facts about other companies named in those filings. Whole reads returned 631 such facts against 290 for windows, mostly the filer's own structure (a landlord's subsidiaries). A company the engine tracks has its own searches and its own filings read whole; the loss is incidental facts about companies nobody tracks.
  - Statements that use a name the engine doesn't know (an abbreviation such as "TMICC" or a defined term). Windows only open around names the engine searches for.
- How much it matters: low. Third-party filings rarely state who owns a brand (7% name an investor), and those facts usually also appear on the owner's portfolio page or in a release. Their extra value is as an official source that verifies a fact alone, and windows kept every such statement in the test.

**2. 10-Qs older than the filer's latest 10-K skipped** (Q7).

- Evidence: measurement 3.
- What could be missed: a deal named only in an old 10-Q (about 1 in 420, mostly small purchases folded into a larger line in the 10-K); a quarter-level date where the 10-K gives only the year (10-Ks usually give the date). 10-Qs filed since the latest 10-K are still read, so recent deals are kept.
- How much it matters: very low for brand ownership. The one miss in the sample was a roll-up's purchase of a few sites, not a brand changing hands.

**3. No automatic re-read when the prompt or model changes** (Q4).

- Evidence: the cost alone. A full re-read costs about as much as the seeding pass's DeepSeek reads.
- What could be missed: improvements a new prompt version brings (a fixed false claim, a newly caught fact) reach only new documents until the developer chooses a re-read. Facts from two approved versions sit side by side. A document that produced no facts under the old version is never looked at again unless a broad re-read runs.
- How much it matters: low to moderate. Every version passes the same approval check before it ships (known facts, exact quotes, blind precision, no rule breaks; "Extraction prompt rules"), so older facts met the bar of their day. A known kind of error can be fixed with a targeted re-read of the documents that produced it. Seeding waits for p10 so the first pass uses the newest approved prompt.

**4. No timers before revenue: one operator pass** (Q5, Q9).

- Evidence: none needed; it's a choice about when money is spent.
- What could be missed: freshness. Between passes nothing updates:
  - a sale or exit isn't reflected, so a card can show a former owner as current until the next pass, and a new PE purchase doesn't appear;
  - the deal feed shows nothing new;
  - pending deals don't close in the data;
  - failed reads wait for the next pass, so a brand can stay "not yet checked" longer;
  - the drift check and the golden check (a silent model change) run only at pass time.
- How much it matters: moderate, and it grows with the gap between passes. Cards show "checked {date}", so readers can see the age; after 18 months without confirmation a hop shows "No source has shown this since…". The cheap "new deals" pass (wire feeds, new releases, new deal-type EDGAR filings, roughly $2 to $25) is the mitigation; run regularly, it keeps sales and purchases current.

**5. The engine on the developer's machine, static search, a free report function** (Q6).

- Evidence: none needed; it's a choice about hosting.
- What could be missed:
  - search quality: matching on names, owners and industry words only, with no meaning-based ranking;
  - the demand log (searches that found nothing), unless the small Cloudflare function records them;
  - updates when the machine is off or fails. The website itself stays up, since it's static on Cloudflare.
- How much it matters: low for v1, since people look brands up by name. The operational risk of one machine is real; backups (Backblaze B2 with Object Lock) cover the data. Fetching from a home connection is not a loss: research found 90 of 93 PE firm sites readable from a home IP ("Rosters, portfolio pages and the registry").

**6. SEC headers from the first request** (Q8). No data trade-off. If the SEC still refuses, the engine stops SEC requests instead of retrying, and EDGAR facts wait until it's resolved.

**Considered and rejected: a newsroom first-crawl filter** (Q3). Measurement 4 showed every filter that skipped a meaningful share of releases lost 3% to 12% of ownership pairs, mostly facts in About paragraphs, people and charity releases, and deals worded "sell", "purchased" or "invests". At $0.00136 a release, the best filter would have saved about $15 to $50. Every release is still read.

#### What is specific to the local product

- EDGAR on practice names: practices and long-tail rollups are private, so nearly all their hits are third-party filings (landlords' tenant lists and lenders' schedules for generic names such as "Family Dental"). Measurement 2 found no landlord or lender filing that states an owner, so windows lose little here; the risk is the same as cut 1.
- The page price: practice websites and local news pages weren't measured. The low ends assume they cost what a press release did ($0.00136); if they cost $0.003, the low ends of the page rows roughly double.
- Freshness matters more locally. Dental and vet rollups buy practices continuously, so a "No PE evidence found (checked {date})" result ages faster than a national brand's verdict. The main signal of a new acquisition is the practice appearing on a DSO's location roster; a routine pass re-reads changed roster pages for about $1 to $20 in New York, so regular passes keep most local verdicts current without a full no-evidence refresh.
- The no-evidence refresh runs only when chosen. Between refreshes, an independent practice bought by a DSO that doesn't list it on its roster stays "No PE evidence found" until a refresh or another source catches it.
- No Google Places before revenue: local search runs on the built-in index over census names and addresses (geocoded free through the Census Geocoder). Places enrichment (opening status, current name) waits for a server, so a closed practice can linger until NPPES deactivates it.
- Skipping paid state data (New Jersey's registry; 15 to 30 states in the US scope) loses business-registry records in those states. That weakens a second source and officer links where registries list officers, but PE detection itself rests on rosters, NPPES, releases and search, which stay.
- The US scope may outgrow one machine (up to 3.6 TB of documents and millions of polite fetches); New York and the tri-state fit on a normal desktop.
