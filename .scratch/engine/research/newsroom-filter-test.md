# Research: Would a title-and-opening filter keep the newsroom releases that state ownership?

For engine "Cost cuts before revenue" Q3 · Measured 2026-11-21 (04:29 to 04:50 UTC, a Saturday, so off-peak) · DeepSeek reads $0.24

## Question

Proposed Q3 rule: "On the first crawl, read only releases whose title or opening paragraph names a tracked company or brand, or uses deal words such as acquire, acquisition, sale, sold, merger, investment or portfolio. New releases after that are still read in full as they arrive."

Would this filter keep the releases that state ownership (recall), and what share of releases would it skip (drop rate)? The first crawls are about 45,000 releases (ticket 30's 150 entries × 300), and the cost estimate puts the full range at 45,000 to 150,000.

## Short answer

| | Releases | Fact-yielding | Variant (a): drop rate | (a): recall | Variant (b): drop rate | (b): recall |
|---|---|---|---|---|---|---|
| Step 2, private equity firm newsrooms (Blackstone, TSG Consumer) | 71 | 47 | 35% | 41/47 (87%) | 1% | 46/47 (98%) |
| Step 2, consumer companies with several brands (Serta Simmons Bedding, Pharmavite) | 70 | 47 | 13% | 44/47 (94%) | 7% | 45/47 (96%) |
| Step 2, one brand (Ocean State Job Lot) | 35 | 3 | 69% | 1/3 | 0% | 3/3 |
| Step 2, all | 176 | 97 | 33% | 86/97 (89%) | 3% | 94/97 (97%) |
| Step 1, known ownership-stating releases (biased, see below) | 171 | 171 | n/a | 160/171 (94%) | n/a | 171/171 (100%) |

- Variant (a): the newsroom owner's own name doesn't count as a tracked name. Variant (b): it does.
- Under (b), almost every release names its own newsroom's owner, so the filter skips about 3% of releases. Under (a), it skips a third, and most of what it skips is releases about people, charity and products.
- Counted as distinct ownership pairs rather than releases, (a) keeps 207 of 242 pairs (86%) and (b) keeps 230 of 242 (95%). Many facts sit in the closing "About" paragraph and repeat across releases, so most facts in a skipped release are also found in a kept one.

## Method

### The filter as coded

- **Deal words:** the rule's seven words and their inflections, whole words, any case: acquire, acquires, acquired, acquiring, acquisition(s), sale, sales, sold, merger(s), investment(s), portfolio(s). Words outside the list such as "invests", "buys", "sell", "purchased", "stake" or "merge" don't count. Counting "sales" as a form of "sale" changed no result, because no release was kept by "sales" alone.
- **Tracked names:** every brand and owner named in the chains audit files (`category-audit/`, `follow-up-audits/`, `product-industry-audits/` and their summary files). A script took the bold brand rows, the Brand, Company, Owner, Parent and Holder table columns, and the `- Owner:` style lines, and kept the leading capitalized phrase of each piece. It then dropped dates, filing words ("Form 8-K", "10-K") and single words that are common English words (word frequency 4.0 or more on the Zipf scale, for example "Gap", "Target", "Pilot" and "Mars"), unless the word was in capitals. After reviewing the hits I removed 35 non-entity strings, most of them seen hitting releases, such as "LLC", "NEW YORK", "EDGAR", "Executive Chairman" and law-firm fragments. That left 1,731 names. Matching is case-sensitive, on whole words, and allows a possessive. The list still holds some noise (banks named as 13G holders, such as Goldman Sachs, and a few place names), which can only raise the keep rate.
- **Title:** the release's own title (WordPress title in step 2, the page's `og:title`, `<h1>` or `<title>` in step 1).
- **Opening paragraph:** the first body paragraph of at least 100 characters that ends with a full stop, skipping headings. The full-stop test skips subtitles, which have none. That matters: with subtitles counted as openings, three step 2 results changed.
- **Variant (a):** the owner's own names are removed from the list. In step 2 those are Blackstone and BX; TSG Consumer Partners, TSG Consumer and TSG; Serta Simmons Bedding, Serta Simmons and SSB; Pharmavite; and Ocean State Job Lot, Job Lot and OSJL. The owner's brands still count (Serta, Simmons, Beautyrest and Tuft & Needle at Serta Simmons Bedding; Nature Made, MegaFood and Equelle at Pharmavite), because they are tracked brands. In step 1, names that contain the host's domain label count as the owner's own names, plus the issuer's name for a release copied on a wire or reprint site.
- **Variant (b):** the owner's own names are added to the list.

### Step 1: known positives (no DeepSeek)

- Sources: 166 press-release URLs cited next to an ownership quote anywhere in `.scratch/chains-and-brands/research/` (category audits 49, the private equity consumer scan with its newsroom rebuilds 41, industry screens 38, product-industry audits 21, the pilot 9, follow-up audits 8), and the 44 press releases in the extraction test set (`fetched.json`, stored text). After merging there were 176 candidates.
- Excluded 2: the quoted fact isn't on the linked page (a Phenix Salon Suites quote about 10 Point Capital and a Crash Champions quote about Clearlake, both linked to later releases). Not checked 3: Business Wire and Mortenson Dental Partners answered 403, and a Greater Memphis Chamber reprint answered 404. That leaves 171.
- How each was checked: stored text 44; fetched page 28; the URL slug alone 89 (a slug that already holds a deal word or another tracked name passes, since a slug is made from the title); the slug for (b) and a fetched page for (a) 6 (wire copies whose slug passed only on the issuer's own name, re-checked with that name removed). For 4 more I took the opening from the research quote or the stored text, because the fetched page had no text (KKR's release page), a disclaimer modal (Blackstone's SPANX page), a third-party notice (the FinancialContent copy) or a body outside the page's text blocks (Franchising.com's Primrose page). For every release whose title alone fails variant (a), I read the extracted opening by hand and corrected it where the extraction had picked navigation or a subtitle.

### Step 2: a fresh sample (DeepSeek)

- Five newsrooms named in the chains research, each with a WordPress REST listing, so one request listed 100 items and one more returned the title and body of every sampled release:

| Newsroom | Kind | Releases in the archive | Archive dates | Sampled |
|---|---|---|---|---|
| Blackstone (`/news/press/` items only) | private equity firm | 1,782 | 1998-07 to 2026-11 | 36 |
| TSG Consumer Partners | private equity firm | 101 | 2008-10 to 2026-09 | 35 |
| Serta Simmons Bedding (Serta, Simmons, Beautyrest, Tuft & Needle) | consumer company with several brands | 122 | 2015-01 to 2026-11 | 35 |
| Pharmavite (Nature Made, MegaFood, Equelle, Uqora, Bonafide) | consumer company with several brands | 92 | 2015-03 to 2026-10 | 35 |
| Ocean State Job Lot | brand | 197 | 2023-01 to 2026-11 | 35 |

- Sampling: releases sorted by date and picked at even steps from the oldest to the newest.
- Reads: DeepSeek V4.1 Flash (`deepseek-flash`) on DeepSeek's API with the approved prompt p9. The request was the harness's exactly (`run.py --prompt p9 --no-brand --no-label --schema schema_p9.json --max-tokens 120000`, JSON mode). I ran it from a copy in my scratch directory that adds a spend guard and stops on 401, 402 or a balance error. The document was the release title plus the body text, converted with the harness's text rule. The WordPress body leaves out page navigation, so these reads are shorter than whole-page reads.
- Fact-yielding: the read returned at least one `owned_by`, `acquired_by`, `operated_by` or `licensed_to` claim whose quote string-matches the stored text (whitespace, quote marks and ® normalized). 418 of 435 ownership claims matched; the 17 that didn't were left out. All 176 reads finished with `stop`. I didn't judge whether the matched claims are correct, so a claim counts as DeepSeek stated it.
- Distinct pairs: subject, hop and object with legal suffixes removed, where `owned_by` and `acquired_by` count as one hop.

### Web etiquette

User agent `ownership-research/0.1 (public-data research)`. I read robots.txt before the first request to each of 40 hosts, including redirect targets, followed every redirect by hand so robots.txt was checked on each hop, honored crawl-delay (Leonard Green's 10 seconds, though it was only probed) and left at least 1 second between requests to a host. No disallowed path was requested. Requests: 48 to WordPress REST endpoints (probes, listings and the five content calls) and 44 page requests for step 1 (43 pages plus one redirect hop, within the step's cap of about 60). Refusals: Albertsons Companies answered 403 to its REST probe, so I made no more requests there and used Pharmavite instead. Business Wire and Mortenson Dental Partners answered 403 (Mortenson's robots.txt did too), and I made no further requests to either. No challenge page was met. No request went to WhoIsMyDentist, Private Equity Vet or Reddit.

## Step 1 results: known positives

| Group | Releases | Variant (a) keeps | Variant (b) keeps |
|---|---|---|---|
| All | 171 | 160 (93.6%) | 171 (100%) |
| On the organization's own site | 115 | 112 (97.4%) | 115 |
| Wire, reprint or third-party copy | 48 | 40 (83.3%) | 48 |
| Law firm deal pages | 8 | 8 | 8 |
| From the extraction test set | 44 | 41 (93.2%) | 44 |
| From the research files only | 127 | 119 (93.7%) | 127 |

**These positives are biased toward passing.** Researchers picked them because they state ownership, most are deal announcements, and the tracked-name list was built from the same research, so the subject brand is on the list by construction. Read these numbers as an upper bound for deal announcements, not as the filter's recall on a whole archive.

Under (b), every release names its issuer in the title or opening. Under (a), 11 releases were skipped:

| Release | Where | The ownership fact | Why it fails (a) |
|---|---|---|---|
| ZIPS Car Wash Announces Successful Emergence from Financial Restructuring and Appointment of Industry Leader Pete Nani as Chief Executive Officer | zipscarwash.com | "emerged from its chapter 11 process on April 30, 2025" (the change of ownership in the restructuring) | Only its own name; "emergence" is not a deal word |
| Serta Simmons Bedding Completes Financial Restructuring and Emerges from Chapter 11 | sertasimmons.com | the new board after the lender takeover, "Established private equity investor Mark Genender (Managing Partner, Bristol Growth Capital, LLC)" | The opening names only "SSB", its own abbreviation |
| Franchise Group Successfully Completes Financial Restructuring | PR Newswire | the lender group that took the company, "The ad hoc group of debtor-in-possession and first lien term lenders..." | No deal word; the subtitle names Pet Supplies Plus, but a subtitle isn't the opening paragraph |
| CEC Entertainment Successfully Completes Financial Restructuring | PR Newswire | "Under new ownership, and with the leadership of our new Board" | No deal word or other name in the opening |
| Hair Cuttery Family of Brands Prospers Under New Ownership | PR Newswire | "HC Salon Holdings ... purchased the Hair Cuttery brand through an asset sale in the bankruptcy process" (second paragraph) | "Ownership" and "purchased" are not deal words |
| Eagle Merchant Partners Invests in 19 Auto Collision Centers in Pacific Northwest | PR Newswire | "has invested in Puget Collision" (in the opening paragraph) | "Invests" and "invested" are not deal words |
| Smile Doctors Outpaces First-Half Growth Plan, Nears 600 Locations Nationwide | GlobeNewswire copy | "With the long-term and continued backing of THL Partners and Linden Capital Partners" (body) | Growth news; only its own name |
| ModWash Celebrates Grand Opening in Maumee, OH with Free Washes and Community Fun | EIN Presswire | "Founded by Karen Hutton ... ModWash has grown to more than 123 locations" | Store news; only its own name |
| Eyebuydirect Rebrand Cements New Positioning That Empowers Individuality | PR Newswire | "Eyebuydirect is a subsidiary of EssilorLuxottica" (closing About) | Brand news; only its own name |
| BrightStar Care Names Lori Gustafson as Chief Commercial Officer | PR Newswire | "BrightStar Care is owned by Peak Rock Capital" (closing About) | Appointment; only its own name |
| Savings are Served: Meijer Offering Deep Discounts on Turkeys and Thanksgiving Favorites | newsroom.meijer.com | "Meijer is a privately owned, family-operated retailer" (closing About) | Promotion; only its own name |

Two earlier findings line up with this. The Apollo newsroom rebuild ("pe-consumer-scan" n1) noted that the Diamond Resorts, Outerwall and ClubCorp closing releases carry no deal word in their titles. Here all three pass through their opening paragraphs ("acquired", "merger"). The Bain rebuild (n2) read by hand the 73 private equity titles that had no keyword and found 5 deals among them (Maesa, Rodeo Dental, Penn Foster, Arosa/LivHOME, Virgin). That was a title-only filter, so it isn't the same rule.

## Step 2 results: a fresh sample

### Releases kept and recall, per newsroom

| Newsroom | Releases | Fact-yielding | (a) kept | (a) drop rate | (a) recall | (b) kept | (b) drop rate | (b) recall |
|---|---|---|---|---|---|---|---|---|
| Blackstone | 36 | 22 | 22 | 39% | 19/22 | 35 | 3% | 21/22 |
| TSG Consumer Partners | 35 | 25 | 24 | 31% | 22/25 | 35 | 0% | 25/25 |
| Serta Simmons Bedding | 35 | 29 | 33 | 6% | 28/29 | 33 | 6% | 28/29 |
| Pharmavite | 35 | 18 | 28 | 20% | 16/18 | 32 | 9% | 17/18 |
| Ocean State Job Lot | 35 | 3 | 11 | 69% | 1/3 | 35 | 0% | 3/3 |
| **Private equity firms** | 71 | 47 | 46 | 35% | 41/47 (87%) | 70 | 1% | 46/47 (98%) |
| **Consumer companies** | 70 | 47 | 61 | 13% | 44/47 (94%) | 65 | 7% | 45/47 (96%) |
| **Brand** | 35 | 3 | 11 | 69% | 1/3 | 35 | 0% | 3/3 |
| **All** | 176 | 97 | 118 | 33% | 86/97 (89%) | 170 | 3% | 94/97 (97%) |

Counting only claims where the subject or object is a tracked name gives nearly the same figures: (a) 84 of 95 and (b) 92 of 95.

### Distinct ownership pairs kept

| Newsroom | Pairs in the sample | (a) found in a kept release | (b) found in a kept release |
|---|---|---|---|
| Blackstone | 105 | 88 | 94 |
| TSG Consumer Partners | 95 | 80 | 95 |
| Serta Simmons Bedding | 25 | 24 | 24 |
| Pharmavite | 14 | 14 | 14 |
| Ocean State Job Lot | 3 | 1 | 3 |
| All | 242 | 207 (86%) | 230 (95%) |

Pairs lost under (a): 11 Hilton hotel brands owned by Hilton Worldwide and Hilton Worldwide owned by Blackstone; GSO Capital Partners owned by Blackstone; 4 Vitus Group pairs and Morley Fund Management owned by Aviva; 15 TSG holdings named in promotion releases (Pathway Vet Alliance, Pabst, SweetWater, Revolve, Radio Systems, Smashbox, e.l.f., Alexis Bittar, Paige Denim, Yard House, Duckhorn, Dutch Bros, and financings in Robinhood, Revolut and Scopely); CB2 owned by Crate & Barrel; and the Perlman family as owners of Ocean State Job Lot. Pairs lost under (b): the 12 Hilton pairs and CB2.

### Every missed release

Variant (a) skipped 11 fact-yielding releases. The 3 marked (b) were also skipped under variant (b).

| Newsroom, date | Title | Ownership facts DeepSeek found | Where the fact sits |
|---|---|---|---|
| Blackstone, 2019-06-14 | GSO Capital Partners' Second Energy Select Opportunities Fund Strategy Closes on $4.5 Billion in LP Commitments | GSO Capital Partners owned by Blackstone ("GSO Capital Partners, Blackstone's (NYSE: BX) credit platform") | Opening paragraph, but only Blackstone's own name |
| Blackstone, 2010-04-08 (b) | Hilton Worldwide Completes Restructuring of Existing Debt | Hilton Worldwide owned by Blackstone; Waldorf Astoria, Conrad, Hilton, DoubleTree, Embassy Suites, Hilton Garden Inn, Hampton, Homewood Suites, Home2 Suites and Hilton Grand Vacations owned by Hilton Worldwide | Body and closing About |
| Blackstone, 2007-03-12 | Blackstone Real Estate Partners Broadens Investor Base for Vitus Group | Vitus Group owned by Blackstone Real Estate Partners and acquired by a consortium (Morley Fund Management, Round Hill Capital); Morley owned by Aviva | Opening paragraph: "is to sell its majority shareholding" ("sell" isn't a deal word) |
| TSG Consumer Partners, 2025-04-14 | TSG Consumer Appoints Sean Sullivan as Managing Director and Chief Legal Officer | The Duckhorn Portfolio and Dutch Bros Coffee (former partner companies) owned by TSG | Body (biography) |
| TSG Consumer Partners, 2021-01-04 | TSG Consumer Partners Announces Promotions | Pathway Vet Alliance, ATI, Pabst, SweetWater, Revolve, Radio Systems and Privé Revaux owned by TSG; later-stage financings in Robinhood, Revolut and Scopely | Body (year in review) |
| TSG Consumer Partners, 2013-12-05 | TSG Promotes Baxter Moser To Partner; Costello To Principal | Smashbox, Alexis Bittar, Paige Denim, e.l.f., Yard House and Radio Systems (PetSafe) owned by TSG | Body (biographies) |
| Serta Simmons Bedding, 2018-06-28 (b) | Tomorrow Sleep Partners with CB2 for First Brick-and-Mortar Experience | Tomorrow Sleep owned by Serta Simmons Bedding; CB2 owned by Crate & Barrel | Body |
| Pharmavite, 2022-03-08 (b) | Study finds Omega-3 Fatty Acids Associated with Healthy Sleep Duration | Pharmavite owned by Otsuka; Nature Made, Equelle, MegaFood and Uqora owned by Pharmavite | Body and closing About |
| Pharmavite, 2019-10-21 | Pharmavite Appoints Rhonda Hoffman Chief Marketing Officer | Pharmavite owned by Otsuka; Nature Made, Equelle, MegaFood and Innate Response owned by Pharmavite | Closing About |
| Ocean State Job Lot, 2025-10-23 | Ocean State Job Lot Charitable Foundation and the United Cajun Navy Partner to Deliver More Than 91,000 Pounds of Organic Pasta to Military Families in Need | Ocean State Job Lot owned by Alan Perlman ("Alan Perlman, Owner and Co-Founder") | Body (quote attribution) |
| Ocean State Job Lot, 2025-02-13 | Ocean State Job Lot Launches 'Feed for Free' Program to Combat Food Insecurity in Rhode Island | Ocean State Job Lot owned by Marc Perlman ("Marc Perlman, Principal Owner and CEO") | Body (quote attribution) |

### Other observations

- 37 of the 97 fact-yielding releases hold ownership facts only in the closing "About" paragraph: 23 of 29 at Serta Simmons Bedding and 14 of 18 at Pharmavite. The same paragraph repeats in many releases, which is why the pair-level recall is higher than the release-level recall for consumer companies.
- Under (a), 63 of the 118 kept releases were kept by a tracked name alone, with no deal word, and 39 of those yielded a fact. 31 were kept only because of the opening paragraph (the title alone would fail), and 17 of those yielded a fact.
- Of the releases (a) keeps, 86 of 118 (73%) yield a fact. Of those it skips, 11 of 58 (19%) do.
- Cost per read in this sample: $0.00136 on average ($0.00185 at Blackstone, $0.00038 at Ocean State Job Lot), against the cost estimate's $0.003 per page. These were body-only reads, so whole pages with navigation would cost more.

## DeepSeek spend

- 176 reads, all off-peak (Saturday). Spend from the usage figures at off-peak prices ($0.003 per million cache-hit input tokens, $0.15 per million cache-miss input tokens and $0.60 per million output tokens): **$0.239**. Output tokens, mostly reasoning, made up most of it: one Blackstone release used 17,800 output tokens (15,900 of them reasoning) and cost $0.011.
- Balance: **$3.51** before my first call (04:38 UTC) and **$3.25** right after my last call (04:46 UTC). It read **$2.99** at 04:50 UTC, after my last call, while another agent's test ran on the same account. The balance drop therefore isn't mine alone.
- No 401, 402 or balance error came back, and the spend guard (cap $0.75) never fired.

## What this means for Q3

- **Variant (b), where the newsroom owner's own name counts, saves almost nothing.** It skipped 3% of sampled releases: 1% at the firms, 0% at the brand and 7% at the consumer companies. On the cost estimate's $135 to $660 for first crawls, 3% is about $4 to $20. Its recall was 97% of fact-yielding releases and 95% of distinct pairs. The 3 releases it missed name neither a tracked name nor a deal word up front: Hilton's debt release, a Pharmavite study release and a Tomorrow Sleep retail partnership.
- **Variant (a), where the owner's own name doesn't count, skips about a third.** It skipped 35% at the firms, 13% at the consumer companies and 69% at the brand, and kept 89% of fact-yielding releases and 86% of distinct pairs. Applied to the cost estimate's range, a one-third cut is about $45 to $220. The real share depends on the mix, since brand newsrooms skip far more than consumer-company newsrooms. The cost estimate's upper end, 500 newsrooms, comes from counting each listed brand's own newsroom.
- **What variant (a) misses** is mostly releases about people, charity, products and debt, whose ownership facts sit in the body or the closing About paragraph: TSG's promotion releases listing portfolio companies, Pharmavite's Otsuka line, and the owner family named as speakers at Ocean State Job Lot. It also misses deals worded with verbs not on the list ("is to sell", "invests", "purchased") and restructurings that change the owner without a deal word ("emerges from Chapter 11", "under new ownership"). At the one brand newsroom, it kept only 1 of the 3 fact-yielding releases, and both misses were the owner family's statements.
- **Consumer-company newsrooms barely shrink under either variant**, because almost every release names one of the company's tracked brands.
- **The known-positive set (step 1)** passes 94% under (a) and 100% under (b). It is biased toward deal announcements, which the filter is built to catch.
- The rule leaves new releases as full reads, so the filter affects only the archive backlog on the first crawl.
- **Limits:**
  - The sample is small: 176 releases, 97 of them fact-yielding, and the brand row rests on 3 positives from one newsroom.
  - All five newsrooms run on WordPress.
  - The tracked names come from the research files, not the engine's tracked-entity list, and include some noise.
  - Titles and openings were found by heuristics and corrected by hand only for releases whose title fails.
  - DeepSeek's claims were string-matched but not judged for correctness.

## Addendum: other filters, tested offline (main session, 2026-11-20)

The step 2 releases and their DeepSeek facts were re-scored with other filters, at no cost. Recall here counts distinct ownership pairs (subject and owner), since About paragraphs repeat the same pair across many releases. This re-implementation of variant (a) differs slightly from the agent's (its name matching is simpler), so compare rows with each other rather than with the tables above.

| Filter | Releases skipped | Ownership pairs kept |
|---|---|---|
| (a) title and opening, Q3's words, names other than the newsroom's own | 25% | 231/263 (88%) |
| (c) as (a), plus the closing About paragraph and more verbs (sell, purchased, invests, owned, ownership, stake, majority, restructuring, recapitalization, subsidiary, backed, affiliate) | 6% | 255/263 (97%) |
| (f) every release from the last 2 years, older ones by (c)'s words or names in title and opening | 14% | 251/263 (95%) |
| (g) as (f) with the last 1 year | 18% | 247/263 (94%) |
| (h) every release from the last 2 years, older ones only by Q3's words in the title | 62% | 138/263 (52%) |

- Adding the About paragraph restores recall but keeps almost every release, because most About paragraphs state ownership. No filter tried here skips much while keeping 95% or more of the pairs.
- Measured price: the 176 releases cost $0.239 off-peak, $0.00136 each, well under the $0.003 to $0.0044 per page the cost estimate used. At that price a full first crawl of 45,000 to 150,000 releases costs about $61 to $204, so a filter that skips a quarter would save about $15 to $50.

## Files

Scripts, downloads, DeepSeek outputs and per-release results are in the session scratchpad (temporary): `/tmp/claude-1000/-home-iherr-projects-enshittified-demystified/41582336-4e56-49b0-ae4f-e725e9681e76/scratchpad/`. The tracked-name list is `work/tracked.json`, step 1 results are `work/step1_results.json` and `work/step1_issuer.json`, and step 2 results are `work/scored2b.json`.
