# Research: USPTO trademark data as an official source

Ticket: [56-research-uspto-trademark-data](../issues/56-research-uspto-trademark-data.md) · Researched 2026-11-04.

**Sources.** USPTO pages, USPTO data documentation, the USPTO's own catalog file (`data.json`), the Trademark Manual of Examining Procedure (TMEP, May 2026 edition, the current one), and live USPTO systems. For the brand spot checks, the operating owner comes from SEC filings or company or sponsor press releases.

**How things were fetched.** USPTO systems were called with curl using the user agent `ownership-research/0.1 (public-data research)`, which carries no contact details. sec.gov refuses that user agent ("Undeclared Automated Tool", HTTP 403) and no email was added, so SEC filings were read through the WebFetch tool instead. Points marked **[observed]** come from live USPTO responses on 2026-11-04. They are not documented behaviour.

**Not signed up for anything.** Since 2026-06-18 the USPTO Open Data Portal (ODP) needs a USPTO.gov sign-in, and its API needs a key tied to an ID.me identity check. The TSDR API needs its own key. No account was created and no key was requested, so **no bulk file was downloaded** and the bulk formats below come from USPTO documentation only.

**Bottom line.**
- **Current owner of one mark: yes.** USPTO keeps a "Trademark database" that shows one owner per application or registration: the *last recorded owner*. TSDR displays it as "Current Owner(s) Information", one mark at a time.
- **That owner field has gaps.** It updates automatically only for six kinds of recorded documents. It updates even when the chain of title is broken. Recording is "a ministerial act, and not a determination of the document's validity". [U-TMEP §§503.01(c), 504]
- **Ownership changes are recorded in a separate Assignment database,** one record per recorded document. Each record has a free-text conveyance, assignors, assignees, and the serial/registration numbers it covers. Security interests (loan collateral), mergers, name changes and licenses are all recorded there. Only some of them change the owner field.
- **Spot checks (8 brands): the registered owner never named the private-equity sponsor.**
  - For the 5 sponsor-owned brands it was a brand-level subsidiary, four of them named "... IP Holder(s)".
  - The sponsor deals themselves (stock acquisitions) left no USPTO record.
  - For the 3 public companies it matched the filer or a named subsidiary.
  - In 1 of 8 (Jersey Mike's), the TSDR owner field disagrees with an assignment recorded in 2019.

Source keys used below:
- [U-BULK] USPTO, *Trademark bulk data*: https://www.uspto.gov/trademarks/apply/check-status-view-documents/trademark-bulk-data (the ticket's URL now 301-redirects here)
- [U-DJ] USPTO, Project Open Data catalog `data.json`: https://www.uspto.gov/data.json (served from https://www.uspto.gov/sites/default/files/documents/data.json)
- [U-BDSS] USPTO system status, *Bulk Data Storage System (BDSS) Retirement* (Apr 8–11, 2025): https://www.uspto.gov/system-status/20250408-bulk-data-storage-system-bdss-retirement
- [U-ODPNEWS] USPTO news, *USPTO launches new Open Data Portal* (Feb 2025): https://www.uspto.gov/about-us/news-updates/uspto-launches-new-open-data-portal-easy-quick-access-data
- [U-REG] USPTO news, *USPTO Open Data Portal to require registration for access beginning June 18, 2026*: https://www.uspto.gov/about-us/news-updates/uspto-open-data-portal-require-registration-access-beginning-june-18-2026 ; alert: https://www.uspto.gov/subscription-center/2026/register-access-usptos-open-data-portal
- [ODP] ODP help pages. These are JavaScript-only pages that returned an empty shell to curl and WebFetch, so their wording was read **only through search-engine index text**, not fetched directly:
  - https://data.uspto.gov/support/universal-registration
  - https://data.uspto.gov/apis/getting-started
  - https://data.uspto.gov/apis/api-rate-limits
  - https://data.uspto.gov/apis/bulk-data/download
  - https://data.uspto.gov/support (FAQ)
- [U-DEV-TDXF] developer.uspto.gov product page *Trademark daily XML file (TDXF) assignments*, Wayback copy of 2025-06-10: http://web.archive.org/web/20250610054934/https://developer.uspto.gov/product/trademark-daily-xml-file-tdxf-assignments (the live developer.uspto.gov pages now redirect to data.uspto.gov)
- [U-ASGDTD] USPTO, *Trademark Assignment Daily XML DTD Element Documentation (V.4)*: https://www.uspto.gov/sites/default/files/products/assign-documentation.pdf
- [U-APPDOC] USPTO, *Trademark applications XML documentation* (PDF created 2012-05-09): https://www.uspto.gov/sites/default/files/products/applications-documentation.pdf
- [U-ECON-ASG] USPTO Office of the Chief Economist, *Trademark Assignment Dataset*: https://www.uspto.gov/ip-policy/economic-research/research-datasets/trademark-assignment-dataset ; schema: https://www.uspto.gov/sites/default/files/documents/TM_assignment_dataset_schema.pdf
- [U-ECON-CF] USPTO OCE, *Trademark Case Files Dataset*: https://www.uspto.gov/ip-policy/economic-research/research-datasets/trademark-case-files-dataset ; variable tables: https://www.uspto.gov/sites/default/files/documents/casefiles_vartable_2023_final.pdf
- [U-OCE24] USPTO, *Updated Trademark datasets now available* (2024): https://www.uspto.gov/subscription-center/2024/updated-trademark-datasets-now-available
- [U-TMEP] TMEP Chapter 500 *Change of Ownership*, May 2026 edition (marked "Current" on 2026-11-04): https://tmep.uspto.gov/RDMS/TMEP/print?version=current&href=TMEP-500d1e1.html
- [U-ASGPAGE] USPTO, *Trademark assignments: change/search ownership*: https://www.uspto.gov/trademarks/trademark-assignments-change-search-ownership
- [U-ASGNEWS] USPTO news, *USPTO enhances assignment records search process*: https://www.uspto.gov/about-us/news-updates/uspto-enhances-assignment-records-search-process
- [U-TSDRFAQ] TSDR FAQ: https://tsdr.uspto.gov/faqview
- [U-TSDRGUIDE] USPTO, *TSDR API Key Manager user guide* (Sept 2020): https://www.uspto.gov/sites/default/files/documents/tm-enterprise-api-user-guide-v2.pdf
- [U-TOU] USPTO, *Terms of use for USPTO websites*: https://www.uspto.gov/terms-use-uspto-websites
- [U-TSDR] Live TSDR status pages `https://tsdr.uspto.gov/statusview/rn{registration no.}` and assignment abstracts `https://tsdr.uspto.gov/assignments/{serial no.}?searchprefix=sn`. These are the URLs the TSDR web page itself loads, found in https://tsdr.uspto.gov/js/SearchPage.js.

---

## 1. What USPTO publishes

### Bulk products

The old Bulk Data Storage System (bulkdata.uspto.gov) was retired on April 11, 2025. Its data moved to the ODP "Bulk Data Directory" at https://data.uspto.gov/bulkdata/datasets. [U-BDSS] **[observed]** `bulkdata.uspto.gov` no longer resolves in DNS.

The USPTO's own catalog lists these trademark products. All are `accessLevel: public` under license `https://creativecommons.org/publicdomain/mark/1.0`, and all have catalog `modified` date 2025-08-28. [U-DJ]

| Product (ODP id) | What it holds | Cadence | Format | Coverage |
|---|---|---|---|---|
| Trademark Application XML (`trtdxfap`) | "Pending and registered trademark text data (no images) to include word mark, serial number, registration number, filing date, registration date, goods and services, classification number(s), status code(s), and design search code(s)" | daily (`R/P1D`) | XML | 1884 – present |
| Trademark Assignment XML (`trtdxfag`) | "Assignment (ownership) text data (no images)" | daily (`R/P1D`) | XML | 1955 – present |
| TTAB XML (`ttabtdxf`) | Trial and Appeal Board text data | daily | XML | 1951 – present |
| Trademark Case Files Dataset (`trcfeco2`) | research dataset: "12.1 million trademark applications … between 1870 and January 2023" | yearly (`R/P1Y`) | CSV, Stata | 1870 – 2023 |
| Trademark Assignment Data for Academia (`traseco`) | research dataset: "1.29 million assignments and other transactions … between 1952 and 2023" | yearly | CSV, Stata | 1952 – 2023 |
| Trademark Official Gazette | weekly front-page data per published mark, with lists of cancelled and renewed registrations | weekly | PDF | 2001 – present |

Notes on the table:
- **Annual backfiles.** The 2025 developer.uspto.gov page for the daily assignments file says "Assignment text data (no images) in CY2025", in the "U.S. Trademark Assignments Version 0.4" DTD, and links a sibling "Trademark annual XML assignments" product. Its latest release was "2025-04-13, Download (1.55 KB)". [U-DEV-TDXF] Search-index text of the annual product pages says the assignments backfile covers "JAN 3, 1955 - DEC 31, 2024" and the applications backfile "APR 1884 - DEC 2024" (Trademark Applications DTD v2.0). **Unconfirmed:** those developer.uspto.gov pages now redirect, and the ODP pages need sign-in, so they could not be read directly.
- **File sizes for the current daily files: unconfirmed.** They are behind the ODP sign-in.
- **Research datasets.** The OCE pages give the newest numbers. Case Files (2023 update): 12.7 million applications, Oct 1870 – Mar 2024; the full CSV set is 4.33 GB. Assignments (2023 update): over 1.38 million assignments on about 2.39 million properties, Mar 1952 – Jan 2024. [U-ECON-CF][U-ECON-ASG][U-OCE24] The Case Files `owner` table alone has 28,273,547 rows and is 6.1 GB as Stata. [U-ECON-CF vartable]
- **Research datasets are released yearly and run behind.** The newest update reaches January / March 2024.

### Single-record lookups

- **TSDR** (Trademark Status & Document Retrieval): web pages, and an API at `tsdrapi.uspto.gov` (section 4).
- **Assignment Search** inside Assignment Center (https://assignmentcenter.uspto.gov/). It replaced "Assignments on the Web" on October 20, 2025. [U-ASGNEWS] TMEP points owners there to check chain of title. [U-TMEP §504]

## 2. Access and terms

- **ODP website, since 2026-06-18:** "you'll need to have a USPTO.gov account to access, search, and download these datasets". The stated reason: "improve site security while limiting costly, unregistered bot traffic". [U-REG]
  - **[observed]** Without a session, every data.uspto.gov file URL tried returned only the 20,666-byte app shell. That includes `.../ui/datasets/products/files/TRTDXFAP/...doc` and `.../TRASECO/2023/tm_convey.csv.zip`.
- **ODP API:** needs a USPTO.gov account plus "a validated and linked ID.me account to request an API Key". The key goes in an `x-api-key` header. [ODP getting-started, via search index]
  - Four profile fields became required on 2026-08-18: job title, organization name, organization type, intended use. Keys for accounts that had not filled them by 2026-10-08 were deactivated. [ODP, via search index]
  - **[observed]** `GET https://api.uspto.gov/api/v1/datasets/products/search` without a key → HTTP 401 `{"message":"Unauthorized"}`.
- **ODP API limits** [ODP api-rate-limits and bulk-data/download, via search index; unconfirmed by direct fetch]:
  - 4–15 requests per second, depending on the call type.
  - No concurrent calls with the same key.
  - Metadata calls capped at 5 million per week.
  - 20 downloads of the same file per key per year; the 21st returns HTTP 429.
- **TSDR API key:** "As of October 2, 2020, you must register in order to use the TSDR APIs", at https://account.uspto.gov/api-manager/. [U-TSDRFAQ] The key goes in a `USPTO-API-KEY` header. [U-TSDRGUIDE]
  - **[observed]** `tsdrapi.uspto.gov/ts/cd/casestatus/sn…/info.xml` without a key → HTTP 401 with text "you'll need to register for an API key to download bulk data from our TSDR APIs".
  - **Unconfirmed:** whether a TSDR key now also requires ID.me.
- **Website terms:** USPTO web databases are "not designed or intended to be a source for bulk downloads of USPTO data". Anyone "generating unusually high numbers of database accesses (searches, pages, or hits), whether generated manually or in an automated fashion … may be denied access to USPTO servers without notice". Bulk data is to be taken from the bulk products instead. [U-TOU]
- **Copyright:** "most government-produced materials appearing on this website are not subject to copyright restrictions". [U-TOU] The catalog marks all trademark datasets public domain. [U-DJ]

## 3. Does any file state the current owner?

**Yes, one owner per mark, in the Trademark database.**
- TMEP §504: "The Trademark database will show only the last recorded owner, not the complete chain of title. The complete chain of title can be obtained from the Trademark Assignment Search database".
- The TSDR FAQ says the Status tab is "the official record for the mark, including … current owner information". [U-TSDRFAQ]
- **[observed]** Each TSDR status page has a "Current Owner(s) Information" block: owner name, address, "Legal Entity Type", and "State or Country Where Organized".

**How the owner field gets updated (TMEP May 2026):**
- **Six document types update it automatically** (§504): "Assignment of entire interest and goodwill; Nunc Pro Tunc Assignment …; Merger; Change of Name; Merger and Change of Name; or Entity Conversion".
  - The filer must tick the matching "Nature of Conveyance" box, not "Other".
  - "In all other situations, the new owner must separately notify the Trademark Operation in writing".
- **No check of the chain of title** (§504 and §504.03): "The 'Ownership' field in the Trademark database will be automatically updated whether or not the records of the Assignment Recordation Branch show clear chain of title". Examining attorneys check the chain only when the owner takes an action.
- **Cases where it does not update automatically** (§504.01):
  - execution-date conflicts with an earlier recorded document;
  - several assignments with the same execution date filed on the same day;
  - "blackout" windows of about three weeks before publication or registration;
  - Board (TTAB) proceedings;
  - more than nine ownership changes before publication, or nine between publication and registration.
- **Weekly batch:** the Assignment Recordation Branch sends updates to the Trademark Operation "once a week". [§504.02]
- **TSDR shows when it failed.** USPTO says the prosecution history then shows that "Ownership records not automatically updated". [U-ASGPAGE] **[observed]** The actual TSDR entry reads "ASSIGNMENT OF OWNERSHIP NOT UPDATED AUTOMATICALLY". All eight spot-check marks carry it at least once.
- **Recording is not a validity check.** 37 C.F.R. §3.54: recording "is not a determination by the Office of the validity of the document or the effect that document has on the title". TMEP §503.01(c): "The act of recording a document is a ministerial act".
- **Owner details come from the filer.** In the assignment data, names and addresses are "those that are supplied by the submitter of the assignment document". [U-ASGDTD]
- **Recording is not shown to be mandatory.** TMEP quotes 15 U.S.C. §1060(a)(4): an unrecorded assignment is "void against any subsequent purchaser for valuable consideration without notice" unless recorded within 3 months or before that purchase. [U-TMEP §501.03] I found no statement that recording is otherwise required.

**In the bulk files:**
- **Applications XML.** Each case file carries repeating `<case-file-owner>` entries with a two-digit `<party-type>` code. [U-APPDOC] The 2012 documentation lists codes for "Trademark records that have not had the ownership information modified on or after November 2, 2003":
  - 10 Original Applicant;
  - 11–19 1st–6th New Owner Before Publication;
  - 20 Owner at Publication;
  - 21–27 1st–4th New Owner After Publication.

  **Unconfirmed:** the rest of the table, including any post-registration or "current owner" code and the post-2003 coding. It did not come out of that PDF. The current documentation ("Trademark-Applications-Documentation-v2.3-20250813.doc", linked from [U-ECON-CF]) is behind the ODP sign-in. So whether one XML row is explicitly flagged as the current owner is **unconfirmed**.
- **Case Files research dataset.** Its `owner` table keeps every owner row per serial, with `own_type_cd` ("Owning party type code <party-type>"). A separate `owner_name_change` table holds "Assignment, name change description". [U-ECON-CF vartable]
- **Assignments XML.** It does not state a current owner; it is a log of recorded documents (section 3a).

### 3a. How changes are recorded

- **Assignment XML, one entry per recorded document** [U-ASGDTD]. Each `<assignment-entry>` holds:
  - `reel-no` / `frame-no`, `date-recorded`, `last-update-date`, `purge-indicator` ("Indicates when an assignment record has been deleted from the Historical database"), `page-count`;
  - `conveyance-text` ("textual description of the interest conveyed or transaction recorded", free text);
  - assignors (each with `execution-date`, `legal-entity-text`, `nationality`, and formerly / dba / composed-of statements);
  - assignees;
  - `properties`: a list of `serial-no`, `registration-no`, and international registration number. **The entry has no mark text.** Mark names must be joined from the applications data.
- **Mergers and name changes** are recorded as "proper link[s] in the chain of title". "A mere change of name does not constitute a change of legal entity". [U-TMEP §503.02]
- **Security interests and licenses:** "license agreements, security agreements, and agreements between parties limiting future extension of use" may be recorded "to give third parties notification of equitable interests". They "do not constitute a transfer or change of title". [U-TMEP §503.02] They are not among the six types that update the owner field. [§504]
- **Madrid (§66(a)) marks** are recorded with WIPO's International Bureau. USPTO updates its database from the International Register. [U-TMEP §504.04]
- **Conveyance labels in practice [observed].** These come from the spot-check abstracts and show the free text is not a closed list:
  - "ASSIGNS THE ENTIRE INTEREST"
  - "SECURITY INTEREST"
  - "RELEASE OF SECURITY INTEREST"
  - "NOTICE OF GRANT OF BACK-UP SECURITY INTEREST IN TRADEMARKS"
  - "SUPPLEMENT NO. 2 TO THE FIRST LIEN SECURITY AGREEMENT (APRIL 2020)"
  - "ENTITY CONVERSION"
  - "CHANGE OF NAME"
  - "MERGER (SEE DOCUMENT FOR DETAILS)"
  - "U.S. TRADEMARK ASSIGNMENT"
  - "CORRECTIVE ASSIGNMENT TO CORRECT …"

  The research dataset adds a constructed `conv_group` column (`tm_convey`). [U-ECON-ASG schema] **Unconfirmed:** what its codes mean (they are documented in the OCE working paper, which was not read).
- **The recorded document itself** [observed]. TSDR links each assignment to `https://assignmentcenter.uspto.gov/ipas/search/api/v3/public/download/trademark/{reel}/{frame}`. This served a PDF without sign-in. The one fetched (reel/frame 6825/0315) was 5 pages of JPEG images with no text layer.

## 4. Single-mark API (TSDR)

- **Endpoints** [U-TSDRGUIDE]:
  - `https://tsdrapi.uspto.gov/ts/cd/casestatus/sn{serial}/info.xml` (XML status)
  - `.../content` (HTML)
  - `.../content.zip` (XML + CSS)
  - `.../download.pdf`
  - document bundles under `/ts/cd/casedocs/bundle.pdf?sn=…` or `?rn=…`
  - TSDR FAQ: `.../casestatus/rn{reg}/content.zip` returns the assignment content. [U-TSDRFAQ]
- **Limits:** "All requests are rate limited at 60 requests per API key per minute. PDF and ZIP downloads are rate limited at 4 requests per API key per minute." [U-TSDRFAQ] The 2020 guide adds off-peak limits, 10 p.m.–5 a.m. EST: 120 per minute, and 12 per minute for PDF/ZIP. It calls all of these "subject to change". Over the limit returns HTTP 429. [U-TSDRGUIDE]
- **Change detection without a key [observed].** `https://tsdrapi.uspto.gov/last-update/info.json?sn={serial}` returned HTTP 200 without a key, with separate `caseStatusData` and `caseProsecutionData` last-modified dates. The guide documents this endpoint (TM-LUS). [U-TSDRGUIDE]
- **Web page without a key [observed].** The TSDR web page's status (`/statusview/rn…`) and assignment-abstract (`/assignments/{sn}?searchprefix=sn`) URLs returned full HTML without a key. This is the web interface, so the high-volume clause in [U-TOU] applies.
  - Each status page includes "This page was generated by TSDR on {timestamp}", so its bytes change on every fetch.
- **Undocumented search backend [observed].** Assignment Center's public search page calls `POST https://assignmentcenter.uspto.gov/ipas/search/api/v3/public/search/trademark`. It answered without sign-in and returns, for each property, the mark text, serial and registration numbers, and a `currentOwner` field.
  - I used it only to find registration numbers for the spot checks. For all ten marks whose TSDR page I fetched, its `currentOwner` matched the TSDR owner field.
  - It is not documented, and no USPTO page found states whether automated use is allowed. The app also shows a "Trademark export data (API for developers)" link and the text "Effective July 24, 2026, Patent Export Assignment Data Search has been moved to Open Data Portal". **Unconfirmed:** the terms and limits of that trademark export.

## 5. Spot checks: registered owner vs operating owner

All USPTO data was read from TSDR on 2026-11-04 (status page and assignment abstract per mark). "Latest security interest" is the most recent recorded "security" conveyance; whether it is still active was not checked.

| Brand (mark, reg. no.) | TSDR current owner | Operating owner per primary source | Match? |
|---|---|---|---|
| Planet Fitness (PLANET FITNESS, 2438677) | PLANET FITNESS FRANCHISING LLC, Delaware LLC | **Planet Fitness, Inc.** (public). Its 8-K of 2025-12-12 names "Planet Fitness Franchising LLC" among the Guarantors. The Guarantors are "wholly-owned direct and indirect subsidiaries of the Master Issuer", which is "a limited-purpose, bankruptcy remote, indirect subsidiary of the Company". The notes are secured by assets including "intellectual property and license agreements". [PF-8K] | Subsidiary of the filer (a securitization guarantor) |
| Dunkin' (DUNKIN', 4290078) | DD IP Holder LLC, Delaware LLC | **Inspire Brands**, which "today announced the completion of its $11.3 billion acquisition of Dunkin' Brands Group, Inc." (2020-12-15). "Inspire is majority-owned by affiliates of Roark Capital." [INSPIRE-PR] Dunkin' Brands' FY2019 10-K lists "DD IP Holder LLC" (Delaware) among its subsidiaries. [DNKN-EX21] | IP subsidiary; sponsor not named at USPTO |
| Subway (SUBWAY, 1174608) | SUBWAY US IP HOLDER LLC, Delaware LLC | **Affiliates of Roark**: "Subway … today completed its previously announced sale to affiliates of Roark" (2024-04-30). [SUBWAY-PR] No primary source besides USPTO links the IP holder to Subway or Roark. | IP subsidiary; sponsor not named |
| Jersey Mike's (JERSEY MIKE'S, 1993656) | JERSEY MIKE'S FRANCHISE SYSTEMS, INC., New Jersey corporation | **Blackstone funds, majority (agreed).** The 2024-11-18 Business Wire release (from search-index text; direct fetch got HTTP 403 / connection error) says Blackstone's flagship private equity vehicle "will acquire a majority ownership position", expected to close in early 2025. [JM-PR] **Closing: unconfirmed** by a primary source. | **Owner field disagrees with the assignment record** (see notes) |
| Warby Parker (WARBY PARKER, 3908784) | WARBY PARKER INC., Delaware corporation | **Warby Parker Inc.** (public). The FY2025 10-K registrant is "Warby Parker Inc."; its trademarks "are the property of Warby Parker Inc." [WRBY-10K] | Exact match |
| Arby's (ARBY'S, 1065886) | ARBY'S IP HOLDER, LLC, Delaware LLC | **Inspire Brands.** The same 2020 release lists Arby's in Inspire's portfolio and says Inspire is majority-owned by Roark affiliates. [INSPIRE-PR] No primary source besides USPTO links the IP holder to Inspire. | IP subsidiary; sponsor not named |
| Crunch Fitness (CRUNCH, 1809668) | CRUNCH IP HOLDINGS, LLC, Delaware LLC | **Leonard Green & Partners, majority (agreed).** Crunch Holdings, LLC release of 2025-04-15: "LGP will acquire a majority interest in Crunch Fitness from TPG Growth". [LGP-PR] **Closing: unconfirmed** by a primary source. | IP subsidiary; sponsor not named |
| Burger King (BURGER KING, 1057250) | BURGER KING COMPANY LLC, Florida LLC | **Restaurant Brands International** (public). FY2025 10-K: "Burger King®, Whopper®, and BK® are trademarks of Burger King Company LLC". Exhibit 21.1 lists "Burger King Company LLC" under U.S.A. [QSR-10K] | Named subsidiary of the filer |

Per-brand notes, from the assignment abstracts [observed]:

- **Planet Fitness.**
  - 13 recorded documents: PLANET FITNESS, INC. → PLANET FITNESS ENTERPRISES, INC. (2001) → PFIP, LLC (2002) → PLANET FITNESS FRANCHISING LLC (executed 2018-08-01).
  - Security interests, each later released: Praesidian Capital (2006), TD Banknorth (2008), GE Capital (2010), JPMorgan (2014).
  - Latest: SECURITY INTEREST to CITIBANK, N.A., recorded 2018-08-02.
- **Dunkin'.**
  - 3 recorded documents for this mark: Barclays security interest (2013), its release (2015), and SECURITY INTEREST from DD IP HOLDER, LLC to CITIBANK, N.A. (2018-07-13).
  - Nothing records the 2020 Inspire acquisition.
  - A related mark shows how the owner field can freeze. DUNKIN' DONUTS, reg. 897088, was assigned to DD IP HOLDER LLC in 2006 (reel/frame 3317/0707), yet TSDR still shows "DUNKIN'DONUTS USA, INC". That registration was cancelled 2016-04-01.
  - The same pattern appears for ARBY'S, reg. 890565 (owner "ARBY'S INC.", cancelled 2016-04-01).
- **Subway.**
  - Chain: DOCTOR'S ASSOCIATES INC. → SUBWAY IP INC. (2016) → ENTITY CONVERSION to SUBWAY IP LLC (2018) → SUBWAY US IP HOLDER LLC (executed 2024-06-20, about seven weeks after the Roark closing).
  - Same date: "NOTICE OF GRANT OF BACK-UP SECURITY INTEREST IN TRADEMARKS", then SECURITY INTEREST to CITIBANK, N.A. (recorded 2024-06-28).
  - Roark does not appear.
- **Jersey Mike's.**
  - On 2019-12-23 a "U.S. TRADEMARK ASSIGNMENT" from JERSEY MIKE'S FRANCHISE SYSTEMS, INC. to A SUB ABOVE, LLC (Delaware) was recorded (reel/frame 6825/0315). The same day: a back-up security interest to A SUB ABOVE, LLC, and a security interest from A SUB ABOVE, LLC to CITIBANK, N.A.
  - TSDR prosecution history shows "ASSIGNMENT OF OWNERSHIP NOT UPDATED AUTOMATICALLY" on 2020-01-15 and 2020-06-24.
  - The owner field still shows Jersey Mike's Franchise Systems, Inc., and the registration was renewed with status date 2025-12-09.
  - Assignment Search lists A SUB ABOVE LLC as the current owner of other Jersey Mike's marks (e.g. A SUB ABOVE, reg. 4766065). Their TSDR pages were not fetched.
  - Nothing records the Blackstone deal.
- **Warby Parker.**
  - CHANGE OF NAME, JAND, INC. → WARBY PARKER INC. (executed 2021-06-14, recorded 2021-10-14).
  - Security interests: Comerica (2022, released 2024), then JPMorgan (2024).
- **Arby's.**
  - 40 recorded documents since 1991, including a 1994 MERGER and CHANGE OF NAME.
  - A 2015-11-13 sequence ran ARBY'S IP HOLDER TRUST → ARBY'S RESTAURANT GROUP, INC. → ARBY'S SPV GUARANTOR, LLC → ARBY'S FUNDING, LLC → ARBY'S FRANCHISOR, LLC → ARBY'S IP HOLDER, LLC, then a SECURITY INTEREST to CITIBANK, N.A.
  - Neither Roark nor Inspire appears.
- **Crunch.**
  - 22 recorded documents: CRUNCH WORLD → CRUNCH FITNESS INTERNATIONAL (1998) → CRUNCH CFI, LLC (2006) → CRUNCH IP HOLDINGS, LLC (executed 2009).
  - Lenders, in order: JPMorgan, Goldman Sachs Credit Partners, CH Fitness Investors, Bank of America, Piper Jaffray Finance (2019), GOLUB CAPITAL MARKETS LLC (2024-09-27).
  - On 2025-06-12, a security interest to "GOLUB CAPITAL MARKET LLC" and a release from GOLUB CAPITAL MARKETS LLC were both recorded.
  - Neither TPG nor LGP appears.
- **Burger King.**
  - BURGER KING CORPORATION → BURGER KING BRANDS, INC. (executed 1990) → back to BURGER KING CORPORATION (2009) → BURGER KING COMPANY LLC (2022).
  - Many first- and second-lien security agreements to JPMorgan and Wilmington Trust as collateral agents.
  - Latest: "FIRST LIEN INTELLECTUAL PROPERTY SECURITY AGREEMENT (2024)" to Wilmington Trust.

**What the eight checks show (facts only):**
- 0 of 8 registered owners name a private-equity sponsor.
- 4 of 5 sponsor-owned brands are held by entities named "… IP Holder" / "… IP Holdings"; the fifth is the franchisor entity.
- None of the 4 sponsor deals named above (Inspire/Dunkin', Roark/Subway, Blackstone/Jersey Mike's, LGP/Crunch) appears in the USPTO records.
- All 8 marks have recorded security interests that name lenders or collateral agents.

Owner sources:
- [PF-8K] Planet Fitness, Inc. Form 8-K, report date 2025-12-12: https://www.sec.gov/Archives/edgar/data/1637207/000163720725000088/plnt-20251212.htm
- [INSPIRE-PR] Inspire Brands, *Inspire Brands Completes Acquisition of Dunkin' Brands*, 2020-12-15: https://inspirebrands.com/inspire-brands-completes-acquisition-of-dunkin-brands/
- [DNKN-EX21] Dunkin' Brands Group, Inc. FY2019 10-K Exhibit 21.1: https://www.sec.gov/Archives/edgar/data/1357204/000135720420000015/dnkn-ex211subsidiaries.htm
- [SUBWAY-PR] Subway, *Subway® Sale to Roark is Complete*, 2024-04-30: https://newsroom.subway.com/2024-04-30-Subway-R-Sale-to-Roark-is-Complete
- [JM-PR] Jersey Mike's / Blackstone, *Jersey Mike's to Partner with Blackstone…*, Business Wire 2024-11-18: https://www.businesswire.com/news/home/20241118982737/en/ (also https://www.blackstone.com/news/press/jersey-mikes-to-partner-with-blackstone-to-accelerate-leading-franchisors-continued-growth/). Both refused direct fetches. The wording above comes from search-index text.
- [WRBY-10K] Warby Parker Inc. FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1504776/000150477626000006/wrby-20251231.htm
- [LGP-PR] Crunch Holdings, LLC release on Leonard Green's site, 2025-04-15: https://www.leonardgreen.com/crunch-fitness-announces-strategic-investment-from-leonard-green-partners/
- [QSR-10K] Restaurant Brands International Inc. FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1618756/000161875626000017/qsr-20251231.htm ; Exhibit 21.1: https://www.sec.gov/Archives/edgar/data/1618756/000161875626000017/ex211qsr_20251231x10k.htm

TSDR records used (status page `https://tsdr.uspto.gov/statusview/rn{N}`, abstract `https://tsdr.uspto.gov/assignments/{SN}?searchprefix=sn`):

| Mark | Reg. no. | Serial no. |
|---|---|---|
| PLANET FITNESS | 2438677 | 74435592 |
| DUNKIN' | 4290078 | 85494887 |
| SUBWAY | 1174608 | 73021264 |
| JERSEY MIKE'S | 1993656 | 75002269 |
| WARBY PARKER | 3908784 | 77792561 |
| ARBY'S | 1065886 | 73083231 |
| CRUNCH | 1809668 | 74363506 |
| BURGER KING | 1057250 | 73076655 |
| DUNKIN' DONUTS (cancelled) | 897088 | 72301212 |
| ARBY'S (cancelled) | 890565 | 72268358 |

## 6. Candidate citable units under the RawDocument rule

The RawDocument rule is one document per smallest citable unit. Bulk rows are stored as header line + row line ([engine/01](../../engine/issues/01-rawdocument-shape.md)). These are the units USPTO data offers. The choice is the developer's.

| Candidate unit | Key | What it states | Facts that bear on it |
|---|---|---|---|
| One recorded assignment (`<assignment-entry>` in the daily assignments XML) | reel/frame | Who conveyed what to whom, when executed and recorded, and which serial/registration numbers it covers | XML, not line-based, so "header line + row" doesn't map directly. No mark text. One entry can cover many marks. Can later change (`last-update-date`, `purge-indicator`). [U-ASGDTD] |
| One case file (`<case-file>` in the daily applications XML) | serial number | Mark text, status, owner entries by party type | XML. Whether one entry is flagged "current" is unconfirmed (section 3). [U-APPDOC] |
| One TSDR status record (API `info.xml`, or the web page) | serial number | "Current Owner(s) Information" as of the fetch | The API needs a key. The web page embeds a generation timestamp, so every fetch has a new sha. [observed] |
| One TSDR assignment abstract | serial number | The full recorded chain for one mark | Web endpoint; grows over time. [observed] |
| One recorded document image | reel/frame | The signed instrument itself | Image-only PDF with no text layer (one sample); quoting it verbatim would need OCR. [observed] |
| Research CSV rows (`tm_assignment`, `tm_assignee`, `tm_docid`, …) | `rf_id` (+ serial) | The same assignment data, normalized | Fits "header + row", but one fact spans rows in several files. Yearly and about 2 years stale. [U-ECON-ASG] |

## 7. Open questions for the developer (facts only, no recommendation)

1. **Adopt USPTO as a source type?** Facts that bear on it:
   - USPTO is the federal register for marks.
   - The data is marked public domain. [U-DJ]
   - Access now needs a USPTO.gov sign-in (website), an ID.me-linked ODP key (ODP API), or a TSDR key (TSDR API). [U-REG][ODP][U-TSDRFAQ]
2. **Does it self-verify (join the official list)?** Facts:
   - Recording is "ministerial" and not a validity check. [37 CFR §3.54; U-TMEP §503.01(c)]
   - The owner field updates without checking chain of title. [§504]
   - The owner field can disagree with recorded assignments (Jersey Mike's) or stay frozen on dead registrations (DUNKIN' DONUTS 897088).
   - Party data is "supplied by the submitter". [U-ASGDTD]
   - In 7 of 8 checks the registered owner was a brand-level entity (IP holder, franchisor or named subsidiary), not the top company. Only Warby Parker matched the parent exactly. The sponsor was never named.
3. **One source type or two?** ADR 0003 counts publisher datasets. Facts:
   - TMEP describes two databases: the Assignment database (Assignment Recordation Branch) and the Trademark database. Corrections to one are not automatically reflected in the other. [U-TMEP §§504.02, 504.03]
   - But the owner field is fed weekly from the assignment records. [§504.02] The two are not independent of each other.
4. **What would a USPTO claim attach to?** A mark is not a business entity. The registered owner here is an IP subsidiary, and no recorded document links it to the operating parent or sponsor. That link came from SEC filings (Planet Fitness, Dunkin', Burger King) or from no primary source at all (Subway, Arby's, Crunch, Jersey Mike's). How marks, IP subsidiaries and brands relate is a brand-model question (ticket 53).
5. **Security interests.** Every chain checked records secured parties: Citibank, N.A., JPMorgan, Wilmington Trust, Golub Capital Markets LLC, and others. Whether these feed any relationship (`lends_to` or otherwise) is a schema decision. Note that the "secured party" is often an agent or trustee, not the lender of record.
6. **Using the web endpoints.** Whether to use them (TSDR status page, Assignment Search backend) or only the keyed APIs and bulk files is a sourcing-rule question. [U-TOU] discourages high-volume use of the web databases.

## 8. Unconfirmed, and why

- **Current daily file sizes and the exact annual-product coverage:** behind the ODP sign-in; developer.uspto.gov now redirects.
- **ODP rate limits, ID.me and profile-field wording:** ODP pages render only with JavaScript and were read through search-index text, not fetched.
- **Whether the applications XML flags one owner as current, and the post-2003 party-type codes:** the 2012 PDF table did not extract past code 27; the current documentation (v2.3, 2025-08-13) is behind sign-in.
- **Whether a TSDR API key now needs ID.me:** no USPTO page found says either way.
- **Meaning of the research dataset's `conv_group` codes:** not read.
- **Closing of the Blackstone/Jersey Mike's and LGP/Crunch deals:** only news reports were found, no primary closing release. The Jersey Mike's announcement itself was read only through search-index text (HTTP 403).
- **Terms and limits of the Assignment Center "Trademark export data (API for developers)":** not documented on any page read.
