# Research: Web search APIs for finding a brand's past coverage

Type: research
Status: resolved
Map: [engine](../map.md)

## Question

Which web search APIs could the engine use to find pages about a brand's past ownership changes (press releases on issuers' sites, news articles, adviser pages), and what do their terms, prices, coverage and query features allow?

## Context

- Raised 2026-11-08 in "Press and EDGAR full-text connectors": Google News RSS is blocked (robots.txt for `*` and naming Anthropic's crawlers, Google's terms, a personal-use notice), GDELT is deferred, and wire feeds hold only their latest 20 items, so nothing finds a release from 2021 (Dental365's acquisition through The Resolute Fund V). The audit workers found such pages with web search.
- Results would be pointers only: the engine then fetches each page from its own site under the bot rules (own bot name, robots.txt path by path, never getting around a block) and stores it as a document. Search results themselves are never evidence.
- Recalled from memory, to confirm or correct: Microsoft retired the Bing Search APIs in 2025; Google's Programmable Search (Custom Search JSON API) and Brave's Search API exist with terms not checked.
- The decision (which route, if any) goes to "Retrieval fan-out, tracked entities and refresh cadence".

## Find out

For each candidate API (at least: Google Programmable Search / Custom Search JSON API, Brave Search API, the Bing APIs' status and any successor, and any other API that returns web results from its own index, such as Mojeek or Exa; note but don't recommend services that scrape another engine's results, such as SerpAPI, and say why):
- **Availability:** current status, any announced retirement or limits on new customers or on whole-web search.
- **Terms:** whether results may be stored, for how long, and whether automated, commercial or AI use is allowed; whether results may be used to decide which pages to fetch.
- **Price:** cost per 1,000 queries, free tiers, daily caps.
- **Query features:** exact-phrase quoting, site filters, date range filters, result count per query, and whether the index covers old pages (2015–2024).
- **Rough cost for launch:** about 374 brands, a few queries each (brand name plus "acquired", "acquisition", "private equity", "portfolio"), and a quarterly re-run.

## Rules

- Primary sources only: each vendor's own documentation, pricing and terms pages. No third-party comparison blogs as sources.
- Respect robots.txt; any user agent carries no contact detail (CLAUDE.md, memory). Don't sign up for accounts or call paid endpoints.
- Mark anything unconfirmed.

## How to resolve

AFK: a subagent invokes the `research` skill and writes `.scratch/engine/research/web-search-apis.md`, then appends `## Answer` here. No branches, commits or pushes.

## Answer

- **Google Custom Search JSON API** is closed to new customers and stops on 2027-01-01. Since 2026-01-20, new Programmable Search engines cannot search the whole web (50-domain cap). Its terms bar automated queries and any non-transitory storage. Google's grounding terms (Gemini and Vertex) expressly forbid "using Links to identify destination pages for crawling or scraping".
- **Bing Search APIs were retired on 2025-08-11** (memory confirmed). The successor, Grounding with Bing ($14 per 1,000), returns LLM answers with citations, and its terms name "indexing links" and "using links for crawling or scraping" among the uses that are not allowed.
- **Brave** ($5 per 1,000, $5 monthly credit, 20 results, quotes, `site:`, custom date range): only "transient storage" unless on a plan with storage rights, whose price is not published. No AI training on results. The terms do not address fetching result URLs.
- **Mojeek** (£2 per 1,000 with a 1-hour cache, or £3 per 1,000 with indefinite storage): AI and commercial use allowed, no attribution. The terms contemplate retrieving pages from result URLs and put publisher terms on the customer. Its date filters use the last-modified date, and exact-phrase search is not documented.
- **Exa** ($4 to $7 per 1,000, $10 monthly free credit, 1,200-domain filter, published-date filter) and **Perplexity** ($5 per 1,000, 20-domain filter, publication-date filter): neither set of terms addresses storing results or fetching their URLs plainly. Exa may silently drop exact-phrase restrictions.
- **SerpApi-style resellers** scrape paths that Google's and Bing's robots.txt disallow for all crawlers, and Google sued SerpApi on 2025-12-19.
- **Launch cost:** 1,496 queries per quarterly run comes to roughly $2 to $11 per run on any raw-result API (under $50 a year). Free credits cover most of a run on Brave and Exa. Price does not separate the candidates; terms and coverage do.
- **Open:** no vendor documents index depth for 2015 to 2024 pages, and testing it needs an account. Whether keeping a result URL after fetching counts as "storing results" is a legal question.

[findings](../research/web-search-apis.md)
