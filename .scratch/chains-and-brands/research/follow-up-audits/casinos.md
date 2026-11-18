# Follow-up audit: casinos (every US casino brand)

Ticket: [93 Research: Follow-up audits of four industries](../../issues/93-research-follow-up-audits-four-industries.md), item 4 · Worker report, 2026-11-18 (fetches logged 00:00–00:17 UTC). Saved pages are in the session scratchpad (temporary): `pages/fu-casinos/` (NNN.html raw, NNN.txt visible text, `index.tsv`, `robots.tsv`, `robots/`). Scripts are in `scripts/fu-casinos/` (`robots.py`, `get.py`, `qcheck.py`, `quotes.tsv`, `neg.tsv`, `wiki_rows.tsv`). Pages reused from the earlier screen are in `pages/screen2-b/` (cited as "s2/NNN").

## Short answer

| | Casinos (every name used at 2+ open US casinos; N = 64 brand rows) |
|---|---|
| PE-owned plus PE minority stake, by brand row | **2 / 64 (3.1%)**: Bally's and Queen (The Queen Baton Rouge, Casino Queen Marquette, DraftKings at Casino Queen). Both names belong to Bally's Corporation, which Standard General controls (66.8% in the 2026 proxy; ADV `Any PE Funds = Y`, 5 PE funds). Both are PE-owned; no PE minority stake was found. |
| Brands found | **64**: 35 commercial and 29 tribal. 55 have an owner or operator source: a filing or the operator's own site. 9 rest only on the lead list, because the operator page was blocked, failed or not fetched. |
| Owner not found | **9 / 64**: Kewadin, Comanche, Gold Ranch, 12 Tribes, Grand Casino (Mille Lacs), Emerald Queen, Kickapoo, Lakeside Entertainment, Parx. Another **18** rows name the owning company or tribal enterprise but not its owners. **1** (Circus Circus) is used by two operators, so its owner is not settled. None of the 28 has any PE lead. |
| Against the bar | **Under 10% on every count tried** except the earlier screen's operator rows (1 of 10). Commercial names only: 2 / 35 (5.7%). Names whose count comes from an SEC filing: 2 / 23 (8.7%). By location: 16 of about 290 locations (5.5%; noted, not decisive). |

- **Biggest finding:** under the glossary's brand rule, casinos fall well below the bar. Brand rows are dominated by large public operators (Caesars, PENN, MGM, Boyd, Red Rock, Wynn, Century), families (Fertitta's Golden Nugget, Cordish's Live!, Bluhm's Rivers, Jacobs, Herbst) and tribes (29 rows, among them Hard Rock). The only PE owner of a casino name is Standard General through Bally's.
- **PE runs single casinos, not names.** Clairvest (PE) bought MGM Northfield Park's operations in April 2026 and the casino is now "Northfield Park Racino", a location rather than a brand. Apollo's Venetian operator licenses the name from Las Vegas Sands, and the Venetian is one US location. Clairvest's other US gaming holdings are single sites (Delaware Park, The Nash Casino) or a historical-racing operator (Wyoming Downs).
- **The earlier screen's 10% came from the row rule.** With operators as rows, Bally's was 1 of 10. With names as rows, each big operator becomes 4 to 8 rows (Caesars 7, PENN 5, Boyd 3 plus a licensed share of Ameristar) and every multi-site tribe is a row. That swamps Bally's 2 rows.

## How this was sourced

- **The list of names** comes from three kinds of source, none of which knows anything about ownership:
  - **Operators' own property lists:** 10-Ks for Caesars, MGM, PENN, Boyd, Red Rock (Station), Churchill Downs, Century, Wynn and Golden (FY2025); 10-Qs for Q3 2026 (Caesars, MGM, Bally's); Bally's FY2025 10-K (s2/062).
  - **Operators' own sites** for non-SEC brands: Cordish, Rush Street, Wind Creek, Mohegan, JACK, Jacobs, Wild Rose, Genting, Landry's, Terrible Herbst, Saratoga, Peppermill, Hard Rock/Seminole, and 21 tribal casino sites.
  - **A lead list:** Wikipedia's "List of casinos in the United States" ([page](https://en.wikipedia.org/wiki/List_of_casinos_in_the_United_States), 962 rows parsed). Names were grouped by stem to find every name repeated at 2+ open casinos. Wikipedia was used only to find candidates, and as the count source for 13 rows where no operator count was available (flagged "lead"). It was never used for ownership.
  - State regulators' licensee lists and the AGA were not used. One property list per operator covered the commercial names, and the budget went to the tribal names instead.
- **Counts** come from the operator's own filing or site wherever one was read. Closed and planned casinos are not counted. Each row says where its count came from.
- **Ownership facts** come from SEC filings (10-K, 10-Q, DEF 14A, DEFM14A, Schedules 13D and 13G), operators' own sites (about pages, footers, copyright lines), a sponsor portfolio page (Clairvest) and Form ADV. No trade press was cited.
- **SEC access:** 22 requests to www.sec.gov, all HTTP 200, paced at one every 1.2 s or slower. The SEC submissions JSON fetched by the screen worker earlier in this session (s2/006 to s2/016) was reused to find filings, not refetched.
- **Robots:**
  - robots.txt was read by `robots.py` in a separate, earlier command before the first request to each host. `get.py` refuses any host whose robots record is missing or was written in the same command.
  - No redirect was followed automatically. On a cross-host redirect (fourwindscasino.com, potawatomi.com, warhorsecasino.com, plus five robots.txt redirects), the new host's robots.txt was read first, in its own command.
  - Rules for `*`, `EvidenceEngine`, ClaudeBot, Claude-User, Claude-SearchBot and anthropic-ai were checked. Crawl delays were obeyed: 10 s on mohegangaming.com, jackentertainment.com, circuscircus.com, luckystarcasino.org, everythingtulalip.com and warhorsecasino.com; 5 s on potawatomi.com; 3 s on terribles.com.
  - **rwlasvegas.com disallows ClaudeBot site-wide**, so it was not fetched. Resorts World's facts come from Genting Berhad's own site.
  - rushstreetgaming.com names Claude agents in a group with path-only rules, which allow the pages used. grandcasinomn.com explicitly allows ClaudeBot. Content-Signal lines (rwlasvegas.com) were treated as content.
- **Blocked or failed (none retried):**
  - goldennugget.com: page returned 403. Golden Nugget's ownership comes from Landry's and an SEC proxy; its count comes from the lead list.
  - kewadin.com: robots.txt returned 403 (no restrictions) and the page returned 403.
  - comanchenationcasinos.com: TLS error on robots.txt, so treated as blocked.
  - goldranchcasino.com: unreachable, so treated as blocked.
  - semtribe.com: robots.txt redirected to a 404 page, so it was not fetched. The Seminole facts come from Hard Rock's casino hub.
  - emeraldqueen.com: robots.txt redirected to `/robots.txt/`, so it was not fetched.
  - peppermillcasinos.com: the homepage redirected to a domain-parking site, which was not followed. The Peppermill facts come from peppermillreno.com.
  - parxcasino.com: returned a 212-byte page with no text.
  - grandcasinomn.com: the page renders by script (27 characters of text).
  - No permission-check refusals, no 429, no challenge pages, no Playwright.
- **Never fetched:** competitor sites, Reddit, WhoIsMyDentist, Private Equity Vet, PitchBook, Preqin, CB Insights. Four WebSearch calls were used only to find official domains (Saratoga Black Hawk, Muscogee Nation casinos, Agua Caliente, plus loading the tool).
- **Owner kinds are research notes, not engine classifications.** "Family", "tribal" and "public company" follow the counting rules. "Named, owners not stated" means a primary source names the company or tribal enterprise behind the name but not who owns it.

## The brand rule as applied

- **A row is a distinctive name used at two or more open US casinos,** whatever its suffix:
  - Harrah's X and Harrah's Resort X are one row.
  - Hollywood Casino X and Hollywood Gaming at X are one row.
  - Caesars Palace and Caesars X are one row.
  - MGM Grand X, MGM X and Park MGM are one row.
  - Station's Boulder, Palace, Sunset and Santa Fe Station are one row.
  - The Queen Baton Rouge and Casino Queen are one row.
- **Single-property names are locations,** not rows: Bellagio, Borgata, Flamingo, Paris, Planet Hollywood, The Venetian, Fontainebleau, Foxwoods, WinStar, Northfield Park Racino and so on. Wynn has one US location (Wynn Las Vegas), so it is not a row. Encore has two (Encore at Wynn Las Vegas and Encore Boston Harbor), so it is.
- **Names at licensed or managed locations count toward the name's owner.**
  - Harrah's at five tribal casinos and Caesars Southern Indiana count toward Caesars' rows.
  - Hard Rock Biloxi (Bally's) and Hard Rock Tulsa count toward Hard Rock.
  - Ameristar's two Boyd casinos count toward PENN's trademark.
  - Sam's Town Shreveport (Bally's since August 2026) counts toward Boyd's name.
- **Same words, unrelated owners, are separate names,** each usually at one site and so not a row: Treasure Island (Las Vegas and Minnesota), Thunderbird, Sac and Fox, Lucky Eagle. Two names with one operator source but two different operators are kept as one row and flagged: Circus Circus (Caesars in Reno, another operator in Las Vegas), and Boomtown (PENN's three, plus Boomtown Reno per the lead list, not counted).
- **Out of scope, listed under open questions:**
  - gaming taverns (Golden's 72 taverns; Station's Seventy Six);
  - historical-racing halls (Churchill Downs' Rosie's and Derby City Gaming; Clairvest's Wyoming Downs);
  - truck-stop video-poker casinos (Jacobs' Cash Magic);
  - card rooms (bestbet);
  - umbrella groups whose name doesn't appear on each location: Muscogee Nation Gaming Enterprises' 11 casinos with local names, on the site creeknationcasinos.com ("With 11 locations across eastern Oklahoma, Muscogee Nation Gaming Enterprises is proud to be Oklahoma’s favorite place to play.").
- **Building owners are never brand owners.** VICI and GLPI own many of these buildings, and a REIT is not counted.

## Rows

Ordered by US locations. Sources: "10-K", "10-Q" and "site" are the operator's own; "lead" is the Wikipedia list. Bally's location count is by property; its Black Hawk property is three casinos.

| # | Brand (US locations; count source) | Owner of the name (as stated) | Owner type | Locations run by others (license or management) | PE status | Ev. |
|---|---|---|---|---|---|---|
| 1 | Hollywood Casino / Hollywood Gaming (19; PENN 10-K) | PENN Entertainment, Inc. (NASDAQ: PENN) | public company | none | none (BlackRock 14.1%, (b)) | CA1 |
| 2 | Harrah's (18; Caesars 10-K: 13 owned or leased, 4 managed, 1 branded) | Caesars Entertainment, Inc. (NASDAQ: CZR); take-private by Fertitta pending | public company (pending: family) | 5 tribal casinos managed or branded (Ak-Chin, Cherokee, Cherokee Valley River, Resort Southern California, Northern California) | none | CA2 |
| 3 | **Bally's** (13 properties, 15 casinos; Bally's 10-Q) | Bally's Corporation (NYSE: BALY); Standard General 66.8% | **PE-controlled public company** | none | **PE-owned** | CA3 |
| 4 | Hard Rock (13 open; Hard Rock casino hub) | Seminole Tribe of Florida (Hard Rock International) | tribal | most US sites run by licensees or partners (Biloxi: Bally's; Tulsa: Cherokee Nation; others not checked) | none | CA4 |
| 5 | Horseshoe (10; Caesars 10-K) | Caesars Entertainment, Inc. | public company | none | none | CA2 |
| 6 | Cherokee Casino (9; site) | Cherokee Nation Entertainment, LLC | tribal (named enterprise; owners not stated) | none | none | CA5 |
| 7 | Choctaw Casino (8; site) | Choctaw Casinos & Resorts (site's About text introduces the Choctaw Nation of Oklahoma) | tribal (implied, not stated as ownership) | none | none | CA6 |
| 8 | Wildfire (8: 7 owned, 1 half-owned; Red Rock 10-K) | Red Rock Resorts, Inc. (NASDAQ: RRR) via Station Casinos LLC; Fertitta family entities over 50% of votes | family-controlled public company | none | none | CA7 |
| 9 | Golden Nugget (7; lead) | Landry's, Inc. (lists the brand); Landry's Fertitta, LLC is a subsidiary of Fertitta Entertainment | family | Danville and Cripple Creek appear to be licensees (lead only) | none | CA8 |
| 10 | Osage Casino (7; site) | Osage Casinos (named; owners not stated) | tribal (by name) | none | none | CA9 |
| 11 | Lucky Star (7 incl. 2 travel centers; site) | Lucky Star Casino; footer links "The Cheyenne and Arapaho Tribes" | tribal (link, not a statement) | none | none | CA10 |
| 12 | Ho-Chunk Gaming (7; site) | Ho-Chunk Nation | tribal | none | none | CA11 |
| 13 | Ameristar (6: 4 PENN, 2 Boyd; 10-Ks) | PENN Entertainment (registered trademark) | public company | Boyd runs Ameristar Kansas City and St. Charles (license not stated in either 10-K) | none | CA12 |
| 14 | Caesars (6; Caesars 10-K) | Caesars Entertainment, Inc. | public company | Caesars Southern Indiana is "Branded" (owner not read) | none | CA2 |
| 15 | Seneca (6; site) | Seneca Resorts & Casinos; footer links the Seneca Nation | tribal (link, not a statement) | none | none | CA13 |
| 16 | Terrible's (6 casino towns; site; not every casino carries the name) | Terrible Herbst, Inc. | named, owners not stated | none | none | CA14 |
| 17 | Live! (5; Cordish site) | The Cordish Companies | family | none | none | CA15 |
| 18 | Rivers (5; Rush Street site) | Rush Street Gaming (Neil Bluhm, chairman and founder) | named, owners not stated | Rivers Des Plaines is 61.3% Churchill Downs | none | CA16 |
| 19 | Wind Creek (5 US; site) | Wind Creek Hospitality, the Poarch Band of Creek Indians' gaming entity | tribal | none | none | CA17 |
| 20 | Desert Diamond (5; site) | an enterprise of the Tohono O'odham Nation | tribal | none | none | CA18 |
| 21 | MGM (5; MGM 10-K and 10-Q) | MGM Resorts International (NYSE: MGM) | public company (IAC 13D; IAC is public) | none (Northfield Park sold April 2026 and renamed) | none | CA19 |
| 22 | Kewadin (5; lead) | not found (site 403) | not found | — | not found | CA20 |
| 23 | Oneida Casino (5; lead) | Oneida Casino Hotel; site links "ONEIDA NATION" | tribal (link) | none | none | CA21 |
| 24 | Station (4; Red Rock 10-K) | Red Rock Resorts, Inc. | family-controlled public company | none | none | CA7 |
| 25 | Isle / Isle of Capri (4; Caesars 10-K) | Caesars Entertainment, Inc. | public company | none | none | CA2 |
| 26 | Century Casino (4; Century 10-K) | Century Casinos, Inc. (NASDAQ: CNTY) | public company | none | none | CA22 |
| 27 | Four Winds (4; site) | Pokagon Band of Potawatomi Indians | tribal | none | none | CA23 |
| 28 | Seminole Casino (4; Seminole hub, HTML attributes) | Seminole Tribe of Florida | tribal | none | none | CA4 |
| 29 | Comanche (4; lead) | not found (TLS error) | not found | — | not found | CA20 |
| 30 | Boomtown (3; PENN 10-K) | PENN Entertainment (registered trademark) | public company | Boomtown Reno (lead) is another operator's; not counted | none | CA1 |
| 31 | **Queen** (3; Bally's 10-Q) | Bally's Corporation (from its 2025 Queen merger) | **PE-controlled public company** | DraftKings holds naming rights at the East St. Louis site | **PE-owned** | CA3 |
| 32 | Resorts World (3; Genting site) | Genting Berhad (Las Vegas); Genting Malaysia Berhad (New York City, Catskills) | public company (Bursa Malaysia) | none | none | CA24 |
| 33 | Gold Dust West (3; Jacobs site) | Jacobs Entertainment, Inc. | named, owners not stated | none | none | CA25 |
| 34 | Wild Rose (3; site) | Wild Rose Casino & Resort | named, owners not stated | none | none | CA26 |
| 35 | Agua Caliente (3; site) | Agua Caliente Band of Cahuilla Indians | tribal | none | none | CA27 |
| 36 | Seven Clans (3; lead; the site names Thief River Falls) | operated by the Red Lake Band of Chippewa Indians | tribal | none | none | CA28 |
| 37 | St. Croix Casino (3; site) | St. Croix Casino | named, owners not stated | none | none | CA29 |
| 38 | WarHorse (3; site) | WarHorse Gaming LLC | named, owners not stated | none | none | CA30 |
| 39 | Gold Ranch (3; lead) | not found (host unreachable) | not found | — | not found | CA20 |
| 40 | 12 Tribes (3; lead) | not found (not fetched) | not found | — | not found | CA20 |
| 41 | Argosy (2; PENN 10-K) | PENN Entertainment | public company | none | none | CA1 |
| 42 | L'Auberge (2; PENN 10-K) | PENN Entertainment | public company | none | none | CA1 |
| 43 | Eldorado (2; Caesars 10-K) | Caesars Entertainment | public company | none | none | CA2 |
| 44 | Tropicana (2, plus "Trop Casino Greenville"; Caesars 10-K) | Caesars Entertainment | public company | none | none | CA2 |
| 45 | Diamond Jo (2; Boyd 10-K) | Boyd Gaming Corp. (NYSE: BYD) | public company (family-led) | none | none | CA31 |
| 46 | Belterra (2; Boyd 10-K) | Boyd Gaming Corp. | public company | none | none | CA31 |
| 47 | Sam's Town (2; Boyd 10-K, Bally's 10-Q) | Boyd Gaming Corp. (Bally's bought Shreveport without the name) | public company | Bally's runs Sam's Town Shreveport | none (name is Boyd's) | CA31 |
| 48 | Encore (2; Wynn 10-K) | Wynn Resorts, Limited (NASDAQ: WYNN) | public company | none | none | CA32 |
| 49 | Arizona Charlie's (2; Golden 10-K) | Golden's operating business, now owned by Blake Sartini (Argento) | family | none | none | CA33 |
| 50 | Circus Circus (2; Caesars 10-K, Circus Circus site) | not settled: Caesars lists the trademark (Reno); the Las Vegas site names no owner | not settled (no PE either way) | two operators | none found | CA34 |
| 51 | JACK (2; site) | JACK Entertainment LLC (owns the trademarks) | named, owners not stated | none | none | CA35 |
| 52 | Parx (2; lead) | not found (page empty) | not found | — | not found | CA20 |
| 53 | Saratoga Casino (2; two sites) | not stated (sites name only themselves) | named, owners not stated | none | none | CA36 |
| 54 | Peppermill (2; lead) | Peppermill Resort Spa Casino | named, owners not stated | none | none | CA37 |
| 55 | Mohegan (2 US; Mohegan site) | governed by the Mohegan Tribe | tribal | none | none | CA38 |
| 56 | Odawa (2; site) | Little Traverse Bay Bands of Odawa Indians | tribal | none | none | CA39 |
| 57 | Ojibwa (2; site) | not named (site names only itself) | named, owners not stated | none | none | CA40 |
| 58 | Potawatomi (2; site) | Forest County Potawatomi Community | tribal | none | none | CA41 |
| 59 | Three Rivers (2; site) | Three Rivers Casino Resort | named, owners not stated | none | none | CA42 |
| 60 | Tulalip (2; site: Resort Casino, Bingo & Slots) | not named on the page | named, owners not stated | none | none | CA43 |
| 61 | Grand Casino (Mille Lacs) (2; lead) | not found (page renders by script) | not found | — | not found | CA20 |
| 62 | Emerald Queen (2; lead) | not found (robots redirect, not fetched) | not found | — | not found | CA20 |
| 63 | Kickapoo Casino (Oklahoma) (2; lead) | not found (not fetched) | not found | — | not found | CA20 |
| 64 | Lakeside Entertainment (Cayuga) (2; lead) | not found (not fetched) | not found | — | not found | CA20 |

**PE share by brand row:** 2 of 64 (3.1%), both PE-owned (Bally's, Queen). Owner not found: 9. Named but owners not stated: 18 (rows 6, 7, 10, 11, 15, 16, 18, 23, 33, 34, 37, 38, 51, 53, 54, 57, 59, 60). Not settled: 1 (Circus Circus).

## Evidence per row

- **CA1 PENN (Hollywood, Ameristar's PENN sites, Boomtown, Argosy, L'Auberge).** [PENN 10-K FY2025](https://www.sec.gov/Archives/edgar/data/921738/000092173826000008/penn-20251231.htm):
  - Count: "As of December 31, 2025, we owned, managed, or had ownership interests in 42 gaming and racing properties in 19 states."
  - Trademarks: "including but not limited to, “Ameristar®,” “Argosy®,” “Boomtown®,” “Hollywood Casino®,” “Hollywood Gaming®,” “L’Auberge®,” “M Resort®,” “PENN Entertainment®,” and “PENN Play®.”"
  - Item 2 lists 17 Hollywood Casino and 2 Hollywood Gaming properties, 4 Ameristar, 3 Boomtown, 2 Argosy and 2 L'Auberge.
  - Holders: BlackRock 14.1% ([13G/A, 2026-07-29](https://www.sec.gov/Archives/edgar/data/921738/000201238326002927/xslSCHEDULE_13G_X02/primary_doc.xml), Rule 13d-1(b) box checked); AQR 1.09% ([13G/A, 2026-11-13](https://www.sec.gov/Archives/edgar/data/921738/000116755726000251/xslSCHEDULE_13G_X02/primary_doc.xml), (b)). The screen's [2026 proxy](https://www.sec.gov/Archives/edgar/data/921738/000114036126016846/ny20062568x1_def14a.htm) lists only BlackRock and Vanguard at 5%+.
  - Not PE.
- **CA2 Caesars (Harrah's, Horseshoe, Caesars, Isle, Eldorado, Tropicana).**
  - [Caesars 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1590895/000159089526000011/czr-20251231.htm):
    - Count: "As of December 31, 2025, we own, lease or manage an aggregate of 52 domestic properties in 18 states."
    - Licensed sites: "In addition, we have other properties in North America that are authorized to use the brands and marks of Caesars Entertainment, Inc."
    - Trademarks: "We own or have the right to use proprietary rights to a number of trademarks that we consider, along with the associated name recognition, to be valuable to our business, including Eldorado, Silver Legacy, Isle, Lady Luck, Tropicana, Circus Circus, Caesars, Flamingo, Harrah’s, Horseshoe, Paris, Planet Hollywood, Caesars Rewards, Caesars Sportsbook, and William Hill."
    - Item 2, by name: Harrah's 13 owned or leased plus 4 "Managed" plus 1 "Branded" (Harrah's Northern California); Horseshoe 10; Caesars 5 plus Caesars Southern Indiana ("Branded"); Isle and Isle of Capri 4; Eldorado 2; Tropicana 2 plus Trop Casino Greenville.
  - Pending take-private, per the [10-Q for Q3 2026](https://www.sec.gov/Archives/edgar/data/1590895/000159089526000033/czr-20260930.htm): "Each of the Company and Fertitta Gaming’s obligation to consummate the Merger remains subject to the satisfaction or waiver of certain conditions, including, among others, the expiration or termination of any applicable waiting period under the HSR Act and the receipt of certain gaming regulatory approvals." The 8-Ks since then carry items 5.07 (vote) and 2.02 only, with no closing.
  - Holders: Pentwater 4.6% ([13G/A, 2026-11-16](https://www.sec.gov/Archives/edgar/data/1590895/000091957426008133/xslSCHEDULE_13G_X02/primary_doc.xml), (b), ADV N); Capital World 0.0% ([13G/A, 2026-08-12](https://www.sec.gov/Archives/edgar/data/1590895/000142284926000121/xslSCHEDULE_13G_X02/primary_doc.xml)).
  - Not PE. When the deal closes, Fertitta is family, so still not PE.
- **CA3 Bally's and Queen (PE-owned).**
  - Control:
    - [Bally's proxy 2026](https://www.sec.gov/Archives/edgar/data/1747079/000174707926000028/baly-20260409.htm) (s2/007): "As of the record date, entities affiliated with Standard General L.P. (“Standard General”) beneficially owned an aggregate of 66.8% of our outstanding common shares."
    - Standard General's latest [13D/A No. 28](https://www.sec.gov/Archives/edgar/data/1747079/000089534525000410/xslSCHEDULE_13D_X01/primary_doc.xml) (event 2025-12-22, cover page): "Percent of class represented by amount in Row (11) 66.07 %".
    - No 13D/A has been filed since. Standard General's Form ADV says `Any PE Funds = Y` (5 PE funds).
  - [Bally's 10-Q for Q3 2026](https://www.sec.gov/Archives/edgar/data/1747079/000174707926000108/baly-20260930.htm):
    - "As of September 30, 2026, we own and operate 21 casinos globally, including in the United Kingdom (“UK”) and in 11 states across the United States (“US”)"
    - Its property table lists 13 Bally's-named casino properties: Twin River Lincoln, Tiverton, Dover, Black Hawk (three casinos), Kansas City, Vicksburg, Atlantic City, Shreveport, Lake Tahoe, Evansville, Quad Cities, Chicago (temporary) and Baton Rouge.
    - It lists 3 Queen-named casinos: The Queen Baton Rouge, Casino Queen Marquette and DraftKings at Casino Queen. They came with "The Queen Casino & Entertainment, Inc. (“Queen”), a Parent affiliate", merged in on 2025-02-07.
  - Brand: [Bally's 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1747079/000174707926000019/baly-20251231.htm) (s2/062): "Bally’s is an iconic brand with broad recognition in the gaming industry."
  - Since: majority since the 2025-02-07 merger; both documents are current.
- **CA4 Hard Rock and Seminole Casino.**
  - [casino.hardrock.com](https://casino.hardrock.com/), the Hard Rock and Seminole casino hub: "Copyright © 2026 Seminole Tribe of Florida. All rights reserved."
  - [hardrock.com](https://www.hardrock.com/): "Today, guided by the Seminole tribe of Florida, we've grown into hotels, casinos, dining, and experiences across 68 countries."
  - Hard Rock 2022 release (s2/057): "the Seminole Tribe of Florida acquired the Hard Rock brand".
  - US casinos named on the hub, in HTML alt and title attributes rather than visible text:
    - **13 Hard Rock casinos:** Atlantic City, Biloxi, Bristol, Cincinnati, Northern Indiana, Rockford, Sacramento, Sioux City, Tejon, Tulsa, Seminole Hard Rock Hollywood, Seminole Hard Rock Tampa, and Rocksino by Hard Rock Deadwood. Kenosha and Las Vegas are also on the hub; their opening status was not checked, so they are not counted.
    - **4 Seminole casinos:** Seminole Brighton Bay, Seminole Casino Coconut Creek, Seminole Casino Hotel Immokalee and Seminole Classic Casino Hollywood.
  - Tribal, not PE.
- **CA5 Cherokee Casino.** [cherokeecasino.com](https://www.cherokeecasino.com/): "Copyright© 2026 Cherokee Nation Entertainment, LLC. All rights reserved". The page names 9 Cherokee Casino locations, from Tahlequah to "CHEROKEE CASINO WILL ROGERS DOWNS".
- **CA6 Choctaw Casino.** [choctawcasinos.com](https://www.choctawcasinos.com/): "The Choctaw Nation of Oklahoma is a thriving nation of nearly 200,000 people." The footer reads "©2026 Choctaw Casinos & Resorts". The page has location sections for Durant, Grant, Pocola, McAlester, Broken Bow, Idabel, Stringtown and Hochatown (8).
- **CA7 Station and Wildfire.**
  - [Red Rock 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1653653/000165365326000004/rrr-20251231.htm):
    - Count: Station LLC "owns and operates seven major gaming and entertainment facilities and 13 smaller casinos (three of which are 50% owned) in the Las Vegas regional market".
    - The property table lists Palace, Boulder, Sunset and Santa Fe Station, and 7 Wildfire casinos.
    - Half-owned: "We own a 50% interest in three smaller properties in Henderson, Nevada: Barley’s, which features slots, a sports book and a restaurant, The Greens, which features slots, a restaurant and lounge, and Wildfire Lanes".
  - Control, from the [2026 proxy](https://www.sec.gov/Archives/edgar/data/1653653/000119312526173964/d52675ddef14a.htm) (s2/024): "The Fertitta Family Entities hold more than 50% of the voting power of our shares eligible to vote."
  - Holder: Baron (BAMCO) 27.94% of Class A ([13G/A, 2026-06-03](https://www.sec.gov/Archives/edgar/data/1653653/000101791826000049/xslSCHEDULE_13G_X02/primary_doc.xml), (b); ADV N).
- **CA8 Golden Nugget.**
  - [Landry's](https://www.landrysinc.com/) lists "Golden Nugget Hotel & Casino" among its brands. Footer: "© 2024 Landry's, Inc."
  - Caesars merger proxy (s2/017): "Landry’s Fertitta, LLC (the “Parent Guarantor”) is a Texas limited liability company and subsidiary of Fertitta Entertainment, Inc."
  - Count of 7 from the lead list (Las Vegas, Laughlin, Atlantic City, Biloxi, Lake Charles, Danville, Cripple Creek), because goldennugget.com returned 403.
  - Family.
- **CA9 Osage Casino.** [osagecasino.com](https://osagecasino.com/): "Payout amounts are across all seven locations." Footer: "©2026 Osage Casinos."
- **CA10 Lucky Star.** [luckystarcasino.org](https://www.luckystarcasino.org/): "With seven locations across Oklahoma, Lucky Star Casino brings winning excitement closer to home." The footer links "The Cheyenne and Arapaho Tribes".
- **CA11 Ho-Chunk Gaming.** [ho-chunkgaming.com](https://www.ho-chunkgaming.com/): "Ho-Chunk Gaming Wisconsin is owned and operated by the Ho-Chunk Nation". It lists 7 locations: Beloit, Black River Falls, Madison, Nekoosa, Tomah, Wisconsin Dells, Wittenberg.
- **CA12 Ameristar.**
  - Trademark: PENN (CA1). PENN's 10-K adds: "The impairment of the trademark at our ACB property resulted from the strategic decision to rebrand ACB." (Ameristar Council Bluffs).
  - [Boyd 10-K](https://www.sec.gov/Archives/edgar/data/906553/000143774926004908/bgc20251121_10k.htm) lists "Ameristar Casino * Hotel Kansas City" and "Ameristar Casino * Resort * Spa St. Charles"; neither 10-K mentions a license.
- **CA13 Seneca.** [senecacasinos.com](https://senecacasinos.com/) lists "Seneca Niagara Resort & Casino Seneca Allegany Resort & Casino Seneca Buffalo Creek Casino", plus Seneca Gaming & Entertainment Irving, Salamanca and Oil Spring (6). The footer links the Seneca Nation.
- **CA14 Terrible's.** [terribles.com/gaming](https://www.terribles.com/gaming/): "Play & earn rewards with Terrible's Gaming at a casino near you. PAHRUMP SEARCHLIGHT INDIAN SPRINGS FERNLEY WINNEMUCCA CARLIN". Footer: "© 2023 Terrible Herbst, Inc. All rights reserved." Casino names were not shown; the lead list has Terrible's Casino Searchlight and Terrible's Town Pahrump.
- **CA15 Live!**
  - [Cordish, Gaming](https://cordish.com/businesses/gaming): "We developed and fully operate Live! Casino & Hotel Maryland, Live! Casino & Hotel Philadelphia, Live! Casino Pittsburgh, Live! Casino & Hotel Louisiana and Live! Casino Virginia".
  - [Cordish, About](https://cordish.com/About): "five generations of privately-held, family ownership".
- **CA16 Rivers.**
  - [Rush Street, Our Company](https://www.rushstreetgaming.com/our-company): "Rush Street has developed six regional destination casinos, including five in downtown Pittsburgh and Philadelphia, Portsmouth, the Capital Region of New York, and in the Chicago suburbs." The same page lists "Neil Bluhm Chairman and Founder".
  - [Casinos page](https://www.rushstreetgaming.com/casinos): Rivers Des Plaines, Philadelphia, Pittsburgh, Portsmouth and Schenectady.
  - [Churchill Downs 10-K](https://www.sec.gov/Archives/edgar/data/20212/000002021226000025/chdn-20251231.htm): "The Company has a 61.3% equity ownership in Midwest Gaming Holdings, LLC ("Midwest Gaming"), the parent company of Rivers Casino Des Plaines ("Rivers Des Plaines")."
  - Clairvest's portfolio lists Rivers Casino as "Exited".
- **CA17 Wind Creek.**
  - [windcreek.com/hospitality](https://windcreek.com/hospitality): "As the principal gaming and hospitality entity for the Poarch Band of Creek Indians, Wind Creek continues to grow".
  - [Footer](https://windcreek.com/bethlehem): "Footer Primary Locations Atmore Bethlehem Montgomery Wetumpka Aruba Curaçao Chicago Southland Miami". The Miami entry links to Magic City Casino, so 5 US casinos carry the Wind Creek name.
- **CA18 Desert Diamond.** [ddcaz.com](https://www.ddcaz.com/): "Desert Diamond Casino & Entertainment. An Enterprise of the Tohono O’odham Nation." The page also says "you can use it at our five exciting locations".
- **CA19 MGM.**
  - [MGM 10-K FY2025](https://www.sec.gov/Archives/edgar/data/789570/000078957026000018/mgm-20251231.htm): "principal intellectual property consists of trademarks for, among others, Aria, Vdara, Bellagio, The Cosmopolitan, Borgata, Mandalay Bay, MGM, MGM Grand, MGM Resorts International, Luxor, Excalibur, New York-New York, Park MGM, Beau Rivage, Empire City, LeoVegas, and BetMGM".
  - MGM-named US casinos: MGM Grand Las Vegas, Park MGM, MGM Grand Detroit, MGM National Harbor, MGM Springfield.
  - [10-Q for Q3 2026](https://www.sec.gov/Archives/edgar/data/789570/000078957026000107/mgm-20260930.htm): "In April 2026, the Company completed the sale of the operations of MGM Northfield Park to private equity funds managed by Clairvest Group Inc. for cash consideration of $546 million".
  - [Clairvest portfolio](https://www.clairvest.com/portfolio/): "Northfield Park Racino Fund: Fund VII Status: Active Industry: Gaming", ownership "Majority". The casino no longer carries the MGM name.
  - Holders: IAC's 13D (a public company). The screen's proxy check found no PE holder.
- **CA20 Owner not found (9).**
  - Kewadin (site 403), Comanche (TLS error), Gold Ranch (host unreachable), Grand Casino (Mille Lacs; script-rendered page), Parx (empty page), Emerald Queen (robots redirect).
  - Not fetched, for budget: 12 Tribes, Kickapoo Casino and Lakeside Entertainment.
  - Their counts come from the lead list. The lead list names a tribe for several of them; that is not used as evidence.
- **CA21 Oneida Casino.** [oneidacasinohotel.com](https://oneidacasinohotel.com/): "© 2026 Oneida Casino Hotel. All rights reserved." The site's "About Oneida" menu links "ONEIDA NATION". The count of 5 comes from the lead list.
- **CA22 Century Casino.**
  - [Century 10-K FY2025](https://www.sec.gov/Archives/edgar/data/911147/000091114726000009/cnty-20251231x10k.htm) lists four US casinos: "Century Casino & Hotel – Caruthersville – Caruthersville, Missouri", "Century Casino & Hotel – Cape Girardeau – Cape Girardeau, Missouri", "Century Casino & Hotel – Central City, Colorado" and "Century Casino & Hotel – Cripple Creek, Colorado".
  - Holders: the screen's 13G holders all have ADV N. Brigade (ADV Y) has a nomination agreement but no 5% stake.
  - Recent 8-Ks, not read: item 1.01 on 2026-09-29, item 3.01 on 2026-10-23, item 4.02 on 2026-11-16. None has item 2.01, so no completed sale.
- **CA23 Four Winds.** [fourwindscasino.com](https://fourwindscasino.com/): "© Pokagon Band of Potawatomi Indians." The page names New Buffalo, Hartford, Dowagiac and South Bend.
- **CA24 Resorts World.** [genting.com](https://www.genting.com/): "GENTING BERHAD Resorts World Las Vegas" and, under Genting Malaysia Berhad, "Resorts World New York City Resorts World Catskills". The lead list adds Resorts World Hudson Valley, which is not counted.
- **CA25 Gold Dust West.** [Jacobs, JEI Casinos](https://jacobsentertainmentinc.com/jei-casinos/): "Gold Dust West in Reno, Carson City and Elko, Nevada". [Homepage](https://jacobsentertainmentinc.com/): "Jacobs Entertainment, Inc. (JEI) is a developer, owner and operator of gaming and entertainment facilities in four regions of the United States."
- **CA26 Wild Rose.** [wildroseresorts.com](https://www.wildroseresorts.com/) lists Clinton, Emmetsburg and Jefferson. Footer: "©2026 Wild Rose Casino & Resort. All Rights Reserved".
- **CA27 Agua Caliente.** [About](https://www.aguacalientecasinos.com/about-us/): "The Agua Caliente Casinos are owned and operated by the Agua Caliente Band of Cahuilla Indians". The site names Rancho Mirage, Palm Springs and Cathedral City.
- **CA28 Seven Clans.** [sevenclanscasino.com](https://www.sevenclanscasino.com/): "Seven Clans Casino is proudly operated by the Red Lake Band of Chippewa Indians."
- **CA29 St. Croix Casino.** [stcroixcasino.com](https://www.stcroixcasino.com/) lists Turtle Lake, Danbury and Hertel. Footer: "Copyright © St. Croix Casino | All Rights Reserved".
- **CA30 WarHorse.** [warhorsecasino.com](https://www.warhorsecasino.com/) lists Lincoln, Omaha and South Sioux. Footer: "© 2025 WarHorse Gaming LLC. All rights reserved."
- **CA31 Boyd (Diamond Jo, Belterra, Sam's Town).**
  - [Boyd 10-K FY2025](https://www.sec.gov/Archives/edgar/data/906553/000143774926004908/bgc20251121_10k.htm): "we operate 27 brick-and-mortar gaming entertainment properties". It lists Diamond Jo Casino (Dubuque) and Diamond Jo Worth, Belterra Casino Resort and Belterra Park, and Sam's Town Las Vegas and Shreveport. Sam's Town Tunica "was permanently closed on November 9, 2025".
  - [Bally's 10-Q](https://www.sec.gov/Archives/edgar/data/1747079/000174707926000108/baly-20260930.htm): "On August 3, 2026, the Company completed the acquisition of Sam’s Town Shreveport for aggregate consideration of approximately $35.8 million." and "No goodwill or identifiable intangible assets were recognized as part of the transaction."
  - Holders: Cohen & Steers 8.47% ([13G/A](https://www.sec.gov/Archives/edgar/data/906553/000119312526350676/xslSCHEDULE_13G_X02/primary_doc.xml), (b), ADV N). Boyd family per the screen's proxy.
- **CA32 Encore.** [Wynn 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1174922/000117492226000013/wynn-20251231.htm):
  - "We opened Wynn Las Vegas in April 2005 and Encore, an expansion of Wynn Las Vegas, in December 2008."
  - "On June 23, 2019, we opened Encore Boston Harbor, an integrated resort in Everett, Massachusetts".
  - 2026 13G filers: BlackRock 4.9% ((b)); Susquehanna 4.1% ((b)); Kevyn and Gillian Wynn 5.65% ((c), individuals). Not PE.
- **CA33 Arizona Charlie's.**
  - [Golden 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1071255/000107125526000015/gden-20251231.htm): "Our Arizona Charlie’s Boulder and Arizona Charlie’s Decatur casino properties primarily serve local Las Vegas gaming patrons".
  - Buyer: [merger proxy](https://www.sec.gov/Archives/edgar/data/1071255/000119312526096620/d26120ddefm14a.htm) (s2/028): "OpCo Buyer is controlled by Blake Sartini, the Chief Executive Officer and Chairman of the Board." Delisted 2026-04-30 (Form 25).
  - Family.
- **CA34 Circus Circus.** Caesars' 10-K lists "Circus Circus Reno" and the Circus Circus trademark (CA2). The [Circus Circus Las Vegas site](https://www.circuscircus.com/) names no owner (footer "Copyright © 2026" only). Two operators use one name; neither shows PE evidence.
- **CA35 JACK.**
  - [jackentertainment.com](https://jackentertainment.com/): "© 2026 JACK Entertainment LLC Trademarks used herein are owned by JACK Entertainment LLC and its affiliated companies."
  - [About](https://jackentertainment.com/about-us/): "When you’re at JACK Cleveland Casino or JACK Thistledown Racino".
- **CA36 Saratoga Casino.** [saratogacasino.com](https://saratogacasino.com/): "Saratoga Casino Hotel does not offer any online gambling services." [saratogacasinobh.com](https://saratogacasinobh.com/): "Saratoga Black Hawk does not offer any online gambling services." Neither names an owner.
- **CA37 Peppermill.** [peppermillreno.com](https://www.peppermillreno.com/): "© 1996 - 2020 Peppermill Resort Spa Casino, All Rights Reserved." The Wendover site was not fetched; the count is from the lead list.
- **CA38 Mohegan.** [Mohegan, Our Company](https://mohegangaming.com/our-company/): "The company is governed by the Mohegan Tribe" and "Mohegan’s footprint spans properties in Connecticut, Pennsylvania, and Niagara Falls, Canada." Mohegan Casino Las Vegas, opened in 2021, is no longer listed, so the US count is 2.
- **CA39 Odawa.** [odawacasino.com](https://www.odawacasino.com/): "Odawa Casino is owned and operated by the Little Traverse Bay Bands of Odawa Indians." The page lists Petoskey and Mackinaw City.
- **CA40 Ojibwa.** [ojibwacasino.com](https://www.ojibwacasino.com/): "Baraga: (906) 353-6333 | Marquette: (906) 249-4200". No owner is named.
- **CA41 Potawatomi.** [potawatomi.com](https://www.potawatomi.com/) lists Milwaukee and Carter. Footer: "© 2026 Forest County Potawatomi Community, Wisconsin".
- **CA42 Three Rivers.** [threeriverscasino.com](https://www.threeriverscasino.com/): "Three Rivers Casino is an award-winning destination with two prime locations along the stunning Oregon Coast—Coos Bay and Florence."
- **CA43 Tulalip.** [everythingtulalip.com](https://www.everythingtulalip.com/) lists Tulalip Resort Casino and "Tulalip Bingo & Slots"; Quil Ceda Creek Casino is a separate name. No owner is named.

## Licensed and shared names

- **Caesars:**
  - Harrah's at four managed tribal casinos (Ak-Chin, Cherokee, Cherokee Valley River, Resort Southern California) and one "Branded" site (Harrah's Northern California).
  - Caesars Southern Indiana is "Branded".
  - Planet Hollywood is a single-location name that Caesars has "the right to use".
  - The brand stays Caesars' in every case.
- **PENN:**
  - Ameristar at Boyd's Kansas City and St. Charles casinos. The trademark is PENN's; neither 10-K mentions a license.
  - Margaritaville (single location): "Among others, we have a licensing agreement with a third-party to use the “Margaritaville” trademark in connection with the operations of Margaritaville in Bossier City, Louisiana."
- **Boyd:** Sam's Town Shreveport is run by Bally's since 2026-08-03. Bally's bought no intangible assets, so the name stays Boyd's; the license terms are not stated.
- **Hard Rock (Seminole):**
  - Licensees or partners run most US Hard Rock casinos. Bally's runs Biloxi (the screen's Bally's 10-K names Hard Rock among its licensed brands). Cherokee Nation Entertainment runs Tulsa.
  - The others (Atlantic City, Sioux City, Sacramento, Tejon, Northern Indiana, Rockford, Bristol, Deadwood) were not checked one by one.
- **Golden Nugget:** Danville and Cripple Creek look like licensed sites, per the lead list. Not confirmed.
- **Bally's Queen:** "DraftKings at Casino Queen" carries a DraftKings naming-rights prefix; the casino is Bally's.
- **Not rows, noted for the licensing rule:**
  - The Venetian and Palazzo: Las Vegas Sands licenses the names to the Apollo-managed operator (screen: LVS 10-K). It is one US location.
  - MGM Northfield Park: renamed Northfield Park Racino under Clairvest. No license was found; the name changed.
- **Same name, two operators:** Circus Circus (Caesars in Reno, another operator in Las Vegas) and Boomtown (PENN's three, plus Boomtown Reno in the lead list).

## Firms named

- **Standard General L.P.** (Bally's, 66.8% per the 2026 proxy; 66.07% per 13D/A No. 28): PE, control.
- **Clairvest Group Inc.** ("Clairvest is a top performing private equity management firm", [clairvest.com](https://www.clairvest.com/)): majority owner of Northfield Park Racino (Fund VII), Wyoming Downs and Delaware Park; minority in The Nash Casino and Meadowlands; exited Rivers Casino. No multi-location casino name.
- **Apollo Global Management** (the Venetian operator, licensee): PE, not a brand owner.
- **Fertitta Entertainment / Landry's** (Golden Nugget; Caesars pending): family.
- **The Cordish Companies** (Live!): family. **Rush Street Gaming** (Rivers; Neil Bluhm, founder). **Jacobs Entertainment, Inc.** **Terrible Herbst, Inc.** **JACK Entertainment LLC.** **Argento / Blake Sartini** (Arizona Charlie's).
- **Genting Berhad and Genting Malaysia Berhad** (Resorts World): public companies.
- **Churchill Downs Inc.** (61.3% of Rivers Des Plaines): public company.
- **IAC Inc.** (MGM 13D): public company.
- 13G holders checked in 2026 filings:
  - BlackRock (PENN 14.1%, Wynn 4.9%), Baron/BAMCO (Red Rock 27.94%), Cohen & Steers (Boyd 8.47%), Pentwater (Caesars 4.6%), AQR (PENN 1.09%), Capital World Investors (Caesars 0.0%), Susquehanna (Wynn 4.1%): all filed under Rule 13d-1(b).
  - Kevyn and Gillian Wynn (Wynn 5.65%) filed under 13d-1(c), as individuals.

## Form ADV results (SEC `ia110226-registered`, `ia11022026-exempt`, November 2026)

| Firm (role) | Adviser entity | CRD | Type | Any PE Funds | PE funds |
|---|---|---|---|---|---|
| Standard General (Bally's, Queen) | Standard General L.P. | 151831 | RIA | Y | 5 |
| Clairvest (Northfield Park Racino; Wyoming Downs) | Clairvest GP Manageco Inc. | 162568 | ERA | Y | 6 |
| Apollo (Venetian operator, licensee) | Apollo Capital Management, L.P. | 143161 | RIA | Y | 214 |
| Baron (Red Rock 13G) | BAMCO, Inc.; Baron Capital Management, Inc. | 110789; 110791 | RIA | N | |
| Cohen & Steers (Boyd 13G) | Cohen & Steers Capital Management, Inc. | 106266 | RIA | N | |
| Pentwater (Caesars 13G) | Pentwater Capital Management LP | 156873 | RIA | N | |
| AQR (PENN 13G) | AQR Capital Management, LLC | 111883 | RIA | N | |
| Capital World Investors (Caesars 13G) | Capital Research and Management Company | 110885 | RIA | N | |

Not in either file, or not advisers: Susquehanna (none of its entities, as the screen also found), Fertitta Entertainment, Cordish, Rush Street, Jacobs, Terrible Herbst, JACK, Argento, IAC, Genting, Churchill Downs, and the tribes.

## Rows resting on documents older than 18 months

- **PE rows: none.** Bally's and Queen rest on the 10-Q of 2026-11-16, the proxy of 2026-04-09 and Standard General's 13D/A of 2025-12-23 (11 months old).
- **Non-PE rows** rest on filings from 2026 or on pages seen today, which confirm on every view. Some footers carry old years: Peppermill "© 1996 - 2020", Terrible Herbst "© 2023", Landry's "© 2024", Ho-Chunk "© 2024", WarHorse "© 2025". The only old document used is Hard Rock's 2022 release (s2/057), and the hub's 2026 copyright line confirms it.

## Surprises

- **MGM sold Northfield Park's operations to Clairvest (PE) in April 2026, and the casino dropped the MGM name** ("Northfield Park Racino" on Clairvest's portfolio). Clairvest gets a casino, not a brand, and MGM's row falls from 6 locations to 5.
- **Bally's has a second multi-site name, Queen** (3 casinos from Standard General's 2025 Queen merger). That gives casinos 2 PE rows rather than 1.
- **Bally's bought Sam's Town Shreveport (2026-08-03) without buying the name.** It recognized no intangible assets, so Sam's Town stays Boyd's name, now at a Bally's casino. Boyd closed Sam's Town Tunica on 2025-11-09.
- **Ameristar is split between two operators** (PENN 4, Boyd 2), with PENN holding the trademark. PENN booked an impairment for a "strategic decision to rebrand ACB" (Ameristar Council Bluffs).
- **Encore is a brand but Wynn is not** (Wynn has one US location), and the Venetian is not a row at all (one US location). Both follow from the "several locations" rule plus the US-only scope.
- **Tribal names are 29 of 64 rows.** None can be PE, which pulls the share well below the operator count.
- **Rivers Des Plaines is 61.3% Churchill Downs,** and Clairvest has exited Rivers.
- **Mohegan no longer lists a Las Vegas casino.** Muscogee Nation's site names its casinos locally (Lake Eufaula Casino Hotel, One Fire Casino, River Spirit and so on), under the umbrella of Muscogee Nation Gaming Enterprises (domain creeknationcasinos.com). The lead list's "Creek Nation Casino of Eufaula" names look out of date.
- **Resorts World Las Vegas disallows ClaudeBot;** Golden Nugget's site returned 403.
- **Century Casinos filed 8-Ks with items 3.01 (2026-10-23) and 4.02 (2026-11-16)**, a listing notice and non-reliance on past financial statements. Not read; ownership is unaffected.

## Open questions for the developer (numbers only; nothing decided)

1. **Which rows count:**
   - All 64 names: 2 / 64 (3.1%).
   - Without the 9 lead-only rows whose owner was not found: 2 / 55 (3.6%).
   - Commercial names only: 2 / 35 (5.7%).
   - Names whose count comes from an SEC filing (21 public-company names, plus Arizona Charlie's and Circus Circus): 2 / 23 (8.7%).
   - The earlier screen's operator rows: 1 / 10 (10%).
   - Only the operator rule reaches 10%.
2. **Queen:** counted, 2 / 64. Not counted (if DraftKings at Casino Queen, The Queen Baton Rouge and Casino Queen Marquette are read as different names): 1 / 63 (1.6%).
3. **Boundary formats:**
   - Adding Churchill's Rosie's (6) and Derby City Gaming (2), Station's Seventy Six taverns (3) and bestbet (3, lead): 2 / 68 (2.9%).
   - Also adding Clairvest's Wyoming Downs as a PE row (multi-site naming not verified): 3 / 69 (4.3%).
   - Not counted: Golden's 72 taverns (several names) and Jacobs' Cash Magic truck-stop casinos.
4. **Umbrella names:** adding Muscogee Nation Gaming Enterprises' group (11 locations with local names) as a row gives 2 / 65 (3.1%).
5. **Location share:** 16 PE-named locations (13 Bally's properties, 3 Queen) of about 290 counted locations (5.5%). With Bally's Black Hawk as three casinos: 18 of about 292 (6.2%).
6. **Shared and licensed names:** Circus Circus (2 operators) and Ameristar (2 operators) are counted once each; splitting them changes the denominator by 2.
7. **Audit status:** this is a count of every brand found, not a 30-brand sample. Rows 22, 29, 39, 40 and 61 to 64, plus Parx, need an operator source to be confirmed; none is a PE lead.

## Cost

- **Page requests:** 81 (22 to www.sec.gov, 59 to 46 other hosts): 74 HTTP 200, 3 × 301, 2 × 302, 2 × 403.
- **robots.txt requests:** 61 (47 OK, 11 redirects followed by a separate read, 1 × 403 meaning no restrictions, 2 unreachable meaning blocked).
- **Searches:** 4 WebSearch calls (domain lookups only); no WebFetch.
- **SEC pace:** at least 1.2 s between requests.
- **Tokens and time:** roughly 200k tokens; about 45 minutes, including writing.

## Quote check

- **Result:** 90 of 90 quotes found verbatim in the saved page text, by `scripts/fu-casinos/qcheck.py` over `quotes.tsv`. This includes short field and label fragments ("Exited", "Ownership: Majority", "ONEIDA NATION", "The Cheyenne and Arapaho Tribes"). A second pass confirmed that every checked quote used in this report appears in it exactly as checked. One fragment, "Creek Nation Casinos", failed: it came from a search-result title, not the page. It was removed from the report. Whitespace, curly quotes, dashes and zero-width characters were normalized. The quotes come from 53 pages in this session's cache and 6 pages in the screen's cache.
- **Negative control:** 8 deliberately altered copies all failed (`neg.tsv`: changed numbers, owners and verbs).
- **Not covered by the check:**
  - Values read from HTML attributes: Hard Rock's and Seminole's casino names in alt and title attributes, and Choctaw's location URLs.
  - Values read from tables and form fields: 13G percentages and checked Rule boxes (read from the `box-checked.jpg` image alt text), 10-K property tables, Clairvest's "Ownership: Majority" field.
  - Counts taken from the Wikipedia lead list.
