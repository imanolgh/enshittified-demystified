# Research: Web search APIs for finding a brand's past coverage

Ticket: [71-research-web-search-apis](../issues/71-research-web-search-apis.md) · Researched 2026-11-08 · Primary sources only: each vendor's own documentation, pricing pages, terms pages and robots.txt, plus Google's own blog post on its SerpApi lawsuit.

**Bottom line:** **Google** and **Microsoft** are out for this use. Google's Custom Search JSON API is **closed to new customers** and stops on **January 1, 2027**, and its terms bar automated queries and any non-transitory storage. Microsoft **retired the Bing Search APIs on August 11, 2025** (the ticket's memory is right). Its successor, "Grounding with Bing Search", returns LLM answers with citations at $14 per 1,000. Its terms name "using links for crawling or scraping" as a use that is not allowed. Google's grounding product has the same ban in nearly the same words. Four APIs sell raw result lists (URL, title, snippet) from an index the vendor calls its own, and none of them bars the pointer-only use outright: **Brave** ($5 per 1,000, storage only with a plan that includes storage rights), **Mojeek** (£2 per 1,000 with 1-hour caching, or £3 per 1,000 with "indefinite data retention"), **Exa** ($4 to $7 per 1,000) and **Perplexity** ($5 per 1,000, or $1 for "Fast Search"). Launch cost is small for every one of them, at roughly **$2 to $11 per quarterly run** (374 brands × 4 queries = 1,496 queries). **No vendor documents how far back its index reaches.** Whether a 2021 release can be found at all could only be tested with an account, and I did not open one.

Fetch method note: pages were read on 2026-11-08 with WebFetch and plain `curl` (default user agent, no contact detail, no spoofing). I checked robots.txt first on `support.google.com`, `www.microsoft.com`, `brave.com`, `www.mojeek.com`, `exa.ai` and `www.perplexity.ai`, and fetched no disallowed path. I opened no accounts and called no search endpoint, free or paid. Terms quoted from Google's Programmable Search terms, Microsoft's enterprise grounding terms, Brave's terms, Mojeek's terms and Exa's two PDFs were read from the raw page or PDF text. Other quotes came through WebFetch, which returns short excerpts.

Sources:
- [G-CSE] Google Custom Search JSON API overview: https://developers.google.com/custom-search/v1/overview
- [G-CSE-LIST] Custom Search JSON API, `cse.list` reference: https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
- [G-CSE-TERMS] Custom Search JSON API Additional Terms of Service (last modified January 11, 2020): https://developers.google.com/custom-search/terms
- [G-PSE-TOS] Programmable Search Engine Terms of Service (no date shown): https://support.google.com/programmable-search/answer/1714300?hl=en
- [G-PSE-SITES] Programmable Search Engine Help, "Update sites in your search engine": https://support.google.com/programmable-search/answer/12397162?hl=en
- [G-SRA] Custom Search Site Restricted JSON API: https://developers.google.com/custom-search/v1/site_restricted_api
- [G-STRUCT] Programmable Search, structured search (page dates): https://developers.google.com/custom-search/docs/structured_search
- [G-GEMINI] Gemini API Additional Terms of Service (effective March 23, 2026): https://aistudio.google.com/docs/terms
- [G-CLOUD] Google Cloud Service Specific Terms, §20(k) Grounding with Google Search and §20(l) Web Grounding for Enterprise: https://cloud.google.com/terms/service-terms
- [G-ROBOTS] https://www.google.com/robots.txt
- [G-SERPAPI] Google blog, "Why we're taking legal action against SerpApi's unlawful scraping" (December 19, 2025): https://blog.google/innovation-and-ai/technology/safety-security/serpapi-lawsuit/
- [MS-LIFE] Microsoft Lifecycle, "Bing Search APIs Retiring on August 11, 2025" (page dated 2025-05-15): https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement
- [MS-PRICE] Grounding with Bing product and pricing page: https://www.microsoft.com/en-us/bing/apis
- [MS-TOU] Terms of Use for Grounding with Bing Search and Grounding with Bing Custom Search (last updated November 2025): https://www.microsoft.com/en-us/bing/apis/grounding-legal
- [MS-TOU-ENT] The same terms for use through Microsoft enterprise integrations such as Foundry (last updated November 2025): https://www.microsoft.com/en-us/bing/apis/grounding-legal-enterprise
- [MS-WEB] Microsoft Foundry, "Overview of web grounding capabilities" (updated 2026-09-17): https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/web-overview
- [MS-BING-TOOLS] Microsoft Foundry, "Use Grounding with Bing Search tools with the agents API" (updated 2026-10-21): https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/bing-tools
- [BING-ROBOTS] https://www.bing.com/robots.txt
- [BRAVE-API] Brave Search API product and pricing page: https://brave.com/search/api/
- [BRAVE-TOS] Brave Search API Terms of Use (last updated 1 Sep, 2026): https://api-dashboard.search.brave.com/terms-of-service
- [BRAVE-QUERY] Brave web search query guide: https://api-dashboard.search.brave.com/app/documentation/web-search/query
- [BRAVE-REF] Brave web search API reference: https://api-dashboard.search.brave.com/api-reference/web/search/get
- [BRAVE-OPS] Brave search operators: https://api-dashboard.search.brave.com/documentation/resources/search-operators
- [MJ-API] Mojeek Search API product and pricing page: https://www.mojeek.com/services/search/web-search-api/
- [MJ-TERMS] Mojeek Search API Terms of Service Agreement (no date shown): https://www.mojeek.com/about/legal/api-terms.html
- [MJ-PARAMS] Mojeek API request parameters: https://www.mojeek.com/support/api/search/request_parameters.html
- [MJ-OPS] Mojeek search operators: https://www.mojeek.com/support/search-operators.html
- [EXA-PRICE] Exa API pricing: https://exa.ai/pricing
- [EXA-SEARCH] Exa `/search` reference: https://exa.ai/docs/reference/search
- [EXA-RATE] Exa rate limits: https://exa.ai/docs/reference/rate-limits
- [EXA-TOS] Exa Labs Terms of Service, PDF linked from the exa.ai footer (no date in the text; the PDF file was created 2025-03-04): https://exa.ai/assets/Exa_Labs_Terms_of_Service.pdf
- [EXA-MSA] Exa Online Master Subscription Agreement v2.2026-09-17 ("Effective September 16, 2026"): https://exa.ai/msa
- [PPLX-PRICE] Perplexity API pricing: https://docs.perplexity.ai/getting-started/pricing
- [PPLX-OVERVIEW] Perplexity Search API overview: https://docs.perplexity.ai/docs/search/overview
- [PPLX-DATE] Perplexity search date and time filters: https://docs.perplexity.ai/docs/search/filters/date-time-filters
- [PPLX-DOMAIN] Perplexity search domain filter: https://docs.perplexity.ai/docs/search/filters/domain-filter
- [PPLX-RATE] Perplexity rate limits and usage tiers: https://docs.perplexity.ai/docs/admin/rate-limits-usage-tiers
- [PPLX-TOS] Perplexity API Terms of Service (last updated January 23, 2026): https://www.perplexity.ai/hub/legal/perplexity-api-terms-of-service
- [PPLX-ADD] Perplexity API Terms, Search Addendum (last updated September 22, 2025): https://www.perplexity.ai/hub/legal/perplexity-api-terms-of-service-search
- [PPLX-BLOG] Perplexity, "Introducing the Perplexity Search API" (Sep 25, 2025): https://www.perplexity.ai/hub/blog/introducing-the-perplexity-search-api
- [SERPAPI] SerpApi home page: https://serpapi.com/
- [PRESS] Prior research in this repo, for Google's Terms of Service on robots.txt: [press-feeds.md](press-feeds.md)

---

## 1. Google: Programmable Search and the Custom Search JSON API

**Availability: closed to new customers, ends January 1, 2027.** The overview page says: "The Custom Search JSON API is closed to new customers." and "Existing Custom Search JSON API customers have until January 1, 2027 to transition to an alternative solution." It names Vertex AI Search as "a favorable alternative for searching up to 50 domains". For "full web search" it offers only a "contact us" form and names no product [G-CSE].

**Whole-web search is going away in Programmable Search too.** Since January 20, 2026, "All new engines must now be configured to use the "Sites to search" feature." Existing engines set to "Search the entire web" "can continue to use this option until January 1, 2027", and turning the option off "can not be toggled back to On". A "Sites to search" engine is capped at 50 distinct domains ("Your URL patterns cannot be from more than 50 distinct domains"). Engines registered for "eligible nonprofit organizations, accredited educational institutions, and government agencies" are exempt from the 50-domain cap [G-PSE-SITES]. The exemption does not reopen the JSON API to new customers. The Site Restricted JSON API "will cease to serve traffic on January 8, 2025" [G-SRA], so that date has passed.

**Price (existing customers only).** "100 search queries per day for free", then "$5 per 1000 queries, up to 10k queries per day" [G-CSE].

**Terms.** The JSON API's Additional Terms incorporate the Google APIs Terms of Service and the Programmable Search Engine Terms of Service [G-CSE-TERMS]. The Programmable Search terms say:
- Queries come from people: "You shall receive a Query from the End User and shall forward that Query to Google" (§1.3), and Queries "must originate from the Site" (§1.1).
- No automated queries: you may not "directly or indirectly generate queries, or impressions of or clicks on Results, through any automated, deceptive, fraudulent or other invalid means (including, but not limited to, click spam, robots, macro programs, and Internet agents)" (§1.4(i)).
- No storage: you may not "'crawl', 'spider', index or in any non-transitory manner store or cache information obtained from the Service (including, but not limited to, Results, or any part, copy or derivative thereof)" (§1.4(l); the original uses double quotes around crawl and spider). Also, "You may not in any way frame, cache or modify the Results produced by Google, except as otherwise agreed to between You and Google" (§1.3).
- Display: you may not "display any Results to any third parties other than End Users" (§1.4(d)). The search box must show a graphic indicating the service comes from Google (§2.3). [G-PSE-TOS]

These terms do not mention AI.

**Query features** [G-CSE-LIST]:
- Exact phrase: `exactTerms`, "Identifies a phrase that all documents in the search results must contain."
- Site filter: `siteSearch` with `siteSearchFilter` = `i` (include) or `e` (exclude).
- Date: `dateRestrict` takes only relative windows (`d[number]`, `w[number]`, `m[number]`, `y[number]`), and `sort=date` sorts by date. Google "estimates the date for a page based the URL, title, byline date and other features" [G-STRUCT]. The docs show no absolute date range on that estimated date; the only range example uses a custom `review-date` attribute.
- Results: `num` is 1 to 10, and `start + num` cannot exceed 100, so a query returns at most 100 results.

**Google's grounding products have an explicit ban on this use.** Gemini API grounding with Google Search, Vertex AI grounding and Web Grounding for Enterprise (which uses "GCP's web index") all share §20(k) of the Google Cloud Service Specific Terms. That section says it "is a violation of these terms to use Grounding with Google Search to extract or collect one or more of these components for another purpose (for example, using programmatic or automated means to collect Links, using Links to build an index, or using Links to identify destination pages for crawling or scraping)" [G-CLOUD]. The Gemini API terms say the same and forbid using grounded results "to create a database" [G-GEMINI].

## 2. Microsoft: Bing Search APIs and Grounding with Bing

**Retired August 11, 2025 (confirmed).** "Bing Search APIs will be retired on August 11, 2025. Any existing instances of Bing Search APIs will be decommissioned completely, and the product will no longer be available to be used or new customer signup." The successor named is "Grounding with Bing Search as part of Azure AI Agents", which "allows Azure AI Agents to incorporate real-time public web data when generating responses with an LLM" [MS-LIFE].

**The successor returns LLM output, not result lists.** The product page says the service "is designed to function as an add-on feature for select Microsoft products" and that "Outputs are not directly accessible for use in other applications or programs" [MS-PRICE]. The enterprise terms define the service as access to "Bing Services Output after being processed and summarized using an LLM" (§1(g)) [MS-TOU-ENT]. In Foundry the developer gets an agent response with `url_citation` annotations. The tool takes `count`, `freshness`, `market` and `set_lang` parameters, and the agent writes the actual queries [MS-BING-TOOLS][MS-WEB]. Foundry's newer "Web Search" tool also runs on Bing and falls under the same grounding terms [MS-WEB].

**Price.** Grounding with Bing Search and Grounding with Bing Custom Search are each "$14 per 1,000 transactions", "150 transactions per second", "1 Million transactions per day". No free tier is listed [MS-PRICE]. The cost of the model tokens on top was not checked.

**Terms: storage, and using links to fetch pages, are both barred.**
- §3(c) (enterprise): "Customer may copy, store, cache or archive Bing Services Output solely (1) to the extent permitted by copyright law and (2) as an integrated part of its own work product, so long as the work product is not created for the purpose of or intended for use as a substitute for the Services or the Bing Services Output (for example, creating a database of Bing Services Output, indexing links contained in the Bing Services Output, **using links for crawling or scraping**, or offering a separate search offering). Customer may not otherwise copy, store or cache Bing Services Output." [MS-TOU-ENT]
- Use limited to search experiences: "Customer may only use the Bing Services Output in Customer Solutions that are internet search experiences." The appendix defines that as content that responds to "the end user's direct query", helps users "find and navigate to the Resources", and shows "a visible indication that the end user is receiving an internet search result". References must be displayed "in the exact form provided by Microsoft" [MS-TOU-ENT].
- No AI training: "Customer may not use any Bing Services Output to train any AI Models" [MS-TOU-ENT]. The standalone terms carry the same restrictions [MS-TOU].

## 3. Brave Search API

**Availability.** Open to new customers on prepaid credits ("Prepaid credits, no subscription", "No minimums") [BRAVE-API]. Brave says "Every result comes from Brave's own independent index" and "There is no fallback to another search engine for any query" [BRAVE-API]. It gives no index size ("a vanity stat").

**Price.** The "Search" plan costs "$5 per 1,000 requests", includes "$5 in free credits every month", and allows 50 queries per second. The "Answers" plan (LLM answers) costs $4 per 1,000 plus $5 per million tokens. Enterprise pricing is custom and adds "Full-funnel Zero Data Retention" [BRAVE-API]. No monthly cap is listed. One search-result snippet of an older Brave guide page mentioned a free tier of 2,000 queries a month and plans from $3 CPM. I did not open that page, and the current pricing page shows the $5 plan, so the current page governs.

**Terms** [BRAVE-TOS]:
- Storage: you may not "store, cache, or create a database of Search Results, in whole or in part, other than transient storage required for operation of Customer Applications or related software, service or systems" (§3(b)(i)). The terms give no time limit for "transient".
- Storage rights are sold separately. The FAQ asks "Can I store results or use them to train models?" and answers "Yes, with a plan that includes storage rights" [BRAVE-API]. No current page I read names that plan or its price.
- AI: you may not "use the Search Results to create, evaluate, train, re-train, fine-tune, benchmark or otherwise improve artificial intelligence models or services offered by Customer or third parties" (§3(b)(xiii)).
- After termination: you may not "retain Documentation or Search Results in Customer's possession and control" (§3(b)(xiv)).
- Attribution is optional: "Customer may provide attribution", and if it does, it shows "POWERED BY BRAVE" plus the logo (§4(d)).
- Results are licensed for use "with the Customer Applications" (§3(a)(ii)). Brave owns Search Results, subject to third parties' rights in Third-Party Content (§9).
- **The terms say nothing about using result URLs to fetch pages**, for or against.

**Query features** [BRAVE-REF][BRAVE-QUERY][BRAVE-OPS]:
- Exact phrase: `""` "Returns web pages containing exact matches to your query in the specified order." Also `site:`, `-`, `intitle:`, `inbody:`, `filetype:` and uppercase `AND`/`OR`/`NOT`. The operators page says they are experimental and may change.
- `q`: "Maximum of 600 characters and 75 words."
- `count`: up to 20 results per request. `offset`: 0 to 9, counted in pages, so one query can reach 200 results over 10 billed requests.
- `freshness`: `pd`, `pw`, `pm`, `py`, or a custom range `YYYY-MM-DDtoYYYY-MM-DD`. It filters "by page age", where "The age of a page is determined by the most relevant date reported by the content, such as its published or last modified date."
- Old pages: no statement on index depth.

## 4. Mojeek Search API

**Availability.** Open, pay-as-you-go with "no minimum commitment". Mojeek describes a "Global index with billions of fresh webpages" crawled by "MojeekBot which respects Robots Exclusion Protocol" [MJ-API].

**Price** (GBP, excluding VAT) [MJ-API]:

| Plan | Per 1,000 requests | Queries/sec | Queries/day | Results per request | Storage |
|---|---|---|---|---|---|
| Startup | £2 | 5 | 100,000 | up to 10 | "cache results for one hour" |
| Business | £3 | 10 | 400,000 | up to 40 | "storage rights which permit indefinite data retention" |
| Enterprise | custom | no limit listed | no limit listed | up to 100 | as Business, plus zero data retention |

New accounts can "claim a free credit" on Startup; the amount is not stated. A bank card is required, but "no automatic payments are processed" [MJ-API].

**Terms** [MJ-TERMS] (§1.6, read from the raw page):
- AI and commercial use are allowed: Data "may be used in any application, including internet search experiences and artificial intelligence applications such as retrieval-augmented generation, grounding, AI agents and assistants, and model evaluation". "You may use Data for commercial purposes … without attribution to Mojeek." "You may combine Data with search results from other sources, including other search engines."
- Storage: "You may retain Data indefinitely only if you subscribe to a plan with storage rights." "Do not compile, copy or store any Data unless you subscribe to a plan with storage rights. Without storage rights, do not cache any Data except temporarily, to serve the same user, for up to 1 hour."
- **Fetching linked pages is contemplated.** "Data consists of publicly available URLs, page titles and query-dependent snippets from webpages that do not block Mojeek from crawling or indexing them. Mojeek grants no rights in the third-party content contained in or linked from the Data. You are responsible for complying with copyright law and with publishers' terms and permissions, including any reservation of rights over text and data mining, in your use of the Data and any content you retrieve from the URLs."
- "Do not use Data as part of any search index."
- Automated access: the terms bar "using or accessing the Services by any automated means, unless you are an authorised Services user" (§1.4). An API customer is presumably an authorised user, but the terms do not define the phrase.
- Changes: "at least 30 days' advance notice of any material changes".

**Query features** [MJ-PARAMS][MJ-OPS]:
- Site: the `site` parameter or `site:` operator. `fi` and `fe` include or exclude up to 25 domains.
- Date: `since` and `before` take `YYYYMMDD` (or `day`, `month`, `year`). The operators page says they filter on pages "last modified since then", meaning the last-modified date, not the publication date. `datewr=100` ranks by date, and `date=1` returns the last-modified date.
- Results: `t` sets results per page and `s` the start index. No maximum is documented; the plan sets the per-request cap.
- Exact phrase: **not documented** in the request parameters or on the operators page (which lists `intitle:`, `intext:`, `inurl:`, `inanchor:`, `site:`, `since:`, `before:`).
- Old pages: no statement on index depth.

## 5. Exa

**Availability.** Open, self-serve, with a free tier of "$10 in credits (up to 2,500 Lite searches)" that resets to $10 on the first of each month, no card required [EXA-PRICE]. Exa is a neural and semantic engine. The docs say `lite` "serves content directly from Exa's regularly refreshed search index", and `snapshotAsOf` returns "the newest stored version of each page as of this instant", served "from stored versions only" [EXA-SEARCH]. No index size or depth is stated.

**Price** [EXA-PRICE]: per 1,000 requests with up to 10 results, `lite` and `instant` cost $4 and `auto` and `fast` cost $7. Each result above 10 adds "$1 per 1k results". Deep search costs $12 to $15. Page contents cost "$1 / 1k pages, per content type". The engine would not need contents, because it fetches pages itself. Default rate limit is "10 QPS" [EXA-RATE].

**Terms: two documents, and neither speaks plainly to storing API results.**
- The self-serve Terms of Service PDF [EXA-TOS] covers "our application programming interface ("API")" and defines "Output" as the "responses and … search results" the engine produces. §4.2(a) bars you from doing the following with "any information contained on, or obtained from or through, the Services": "download, modify, copy, distribute, transmit, display, perform, reproduce, duplicate, publish, license, create derivative works from, or offer for sale". The only exceptions are "temporary files that are automatically cached by your web browser for display purposes, or as otherwise expressly permitted in these Terms or by us in writing". §4.2(j) bars using any automatic device "to monitor, extract, copy or collect information or data from or through the Services". Read literally, both clauses cover ordinary API use, and §1.1 separately licenses the API "for the limited purposes set forth in the documentation". The PDF shows no effective date. Exa also takes a "perpetual and irrevocable license" to User Input and Output to improve its products (§1.2(c)).
- The Master Subscription Agreement [EXA-MSA] applies only where an Order Form is executed. Under it, "Customer owns Customer Data", and Customer Data "means Input and Output together" (§4.1, §1.3). It bars using the Services "to develop, maintain, or distribute any competitive products or services" (§3.4(c)). In the clauses I read I found no restriction on storing Output.
- Neither document addresses using result URLs to fetch pages.

**Query features** [EXA-SEARCH]:
- `numResults`: default 10, "maximum public limit is 100 results".
- `includeDomains` / `excludeDomains`: up to 1,200 entries each, with path prefixes allowed. The docs recommend these over a `site:` operator.
- `startPublishedDate` / `endPublishedDate`: ISO 8601. `publishedDate` is "An estimate of the creation date, from parsing HTML content". `startCrawlDate` / `endCrawlDate` are deprecated and ignored.
- `category`: `company`, `publication`, `news`, `personal site`, `financial report`, `people`. `company` and `people` do not support date filters.
- Exact phrase: **not documented as a guarantee.** The `RESTRICTIONS_RELAXED` notice says that when "the `site:` or exact-phrase restrictions written in the query matched nothing", "the results come from a search with them removed". The deprecated `includeText` matches "word-level rather than exact phrase".

## 6. Perplexity Search API

**Availability.** Launched "Sep 25, 2025", with "an index covering hundreds of billions of webpages" [PPLX-BLOG]. The post does not say whether Perplexity runs its own crawler. The `/search` endpoint returns ranked results, each with `title`, `url`, `snippet`, `date` and `last_updated` [PPLX-OVERVIEW].

**Price.** "$5.00 per 1K requests"; "Fast Search" costs $1.00 per 1,000. Billing is per `POST /search` request, and one request can carry several queries [PPLX-PRICE]. The pricing page mentions no free tier. The rate limit is 50 query units per second on every tier [PPLX-RATE].

**Terms.**
- The Search Addendum says "Customer does not own, and Perplexity shall not grant it ownership of, the Search API's Output", and that "Perplexity may retain, copy, distribute and otherwise use Search Data for its lawful business purposes" [PPLX-ADD]. This overrides the main terms' "owns all Output" (§2.3.1) for search [PPLX-TOS].
- The main license lets the customer "receive Output … and display such Output, in each case, solely within the Customer Applications in accordance with the API Documentation" (§2.1) [PPLX-TOS].
- Neither document has a clause on how long results may be stored, or on fetching linked pages. No attribution requirement was found.

**Query features** [PPLX-OVERVIEW][PPLX-DATE][PPLX-DOMAIN]:
- `max_results`: 1 to 20 for web search, default 10.
- `search_domain_filter`: "a maximum of 20 domains". It runs as an allowlist or a denylist (prefix `-`), not both at once, and accepts path-level entries.
- Date: `search_after_date_filter` / `search_before_date_filter` filter by publication date, in `%m/%d/%Y` format. `last_updated_after_filter` / `last_updated_before_filter` filter by modification date. `search_recency_filter` takes `hour`, `day`, `week`, `month` or `year`. In the docs' own example, a March 1 to 5, 2025 publication filter returns results dated as early as 2019, so the filter's behavior is not clear.
- Exact phrase: **not documented** in the pages read.

## 7. Resellers that scrape another engine (SerpApi and similar)

SerpApi describes itself as a way to "Scrape Google and other search engines". It says it routes each request "through the proxy server nearest to your desired location" and will "solve all CAPTCHAs". It sells a "U.S. Legal Shield [that] covers the scraping and parsing of search engine data". The cheapest plan is $25 a month for 1,000 searches [SERPAPI]. Why this does not fit:
- Google's robots.txt has `Disallow: /search` for `User-agent: *` [G-ROBOTS], and so does Bing's [BING-ROBOTS]. Google's Terms of Service forbid automated access that violates robots.txt [PRESS]. A reseller's results therefore come from fetches the engine's own bot rules would refuse to make, and buying them would be a way around a block.
- Google sued SerpApi on December 19, 2025 "for circumventing security measures protecting others' copyrighted content". It accuses SerpApi of "cloaking themselves, bombarding websites with massive networks of bots" and giving "their crawlers fake and constantly changing names" [G-SERPAPI]. I did not read the complaint or any ruling.

---

## Summary tables

**Availability and terms**

| API | New customers | Raw result list | Store results | Use results to pick pages to fetch | AI use |
|---|---|---|---|---|---|
| Google Custom Search JSON | **No** (closed; ends 2027-01-01) | Yes | No non-transitory storage | Queries must come from end users; automated queries barred | Not addressed |
| Google grounding (Gemini, Vertex) | Yes | No (LLM answer + links) | Narrow cases only | **Expressly barred** | It is an AI product |
| Bing Search APIs | **Retired 2025-08-11** | n/a | n/a | n/a | n/a |
| Grounding with Bing | Yes | No (LLM answer + citations) | Barred; "indexing links" and "using links for crawling or scraping" given as examples | **Expressly barred** | No training |
| Brave | Yes | Yes | Transient only, unless on a plan with storage rights | Not addressed | No training, evaluating or benchmarking AI |
| Mojeek | Yes | Yes | Startup: 1 hour, same user. Business/Enterprise: indefinite | Contemplated ("content you retrieve from the URLs") | Allowed, named |
| Exa | Yes | Yes | Self-serve ToS restricts copying (unclear for API); MSA: customer owns Output | Not addressed | Not addressed |
| Perplexity | Yes | Yes | Not addressed; customer does not own Search output | Not addressed | Not addressed |

**Query features**

| API | Exact phrase | Site filter | Date range | Results per request | Index depth documented |
|---|---|---|---|---|---|
| Google CSE | `exactTerms` | `siteSearch` | Relative only (`dateRestrict`) | 10 (max 100 per query) | No |
| Brave | `""` (experimental) | `site:` | Custom range on page age (published or last modified) | 20 (max 200 per query) | No |
| Mojeek | Not documented | `site`, `fi`/`fe` (25) | `since`/`before`, on last-modified date | 10 / 40 / 100 by plan | No |
| Exa | May be silently dropped | `includeDomains` (1,200) | Published date (estimated from HTML) | up to 100 (above 10 billed extra) | No |
| Perplexity | Not documented | `search_domain_filter` (20) | Publication date or last-updated | up to 20 | No |

## Rough launch cost

Assumptions from the ticket: 374 brands × 4 queries (brand name plus "acquired", "acquisition", "private equity", "portfolio") = **1,496 queries per run**, four runs a year = **5,984 queries a year**. One request per query, first page only. Prices exclude tax. Free credits are shown separately because they reset monthly and would also be spent by any other use in that month.

| API and plan | Per run (1,496) | Per year (4 runs) | Free credit against a run | Notes |
|---|---|---|---|---|
| Brave Search ($5/1k, 20 results) | $7.48 | $29.92 | $5/month, so about $2.48 net | Storage-rights plan price unknown |
| Mojeek Startup (£2/1k, 10 results) | £2.99 | £11.97 | signup credit, amount unknown | 1-hour cache limit |
| Mojeek Business (£3/1k, 40 results) | £4.49 | £17.95 | n/a | Indefinite storage rights |
| Exa lite ($4/1k, 10 results) | $5.98 | $23.94 | $10/month covers it | |
| Exa auto ($7/1k, 10 results) | $10.47 | $41.89 | $10/month, so about $0.47 net | |
| Perplexity ($5/1k, up to 20 results) | $7.48 | $29.92 | none listed | Fast Search: $1.50 a run |
| Grounding with Bing ($14/1k) | $20.94 | $83.78 | none | Terms bar the use; model tokens extra |

Sensitivity: at 10 queries per brand (for example, adding former names from `renamed_from` claims), a run is 3,740 queries: Brave $18.70, Mojeek Business £11.22, Exa auto $26.18, Perplexity $18.70. Asking for 20 results instead of 10 costs nothing extra on Brave or Perplexity. It needs two Startup requests on Mojeek (Business returns 40), and on Exa lite it raises the price to $14 per 1,000 requests ($4 + 10 × $1).

---

## Implications for the design (facts and consequences, no decisions)

- **Google and Microsoft are closed to this use.** Google's JSON API takes no new customers and ends on 2027-01-01, and its terms require queries to come from end users and bar non-transitory storage. Both Google's grounding terms and Microsoft's Bing grounding terms name the pointer-only pattern ("using Links to identify destination pages for crawling or scraping", "using links for crawling or scraping") as not allowed. Bing's output is also LLM-processed and "not directly accessible for use in other applications".
- **Four raw-result APIs remain, and they differ mainly on storage.** Brave, Mojeek, Exa and Perplexity all return URL lists from an index each calls its own, and none of their terms bars using a URL to fetch the page. Mojeek's terms are the only ones that address it, by putting the publisher's terms and text-and-data-mining reservations on the customer "in your use of … any content you retrieve from the URLs".
- **"Pointer only" still involves keeping search results for a while.** A fetch queue that waits on the per-domain token bucket holds result URLs, and so does any provenance row recording which query found a page. Brave's default terms allow only "transient storage required for operation", and Mojeek Startup allows 1 hour "to serve the same user". A page the engine later fetches from the publisher is the publisher's content, not a search result. But whether keeping that URL, or the query that found it, counts as storing "Search Results" is a legal question. Plans with storage rights (Mojeek Business, a Brave plan whose price is not published) take the question away.
- **The search vendor is never the source.** The stored document comes from the publisher's site under the engine's bot rules, so it takes the publisher's source type. ADR 0003 already says "one source type per publisher, never per fetch method". Publisher terms still apply to the fetch, such as PR Newswire's ban on "database storage and retrieval" [PRESS]. Ten results from one vendor's index add no independence.
- **Date filters use the vendor's guess at the date, and can drop the page being sought.** Mojeek filters on last-modified date. Brave uses "published or last modified". Exa estimates a creation date from the HTML. Perplexity's own date example returns out-of-range results. A 2021 release that was edited or re-crawled later can fall outside a 2021 window. Running a query with no date filter avoids that risk but returns more recent noise.
- **Exact-phrase guarantees differ.** Brave documents quotes (as experimental). Exa drops exact-phrase and `site:` restrictions that match nothing and says so only in a notice. Mojeek and Perplexity document no phrase operator. So a result may not contain the brand name at all. The engine's own fetch and extraction (which emits `no_evidence_found` for a page no claim cites) handles that, at the cost of wasted fetches.
- **Price does not separate the candidates.** At launch scale every raw-result API costs under $50 a year at 4 queries per brand, and Brave's and Exa's monthly credits cover most or all of a single run. The choice turns on terms and coverage.
- **Coverage of 2015 to 2024 is unknown for every vendor.** None documents index depth, and testing it needs an account. Brave and Exa offer monthly free credits, and Mojeek offers a signup credit. The ticket's case, Dental365's 2021 acquisition through The Resolute Fund V, is a ready test query.
- **Search filters are not a coverage gate.** Mojeek's `fi` (25 domains), Perplexity's domain filter (20) and Google's 50-domain "Sites to search" cap all limit how many publishers one query can be pinned to. Exa allows 1,200 domains in `includeDomains`.

## Unconfirmed / open

- **Index depth and recall for old pages** (2015 to 2024) for Brave, Mojeek, Exa and Perplexity. Not documented and not tested, because no accounts were opened.
- **Brave:** which plan carries storage rights and at what price; whether the $5 monthly credits roll over; whether the News Search endpoint is priced and governed the same way (not checked). The older "2,000 free queries / $3 CPM" figures were seen only in a search snippet.
- **Mojeek:** the size of the signup credit; whether quoted exact phrases work; the maximum `s` start index; whether an API customer is an "authorised Services user" under §1.4; whether a fetch queue waiting longer than an hour breaks the Startup 1-hour cache rule; whether a document store with full-text search counts as "any search index" (the Data is URLs, titles and snippets, not the fetched pages).
- **Exa:** which document governs self-serve API use, and whether §4.2(a) and (j) of the undated ToS PDF restrict storing API results; whether a small customer can get an Order Form under the MSA; whether exact phrases are honored.
- **Perplexity:** whether Search API output may be stored and for how long; whether its index is built by its own crawler; exact-phrase support; how deep results can be paged.
- **Google:** the unnamed "full web search solution" behind the overview's contact form. Vertex AI Search (now "Agent Search") website search for up to 50 domains: its price and its storage and crawling terms were not read (the pricing page did not render).
- **Microsoft:** model token costs on top of the $14 per 1,000 grounding price.
- **Other APIs not checked:** Kagi, You.com, Tavily, Parallel, Linkup and Marginalia, including whether each serves results from its own index.
- **Legal questions for the developer:** whether keeping a result URL (or the query that found it) after fetching the page counts as storing search results under Brave's or Mojeek Startup's terms; and Exa's self-serve ToS wording.
