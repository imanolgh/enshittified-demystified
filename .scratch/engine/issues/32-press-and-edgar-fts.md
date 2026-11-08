# Press and EDGAR full-text connectors

Type: grilling
Status: resolved
Blocked by: 08, 10, 24  (Research: EDGAR access, BDC identification and SoI formats; Research: Press-release and news feed sources; Source independence and syndication)
Map: [engine](../map.md)
EDGAR full-text search and the 13D/13G connector moved to [EDGAR full-text search and ownership filings](70-edgar-fts-and-ownership-filings.md) on 2026-11-08; this ticket now covers press releases and news.

## Question

How do the press-release/news connector and the EDGAR full-text search connector find, fetch, classify and store documents?

## Context

- Feed list and Google News query format; resolving Google News redirect URLs (from "Research: Press-release and news feed sources").
- **Classifying a domain** as `press_release` vs `news` (wire-domain list) — ties to "Source independence and syndication".
- **Matching general feed items** against hundreds of thousands of entity names for "instant refresh on mention" (research_flows.md:114).
- Poll cadence: 6-hourly per tracked entity (research_flows.md:110) — rate limits.
- EDGAR FTS: endpoint/params/form types/pagination; which files of a hit to store; EX-99 stored as `press_release` (ADR 0003:10); SEC user agent + ~10 req/s (from "Research: EDGAR access…").
- GDELT is in the Beat table (research_flows.md:110) but deferred — drop.
- Query construction and caps: which aliases, quoting, location terms, max hits per connector, max documents per entity.
- **From "Owner kind: storage, evidence and the PE-firm test"** (2026-11-07; ADR 0001 amended; table in evidence_layer_plan.md §4 `owner_kind_evidence`): rank 2 owner-kind evidence includes a press release the owner issued, so the press connector must record a release's issuer in a form code can match to an entity.
- **From "Category precedence and public companies"** (2026-11-07; ADR 0001 amended): above a public company, a PE firm's minority stake counts only from a 13D, or a 13G not filed under Rule 13d-1(b); proxy tables only confirm a holder. So 13Ds and 13Gs need a connector that copies the rule box into document meta. Checked 2026-11-07: T. Rowe Price Associates' SCHEDULE 13G of 2026-11-06 (accession 0000080255-26-000673, Pacific Biosciences, 10.8%) has the structured field `designateRulePursuantThisScheduleFiled` = `Rule 13d-1(b)` and `typeOfReportingPerson` = `IA` in its `primary_doc.xml`. A 13D or 13G amendment reporting 5% or less ends the holder's hop. Which producer reads these filings, how they are found, and how older filings without the structured format are read, is this ticket's.
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07; notes in evidence_layer_plan.md §4 `documents` and `fetches`): connectors fill `published_on` from structured fields only: a feed item's publication date, an SEC filing date, or a page's `datePublished` / `article:published_time`.
- **To confirm** (stated from memory in "Category precedence and public companies", 2026-11-07, not checked): PE sponsors that held shares before an IPO usually file their 13G under Rule 13d-1(d), and activists file a 13D; which box 3G (Restaurant Brands), Trian (Wendy's), Leonard Green and TPG (Life Time) actually used was not checked. Only Rule 13d-1(b) was verified, on T. Rowe Price's filing. Check these four filings when building the 13D and 13G connector, since their category depends on it.
- **From "Brand card, receipt and edge shapes"** (2026-11-07; formerly "Claim card and graph output shapes"; glossary "Brand card" and "Receipt"): receipts never re-serve archived copies of press releases or news; they show the quote, source, live link and dates. Whether storing wire copies at all fits the wire services' terms (flagged by "Research: Press-release and news feed sources") is still an open legal call for the developer.
- **From "Source independence and syndication"** (2026-11-08; ADR 0002 amended; notes in evidence_layer_plan.md §4 `documents`): a press release's speaker is its issuer wherever the copy sits, so the press connector must read the issuer (the wire's "SOURCE" line or the release's own byline) and set `speaker_entity_id`; a wire tag in the text ("/PRNewswire/", "/GLOBE NEWSWIRE/", "(BUSINESS WIRE)") marks a reposted release as a copy. A news article's speaker is its outlet (null speaker, domain). This ticket is now takeable.

## Comments

### Round 1 (2026-11-08)

Facts read ("Research: Press-release and news feed sources"): PR Newswire's terms bar robots, data mining and "database storage and retrieval"; Business Wire's per snippets; GlobeNewswire's and Business Wire's `www` hosts returned 403 to honest bots; Business Wire's feed host disallows `/rss/` for `*`; Google News RSS is blocked by robots.txt (for `*`, and naming Anthropic's crawlers), Google's terms and a personal-use notice; wire feeds hold 20 items; `dc:contributor` names the issuer; wire tags survive republication.

- **Split** (Q0): EDGAR full-text search and the 13D and 13G connector moved to new ticket "EDGAR full-text search and ownership filings"; "Retrieval fan-out, tracked entities and refresh cadence" waits on both.
- **Wire services** (Q1, option b): wire feeds are used for discovery only (title, date, issuer); the release is stored from the issuer's own site (found by its domain identifiers, newsroom or sitemap, matching title and date), an SEC exhibit or an adviser's page, never from a wire site. A release that exists only on the wire can't be a source. The connector build measures how often issuers post their own releases. The developer asked whether a release "cites its source": it is the source, the issuer's own words; if the issuer never posts it, the fact must come from another party, a portfolio page, an adviser, a filing or a news article.
- **Matching and polling** (Q2): feed item title, summary and issuer matched against tracked entities' names and aliases (whole words, exact phrases, case-insensitive); unmatched items dropped unstored. Subject feeds (M&A, private placement, venture capital, restructuring, dentistry, health care, restaurants, animals and pets, fitness, and GlobeNewswire's equivalents) polled faster than each turns over 20 items, with a daily backfill from the wires' news sitemaps; intervals: "Retrieval fan-out, tracked entities and refresh cadence".
- **Classification and speaker** (Q3): a page on a wire domain (`prnewswire.com`, `prweb.com`, `newswire.ca`, `globenewswire.com`, `businesswire.com`, `accessnewswire.com`, `accesswire.com`, `einpresswire.com`) is a `press_release`; elsewhere, a page on the issuer's own domain or carrying a wire tag is a `press_release`, otherwise `news`. The issuer (feed `dc:contributor`, else the release's "SOURCE" line) sets `speaker_entity_id` and owner-kind rank 2; a news article's speaker is its outlet.
- **Older releases** (Q4): Google News and GDELT dropped; new research ticket "Research: Web search APIs for finding a brand's past coverage" run in the background; the historical route goes to "Retrieval fan-out, tracked entities and refresh cadence" once it reports.
- **The bot** (Q5, option a, after the developer asked about the legal position): the project's own bot name; robots.txt followed path by path for our name and `*`; rules naming only AI crawlers don't stop us. Never get around a block: Playwright sends our bot's name too, no proxies or CAPTCHA services, a challenge page counts as `blocked`; stop fetching from a site as soon as it asks. The developer first proposed getting around 403s and challenge pages until warned; Claude advised against it (circumventing a technical block is the clearest "without authorization" pattern, undercuts fair use, and buys little because option b never needs wire release pages) and declined to build it; the developer agreed. Legal notes given (not legal advice, from memory): copyright (facts uncopyrightable, *Feist*; internal full copies with small display accepted in Google Books and Turnitin; *Thomson Reuters v. Ross* went the other way), terms of use (hiQ lost on contract), computer-access laws (*Van Buren*, hiQ; *Craigslist v. 3Taps* lost after routing around a block), robots.txt not a law but evidence of good or bad faith.
- **Legal review** (Q6): new task ticket "Legal review before launch", blocking launch: stored copies of news and wire articles, the wires' terms, a takedown process (conflicts with "documents are never deleted"), defamation exposure, and whether the product should sit in a company.
- **Stored copies** (Q7, option a, developer's ruling): full copies stay as designed ("Document storage, fetch log and last-confirmed") and are never shown publicly; the developer understood copies were not stored and was corrected; the legal review confirms the position. Turned down: keeping only quoted paragraphs for news.

## Answer

Resolved 2026-11-08 in a grilling session (one round with follow-ups, recorded under Comments). Split before deciding: EDGAR full-text search and ownership filings went to their own ticket.

- **Wires, discovery only:** PR Newswire and GlobeNewswire subject feeds are polled to learn that a release exists (title, date, issuer); the release is stored from the issuer's own site, an SEC exhibit or an adviser's page, never from a wire site. A wire-only release can't be a source; the build measures how often issuers post their own releases.
- **Matching:** feed items match tracked entities by exact names and aliases; unmatched items are dropped. Feeds are polled faster than they turn over, with a daily news-sitemap backfill (intervals: "Retrieval fan-out, tracked entities and refresh cadence").
- **Classification:** wire domains, issuer domains and wire tags mark a `press_release`; otherwise `news`. The issuer sets `speaker_entity_id` and owner-kind rank 2; a news article's speaker is its outlet. A stored issuer copy with no date of its own takes the feed item's date as `published_on`.
- **The bot:** the project's own name; robots.txt followed path by path for that name and `*` (rules naming only AI crawlers don't stop it); never gets around a block (Playwright identifies itself, no proxies or CAPTCHA services, a challenge page is `blocked`); stops when a site asks. Getting around blocks was proposed and turned down.
- **Stored copies:** full private copies stay as designed (developer's ruling), never shown publicly.
- **Older coverage:** Google News and GDELT dropped; "Research: Web search APIs for finding a brand's past coverage" is running; the historical route is decided in "Retrieval fan-out, tracked entities and refresh cadence".
- **Legal:** new task "Legal review before launch" (chains map) gates launch.
- Docs: CLAUDE.md scrape etiquette; evidence_layer_plan.md sources table and a press-connector note; research_flows.md notes. No ADR.

Handed on:
- "EDGAR full-text search and ownership filings": EDGAR full-text search, EX-99, 13D/13G.
- "Retrieval fan-out, tracked entities and refresh cadence": feed intervals, the historical route.
- "Operational identity, budgets and guardrail values": the bot's name, no proxies, document caps.
- "Rosters, portfolio pages and the registry": newsroom URLs for issuers.
- "Entity resolution algorithm": issuer names; finding an issuer's site.
- "Competitor and third-party data rule": the legal review.
- chains "Category brand lists and brand-level checked": press as a required source.
- "Testing and acceptance bars": the legal gate; the issuer-post measurement.
