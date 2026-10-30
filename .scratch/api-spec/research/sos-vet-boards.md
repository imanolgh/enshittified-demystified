# SoS registries and vet license boards in the shortlisted launch states: research findings

Ticket: [11-research-sos-vet-boards](../issues/11-research-sos-vet-boards.md). Researched 2026-10-29.
States: **New York** (fixed), plus candidates **Florida, Colorado, Texas, Arizona**.

## How this was sourced (read first)

- **Primary sources only.** These are official state sites, statute text from the legislatures' own sites, and dataset metadata served by the state open-data portals' own APIs (`/api/views/<id>.json`, Socrata catalog API).
- **"Observed"** marks facts I measured from the live data, such as row counts from `$select=count(*)` or files I downloaded and counted. They are measurements, not agency documentation.
- **Unreachable or not fetched:**
  - `vetboard.az.gov` returned HTTP 403 to automated fetches, and `archivevetboard.az.gov` did not resolve (DNS). I did not try to get around either block.
  - `www.op.nysed.gov` and `www.nysed.gov` failed TLS verification in the fetch tool ("unable to verify the first certificate"). I read them with curl and certificate checking turned off. The content is the agencies' own pages.
  - The NYSED verification app's back-end API (`api.nysed.gov/rosa/…`) was **not called**. I only read the app's served JavaScript.
- Anything I could not confirm from a primary source is marked **Unconfirmed**.

---

## 1. New York (fixed launch state)

### 1a. SoS: NY Department of State, Division of Corporations

**Access: free, bulk, with an API.** The DOS publishes its corporation database on the state open-data portal, data.ny.gov (Socrata). Every dataset supports CSV/JSON export and the SODA API.

| Dataset (id) | What it holds | Cadence (portal metadata) | Rows (observed 2026-10-29) |
|---|---|---|---|
| Active Corporations: Beginning 1800 ([n9v6-gdp6][ny-active]) | One row per **active** entity | "Monthly" | 4,307,766 |
| Corporations and Other Entities: All Filings ([63wc-4exh][ny-all]) | Every filing in the DOS electronic database | "Weekly" | 21,054,231 |
| …All Filings – Address ([2tms-hftb][ny-addr]) | Addresses from each filed document | Weekly | 18,616,326 |
| …All Filings – Name Status History ([ekwr-p59j][ny-name]) | Current and **previous names** per entity | Weekly | 7,526,295 |
| …All Filings – Entity Status History ([3gg2-jgnp][ny-status]) | Status after each filing | Weekly | 21,054,231 |
| …All Filings – Constituent ([dnbf-xifz][ny-const]) | **Non-surviving merger/consolidation constituents** | Weekly | 92,601 |
| Daily Corporation and Other Entity Filing Data ([k4vb-judh][ny-daily]) | Filings processed in the previous 30 days | "Daily" | 93,229 |

The portal catalog also lists `…Stock` (kiwr-v7e8) and `…Limited Partnerships` (bvn2-rs8p).

**Fields, from the portal's column metadata:**
- **Active Corporations:** `dos_id`, `current_entity_name`, `initial_dos_filing_date`, `county`, `jurisdiction`, `entity_type`. It also has `dos_process_*` (the service-of-process name and address), `chairman_*` (name and address), `registered_agent_*` and `location_*` (principal location) ([n9v6-gdp6 metadata][ny-active-meta]).
  - Fill rates observed: `chairman_name` is filled on 471,767 of 4.3M rows, `registered_agent_name` on 883,955, and `location_*` on about 350k.
  - The metadata caveats say: "Current Entity Name: Contains only the name by which the corporation is currently known." Also: "This data does not include information on inactive corporations." Also: "Service of Process Address … may not reflect the physical location of the corporation or any of its officers."
- **All Filings:** `corpid_num`, `film_num`, `date_filed`, `eff_date`, `entitytype`, `documenttype`, `law`, `corp_name`, `fict_name`, `juris`. It also carries amendment flags (`amd_corp_name_flag`, `amd_reg_agt_flag`, `amd_chair_flag`, …) and `constituent_flag` ([63wc-4exh metadata][ny-all-meta]).
- **Daily filings:** filing type, `dos_id`, `corp_name`, **`pre_corp_name`** (prior name), **filer name and address**, service-of-process name and address, and **`mrgr_const_name1..3`** (merger constituents) ([k4vb-judh metadata][ny-daily-meta]).
- **Address dataset:** `addr_type` takes the values 1–4 or blank (observed counts: 10.9M / 1.95M / 2.6M / 1.5M / 1.6M blank). **What the codes mean is not documented in the metadata. Unconfirmed.**

**Officers and managers.** There is no officer or manager roster. The only person-level fields are the corporate **chairman/CEO** (`chairman_*`) and filer names. NY LLCs carry no member or manager names in these datasets. *Observed:* LLCs are the largest entity type, with 2,070,692 domestic LLCs among the active entities.

**Vet- and dental-relevant entity types** (observed counts of active entities): Domestic Professional Service Corporation 60,258, and Domestic PLLC 54,123. NY Education Law §6706 bars business corporations other than professional service corporations from being "organized for the practice of veterinary medicine" ([EDN §6706][ny-6706]).

**Terms.** Datasets carry no per-dataset license (`license: null`). The portal-wide **OPEN-NY Terms of Use** (last modified March 8, 2013) govern them ([OPEN-NY ToU PDF][ny-tou]):
- The preamble says: "do not contain restrictions requiring members of the public to use attribution … impose share-alike or technical restrictions, nor require … pre-approval before re-use". Also: "So long as you are not doing anything malicious with NYS data, you may use it as you wish."
- The license grant: "a non-exclusive, revocable license to use the Content".
- The ToU also say: "You must not create accounts with OPEN-NY or access the site through unauthorized means, including … by using an automated device, script, bot, spider, crawler or scraper."
  - That bullet sits under the **"Public Participation"** heading, which covers uploading and commenting.
  - Whether it also applies to read-only SODA API use is **not stated**. The portal does publish an API for every dataset.
  - **Unconfirmed / for the developer:** how this bullet applies to automated API reads.

**Captcha and rate limits.** No captcha appears on the API. Socrata's per-app-token throttling terms were not researched. **Unconfirmed.**

### 1b. Vet board: NYSED Office of the Professions (OP)

**Licensing unit.** NY licenses **individual veterinarians and veterinary technicians only**. Education Law Article 135 (§§6700–6715) has no premises or facility licensing section. Its sections cover the definition of practice, licensing, the board, exemptions, corporate practice (§6706), limited permits, vet techs, treatment records and dispensing ([EDN Art. 135 index][ny-a135]).
- Licensees must register each practice location. OP's FAQ #11 says a licensee needs a registration certificate per office, and additional offices are registered through the Registration/Fee Unit ([OP FAQ][op-faq]).
- That gives a per-licensee office list inside OP. Whether it is publicly released is **unconfirmed**.
- **Registered counts** as of April 1, 2024: Veterinary Medicine 7,803 and Veterinary Technology 6,355 ([OP statistics 2024][op-stats]).

**Online search.**
- The search is a JavaScript app at `eservices.nysed.gov/professions/verification-search`. Its "About" text, from the served bundle ([vsc.js][op-vsc]), says the data is "from the Office of Professions' official database and is updated daily, Monday through Friday."
- The licensee view renders an `address` element. Whether this is a full practice address or only city/state is **unconfirmed**, because the API was not called.
- A third-party summary states that results show name, profession, license number, location, original license date and registration status. **Unconfirmed from an OP page.**

**Bulk files exist on request (key finding).** The same served bundle carries this "Download" text ([vsc.js][op-vsc]):
- "The Department is developing an Application Programming Interface (API) solution to allow institutions to timely and efficiently obtain bulk verification of NYS licensees."
- "In the interim, to request bulk verification files of currently registered NYS licensees, please submit a Bulk Verifications Request Form ([op-support form][op-bulk]) … Once your request is processed, you will be given access to these files, **which are updated weekly**."
- **Unconfirmed:** who qualifies (the text says "institutions"), the fields in the files (practice address or not), cost, and reuse terms.

**Terms on nysed.gov.** The NYSED Terms of Use grant permission to copy materials "for personal, private and educational purposes, except that reproducing materials for profit or any commercial use is strictly forbidden without express prior written permission" ([NYSED ToU][nysed-tou]). Whether licensee *data* counts as such "materials" is **unconfirmed**. No ToU text specific to automated use of the verification search was found.

### 1c. FOIL fallback for the NY licensee list

- **Office.** FOIL requests go to the NYSED **Records Access Officer**, 89 Washington Ave, Room 144 EB, Albany NY 12234. Channels are the online FOIL form or `FOIL@nysed.gov`. Appeals go to `FOILappeal@nysed.gov` within 30 days ([NYSED FOIL page][nysed-foil]).
- **Cost.**
  - NYSED charges "$.25 per page for photocopies"; "Additional copy preparation fees may apply as permitted by law" ([NYSED FOIL][nysed-foil]).
  - Statute: for electronic records the agency may charge only actual cost. That is the hourly salary of the lowest-paid capable employee plus media. "No fee shall be charged unless at least two hours of agency employee time is needed," and search time is excluded ([POL §87(1)(b)–(c)][pol87]).
- **Turnaround** (statute). The agency must grant, deny or acknowledge within **5 business days**. If it grants, it must deliver within **20 business days** of acknowledgment or give a written reason and a date certain ([POL §89(3)(a)][pol89]).
- **Limit that matters.** POL §89(2)(b)(iii) defines "sale or release of lists of names and addresses if such lists would be used for solicitation or fund-raising purposes" as an unwarranted invasion of privacy. Under §89(3)(a), the agency "may require a person requesting lists of names and addresses to provide a written certification" that the list will not be used or resold for solicitation or fund-raising ([POL §89][pol89]).
- **Fields.** Which fields NYSED would release (practice address vs mailing address) is **unconfirmed**. No NYSED page states it.
  - OP's own written-verification page says documents released under FOIL "can only be released to the initial requestor, NOT third parties" ([OP written verification][op-written]).
  - That sentence is about a licensee's own application materials. Whether it also covers a licensee roster is **unconfirmed**.
- **Recommended next step** (fact-finding, not a decision): file one FOIL request naming the veterinarian and vet-tech professions and asking for name, license number, status, and registered practice/office address(es). This would settle the fields, cost and timing empirically. Separately, submit the Bulk Verifications Request Form above.

---

## 2. Florida

### 2a. SoS: Florida Department of State, Division of Corporations (Sunbiz)

**Access: free bulk files.**
- "The Division of Corporations offers **free data downloads** for informational purposes. Downloads are offered as is and may be changed, replaced or deleted at any time."
- Host: `https://sftp.floridados.gov`. Public credentials are published on the page itself (user `Public`) ([Data Downloads][fl-dd]).
- **Daily** files: "generated on work days and contain the filings added to our record that day", for example `doc/cor/yyyymmddc.txt` and events `doc/cor/events/yyyymmddce.txt` ([Daily Data][fl-daily]).
- **Quarterly** full files are "generated quarterly in January, April, July, and October" and contain "all data on record at the time the file is generated".
  - Corporate: `doc/quarterly/cor/cordata.zip` (split into 10 files by last digit) plus `corevent.zip`.
  - Fictitious names: `ficdata.zip` plus `ficevt.zip` ([Quarterly Data][fl-qtr]).
- **Format:** fixed-width ASCII with no headers. The document number (6 or 12 characters) is the unique key ([Data Usage Guide][fl-guide]).

**Fields** ([Corporate File Definitions][fl-cor]). This is a 1,440-character record. It holds:
- corporation number, name, and status A/I;
- filing type (DOMP, FLAL = Florida LLC, FORL, …);
- principal and mailing addresses, file date, FEI number, and last transaction date;
- three annual-report years;
- **registered agent** name, type and address;
- **up to 6 officers**, each with title, type (person or corporation), name and address, plus a "More than six Officers" flag.

Caveat: "data for addresses and listed officers may not reflect the most current information on sunbiz.org because of the limited space in the file."

**Event file** (662 characters) carries event code and description, effective and filed dates, a **conversion/merger number**, and **name-change flags**. "Some corporate filings such as annual reports or address changes, are not considered events" ([cor.html][fl-cor]).

Officer title codes are listed as P/T/C/V/S/D. Whether LLC manager/member titles (for example MGR or AMBR) appear in the 4-character title field is **unconfirmed**; no file was downloaded.

**Terms.**
- The data page calls the files free and "for informational purposes".
- **Tension, flagged for the developer:** the Florida DOS site-wide "Copyright | Terms of Use" says no material "may be copied, reproduced, republished … or distributed in any way, except that you may download the materials on any single computer for your personal, non-commercial use only" ([DOS ToU][fl-tou]).
- Florida's Ch. 119 public-records regime applies to state agency records generally. Which instrument governs the bulk corporate files is **unconfirmed**. The data pages do not reference the site ToU.
- No captcha is mentioned for SFTP. Rate limits were not documented.

### 2b. Vet board: DBPR Board of Veterinary Medicine

**Licensing unit: individuals AND premises.**
- F.S. §474.215(1): "Any establishment, permanent or mobile, where a licensed veterinarian practices must have a **premises permit** issued by the department."
- §474.215(2): the application "shall set forth the name of the licensed veterinarian who will be responsible for the management of the establishment and **the name and address of the owners** of the establishment" ([F.S. 474.215][fl-474215]).

**Download: free CSV, refreshed weekly.**
- The board's Public Records page links `https://www2.myfloridalicense.com/sto/file_download/extracts/lic26vt.csv`. It covers "Active, inactive and voluntarily inactive licensees. NULL & VOID, delinquent and involuntarily inactive records are not included" ([Vet Public Records][fl-vetpr]).
- Columns: Board Number, Occupation Code, Licensee Name, **Doing Business As Name**, Class Code, Address Lines 1–3, City, State, Zip, County Code, License Number, Primary Status, Secondary Status, Original Licensure Date, Effective Date, Expiration Date, Renewal Period, Alternate Lic# ([Vet Public Records][fl-vetpr]).
- DBPR's disclaimer: "Under Chapter 119 … the DBPR provides copies of electronic records to the public through **free download** … Although **data is refreshed weekly**…" ([Public Records ReadMe/Disclaimer][fl-disc]).

**Occupation codes for Board 26** ([Understanding DBPR Codes][fl-codes]): VM Veterinarians, **VE Veterinarian Establishment**, VL Ltd Service Veterinary Practice, **OR Veterinary Owner**, CLIN Clinic Location, plus PVDR and CRSE (course providers and courses).

**Observed** (file last-modified 2026-10-24, 16,667 rows, 22 columns):

| Occupation code | Rows |
|---|---|
| VM | 11,353 |
| VE | 3,141, of which 2,489 have a FL address |
| OR | 511 |
| VL | 67 |

- VE rows carry the clinic name, DBA, practice street address and county. Examples include `GOODVETS BOYNTON BEACH`, and `MESA CREEK VETERINARY GROUP, LLC.` with DBA `AVC OF PASCO`.
- **Unconfirmed:** OR rows (owner name and address) carry no visible link to the establishment they own.
- Some VE rows have the responsible-DVM name shifted into the address columns, so address parsing needs care.
- The extract does not include the §474.215(2) owner name and address for each establishment. That would need a Ch. 119 request (**unconfirmed** whether it would be released).

---

## 3. Colorado

### 3a. SoS: Colorado Department of State (CDOS), via data.colorado.gov

**Access: free bulk data with an API, licensed Public Domain.**
- [Business Entities in Colorado (4ykn-tg5h)][co-ent]: portal metadata `license: Public Domain`, "Update Schedule: Every day after midnight" ([metadata][co-ent-meta]). *Observed* rows: 3,130,907.
- **Fields:** `entityid`, `entityname`, principal and mailing addresses, `entitystatus`, `jurisdictonofformation`, `entitytype`, **registered agent** (name or organization, principal and mailing addresses), `entityformdate`.
- **No officers or managers.** The metadata's prose mentions "owner name, owner address", but no owner column exists in the schema (**unconfirmed what that phrase refers to**).
- [Business Entity Transaction History (casm-dbbj)][co-hist]: Public Domain, daily. *Observed* rows: 21,790,618. Fields: `entityid`, `transactionid`, `historydes`, `comment`, `receiveddate`, `effectivedate`, `name`.
  - The metadata says: "Popular types of transactions include Origination Articles, Amendments, Periodic Reports, **Mergers**, Dissolutions, Statement of Change." So mergers and name changes appear as free-text history rows, not structured links.
- Related sets: Trade Names (u7sb-g482), New business Entities (rd36-7474), and "Statement Curing Delinquency, Change, and Correction" (jcns-5st4) ([catalog][co-cat]).
- The portal's point of contact is "Business Intelligence Center of CO" (`bic-help@xentity.com`) on CDOS's behalf.
- Captcha and rate limits apply only to the Socrata API, and those terms were not researched. **Unconfirmed.**

### 3b. Vet board: DORA Division of Professions and Occupations, State Board of Veterinary Medicine

**Licensing unit: individuals only.**
- No premises license was found. C.R.S. §12-315-122 requires that "a licensed veterinarian must be designated as responsible for the premises." It also lets the board fine "a corporation … that owns or operates a veterinary premises," which is a designation duty, not a registration ([C.R.S. 12-315-122 text][co-122]). I read the statute on colorado.public.law, a mirror of the C.R.S. The official C.R.S. PDF was not fetched.
- **Unconfirmed** that no facility registration exists anywhere in Title 12 Article 315 or in board rules.

**Download: free bulk data with an API, licensed Public Domain, updated daily.**
- Source: [Professional and Occupational Licenses in Colorado (7s5z-vewr)][co-lic] ([metadata][co-lic-meta]).
- *Observed* license types: VET 14,057 (all statuses), T-VET 4, MSVET 10, DEN 16,040.
- **Fields:** name, `entityname`, **city, state, mail zip only (no street address)**, license type and number, issue, renewal and expiry dates, status, discipline fields, and a verification link.
- A vet *clinic* census is therefore not possible from this source. It gives only licensee counts by city or zip.

---

## 4. Texas

### 4a. SoS: Texas Secretary of State (SOSDirect / SOSPortal)

**Access: paid only.**
- SOSPortal search: "There is a $1.00 statutorily authorized fee associated with each search" ([SOSDirect page][tx-sosd]).
- **Bulk order** ([Business Filings Bulk Order][tx-bulk]):
  - Master Unload: **$1,350**
  - Daily Filing Update: **$60 per day** (orderable for the past 30 days)
  - Weekly Filing Update (new formations only): **$20 per week** (past 8 weeks)
  - An SOSPortal account is required. Files stay downloadable for 90 days.
- **Format: JSON** ([JSON record layout spec v1.2][tx-spec]). Each filing package contains:
  - `masterEntityRecord` and `masterAddressRecord`
  - `regAgentBusinessRecord` / `regAgentPersonalRecord` (registered agent)
  - `charterOfficerBusinessRecord` / `charterOfficerPersonalRecord` (0..n **officers/managers**)
  - `charterNamesRecord` (**names**, including prior names)
  - `associatedEntityRecord` (0..n, likely **merger/conversion** links; semantics **unconfirmed**)
  - `filingHistoryRecord` and `auditLogRecord`
- **Terms.** The portal's Rules of Use cover monitoring and "unauthorized or improper use". No redistribution clause was seen ([Rules of Use][tx-tac]). **Fails selection criterion 1 (not free).**
- **Free partial alternative:** the Texas Comptroller's [Active Franchise Taxpayers (9cir-efmm)][tx-ft] on data.texas.gov.
  - *Observed* rows: 3,494,999.
  - Fields: taxpayer number, name, address, county, organizational type, **SOS file number**, SOS charter date and status, and NAICS-like code `_621111`.
  - No registered agent, officers or merger data. No dataset license is set (`license: null`).

### 4b. Vet board: Texas Board of Veterinary Medical Examiners (TBVME)

**Licensing unit today: individuals only.**
- The public tool is the [Licensee Lookup][tx-lookup], a Salesforce-style web app. It is searchable by license number and status, name, city, zip, county and **Practice Name** ([License Verifications page][tx-verif]).
- No downloadable list was found on the board site. The Public Information Act route is `openrecords@veterinary.texas.gov` (linked from [veterinary.texas.gov][tx-vethome]); fields and cost are **unconfirmed**.

**Facility registration is coming (key finding).** SB 2155 (89th Leg., R.S.) was signed by the Governor on 06/20/2025 ([bill history][tx-sb2155h]). It adds Occupations Code Subchapter M, "Veterinary Medical Facilities" ([enrolled text][tx-sb2155]):
- §801.601(a): veterinary medicine "shall be practiced only in or from a veterinary medical facility that is registered with the board", unless exempted by rule.
- §801.602(b)(1): the application must "indicate the type of business entity that provides services at the facility, and provide information regarding the **owners, partners, and operators** of the entity, **including a management services organization** that contracts with the facility."
- Sec. 41: "A veterinary medical facility shall register with the board not later than **September 1, 2027**." Sec. 42(b): Subchapter M takes effect September 1, 2026.
- The TBVME announcement of July 17, 2025 says the board plans to "propose rules regarding facility registration in Fall of 2026", with the portal opening "Summer 2027" ([TBVME announcement][tx-ann]).
- Whether the facility list, or the owner/MSO data, will be published or downloadable is **unconfirmed**. The announcement does not say.

---

## 5. Arizona

### 5a. Entity registry: Arizona Corporation Commission (ACC), not the Secretary of State

**Access: search UI only; no bulk file found.**
- The ACC replaced eCorp with the **Arizona Business Center**: "Arizona Business Center goes live on Monday, January 12, 2026" ([ACC Corporations notices][az-notice]). `ecorp.azcc.gov` now redirects to `arizonabusinesscenter.azcc.gov` (observed).
- No bulk-data or open-data product appears on the ACC Corporations pages ([azcc.gov/corporations][az-corp]). A vendor's API docs also say none exists; that claim is not primary.
- **Fields** (observed in the served Angular bundle, not documented): principal types include Director, Principal, Other Officer, Member, Manager, Member and Manager, Incorporators, and Board of Directors. So **officers, members and managers** are displayed.
- **Captcha.** The bundle sends an `X-reCAPTCHA-Token` header on public document view/download calls (observed). Whether the entity *search* itself is captcha-gated is **unconfirmed**.
- **Public records route** ([ACC Public Records Request][az-prr]):
  - "Requests for customized reports and/or data may be denied," and "a statement of commercial use" is required where applicable.
  - Commercial requests are charged under A.R.S. §39-121.03(B), including "the value of the reproduction on the commercial market." Commercial labor is $30/hour and scans 30 cents per page. Response time is "up to 30 days."
- **Fails selection criterion 1.**

### 5b. Vet board: Arizona State Veterinary Medical Examining Board

**Licensing unit: individuals AND premises.**
- A.R.S. §32-2272(A): "Any person who desires to establish premises at or from which veterinary services are offered to the public … shall file with the board an application for a **veterinary premises license**."
- §32-2272(B): the application must contain "the name of the **person owning the premises** and the name and signature of the veterinarian responsible" ([A.R.S. 32-2272][az-2272]).

**List access: unconfirmed (site unreachable).**
- `vetboard.az.gov` returned **HTTP 403** to this research, so I could not read it directly.
- Search-result snippets, which are not verified, say:
  - the online Licensee Directory is "temporarily unavailable while the Board moves to a new system";
  - an archived verification page had a "Search for a Premises / Crematory" option.
- Whether a downloadable licensee or premises list exists, its fields and its terms are all **unconfirmed**.

---

## 6. Rollup-density evidence (supporting only)

Registry roster counts are what decide the question (ticket 03). Primary-source evidence found:

- **Florida (observed from the DBPR VE extract, 2,489 FL establishments).** Case-insensitive name/DBA matches:
  - BluePearl 18, GoodVets 14, PetVet 7, VCA 6, Banfield 5, Veterinary Emergency Group 3, AVC/NVA/Thrive/Petco 1 each.
  - These are **lower bounds only**. Rollups often keep local clinic names, so name matching undercounts. They are not a density measure.
- **Texas.** SB 2155 §801.602(b)(1) makes registrants disclose "a management services organization that contracts with the facility." That is legislative evidence that MSO-run practice is a recognized pattern in TX, and from 2027 it will be a direct data source. No per-state density figure was found.
- **NY, CO, AZ.** No primary-source density evidence was found in this pass. **Unconfirmed.**
- **Dental.** I found no state-level primary-source DSO density figure for any of the five states. **Unconfirmed.**

---

## 7. Comparison against the selection rule

The selection rule (ticket 03, in order) is: (1) free, terms-permitted SoS bulk data or API; (2) a downloadable or scrapable vet licensee list; (3) rollup density evidence.

| State | (1) Free, terms-permitted SoS bulk/API | (2) Vet list downloadable/scrapable | Premises licensed? | (3) Rollup density evidence |
|---|---|---|---|---|
| **NY** | **Yes.** data.ny.gov SODA plus weekly full-filing sets (names, mergers, status history); OPEN-NY ToU permissive. Caveat: anti-bot bullet sits under "Public Participation". No officer/manager roster beyond chairman. | **Partial.** Online search only. Weekly bulk verification files are available "on request" via the OP form (eligibility, fields and terms unconfirmed). FOIL is the fallback (5/20 business days; actual-cost fees; possible no-solicitation certification). | **No** (individuals only; per-office registrations are internal) | None found |
| **FL** | **Yes, free.** SFTP daily plus quarterly fixed-width files with RA, 6 officers and merger/name-change events. **Terms tension:** DOS site ToU says personal non-commercial use. | **Yes.** Free weekly CSV including **VE establishments** with DBA and street address. | **Yes** (§474.215; owner name and address on the application) | Observed name matches (lower bound) |
| **CO** | **Yes.** data.colorado.gov, **Public Domain**, daily. RA included; **no officers/managers**; mergers only as history text. | **Yes**, but individuals only, city/zip, no street address. | **No** (designation only, §12-315-122; registration otherwise unconfirmed) | None found |
| **TX** | **No.** $1/search; bulk $1,350 master plus $60/day (JSON with officers, names, associated entities). Free Comptroller franchise-tax list is partial. | **No download found.** Web lookup only; PIA request route. | **Not yet.** Facility registration (with owners and MSO) required by **2027-09-01** | MSO disclosure in statute; no density figure |
| **AZ** | **No.** ACC Business Center search only (reCAPTCHA on documents); no bulk file; commercial records requests priced at market value. | **Unconfirmed** (board site 403; directory reportedly offline during system change) | **Yes** (§32-2272; owner on application) | None found |

**Reading the table (facts only; the choice is the developer's):**
- Only **NY, FL and CO** pass criterion 1. Of those, only **FL** has both a free SoS bulk feed and a free vet *establishment* list with street addresses. FL also has the open Florida DOS terms-of-use tension noted in §2a.
- **CO** passes 1 and 2 cleanly on license terms (Public Domain) but gives no clinic-level vet census.
- For **NY's** vet census, the choice is between the OP bulk-verification request and FOIL. Both are pending answers from NYSED.

## Unconfirmed / open

1. Whether the OPEN-NY "automated device … scraper" bullet applies beyond Public Participation, for example to SODA API reads.
2. NY `addr_type` code meanings in dataset 2tms-hftb.
3. NYSED bulk verification files: eligibility, fields (is practice address included?), cost and reuse terms.
4. NYSED FOIL: which licensee fields are released, whether a §89(3)(a) certification is demanded, and actual cost and turnaround in practice.
5. Which terms govern Sunbiz bulk files: the data page ("free … for informational purposes") vs the DOS site ToU ("personal, non-commercial use only") vs Ch. 119.
6. Whether FL Sunbiz officer title codes cover LLC managers and members.
7. FL DBPR: how OR (Veterinary Owner) rows link to VE establishments, and whether §474.215(2) owner data is releasable under Ch. 119.
8. CO: whether any vet facility registration exists in rules. The meaning of "owner name" in the 4ykn-tg5h metadata prose.
9. TX: semantics of `associatedEntityRecord`; whether the 2027 facility registry (including MSO data) will be public or downloadable; PIA fields and cost for the licensee list.
10. AZ: whether Business Center *search* is captcha-gated; the vet board's current directory and premises list (site returned 403); ACC terms on automated use.
11. Socrata API rate limits for the NY and CO portals (app-token terms not read).
12. Any primary-source dental or vet rollup density figure for NY, CO, AZ and TX.

<!-- links -->
[ny-active]: https://data.ny.gov/Economic-Development/Active-Corporations-Beginning-1800/n9v6-gdp6
[ny-active-meta]: https://data.ny.gov/api/views/n9v6-gdp6.json
[ny-all]: https://data.ny.gov/d/63wc-4exh
[ny-all-meta]: https://data.ny.gov/api/views/63wc-4exh.json
[ny-addr]: https://data.ny.gov/d/2tms-hftb
[ny-name]: https://data.ny.gov/d/ekwr-p59j
[ny-status]: https://data.ny.gov/d/3gg2-jgnp
[ny-const]: https://data.ny.gov/d/dnbf-xifz
[ny-daily]: https://data.ny.gov/d/k4vb-judh
[ny-daily-meta]: https://data.ny.gov/api/views/k4vb-judh.json
[ny-tou]: https://data.ny.gov/dataset/OPEN-NY-Terms-Of-Use/77gx-ii52
[ny-6706]: https://www.nysenate.gov/legislation/laws/EDN/6706
[ny-a135]: https://www.nysenate.gov/legislation/laws/EDN/A135
[op-faq]: https://www.op.nysed.gov/about/frequently-asked-questions
[op-stats]: https://www.op.nysed.gov/about/registration-license-statistics/numbers-registered-licensees-2024
[op-vsc]: https://eservices.nysed.gov/nysed-assets/verification_search/vsc.js
[op-bulk]: https://op-support.nysed.gov/hc/en-us/requests/new?ticket_form_id=7599671137683
[op-written]: https://www.op.nysed.gov/verification-search/written-certification-or-verification-of-licensure
[nysed-tou]: https://www.nysed.gov/terms-of-use
[nysed-foil]: https://www.nysed.gov/new-york-state-education-department-foil-requests
[pol87]: https://www.nysenate.gov/legislation/laws/PBO/87
[pol89]: https://www.nysenate.gov/legislation/laws/PBO/89
[fl-dd]: https://dos.fl.gov/sunbiz/other-services/data-downloads/
[fl-daily]: https://dos.fl.gov/sunbiz/other-services/data-downloads/daily-data/
[fl-qtr]: https://dos.fl.gov/sunbiz/other-services/data-downloads/quarterly-data/
[fl-guide]: https://dos.fl.gov/sunbiz/other-services/data-downloads/data-usage-guide/
[fl-cor]: https://dos.sunbiz.org/data-definitions/cor.html
[fl-tou]: https://dos.fl.gov/copyright/
[fl-474215]: http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0474/Sections/0474.215.html
[fl-vetpr]: https://www2.myfloridalicense.com/veterinary-medicine/public-records/
[fl-disc]: https://www2.myfloridalicense.com/public-records-read-medisclaimer/
[fl-codes]: https://www2.myfloridalicense.com/about-us/understanding-dbpr-codes/
[co-ent]: https://data.colorado.gov/d/4ykn-tg5h
[co-ent-meta]: https://data.colorado.gov/api/views/4ykn-tg5h.json
[co-hist]: https://data.colorado.gov/d/casm-dbbj
[co-cat]: https://api.us.socrata.com/api/catalog/v1?domains=data.colorado.gov&q=business%20entities
[co-122]: https://colorado.public.law/statutes/crs_12-315-122
[co-lic]: https://data.colorado.gov/d/7s5z-vewr
[co-lic-meta]: https://data.colorado.gov/api/views/7s5z-vewr.json
[tx-sosd]: https://www.sos.state.tx.us/corp/sosda/index.shtml
[tx-bulk]: https://www.sos.state.tx.us/corp/bulk-order.shtml
[tx-spec]: https://www.sos.state.tx.us/corp/forms/bf-bulk-border-json-spec-v1.2.pdf
[tx-tac]: https://webservices.sos.state.tx.us/termsandconditions/tac.html
[tx-ft]: https://data.texas.gov/d/9cir-efmm
[tx-lookup]: https://apps.veterinary.texas.gov/s/licenseelookup
[tx-verif]: https://veterinary.texas.gov/license-verifications/
[tx-vethome]: https://veterinary.texas.gov/
[tx-sb2155]: https://capitol.texas.gov/tlodocs/89R/billtext/html/SB02155F.htm
[tx-sb2155h]: https://capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=SB2155
[tx-ann]: https://veterinary.texas.gov/announcements/tbvme-now-has-the-authority-to-register-and-regulate-veterinary-facilities/
[az-notice]: https://azcc.gov/corporations/notices
[az-corp]: https://azcc.gov/corporations
[az-prr]: https://azcc.gov/public-records-request
[az-2272]: https://www.azleg.gov/ars/32/02272.htm
