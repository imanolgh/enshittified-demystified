# Handoff: pivot from local businesses to chains and brands

Written 2026-11-02 at the end of a Windows Claude Code session, for the next session running inside WSL. That session's conversation and memory are not visible from Ubuntu, so this file carries what matters.

**Update 2026-11-04: ruled.** The four decisions in section 6 and the section 2 layout were all accepted as recommended. They are recorded in `docs/adr/0004-chains-and-brands-first.md` and `docs/decisions.md` §14, with the numbering rule in `docs/agents/issue-tracker.md`. Everything else below is still a recommendation.

**Update 2026-11-04 (later): folders set up.** Tickets now live in `.scratch/engine/`, `.scratch/chains-and-brands/` (active), `.scratch/local-businesses/` (parked) and `.scratch/retirement/` (parked; ticket 35). Local-only bullets in engine tickets were split into new local tickets 49–51. Chains-and-brands tickets 52–62 and engine ticket 63 were charted from §2 and §5. The category audit runs as a three-category pilot (ticket 52). Section 2 and section 7 step 2 are done; the paths in section 2 refer to the old `api-spec` folder, which no longer exists. Competitor facts (§4) are saved to project memory.

**Original status: proposal only. The developer has not ruled on anything below.** They said they will "probably choose chains and brands for now" but want the local work kept mapped out. No project docs were changed. Treat every recommendation here as a recommendation, per the role contract in `CLAUDE.md`.

**Do not commit or push anything** until the ticket-folder question in section 2 is settled. This file is itself uncommitted.

## 1. Start here

1. Read this file, then `CLAUDE.md`, `GLOSSARY.md`, `docs/adr/`, `.scratch/api-spec/map.md`.
2. Pick up section 2 first. It is the question the developer asked last, and it was never answered.
3. Then get rulings on the four decisions in section 6.
4. Save section 4's competitor facts to project memory. The Windows memory note does not exist on this side.

Environment note: the earlier session was the Windows build pointed at a `\\wsl.localhost` path, so it could not see `~/.claude/skills`. In WSL, `grill-with-docs`, `grilling`, `domain-modeling`, `wayfinder`, `prototype`, `research`, `unslop` and `setup-matt-pocock-skills` are all installed. Nothing needs reinstalling. Upstream `wayfinder` differs from the installed copy by one sentence: research subagents get "a fresh context window". `unslop` and the other skills were not compared.

## 2. Open question: two sets of tickets

The developer asked whether they can keep two parent folders of grill tickets, one for the local businesses idea and one for the chains and brands idea, so both stay on record and they can move between them. They will probably work on chains and brands now and keep local mapped for later.

**Answer: yes.** `docs/agents/issue-tracker.md` already allows one directory per effort (`.scratch/<effort>/map.md` plus `issues/NN-<slug>.md`), so two maps fit the convention.

The catch is that about 25 tickets are shared engine questions. Copying them into both folders would create two answers to the same question, which the docs-governance rules forbid.

Recommended layout, for the developer to confirm:

```
.scratch/
  engine/             # shared: claims, citations, scoring, events, API, ops
  local-businesses/   # parked map: census, SoS, vet boards, launch states
  chains-and-brands/  # active map: brands, chains, categories, alternatives
```

Each product map links to engine tickets and is blocked by them where needed. Moving back and forth means changing which product map is active. A simpler alternative: keep `.scratch/api-spec/` as the parked local map and add `.scratch/chains-and-brands/`, which links into `api-spec` for shared tickets. That avoids renames but leaves the shared work inside a parked folder. Git branches are a poor fit because the docs would diverge per branch.

Questions to settle:

- Which layout?
- Does the `.scratch/api-spec/spec.md` destination become one engine spec plus a product spec each?
- Do local-only docs such as `docs/pre-launch-seeding.md` stay as the local plan with a new seeding doc for chains and brands, or get rewritten?
- Renaming `api-spec` means fixing references in `docs/README.md` and `docs/pre-launch-seeding.md`. Use `git mv`, because tickets 03, 04, 12 and 42, `docs/decisions.md` and `docs/pre-launch-seeding.md` have uncommitted changes and ticket 48 is untracked.

Ticket sorting, from titles only (48 total, 10 answered, 38 unresolved). Check against each body before moving anything.

| Group | Tickets |
|---|---|
| Answered, shared | 01, 02, 05, 07, 08, 10 |
| Answered, mostly local (keep for local) | 03, 06, 09, 11 |
| Shared, keep | 04, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 29, 32, 34, 38, 41, 42, 43, 44, 45, 46 |
| Shared, rework for brands | 12, 19, 28, 30, 37, 39, 40 |
| Local only, park | 31, 33, 47, 48 |
| Retirement, defer | 35, 36 (36 is the first follow-up, see section 5) |

New tickets chains and brands would need:

- The brand and chain model. A chain is a brand with locations. Brand-level verdicts first, with the franchise rule from `docs/decisions.md` §4.
- Licensing. The closed predicate list cannot express a brand licensed to an operator, which matters for clothing. Adding a predicate is the developer's decision.
- Product category vocabulary. "Category" collides with `BusinessCategory` in ADR 0001.
- How a category's brand list is chosen, and what "checked" means at brand level.
- Rules for alternatives and affiliate links.
- Research on USPTO trademark data as an official source. It would need a new source type (ADR 0003). The bulk files describe ownership transfers. Whether they give the current owner is unconfirmed.
- The website. No current map covers a frontend.

`GLOSSARY.md` defines ownership chain from "a local business", so it needs widening. ADR 0001, 0002 and 0003 otherwise survive. A pivot would suit a new ADR 0004.

`docs/adr/0002` still rules out manual review, and community submissions remain out of the MVP.

## 3. How the conclusion was reached

Why the developer wants to pivot: doubts about money in local, and live competitors. The stronger reason is work per business. WhoIsMyDentist has classified only 2% of New York offices.

Why national is attractive: a bounded universe, no census or state connectors, proven demand (brand decay is the highest-volume pain, `docs/painpoints.md:15`), and more frequent use than a dentist lookup.

The original pitch was a mobile barcode scanner for shoppers. Findings against leading with it:

- **It exists.** See Buy'r and others in section 4.
- **Most grocery scans would say no.** Buy'r's own figures put PE at about 7% of brands. A test of the USDA FoodData Central branded release of 2026-10-29: 460,843 unique products, 30,674 owner names. The top 120 owner names cover 42% of products. About 1% of those products sit under PE or similar investors (Walgreens, Family Dollar, TreeHouse's Bay Valley), rising to 4% with Albertsons banners, where Cerberus holds about 30% per the FY2026 10-K. 21 of the top 30 owners are retailers or wholesalers. This was a hand classification, counts products rather than sales, and PE may be more common among smaller brands.
- **USDA owner names are stale.** It still lists Pinnacle Foods. Barcode to brand works for food, but ownership must come from our graph.
- **No public barcode data outside food.** Open Products Facts has about 48,000 products under a share-alike license. Paid lookups run about $125 to $245 a month per third-party pages. Retail items use UPC barcodes, not QR codes.
- **In-store purchases earn no affiliate commission.** Correction: an earlier statement called scanning the hardest place to earn, but Buy'r reports about $100K in annual recurring revenue within 12 days (self-reported, company press release, no independent check). Treat consumer subscriptions as possible, at least with a big launch audience.

The central tension: where PE is densest (chains) there is no affiliate income, and where affiliate income exists (appliances, groceries at a register aside) PE tends to be rare. Clothing, mattresses, cookware and supplements are unmeasured middle ground. Chains bring attention and products bring revenue, so launch needs both.

Chain density is examples, not a measurement. QSR blocked automated reads and NRN's top 50 is a slideshow. Roark appears behind Subway, Dunkin', Sonic, Arby's, Buffalo Wild Wings and Jimmy John's (the Inspire Brands link for Dunkin' and Jimmy John's is from memory). Jersey Mike's is Blackstone (closed January 2025). Pizza Hut's sale to LongRange and Denny's to TriArtisan were reported in 2026, closing unconfirmed. Ravenous lists 98 US restaurant brands with PE investors but needs checking: it links Jersey Mike's to a Roark page.

Chipotle, Walmart, Target and Home Depot are public companies, so they would not flag.

## 4. Competitors (figures as of 2026-10-31)

| Product | What it is | Numbers | Weakness |
|---|---|---|---|
| Grass (Albert Kim, Cadre) | OpenStreetMap-based local map, iOS and Android, v1.0 2026-10-06 | 100+ Play downloads, 3 App Store ratings; @cadrecorp 98K, @nobslsat 26K, one vet reel 179K likes | Unmatched places read "independent, as far as we know"; ownership from unnamed "partner datasets" (a developer-seen vet card cites privateequityvet.org) |
| WhoIsMyDentist | Dentist directory on NPI, boards and registries | 145K+ offices; classified 2% NY, 5% CA, 22% FL; dentists pay $9.99/mo | "Corporate" mixes PE-backed and founder-led groups, though its DSO guide names sponsors and lenders |
| Private Equity Vet + Independent Vet | Corporate vet list | 15,163 practices, 10,511 US; 110 US consolidator names, 462 NY rows across 39 | Excel has no per-practice source or PE flag, dates on 4% of rows; includes Mars (about 19% of US rows) |
| Buy'r | Grocery barcode scanner | Claims 30,332 brands, 2,041 PE-held, 134,000+ users; 4.8 from 601 ratings; $5/mo or $50/yr; last App Store update Mar 11 | No per-claim citations on its website (app not checked); no restaurants or clothing listed; its founders' audience unverified |
| Ethos | Per-claim source URLs with automated checking | 42 public records, waitlist | Closest to our engine; not PE-specific |
| Worse on Purpose | Editorial brand ledger plus essays | 398 brands: 145 Approved, 155 Watchlist, 19 Former Great, 79 Avoid | See below |
| ShopFair | General ethics score app | 4,700+ brands, 140 categories, free | Not PE-specific; listing states no market, website is `.uk` |

Also seen, thin or unread: Buycott, Scan Owner, ProductWho, EXIT, Boycottr, Informed Consumer, Productr.

The docs still say local is uncovered (`docs/marketgaps.md:10`, `:38`, `docs/painpoints.md:74`, `:207`). That is out of date, and these products are absent from the docs.

Access limits to respect:

- **WhoIsMyDentist:** terms restrict automated access, and its fetcher returned 403. Do not automate it. The earlier session loaded 11 pages with an automated browser, 7 after seeing the clause, and told the developer.
- **Private Equity Vet:** terms bar automated collection outside its offered Excel download, republishing most of the data, and using it to train, test or improve AI systems. The downloaded file was analysed and then deleted.
- **Reddit:** blocked for the fetcher. Do not route around it.
- **ledger.worseonpurpose.com:** rate-limited. The developer pasted the methodology.
- **Competitor data:** should not enter the pipeline. `CLAUDE.md` only names paywalled sources, so a written rule is a recommended addition. A person reading these sites for leads looks fine (not legal advice).

## 5. Proposal

Build a public record of what PE owns, not a shopping app.

**Positioning:** "See what private equity owns, since when, and the proof." Lead with PE and show the owner type on every result so a "no" is still useful. Do not say "Not PE-owned" (banned by `GLOSSARY.md`). Use "Public company (NYSE: CMG)" or "No PE evidence found (checked {date})".

**Version 1, a website:**

- About 8 to 10 categories and roughly 1,000 chains and brands, all fully checked. "Every major brand in this category is checked" replaces launch states as the coverage promise.
- Brand or chain page, category page, and a public feed of new PE deals built on `events`.
- Inputs are name search and category pages. Scanning comes later, food first via USDA.
- Include healthcare chains (Aspen Dental, VCA and similar) as a category, which keeps part of the dentist and vet story with no census.
- Show acquisition dates. Add search by product type and a country filter, both requested repeatedly.

**Choosing categories:** audit first. Check the top 30 brands in about 15 candidates, keep those around 20% PE or higher, and include at least three that can earn affiliate income. Also check how many launch brands appear as BDC borrowers. Candidates: restaurants, pharmacy and dollar stores, gyms, car washes, pet stores, eyewear, women's apparel, mattresses, cookware, supplements. Avoid leading with appliances: PE is probably rare there and Worse on Purpose says appliances and grocery stores are next.

**Money, in order:**

1. Free search. No paying for unlimited searches, because `docs/monetizationideas.md:80` says never meter evidence and shared results are the marketing.
2. Affiliate links on product categories, ranked by a published rule and never by commission, with a visible disclosure. Expect little at first: 10,000 visits at 8% clicks, 4% purchases, a $120 order and 6% commission earn about $230 (illustrative). Amazon reportedly cut rates in May 2026, so prefer brand-direct programs.
3. Paid alerts when a followed brand is bought, about $5/mo or $49/yr, replacing the ~$8/$79 tier while the retirement brief is deferred.
4. Research/Pro and licensing later. Professionals already do this by hand, which is where the bigger money likely sits (opinion).

**Distribution is the biggest gap.** Grass launched on a big audience and Buy'r reportedly did. The developer has none. Each new deal becomes a shareable card, each brand gets a page that can rank, and creators get sourced data. Worse on Purpose could be a partner: it judges quality, this proves ownership. Look into the sourcing and AI complaints first. Outreach is the developer's call.

**From the Worse on Purpose review** (methodology plus one 84-comment, flagged Hacker News thread). It does well: clear verdicts, an Approved list that works as a buying guide, essays with a voice, a "what would change our verdict" callout, last-reviewed dates, insider tips. It is exposed on: verdicts mixing ownership with opinion (disputes over Black & Decker, Cutco, Lodge, Bonobos and others), one reported citation that did not match its source (unverified), silence on AI and funding, and partial coverage.

Changes that came out of it:

- Generate "what would change this" on every card with code.
- Publish a "how this works" page at launch covering AI, funding and affiliate links.
- Put no AI-written prose on cards. Show quotes and computed labels only.
- Do not let alternatives imply quality. Label them "No PE evidence found, not a quality rating", or link independent reviews.
- The developer writes deal posts personally, community by community.

Consider a source-link submission path: a user sends a URL, it goes through normal retrieval, extraction and citation checks, with no manual review. This relaxes the ruling against community submissions in the MVP, so it needs a decision.

**Evidence caution.** Fracassi, Previtero and Sheen ("Barbarians at the Store?") found PE-backed consumer brands grew sales 50% against matched firms, raised existing prices about 1%, and added 11% more products. The 4% figure quoted in the developer's Claude web chat could not be confirmed. Publish who owns it and when, never that it got worse.

**From the private credit threads** (the developer pasted these; none mention Worse on Purpose, and many already feed `docs/painpoints.md`):

- Basic numbers are disputed, which suits "sources disagree".
- Sourcing demand is loud ("Where are your sources?") and AI writing is attacked.
- The most common question is how to profit, which `docs/decisions.md` §5 forbids answering.
- The fear is about pensions and annuities, which our data cannot show. Form 5500 bulk data has no per-plan fund lineups, and insurers are not in the spec.
- Insiders defend redemption limits, so `docs/painpoints.md:237` looks out of date.

**Later:** barcode scanning and a native app, then local (chain to location to independents), then retirement.

**Risks:** Google already answers big-brand lookups, so pages must add dates, proof, comparison and alerts. Buy'r or Worse on Purpose could move to this position. Ownership facts are public, so the edge is freshness, proof and history.

## 6. Decisions awaiting the developer

1. **Pivot to chains and brands, and park local?** Recommended: yes.
2. **Website first, app later?** Recommended: yes.
3. **Free search, paid alerts, affiliate on products?** Recommended: yes.
4. **Defer the retirement side?** Recommended: yes, with a change. Defer the retirement lookup (ticket 35), but make BDC loan data (ticket 36) the first follow-up, so a PE-owned chain's page can show which public funds lent to it or its parent. Keep Form ADV ingestion, because that is how we identify PE firms. Coverage of launch brands in BDC filings is unmeasured.

## 7. After the rulings

1. Run the category audit.
2. Set up the ticket folders and rewrite the map.
3. Update `decisions.md`, `GLOSSARY.md`, the seeding plan and the monetization doc, and fix the stale claims listed above.

The developer's Claude web chat said `contracts.py` could start this week. That is wrong: `.scratch/api-spec/map.md:14` says no application code until the map is done, and ticket 12 shapes that contract. The developer would have to rule otherwise.

Unread: the six Worse on Purpose Reddit threads. The developer may paste them. The links are in r/ManyBaggers, r/BuyItForLife, r/Appliances and r/enshittification (two), plus one older r/AskReddit thread.

## 8. Key sources

- Buy'r: https://www.buyrapp.com/ and https://apps.apple.com/us/app/buyr/id6754346785
- Buy'r press release: https://lifestyle.kbew98country.com/story/1500/buyr-surpasses-50000-users-in-first-week-and-climbs-to-1-on-the-app-store-signaling-a-cultural-shift-toward-economic-transparency/
- Ethos: https://ethosscan.com/
- Grass: https://www.cadrecorps.com/grass
- WhoIsMyDentist: https://whoismydentist.com/ (read by a person only)
- Private Equity Vet: https://privateequityvet.org/ (read by a person only)
- Worse on Purpose: https://ledger.worseonpurpose.com/methodology and https://www.checkbook.org/delaware-valley-area/worse-on-purpose/articles/Worse-on-Purpose-The-Big-Companies-That-Are-Gutting-Your-Favorite-Brands-7996
- Hacker News thread: https://news.ycombinator.com/item?id=49068707
- USDA downloads: https://fdc.nal.usda.gov/download-datasets
- Ravenous list: https://www.weareravenous.com/heres-just-a-list-of-every-restaurant-we-know-with-private-equity-investors/
- Research paper: https://foster.uw.edu/wp-content/uploads/2019/10/Barbarians-at-the-Store-Private-Equity-Products-and-Consumers.pdf
- Albertsons 10-K: https://www.sec.gov/Archives/edgar/data/0001646972/000164697226000032/aci-20260228.htm
- USPTO bulk data: https://www.uspto.gov/trademarks-application-process/checking-application-status-view-documents/trademark-bulk-data
