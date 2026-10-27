# NPPES bulk file and NPI Registry API: research findings

Ticket: [06-research-nppes](../issues/06-research-nppes.md). Researched 2026-10-26.

## How this was sourced (read first)

- **The live CMS download page was down on 2026-10-26.** <https://download.cms.gov/nppes/NPI_Files.html> returned only "This site will be down for maintance until further notice", and the zip URLs it used to list now return 404. Every file-level fact below therefore comes from **Internet Archive captures of CMS's own files on `download.cms.gov`**. These are byte copies of the primary source, not third-party summaries. Each capture is linked where it is used.
- **Readme and Code Values.** These are PDFs that CMS ships *inside* every dissemination zip; the download page does not link them separately. I took them from the archived weekly V2 zip for 2026-10-05 to 2026-10-11: [archived zip][wk]. That gave me the **Readme v.2, updated May 12, 2026** and the **Code Values document, updated/effective February 1, 2025**.
- **Statements marked "Observed"** come from running the real CSVs in that weekly zip (32,641 NPI rows), the deactivation zip and the monthly zip's directory listing. They show what the data actually looks like. They are not CMS documentation and may not hold for every file.
- **NPI Registry API docs.** The help page (<https://npiregistry.cms.hhs.gov/api-page>) is a JavaScript single-page app. I took its text from the page's own served bundle (`main-*.js` on npiregistry.cms.hhs.gov) and made one live API call to confirm the response shape.
- **Taxonomy codes.** These come from the NUCC Health Care Provider Taxonomy code set **v26.1 (effective 7/1/26)**, CSV: [nucc_taxonomy_261.csv][nucc261].

[wk]: https://web.archive.org/web/20261014190926/https://download.cms.gov/nppes/NPPES_Data_Dissemination_100526_101126_Weekly_V2.zip
[files1020]: https://web.archive.org/web/20261020170047/https://download.cms.gov/nppes/NPI_Files.html
[mth]: https://web.archive.org/web/20250722170145/https://download.cms.gov/nppes/NPPES_Data_Dissemination_July_2025_V2.zip
[deact]: https://web.archive.org/web/20260915170021/https://download.cms.gov/nppes/NPPES_Deactivated_NPI_Report_091426_V2.zip
[cmsdd]: https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination
[notice]: https://www.cms.gov/regulations-and-guidance/administrative-simplification/nationalprovidentstand/downloads/datadisseminationnpi.pdf
[api]: https://npiregistry.cms.hhs.gov/api-page
[reg]: https://npiregistry.cms.hhs.gov/
[nucc261]: https://www.nucc.org/images/stories/CSV/nucc_taxonomy_261.csv
[nucccsv]: https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40/csv-mainmenu-57
[nucctax]: https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40

---

## 1. Bulk file: location, naming, cadence, size, layout

### Location and naming
- **Index page:** `https://download.cms.gov/nppes/NPI_Files.html`. Download links are relative (`./<file>.zip`), so files sit at `https://download.cms.gov/nppes/<file>.zip` ([snapshot of 2026-10-20][files1020]).
- **File names**, from that snapshot. Names change every release, so a client has to scrape the index page or build the name from a pattern:
  - **Monthly full file:** `NPPES_Data_Dissemination_October_2026_V2.zip`, labeled "(October 12, 2026) - ZIP format (1,106.00 MB)". The pattern is `NPPES_Data_Dissemination_<Month>_<YYYY>_V2.zip`.
  - **Monthly deactivation file:** `NPPES_Deactivated_NPI_Report_101226_V2.zip` (2,616 KB). The pattern is `NPPES_Deactivated_NPI_Report_<MMDDYY>_V2.zip`.
  - **Weekly incrementals:** `NPPES_Data_Dissemination_100526_101126_Weekly_V2.zip` (6.39 MB) and `..._101226_101826_Weekly_V2.zip` (6.33 MB). The pattern is `NPPES_Data_Dissemination_<MMDDYY>_<MMDDYY>_Weekly_V2.zip`. The page listed only the two most recent weeklies.
- **V1 is gone.** The 2026-10-20 snapshot said: "Effective 03/03/2026 NPPES will no longer support Version 1 of the Monthly and Weekly Downloadable File. Version 2 includes all updated field lengths with extended character limits for First Name and Legal Business Name fields" ([snapshot][files1020]). The Readme says V2 began 12/24/2024 ([Readme §1][wk]).
- **Change notices:** CMS offers an email subscription for dissemination-file updates at <https://nppes.cms.hhs.gov/NppesSubscription/subscribe> ([snapshot][files1020]).

### Monthly full file vs weekly incremental
- **Monthly.** Readme §1.2: the monthly files "contain all of the FOIA-disclosable active provider data in NPPES" and "replace the file provided the previous month" ([Readme][wk]). The CMS dissemination page says: "Each month, users will need to download the full replacement monthly NPI File" ([CMS][cmsdd]).
- **Weekly.** Readme §1.3: the weekly files "contain only the new FOIA-disclosable NPPES provider data since the last weekly or monthly files were generated" ([Readme][wk]). CMS calls them "a supplemental file to be used in conjunction with the full replacement monthly NPI file" ([CMS][cmsdd]).
  - Observed: the weekly zip has the same four CSVs and the same 330-column header as the monthly file. Each row is a complete record, not a field-level diff. The sample held 25,495 Type 1 rows, 6,459 Type 2 rows and 687 rows with a blank Entity Type. The blank rows are deactivations: only `NPI` and `NPI Deactivation Date` are filled.
- **Deactivated NPIs inside the full file.** CMS discloses only the NPI number and its deactivation date for these ([CMS][cmsdd]). Observed: the same blank-entity-type rows appear in the weekly CSV.

### Deactivation file
- Observed: the zip contains a single **Excel** file, not a CSV: `NPPES Deactivated NPI Report 20260914.xlsx` ([archived zip][deact]).
  - The title row reads "NPPES Deactivated Records as of Sep 14 2026".
  - It has two columns: `NPI` and `NPPES Deactivation Date` (MM/DD/YYYY).
  - It holds about 355,330 data rows, which is a cumulative list, not a monthly delta.
- CMS calls it a "Full Replacement NPI Deactivation File" ([CMS][cmsdd]).
- No reason code is included. The Readme marks `NPI Deactivation Reason Code` as "not publicly disseminated" ([Readme][wk]).

### Size
- **Compressed:** the October 2026 monthly zip is 1,106.00 MB ([snapshot][files1020]).
- **Uncompressed (Observed),** read from the zip's central directory, July 2025 V2 monthly ([archived zip][mth]):

  | File | Uncompressed size |
  |---|---|
  | `npidata_pfile_20050523-20250713.csv` | about 10.8 GB |
  | `pl_pfile_…` | about 0.10 GB |
  | `othername_pfile_…` | about 0.03 GB |
  | `endpoint_pfile_…` | about 0.12 GB |

  The first date in each name is the start of NPPES (2005-05-23); the second is the cut date.
- **Row count is unconfirmed.** At the weekly sample's average of about 1.2 KB per row, 10.8 GB is roughly 9 million rows. That is an estimate, not a CMS figure.

### Bundle contents and CSV conventions (Readme §1.1 and §1.4, [zip][wk])
- **Files in each zip.** The Readme names them with `_FileHeader`; the files actually ship with lowercase `_fileheader` (observed).

  | File | Contents |
  |---|---|
  | `npidata_pfile_yyyymmdd-yyyymmdd.csv` + `_fileheader.csv` | Main data file and its header |
  | `othername_pfile_…csv` + header | Additional other names for Type 2 NPIs |
  | `pl_pfile_…csv` + header | Non-primary practice locations, Type 1 and Type 2 |
  | `endpoint_pfile_…csv` + header | Endpoints |
  | `NPPES_Data_Dissemination_CodeValues.pdf` | Code value tables |
  | `NPPES_Data_Dissemination_Readme_v.2.pdf` | File layouts |

- **Quoting.** Every value is wrapped in double quotes. Double quotes inside a value are replaced by single quotes.
- **Masking and suppression.**
  - SSNs, ITINs and EINs typed into identifier or license fields are masked as `$$$$$$$$$`, `*********` and `=========`.
  - **EINs and Subpart Parent Organization TINs are suppressed** for all organizations. CMS says it "expects to lift the suppression … in the future."
  - Observed: every Type 2 row has `<UNAVAIL>` in `Employer Identification Number (EIN)`. Every subpart row has `<UNAVAIL>` in `Parent Organization TIN`.

### Main data file column layout (Readme Exhibit 2-1, [zip][wk]): 330 columns
The header was observed and matches the Readme. Fields relevant to the census, with V2 maximum lengths:

| Column(s) | Notes |
|---|---|
| `NPI` (10), `Entity Type Code` (1) | 1 = Individual, 2 = Organization (Code Values §1.1) |
| `Replacement NPI` | |
| `Employer Identification Number (EIN)` | Suppressed (`<UNAVAIL>`) |
| `Provider Organization Name (Legal Business Name)` (100) | Type 2 legal name |
| `Provider Last/First/Middle Name`, prefix, suffix, credential | Type 1 |
| `Provider Other Organization Name` (100) + `… Type Code` (1) | See the other-names note below |
| `Provider Other Last Name` … + `Provider Other Last Name Type Code` | Type 1 former or professional names |
| Business **Mailing** Address: line 1/2, city, state, postal, country, phone, fax | |
| Business **Practice Location** Address: same sub-fields | The primary location only |
| `Provider Enumeration Date`, `Last Update Date`, `NPI Deactivation Date`, `NPI Reactivation Date`, `Certification Date` | MM/DD/YYYY |
| `Authorized Official Last/First/Middle Name`, `Title or Position` (35), `Telephone Number`, plus prefix, suffix, credential | Type 2 only |
| `Healthcare Provider Taxonomy Code_1..15` (10) + `Provider License Number_n` + `License Number State Code_n` + `Healthcare Provider Primary Taxonomy Switch_n` | Switch is Y/N/X; only one Y per NPI (Code Values §1.13) |
| `Other Provider Identifier_1..50` + Type Code / State / Issuer | Issuer type 01 = OTHER, 05 = MEDICAID |
| `Is Sole Proprietor` | Y/N/X. Applies to Type 1 |
| `Is Organization Subpart`, `Parent Organization LBN` (100), `Parent Organization TIN` | Subpart Y/N/X applies to Type 2. TIN suppressed |
| `Healthcare Provider Taxonomy Group_1..15` | Code Values §1.15 lists only 193200000X and 193400000X |

**Other names (Observed, with a documentation gap).**
- **Name type codes** (Code Values §1.6): 1 = Former Name (individual), 2 = Professional Name (individual), 3 = Doing Business As (organization), 4 = Former Legal Business Name (organization), 5 = Other Name (both).
- **Code 6 is undocumented.** A Readme footnote says: "If a 6 is seen in the Provider Other Organization Name Type Code column, there are other names for that Organization in the Other Name Reference File." But **code 6 does not appear in the Code Values table**.
- **Observed: the main file carries no org other names in the sample.** All 6,459 Type 2 rows in the weekly sample have `Provider Other Organization Name = "<UNAVAIL>"` and type code `6`. Organization DBAs and former names live **only** in `othername_pfile`.

**Other Name Reference File (Readme Exhibit 2-2).**
- Columns: `NPI`, `Provider Other Organization Name` (100), `Provider Other Organization Name Type Code`, `Created Date`.
- Readme: "NPPES now collects multiple Other Names associated with Type 2 NPIs."
- Observed: 2,548 rows in the weekly sample, split 3 = 2,106, 5 = 328, 4 = 114. Exact duplicate name rows with different `Created Date` values occur.

**Practice Location Reference File (Readme Exhibit 2-3).**
- Columns: `NPI`, then Secondary Practice Location address line 1/2, city, state, postal, country, phone, extension, fax.
- Readme §2.3: "The Data File contains the first Primary Practice Location, and the Practice Location Reference File will contain all of the non-primary Practice Locations."
- The file has **no name column**. A secondary location carries no DBA or location name.

**Endpoint Reference File (Readme Exhibit 2-4).** This file holds electronic endpoints such as Direct addresses and FHIR URLs, with affiliation LBN and address. It is probably not useful for the census.

---

## 2. Entity type 1 vs type 2, solo practices, multi-site groups

- **Definitions.** Type 1 = Individual and Type 2 = Organization (Code Values §1.1). The API calls them `NPI-1` and `NPI-2` ([API][api]).
- **A solo practice can appear as Type 1 only, or as Type 1 plus Type 2.**
  - `Is Sole Proprietor` (Y/N/X) is defined only for Type 1: "Entity Type 1 Provider (Individual) is a Sole Proprietor" (Code Values §1.2).
  - An unincorporated solo dentist may exist **only** as a Type 1 record flagged as a sole proprietor, with no Type 2 record at all.
  - Observed: among Type 1 dentists (any `1223*` taxonomy) in the weekly sample, 134 were `Y` and 277 were `N`.
  - Observed: incorporated solos do appear as Type 2 records named after the dentist, for example "… DMD LLC" and "… INC. APC". Their authorized official titles are typically OWNER or DENTIST.
  - Whether a given dentist *also* has a Type 2 record cannot be read from a single row. No field in the file links a Type 1 NPI to the Type 2 NPI it works for.
- **A multi-site group can appear in two ways.** The source allows both, and the observed data shows both:
  1. **One Type 2 NPI with secondary practice locations.** Locations other than the primary one go in `pl_pfile`, which allows many locations per NPI. Observed: one NPI had 115 secondary locations in a single weekly file. 22 of the 297 dental-taxonomy Type 2 orgs in the sample had at least one secondary location.
  2. **Several Type 2 NPIs, often subparts.** `Is Organization Subpart = Y` plus `Parent Organization LBN` is disclosed (the TIN is suppressed). Observed: one dental P.C. had two subpart NPIs in different cities, each naming the same parent LBN. 715 of 6,459 Type 2 rows were subparts. 312 legal business names appeared on more than one Type 2 NPI in the sample.
- **Authorized official is a cross-org signal (Observed).**
  - One person held the title "VP, PAYOR RELATIONS" as authorized official on 33 Type 2 dental orgs in the weekly sample. These were dentist-named PLLCs, PCs and PAs across TX, NH, NV, NY, ND and other states.
  - This is a recurring pattern in the data: an authorized official shared across separately named practices. It is not a documented relationship field.
- **The API mirrors the same structure.** The `addresses` array always holds the primary practice location and the mailing address. `practiceLocations` holds everything else. `other_names` can hold several entries ([API][api]).

---

## 3. Taxonomy codes for dental and medical organizations

### Facts that constrain the choice
- **Codes are self-selected and not verified.** NUCC says taxonomy codes "are self-selected by the provider", "define area of specialty", and "Scope of licensure is not within the purview of the taxonomy code set" ([NUCC][nucctax]). NPPES adds that an NPI "does not ensure or validate that the Health Care Provider is Licensed or Credentialed" ([snapshot][files1020]).
- **NUCC splits codes into two sections.** v26.1 has 883 codes: 698 in the "Individual" section and 185 in the "Non-Individual" section ([CSV][nucc261]).
  - Physician and dentist specialties (`207*`, `208*`, `1223*`) are all **Individual**-section codes.
  - Facility-style codes (`261Q*` Clinic/Center, and so on) are **Non-Individual**.
- **Most Type 2 orgs use Individual codes (Observed).**
  - In the weekly sample, 3,149 of 6,459 Type 2 records had a primary taxonomy from the Individual section.
  - Dental orgs mostly carry dentist codes, for example `1223G0001X` General Practice. Only 59 of 297 dental-taxonomy orgs used `261QD0000X` Dental Clinic/Center *without* any `1223*` code.
  - So filtering on Non-Individual codes alone would miss most dental and physician practice organizations. Filtering on Entity Type 2 plus a taxonomy list is what reaches them.
- **Primary vs any slot.** A record can list up to 15 taxonomies and exactly one is flagged primary (Code Values §1.13).
  - Observed: one dental specialty LLC listed `122300000X`, `1223E0200X`, `1223P0221X`, `1223P0300X` and `1223S0112X` together.
  - Matching on "any slot" and matching on "primary only" give different counts.
- **Group taxonomy is a separate field.**
  - Group codes `193200000X` (Multi-Specialty Group) and `193400000X` (Single Specialty Group) are the only values of `Healthcare Provider Taxonomy Group_n` (Code Values §1.15).
  - Observed: every `Taxonomy Group` column was **empty** in the weekly sample.
  - Yet a live API response returned `"taxonomy_group":"193200000X - Multi-Specialty Group"` on a Type 2 dental org. Whether the bulk file populates this field is unconfirmed (see the open list).
- **Neither repo document lists codes.** build_roadmap.md:88 says "Tier-1 taxonomies (dental, medical org types)". research_flows.md:15 says "every dental/medical organization". decisions.md:34 lists Tier-1 as dental, physician/urgent care, ABA, and dermatology/ophthalmology. pre-launch-seeding.md:28-30 adds optometry.

### Candidate codes: dental (NUCC v26.1, [CSV][nucc261])
| Code | Grouping / Classification / Specialization | NUCC section |
|---|---|---|
| 122300000X | Dental Providers / Dentist | Individual |
| 1223D0004X | Dentist / Dental Anesthesiology | Individual |
| 1223D0001X | Dentist / Dental Public Health | Individual |
| 1223E0200X | Dentist / Endodontics | Individual |
| 1223G0001X | Dentist / General Practice | Individual |
| 1223P0106X | Dentist / Oral and Maxillofacial Pathology | Individual |
| 1223X0008X | Dentist / Oral and Maxillofacial Radiology | Individual |
| 1223S0112X | Dentist / Oral and Maxillofacial Surgery | Individual |
| 1223X2210X | Dentist / Orofacial Pain | Individual |
| 1223X0400X | Dentist / Orthodontics and Dentofacial Orthopedics | Individual |
| 1223P0221X | Dentist / Pediatric Dentistry | Individual |
| 1223P0300X | Dentist / Periodontics | Individual |
| 1223P0700X | Dentist / Prosthodontics | Individual |
| 261QD0000X | Ambulatory Health Care Facilities / Clinic/Center / Dental | Non-Individual |
| 261QS0112X | Clinic/Center / Oral and Maxillofacial Surgery | Non-Individual |
| *Edge cases:* 122400000X Denturist; 124Q00000X Dental Hygienist; 125J00000X Dental Therapist; 125K00000X Advanced Practice Dental Therapist; 126800000X Dental Assistant; 126900000X Dental Laboratory Technician; 292200000X Laboratories / Dental Laboratory | | Individual (292200000X is Non-Individual) |

### Candidate codes: medical / physician orgs (NUCC v26.1, [CSV][nucc261])
**Facility-style (Non-Individual) Clinic/Center codes:**

| Code | Specialization |
|---|---|
| 261Q00000X | Clinic/Center (no specialization) |
| 261QP2300X | Primary Care |
| 261QM1300X | Multi-Specialty |
| 261QM2500X | Medical Specialty |
| 261QU0200X | Urgent Care |
| 261QA1903X | Ambulatory Surgical |
| 261QS0132X | Ophthalmologic Surgery |
| 261QE0002X | Emergency Care |
| 261QF0400X | Federally Qualified Health Center (FQHC) |
| 261QR1300X | Rural Health |

The full `261Q*` family has 63 codes. Most of the rest, such as Methadone, Military and Prison Health, are probably outside the scope of the categories above.

**Physician specialties (Individual section) that Type 2 practices commonly carry.** The whole "Allopathic & Osteopathic Physicians" grouping is 238 codes. The roots below cover the Tier-1 categories named in the docs:

| Code / root | Classification | Codes in root |
|---|---|---|
| 207Q00000X | Family Medicine (+ `207Q*` specializations) | 11 |
| 207R00000X | Internal Medicine (+ `207R*` specializations) | 30 with prefix `207R`. NUCC also files 207QB0505X Diabetology under Internal Medicine |
| 208D00000X | General Practice | 1 |
| 208000000X | Pediatrics (+ `2080*`) | 25 |
| 207P00000X | Emergency Medicine (+ `207P*`) | 7. Relevant to the ER-staffing layer in pre-launch-seeding.md:29 |
| 207N00000X | Dermatology (+ `207N*`) | 6 |
| 207W00000X | Ophthalmology (+ `207W*`) | 8 |

**Group codes (NUCC "Group" grouping):** 193200000X Multi-Specialty Group; 193400000X Single Specialty Group.

**Adjacent Tier-1 verticals named in decisions.md:34 and pre-launch-seeding.md:30 (all Individual section):**
- 152W00000X Optometrist, plus 6 `152W*` specializations.
- ABA: 103K00000X Behavior Analyst, 106E00000X Assistant Behavior Analyst, 106S00000X Behavior Technician.

**Observed scale in the weekly sample (Type 2, primary taxonomy).**
- By NUCC grouping:

  | Grouping | Type 2 records |
  |---|---|
  | Ambulatory Health Care Facilities | 1,096 |
  | Allopathic & Osteopathic Physicians | 963 |
  | Behavioral Health & Social Service Providers | 946 |
  | Agencies | 812 |
  | Suppliers | 653 |
  | Dental Providers | 228 |

- Codes outside the healthcare-practice idea are common among Type 2 records, for example `332B00000X` DME supplier, `363LP0808X` NP Psychiatric and `253Z00000X` In Home Supportive Care. A filter needs to keep them out on purpose.

### Code-set versioning
- NUCC publishes the code set twice a year, in January and July ([NUCC CSV page][nucccsv]). The NPPES Code Values document defers to it: "updated twice a year" (Code Values §1.12).
- The CSV page lists "Version 26.1 7/1/26" as current and "Version 25.1, 7/1/25 & 1/1/26" as previous. That implies **no new 26.0 release** for January 2026.
- Code Values §1.12 still points to the old Washington Publishing Company URL (`wpc-edi.com`) for taxonomy codes. NUCC is the current maintainer ([NUCC][nucctax]).

---

## 4. NPI Registry API

All quotes are from the API help page ([api-page][api]) unless marked otherwise.
- **Endpoint:** `https://npiregistry.cms.hhs.gov/api/?version=2.1`.
  - "API Versions 1.0 and 2.0 are NOW retired". `version=1.0`, `version=2.0` and calls without `version` "will no longer work".
  - The planned phase-out date for 2.1 is "TBD".
  - The API is read-only; no key or auth is mentioned.
  - "The API retrieves data from NPPES daily."
- **Parameters:**

  | Parameter | Rules |
  |---|---|
  | `version` | Required: `2.1` |
  | `number` | 10-digit NPI |
  | `enumeration_type` | `NPI-1` or `NPI-2`. "cannot be the only criteria entered" |
  | `taxonomy_description` | Search by taxonomy *description* text, not by code |
  | `name_purpose` | `AO` or `Provider` |
  | `first_name`, `last_name` | Type 1 only. Trailing `*` wildcard needs 2 or more characters |
  | `use_first_name_alias` | True/False, default True. Applies to AO and Type 1 |
  | `organization_name` | Type 2 only. Trailing wildcard needs 2 or more characters. "All types of Organization Names (LBN, DBA, Former LBN, Other Name) associated with an NPI are examined" |
  | `address_purpose` | `LOCATION`, `MAILING`, `PRIMARY` or `SECONDARY`. Default matches mailing *or* any practice location |
  | `city` | |
  | `state` | "cannot be used as the only input criterion … at least one other field, besides the Enumeration Type and Country, must be populated" |
  | `postal_code` | 5 digits match zip+4. Trailing wildcard needs 2 or more characters |
  | `country_code` | Can be the only criterion if it is not US |
  | `limit` | 1–200, default 10 |
  | `skip` | |
  | `pretty` | |

- **Result caps:** "An API query will return a maximum of 200 results per request. The Skip field in the API will let you skip up to 1000 records … up to a maximum of 1,200 records over six requests." The web search UI separately caps at "the first 2100 results".
- **Throttling:** "Effective 6/25/2024: To ensure the best experience, NPPES has limited the amount of NPI Registry queries that can be completed per hour" and "Bulk NPI Registry queries must use the DDS file" ([NPI Registry][reg], search page). **No numeric per-hour limit is published.** A live call returned no rate-limit headers (it was served through CloudFront).
- **Output shape:**
  - JSON with `result_count` and `results[]`.
  - Each result has `number`, `enumeration_type`, `basic` (org name, AO name/title/phone, `organizational_subpart`, `status`, dates), `addresses` (always 2: primary location and mailing), `practiceLocations`, `taxonomies` (up to 15, with `code`, `desc`, `primary`, `license`, `state`, `taxonomy_group`), `identifiers` (up to 50), `other_names` (with `code` and `type`, e.g. `"3"` / `"Doing Business As"`), `endpoints`, `created_epoch` and `last_updated_epoch`.
  - The help page links a CSV-to-JSON field map ([api-page][api]).
  - Observed: a live query with `organization_name=aspen dental*&state=NY&enumeration_type=NPI-2` returned dentist-named PCs whose **DBA** was "ASPEN DENTAL". This confirms that DBAs are searched.
- **Terms:** The API page states none beyond the throttling notice and the license/credential disclaimer. The CMS dissemination page says "There is no charge to view the data" ([CMS][cmsdd]).

---

## 5. Licensing and terms of reuse

- **Legal basis.** The data is published under FOIA and e-FOIA. CMS says it is "required to be disclosed under the FOIA and the eFOIA amendments", and "There is no way to 'opt out' or 'suppress' the NPPES record data for health care providers with active NPIs" ([CMS][cmsdd]). Readme §1 cites Federal Register notice **CMS-6060-N (May 30, 2007)** ([Readme][wk]; [notice PDF][notice]).
- **Cost:** "There is no charge to download the data" ([CMS][cmsdd]). The 2007 notice also says there will be no charge to use the query-only database or to download ([notice][notice]).
- **No license document found.** I found no license text, attribution requirement or redistribution restriction for the NPPES data on the CMS pages or in the Readme. The one usage request is about deactivated NPIs: for users who display downloaded data on their own websites, CMS "suggests that only the same data be displayed for those deactivated NPIs", meaning the NPI and deactivation date only ([CMS][cmsdd]).
- **The NUCC taxonomy code set is licensed differently.** NUCC states: "Vendors interested in incorporating the Health Care Provider Taxonomy code set into their commercial products must complete the license request form found on the CSV page" ([NUCC][nucctax]). The CSV page says "For commercial use, including sales or licensing, a license must be obtained from this web site" ([NUCC CSV][nucccsv]). The pages carry "Copyright 2026 American Medical Association".
  - This covers the code *descriptions and code set*. It does not cover the code values printed inside NPPES records.

---

## Implications for the design (facts and consequences only; decisions are the developer's)

- **File discovery.** File names change monthly and weekly, and the index page can go down (it was down on 2026-10-26, with old zips returning 404). A loader that depends on scraping that page will fail when the page is down. The Internet Archive holds copies, but that is not an official channel.
- **File size.** The main CSV is about 10.8 GB uncompressed with 330 columns. Loading it whole into memory with plain pandas is likely heavy. Reading only selected columns or in chunks is the usual mitigation; this is a size fact, not a recommendation.
- **Alias source.** For Type 2 orgs, DBAs and former names come from `othername_pfile` joined on NPI. The main file's other-name column held only `<UNAVAIL>` in the sample.
- **Locations.** Secondary practice locations come from `pl_pfile` and have no per-location name. A rollup roster location may therefore match an NPI's *secondary* address rather than its primary one.
- **Group membership.** No field in the census links a dentist (Type 1) to the practice entity (Type 2) they work at. Solo unincorporated practices may exist only as Type 1 sole-proprietor records. Whether Type 1 records count toward the "independent denominator" changes the census size and meaning. That is a scope question for the developer.
- **Taxonomy filtering.** A filter that keeps only Non-Individual taxonomy codes misses most dental and physician practice orgs. The candidate list above mixes both sections. Matching on the primary slot only and matching on any slot give different counts.
- **Cross-practice signals.** `Is Organization Subpart` + `Parent Organization LBN`, and a shared authorized official across differently named orgs, are relationship signals already present in an official-filing source (`nppes` is in the self-verifying list in CLAUDE.md). Whether either should produce claims, and with which predicate, is a schema decision.
- **EIN unavailable.** The EIN is suppressed, so it cannot serve as a join key to Form 5500 or IRS data.
- **API limits.** The API caps any query at 1,200 reachable records and throttles by an unpublished per-hour limit. CMS directs bulk use to the dissemination file. On-demand use fits these limits; census-scale use does not.
- **Deactivations.** These arrive in three places: as blank-entity rows in the monthly and weekly CSVs, and as a cumulative XLSX. Reading the XLSX needs an Excel reader.
- **Taxonomy descriptions.** Showing NUCC descriptions in a commercial product may fall under NUCC's license requirement. That is unconfirmed for this use case (see the open list).

## Unconfirmed / open

1. **Download site status.** Whether `download.cms.gov/nppes` is permanently moving or only in maintenance. The index page was down on 2026-10-26 and had been live through 2026-10-20 per the archive. No CMS announcement was found.
2. **Monthly row count and Type 2 count.** These were not measured; about 9 million rows is an estimate from bytes per row.
3. **Whether `Healthcare Provider Taxonomy Group_n` is ever filled in bulk.** It was empty in the weekly sample, but the API returns `taxonomy_group` for the same kind of org. The monthly file was not checked.
4. **Other-name code `6` and `<UNAVAIL>`.** Seen in every Type 2 row of one weekly file. Not checked across a monthly file, and code 6 is missing from the Code Values PDF.
5. **API hourly query limit.** No number is published. The behavior when the limit is exceeded (status code, headers) is unknown.
6. **Exact semantics of weekly files.** The Readme says "only the new" data. Observed rows were complete records, including deactivations. Whether *updated* existing NPIs always appear in the weekly file was not verified.
7. **NUCC license scope.** Whether showing NUCC taxonomy *descriptions* on a public site, or storing the CSV, counts as "incorporating … into commercial products". NUCC's license form terms were not read.
8. **Schedule of EIN suppression lift.** "Expects to lift … in the future" is undated.
9. **Weekly file retention.** Old weeklies are not kept on the CMS page; only the two latest were listed. The retention window was not documented.
10. **What the shared authorized-official pattern represents** (for example an MSO or DSO credentialing contact). It is an observation from one week of data, not a documented relationship.
