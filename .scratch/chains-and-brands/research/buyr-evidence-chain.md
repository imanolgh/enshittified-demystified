# Research: Buy'r's evidence chain

Competitor methodology question from the developer · Researched 2026-11-20 · Not legal advice.

## Summary

Buy'r states its method in one sentence on its FAQ: "Ownership records are built from public corporate filings and companies' own statements, then verified before they are published." It names no filing type, no data vendor and no verification method. The public website shows no source for any ownership record, and the two investigative blog posts read for this note cite no sources either, although each ends "Built from filings and company statements." The barcode database is said to cover "1.5B+ products". Its vendor is unnamed.

Its taxonomy has three tiers: independent, private and megacorp. Independent is split into founder, family, co-operative and employee ownership, and private equity is counted as a subset of private. There is no big pharma tier and no asset-manager tier. Asset managers appear as a "Shareholders" line with percentages under a public parent. In the Blue Wilderness example that line reads "Vanguard (13%), BlackRock (11%), State Street (6%)", with no as-of date and no source. A public listing seems to be what makes a parent a megacorp.

Corrections go through an in-app report or email, and Buy'r asks the reporter for "the brand and a source". The FAQ also says Buy'r is "exploring" an API with "verified ownership records with sources attached". That suggests the records carry sources internally. No source says whether the app shows them.

The origin is still co-founder Ian Carroll's hand-made public spreadsheet of "hundreds of brands" from January 2024. No source explains how it grew to 30,332 brands and 16,875 companies.

## How this was researched

Labels used below:

- [stated]: Buy'r or a co-founder says it, in their own channel (website, store listing, press release, video, post).
- [observed]: seen directly on 2026-11-20 in a page or file fetched for this note.
- [search index]: wording from a web-search result or the search tool's summary of it. The page itself was not fetched, so treat it as unverified.
- [inference]: my reasoning, with the evidence given next to it.
- [unknown]: no source read answers it.

Fetching. Pages were fetched with curl using the user agent `ownership-research/0.1 (public-data research)`, which carries no contact details, and with the WebFetch tool. robots.txt was read before the first request to each host.

The website. The robots.txt for www.buyrapp.com allows every crawler and names AI crawlers explicitly "so Buy'r can be surfaced and cited in ChatGPT, Claude, Perplexity, Gemini, etc." [B-ROBOTS]. The research agent's first attempt to fetch the 23 sitemap pages in one run was refused by the session's permission check, and it stopped. The developer then approved reading eight named pages, and the main session fetched them one at a time on 2026-11-20: the FAQ, the homepage, the terms, the privacy policy, /ugc, /official and two blog posts. Wayback copies were not opened. Buy'r's terms bar using "automated systems to access our Services without permission" [B-TERMS]. Eight single-page reads by an identified user agent, on a site whose robots.txt invites AI crawlers, were judged within that permission. The developer should know the clause exists.

Other blocks and limits:

- medium.com returned HTTP 403 to WebFetch. Not retried.
- x.com's robots.txt disallows every path for `*`. X posts were seen only as search-result titles.
- YouTube serves transcripts under `/api/`, which its robots.txt disallows. Videos were read by title, date and description only, not watched.
- Google Play's data-safety detail page (`/store/apps/datasafety`) is disallowed by robots.txt. Only the summary on the listing was read.
- The press-release mirror cited in the repo (lifestyle.kbew98country.com) did not resolve in DNS. The PR Newswire original was read instead.
- Never fetched: whoismydentist.com, privateequityvet.org, Reddit. No Reddit thread came up in any search.
- No account was created, no app installed, nothing bought.

Source keys (all read 2026-11-20 unless marked):

- [B-ROBOTS] https://www.buyrapp.com/robots.txt
- [B-SITEMAP] https://www.buyrapp.com/sitemap.xml
- [B-FAQ] https://www.buyrapp.com/faq
- [B-HOME] https://www.buyrapp.com/
- [B-TERMS] https://www.buyrapp.com/terms (effective date January 14, 2025)
- [B-PRIV] https://www.buyrapp.com/privacy (effective date January 14, 2025)
- [B-UGC] https://www.buyrapp.com/ugc
- [B-OFFICIAL] https://www.buyrapp.com/official
- [B-CEREAL] Blog post "The Illusion of Choice in the Cereal Aisle", dated Mar 15, 2024: https://www.buyrapp.com/blog/illusion-of-choice
- [B-BLUE] Blog post "Blue Wilderness: The "Wild" Pet Food... Brought to You by the Cheerios People", dated Mar 16, 2024: https://www.buyrapp.com/blog/blue-wilderness-general-mills
- [IOS] App Store listing: https://apps.apple.com/us/app/buyr/id6754346785
- [IOS-REV] App Store reviews page: https://apps.apple.com/us/app/buyr/id6754346785?see-all=reviews&platform=iphone
- [PLAY] Google Play listing: https://play.google.com/store/apps/details?id=com.buyr.app&hl=en_US&gl=US
- [PRN] Buy'r press release, PR Newswire, 2026-01-21: https://www.prnewswire.com/news-releases/buyr-surpasses-50-000-users-in-first-week-and-climbs-to-1-on-the-app-store-signaling-a-cultural-shift-toward-economic-transparency-302667268.html
- [YT-CH] Buy'r YouTube channel: https://www.youtube.com/@BuyrApp/videos . Individual videos are cited as [YT id], at https://www.youtube.com/watch?v={id}.
- [TT-1] Buy'r TikTok video, posted 2025-07-22 (date from the video id): https://www.tiktok.com/@buyr.app/video/7529714630902517047
- [TT-2] Ian Carroll TikTok video, posted 2024-01-18 (date from the video id): https://www.tiktok.com/@iancarrollshow/video/7325570508605656362
- [IC-SITE] Ian Carroll's site, https://iancarroll.org/work/ . The page is a JavaScript app, so its text was read from the site's own bundle: https://iancarroll.org/assets/index-CQ4Dg122.js
- [AG] AppGoblin, third-party app analytics: https://appgoblin.info/apps/com.buyr.app and https://appgoblin.info/apps/com.buyr.app/data-flows
- [SEC-13G] Vanguard Group, Schedule 13G/A on PepsiCo, filed 2025-06-05: https://www.sec.gov/Archives/edgar/data/102909/0000932471-25-000680-index.html ; rendered form: https://www.sec.gov/Archives/edgar/data/77476/000093247125000680/xslSCHEDULE_13G_X01/primary_doc.xml
- [MED] Buy'r post on Medium (HTTP 403, body not read): https://medium.com/@buyrapp/the-illusion-of-choice-how-blackrock-and-vanguard-control-every-aisle-in-your-grocery-store-9af3880bf8aa
- [X-1] https://x.com/IanCarrollShow/status/1744816710912545202 (2024-01-09), [X-2] https://x.com/IanCarrollShow/status/1745175940018397430 (2024-01-10), [X-3] https://x.com/IanCarrollShow/status/1852490149575426320 (2024-11-01), [X-4] https://x.com/IanCarrollShow/status/1998587589264339317 (2025-12-10). Titles from search results only; dates decoded from the post ids.
- [REPO] `.scratch/pivot-handoff-2026-11-02.md`, section 4 and the barcode bullets above it (figures as of 2026-10-31, from an earlier session).

---

## 1. Owner categories Buy'r flags

The brief's description, from memory: private equity, conglomerate, big asset manager (BlackRock, Vanguard, State Street and similar), big pharma, other large corporate owner.

What the website shows instead [B-HOME][B-FAQ], with counts "as of September 2026":

| Tier | Sub-type | Brands | Definition, in Buy'r's words |
|---|---|---|---|
| Independent | Founder | 8,783 | "controlled by its founders, a family, its employees, or a co-operative" [B-FAQ] |
| | Family | 3,707 | |
| | Co-operative | 571 | |
| | Employee | 128 | |
| | Total | 13,189 | |
| Private | Private equity | 2,041 | "privately held by an investment group" [B-FAQ]. The homepage example: "Duke's is held by Advent International, one of 2,041 brands owned by private equity." [B-HOME] |
| | Other privately held | 8,022 | "A further 8,022 brands are privately held." No definition. [B-HOME] |
| Megacorp | | 7,072 | "owned by a public conglomerate" [B-FAQ]. A scan card reads "Type: Publicly traded mega-corp" [B-BLUE]. |

- [observed] The app's tier bar is labelled "Ind / Priv / Mega" [B-HOME]. On the homepage the same bar reads "Independent 13,189 · Family / Private 10,063 · Megacorp 7,072". 10,063 is 2,041 private equity plus 8,022 other private. So in the three-tier view private equity sits in a bar labelled "Family / Private", while family-owned brands are counted as independent.
- [observed] The sub-types add up to 30,324, eight short of the 30,332 brands on record.
- [observed] No big pharma tier and no asset-manager tier appear on any page read. Asset managers appear as shareholders under a megacorp (section 4). Kenvue appears as an ordinary parent company with 17 brands (section 6).
- [stated] "None of them rated, ranked, or recommended." [B-FAQ]. Buy'r does not hand out "approved" badges [IOS][PLAY]. The terms, dated January 14, 2025, still describe "ownership, sourcing, and ethical information" and "ethical ratings" [B-TERMS].
- Earlier wording outside the website: "conglomerate", "megacorp", "big money brands" [IOS][PRN][X-3], and "the Big 3" for asset managers [YT -ZqtCF08Icg].

## 2. Barcode to brand

- [stated] "its barcode database covers 1.5B+ products" and "The barcode database is global, so most products will scan." [B-FAQ][B-HOME]
- [unknown] The vendor or database. GS1, Open Food Facts, USDA FoodData Central, a commercial UPC service and Buy'r's own data are unmentioned on the website, in the store listings, the press release and AppGoblin's summary [B-FAQ][B-PRIV][IOS][PLAY][PRN][AG].
- [inference, weak] 1.5 billion is far larger than any public product database this repo has looked at [REPO], so a commercial lookup service or GS1-derived data is more likely than a crowd-sourced one. No source says which.
- [stated] Search by name is also possible: "You can search for a brand or product by name inside the app and see the same ownership record you would get from a scan." [B-FAQ]
- [stated] Recall notices are "based on official recall feeds" [B-FAQ]. Recipes are "9,800 curated recipes", "Curated by hand. Not generated." [B-HOME]
- [stated] Users add to the data. A reviewer writes that "each and every person who uses this app is helping improve it one scan at a time" (12/18/2025) [IOS]. The App Store age rating notes "Contains User-Generated Content" [IOS].
- [observed] The privacy policy names no data vendor. It mentions only unnamed service providers for "hosting, analytics, customer support" and "Analytics Providers" [B-PRIV]. AppGoblin lists only generic SDKs and Firebase analytics [AG].
- [observed] /ugc is a password-protected creator brief ("This page is unlisted. If we sent you the brief, you already have the word.") [B-UGC]. It is about user-generated marketing content, not data submissions.

## 3. Brand to owner

- [stated] The method, in full: "Ownership records are built from public corporate filings and companies' own statements, then verified before they are published. As of September 2026, Buy'r has ownership records for 30,332 brands across 16,875 companies" [B-FAQ]. Also: "Buy'r only publishes verified corporate structures" [B-FAQ].
- [unknown] Which filings (SEC 10-K exhibit 21 subsidiary lists, 8-Ks, state registrations, foreign filings), what "verified" means, who verifies, and whether LLMs are used. None of it is stated.
- [stated] The chain goes to the top: "Buy'r traces the brand up to its parent company and ultimate owner" and shows "the ultimate parent at the top of the chain" [B-FAQ]. Intermediate brands are kept: "General Mills, Via Blue Buffalo · NYSE: GIS" [B-HOME], and a scan card shows "Parent Brand: Blue Buffalo / Owner: General Mills, Inc. (NYSE: GIS)" [B-BLUE].
- [stated] Premium ($5 a month or $50 a year) "adds ... full ownership hierarchies". "Scanning and ownership lookups are free forever." [B-FAQ]. [inference] The free tier shows the owner and the paid tier shows the full chain.
- [stated] Origin. Carroll "originally built a public spreadsheet mapping ownership across hundreds of brands." [PRN]. "I got my start by going through the grocery store and trying to figure out and make a record of who owns all the products on the shelves." (2025-07-22) [TT-1]. The spreadsheets date from January 2024 [X-1][X-2][TT-2][X-3].
- [unknown] How "hundreds of brands" became 30,332 brands and 16,875 companies.
- [stated] Brand spotlights are "a written investigation into one brand's ownership story, produced with independent journalist Ian Carroll" [B-FAQ], covering "who founded it, who bought it, what changed after, and what the filing actually says" [B-HOME].
- [observed] Carroll also runs Webb (thewebb.io), described on his site as a research platform for "court files, disclosures, primary source material" [IC-SITE]. [inference] It may support the spotlights. No source says it feeds the ownership records.

## 4. Asset-manager stakes: BlackRock, Vanguard, State Street

What the app shows, from the one example on the website:

- [stated] The Blue Wilderness spotlight reproduces a scan result: "Parent Brand: Blue Buffalo / Owner: General Mills, Inc. (NYSE: GIS) / Type: Publicly traded mega-corp / Shareholders: Vanguard (13%), BlackRock (11%), State Street (6%)" [B-BLUE].
- [observed] So the scan card labels the asset managers "Shareholders" and gives a percentage. It does not call them owners. The same post's prose calls the list "the ownership chain" and the firms "our favorite Big Three asset managers" [B-BLUE].
- [observed] No as-of date, filing or source is given for the percentages [B-BLUE]. The post is dated Mar 16, 2024, but the footer quotes counts "as of September 2026", so the percentages' age can't be told.

The coordinator's questions:

- Data source for stakes: [unknown]. No page read mentions 13F, 13D or 13G, proxy statements (DEF 14A) or a market-data vendor. The FAQ's general "public corporate filings" is the only statement.
- Threshold: [unknown]. The one example shows three holders at 6% and above. Whether smaller holders or other firms appear is not shown.
- Passive holdings versus control: [unknown] for the app's logic. The scan card's "Shareholders" label is a separate line from "Owner", which keeps them apart on screen. The tier depends on the owner (megacorp), not the shareholders.
- BlackRock's or Vanguard's own control stakes (GIP, HPS) versus index funds: [unknown].
- Private companies and non-US listings: [unknown]. The example is a US-listed parent.
- Refresh and as-of date: [unknown]. Records are "updated when a sale, merger, or ownership change is confirmed" [B-FAQ], which covers ownership changes, not quarterly shareholder changes.
- What the filings say, for comparison: Vanguard's June 2025 Schedule 13G/A on PepsiCo reports 10.04%, sole voting power 0, shared voting power 1,803,072 shares, sole dispositive power 130,698,184 shares, and certifies the shares "were not acquired and are not held for the purpose of or with the effect of changing or influencing the control" of the issuer [SEC-13G].
- Carroll's own claim is stronger than the app's label: grocery mega-corporations "are all majority owned by the world's biggest financial institutions, most notably BlackRock." (2025-07-22) [TT-1]
- Correction to the earlier draft of this note: the website post at /blog/illusion-of-choice is about the cereal aisle and does not mention asset managers [B-CEREAL]. The Medium post on BlackRock and Vanguard [MED] is a different piece and remains unread. Per the search index only, it concedes that the managers hold shares for clients and gives unsourced figures (PepsiCo: Vanguard 9.29%, BlackRock 7.84%).
- Not checked: whether 13%, 11% and 6% match General Mills' 13G filings or proxy table for any date.

## 5. Private equity

- [stated] 2,041 brands "owned by private equity", as of September 2026, unchanged from the 2026-10-31 check [B-HOME][REPO].
- [stated] Definition: the FAQ's only wording is "privately held by an investment group", given as a reason a brand is not independent [B-FAQ]. Whether that covers venture capital, family offices, sovereign funds and minority stakes is [unknown].
- [observed] The cereal post lists "Three Wishes (venture-backed startup)" among "truly independent cereal brands" [B-CEREAL]. That conflicts with the FAQ's definition of independent (founder, family, employee or co-operative control). It is editorial content, so it may not reflect the database.
- [stated] The firm is named in the one example: "Duke's is held by Advent International" [B-HOME].
- Source: [unknown] beyond "public corporate filings and companies' own statements" [B-FAQ]. No deal database, tracker or partner is named or credited on any page read.
- Deal dates, fund names and source links in the app: [unknown].
- New deals and exits: "updated when a sale, merger, or ownership change is confirmed in filings or company announcements" [B-FAQ]. No cadence or detection method is given.
- Context only: Carroll's site lists "private equity operations" among his research topics [IC-SITE].

## 6. Big pharma

- [observed] Not a category on the website. The FAQ and homepage never mention pharma [B-FAQ][B-HOME].
- [observed] Kenvue, the consumer-health company spun off from Johnson & Johnson, appears as an ordinary parent with 17 brands in the "most brands under one roof" list, alongside Nestlé, PepsiCo and Kraft Heinz [B-HOME]. [inference] Consumer-health brands are classed by their current parent like any other brand, probably as megacorp.
- [unknown] Whether the app adds any pharma flag. The only pharma reference by Buy'r is the video "What's The Truth Around Pfizer's Role In American Cheese?" (2026-02-03, not watched) [YT lZ-RmLMIc9E]. Carroll's site lists "pharmaceutical industry influence" among his topics [IC-SITE].
- Spinoffs and divestitures: [unknown] beyond the general update rule in section 9.

## 7. Conglomerates and other owner types

- [stated] Megacorp means "owned by a public conglomerate" [B-FAQ]. Examples carry a ticker: "The Coca-Cola Company NYSE: KO", "General Mills NYSE: GIS" [B-HOME]. [inference] A public listing is what makes a parent a megacorp. No size threshold or list is published.
- [stated] Parents with the most brands: Nestlé 45, PepsiCo 40, Kraft Heinz 28, Campbell Soup 18, Mars 18, Hershey 18, J.M. Smucker 17, Kenvue 17, Procter & Gamble 17, General Mills 12 [B-HOME].
- Grey cases seen on the homepage [B-HOME]:
  - Mars, which is privately held and family-owned, appears in the "most brands under one roof" list and in the line "Pop-Tarts to Mars" next to megacorp examples. Which tier Mars brands get is [unknown]. By the FAQ's definition a family-controlled company would be independent.
  - Retailer brands take the retailer's ownership: "Publix GreenWise employee owned", "Wegmans family owned".
  - Co-operatives count as independent: Organic Valley, and Cabot Creamery under Agri-Mark, Inc.
  - Founder-owned: Chobani. Family-owned: Amy's Kitchen, Goya, Lundberg, Huy Fong. Employee-owned: Bob's Red Mill, King Arthur.
  - Eden Foods is "Private owned" / "privately held", in the 8,022 other-private group.
- [observed] The cereal post lists "Barbara's (now owned by Weetabix, but smaller)" and "Cascadian Farm (actually General Mills - see how tricky this gets?)" among "truly independent cereal brands" [B-CEREAL]. Both conflict with the FAQ's definition.
- Overlap between tiers: a brand has one tier, set by its owner. Shareholders are shown on a separate line (section 4).

## 8. Citations and verification shown to users

- [stated] "Every one checkable in the app" (of four homepage examples) and "A verdict in plain words, and the evidence under it." [B-HOME]
- [stated] "Buy'r is exploring a way for other apps and AI assistants to query verified ownership records with sources attached." [B-FAQ]. [inference] The records carry sources internally. Whether the app shows them is [unknown].
- [stated] "Counts quoted on this site are stamped with the month they were taken." [B-FAQ]. The counts read "as of September 2026" on 2026-11-20.
- [observed] Neither blog post cites a source [B-CEREAL][B-BLUE]. Unsourced claims include the cereal post's market shares (General Mills 31%, Kellogg's 28%, Post 16%, PepsiCo 10%), "over $50 million annually on lobbying" and "Cereal prices have risen 35% in the last decade", and the Blue Wilderness post's lawsuit details, settlement figures and shareholder percentages. Both posts end "Built from filings and company statements."
- [observed] Both posts are dated March 2024 and signed "Buy'r Team" [B-CEREAL][B-BLUE]. The press release says Buy'r was founded in 2025 [PRN], and the sitemap gives every post a lastmod of 2026-01-14 [B-SITEMAP]. [inference] The dates were carried over from Carroll's earlier content or set by hand.
- [observed] The site has no per-brand or per-company pages [B-SITEMAP]. No record can be linked to or checked from outside the app.

## 9. Updates, corrections, disputes and ownership changes

- [stated] "Records are reviewed continuously and updated when a sale, merger, or ownership change is confirmed in filings or company announcements." [B-FAQ]
- [stated] Corrections: "Every record can be reported from inside the app, or you can write to hello@buyrapp.com with the brand and a source. Buy'r only publishes verified corporate structures, and corrections are made against the records, not against pressure from the company involved." [B-FAQ]
- [stated] Coverage outside the US: "Ownership records are deepest for brands sold in the United States and are being expanded to other markets." [B-FAQ]
- [stated] The terms disclaim accuracy: "We do not guarantee the accuracy, completeness, or timeliness of any information" [B-TERMS].
- [observed] App releases: iOS 1.0 (2025-12-08) through 1.0.7 (Mar 11, 2026, "Minor Backend Updates") [IOS]. Play: "Updated on Mar 10, 2026" [PLAY]. Neither app has had a release since.
- [inference] The records live on a server and change without app releases. Evidence: the "Minor Backend Updates" note and the monthly-stamped counts.

## 10. Who is behind it

Only the points that bear on method:

- Seller: Buy'r LLC [IOS][PLAY][B-TERMS]. Terms governed by Texas law [B-TERMS]. Founded in 2025 by Ian Carroll, Kevin Muise and John Akin, "a three-person founding team and fully self-funded" [PRN]. The FAQ: "Buy'r takes no venture capital, runs no advertising, and does no brand deals." [B-FAQ]
- Timeline: beta livestream 2025-06-13 [YT EJp2pDd81c4]; "Over 60,000 people signed up for beta access" [PRN]; Play first release 2025-12-01 per AppGoblin [AG]; iOS 1.0 on 2025-12-08 [IOS]; press release 2026-01-21 [PRN].
- Carroll is the data's origin (section 3) and the spotlights' journalist [B-FAQ]. The press release calls him "a consumer transparency advocate with over 4 million followers" [PRN]. His site lists "BlackRock operations", "private equity operations" and "pharmaceutical industry influence" among his topics [IC-SITE].
- No job listings, GitHub repositories or Product Hunt page for Buy'r were found.

## 11. Figures since 2026-10-31

| Figure | 2026-10-31 [REPO] | 2026-11-20 | Source |
|---|---|---|---|
| Brands | 30,332 | 30,332, "as of September 2026" | [B-HOME][B-FAQ] |
| Companies | Not recorded | 16,875 | [B-FAQ] |
| Products in barcode database | Not recorded | 1.5B+ | [B-HOME][B-FAQ] |
| PE-held brands | 2,041 | 2,041 | [B-HOME] |
| Independent brands | Not recorded | 13,189 (founder 8,783, family 3,707, co-op 571, employee 128) | [B-HOME] |
| Megacorp brands | Not recorded | 7,072 | [B-HOME] |
| Other privately held | Not recorded | 8,022 | [B-HOME] |
| Users | 134,000+ | 134,000+ | [B-HOME] |
| Curated recipes | Not recorded | 9,800 | [B-HOME] |
| App Store rating | 4.8 from 601 | 4.8 from 601 (unchanged) | [IOS] |
| App Store last update | Mar 11 | Version 1.0.7, Mar 11, 2026 (unchanged) | [IOS] |
| Price | $5/mo or $50/yr | Unchanged. Premium adds "full ownership hierarchies" among other features. | [B-FAQ][IOS] |
| Google Play | Not recorded | 4.5 stars, 1.01K reviews, 50K+ downloads, updated Mar 10, 2026 | [PLAY] |
| AppGoblin estimates (third party, not Buy'r's figures) | Not recorded | About 67K Play installs, about 6K monthly active users, under $10K monthly revenue, marked "Declining" | [AG] |
| YouTube | Not recorded | 4.99K subscribers, 52 videos | [YT-CH] |

Self-reported in the 2026-01-21 press release: 50,000 downloads in the first week, 68,000 user signups, "$100K in ARR within 12 days", and a target of "1 million users by summer 2026" [PRN].

## 12. What this means for this project

Compared with an engine that cites a verbatim quote from a stored document for every ownership claim:

Where Buy'r is strong:

- Broad grocery coverage: 30,332 brands and 16,875 companies, with a barcode database it puts at 1.5B+ products.
- A published taxonomy with counts, including a split of independent ownership into founder, family, co-operative and employee.
- Chains walked to the ultimate parent, keeping intermediate brands (Blue Wilderness, via Blue Buffalo, to General Mills).
- A stated correction path that asks the reporter for a source.
- Product data (ingredients, nutrition, recalls, recipes) next to ownership, and a large launch audience.

Where its evidence chain is weak, or can't be seen from outside:

- The method is one sentence. No filing type, vendor or verification process is named.
- No public record shows a source, and its own investigative posts cite none.
- No public per-brand pages, so a claim can't be linked to, checked or quoted without the app.
- Asset-manager percentages carry no as-of date or filing.
- The three-tier view puts private equity in a bar labelled "Family / Private".
- Editorial posts contradict its own definition of independent (Barbara's, Cascadian Farm, Three Wishes).
- Its co-founder says BlackRock "majority owns" grocery companies. The filings say otherwise, for example Vanguard's 10.04% passive 13G/A on PepsiCo [SEC-13G].
- The apps have had no release since March 2026.

Under this project's rules, Buy'r is a lead a person reads, never a source (`.scratch/chains-and-brands/map.md`, Notes).

## 13. Open questions

1. Website pages still unread: /independence, /team, /media, /roadmap, /contact, /donation, /delete-data, and the blog posts on Burt's Bees and Clorox, Topo Chico and Coca-Cola, "who owns your water" and the user spotlight.
2. Visible only in the app:
   - Whether a brand screen shows sources, as-of dates or deal dates.
   - Which shareholders appear, and above what threshold.
   - The tier given to Mars brands and other large family-owned companies.
   - What the free tier shows compared with Premium's "full ownership hierarchies".
   - What "Enhanced Research Toolkit" (release 1.0.3) is.
3. Videos to watch, by a person (transcripts are robots-blocked):
   - "The Spreadsheet That Started It All: Why We Built Buy'r App" (2025-07-18) https://www.youtube.com/watch?v=GSlKBy1NM8E
   - "We answer your FAQ's- Now we're on the same page!" (2025-08-05) https://www.youtube.com/watch?v=LATx-iChNwc
   - "We Launched Publicly, And You Have Questions: Let's Answer Some FAQ's" (2025-12-12) https://www.youtube.com/watch?v=VNCbaYs7o7g
   - "Your Christmas Dinner: Is It Owned By The Big 3?" (2025-12-20) https://www.youtube.com/watch?v=-ZqtCF08Icg
   - "What's The Truth Around Pfizer's Role In American Cheese?" (2026-02-03) https://www.youtube.com/watch?v=lZ-RmLMIc9E
   - "Our First Livestream- Buy'r Beta" (2025-06-13) https://www.youtube.com/watch?v=EJp2pDd81c4
4. The Medium post on BlackRock and Vanguard [MED] (HTTP 403). Its figures are search-index only.
5. Whether the Blue Wilderness percentages (Vanguard 13%, BlackRock 11%, State Street 6%) match General Mills' 13G filings or proxy table, and for which date. A match would point to the source.
6. X posts (robots.txt blocks all crawlers): [X-1] to [X-4], and the @BuyrApp account https://x.com/BuyrApp
7. Not heard: Shawn Johnson Podcast, episode 35, with Ian Carroll discussing Buy'r: https://open.spotify.com/episode/1MsoRzLnlRkOO8Mn1e5Oh0 . Also a 3-minute InfoWars clip on Buy'r's channel: https://www.youtube.com/watch?v=cK6-O33LSA0
8. The Discord server (needs an account): https://discord.com/invite/zuKRpMuUAJ
9. Unverified: every press-release figure (self-reported), AppGoblin's estimates, every [search index] item, Webb's role in the ownership data, and Carroll's 2024 spreadsheets, which were not found.
