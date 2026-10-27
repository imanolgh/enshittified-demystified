# Research: NPPES bulk file and API

Type: research
Status: resolved
Map: [api-spec](../map.md)

## Question

What do the NPPES bulk dissemination file and the NPI Registry API contain and allow, for building a national healthcare census?

## Find out

- Bulk file: download location and naming (changes monthly), monthly full vs weekly incremental files, deactivation file, size, column layout (organization name, other organization names + type codes, practice/mailing addresses, authorized official, taxonomy codes, enumeration type).
- Entity type 1 (individual) vs type 2 (organization): what solo practices look like; how group practices with multiple sites appear; the secondary practice-location file.
- The exact taxonomy codes for dental and medical organization types the census should include (build_roadmap.md:88 vs research_flows.md:15 disagree on breadth).
- NPI Registry API: endpoint, parameters, result caps (limit/skip), throttling/terms.
- Licensing/terms of reuse.


## How to resolve

AFK. A subagent invokes the `research` skill and writes findings, every claim cited to its primary source, to `.scratch/api-spec/research/nppes.md`. No branches, commits or pushes (map scope ruling 2026-10-26). Then append `## Answer` here: a short summary + link to the findings file.

## Answer

- **Bulk file:** `https://download.cms.gov/nppes/<file>.zip`, V2 only since 03/03/2026. The monthly full replacement zip (`NPPES_Data_Dissemination_<Month>_<YYYY>_V2.zip`) is about 1.1 GB; its main CSV is about 10.8 GB unzipped with 330 columns. There are also weekly incrementals (about 6 MB, complete rows) and a cumulative deactivation file, which is an **XLSX** with only NPI and date. The CMS index page was "down for maintenance" on 2026-10-26, so file facts come from archived copies of CMS's own zips.
- **Layout:** the main file has the legal business name, mailing and primary practice address, authorized official (name, title, phone), 15 taxonomy/license slots with a primary flag, subpart flag with parent LBN, and sole-proprietor flag. EIN and parent TIN are **suppressed** (`<UNAVAIL>`). Org DBAs and former names live only in `othername_pfile`, because the main-file column was `<UNAVAIL>`/code 6 on every Type 2 row in the sample. Secondary locations live in `pl_pfile`, with no per-location name.
- **Type 1 vs 2:** unincorporated solos can exist only as Type 1 sole-proprietor records. Nothing links a Type 1 provider to the Type 2 practice they work at. A multi-site group appears either as one Type 2 NPI with many secondary locations, or as several Type 2 subpart NPIs naming the parent LBN.
- **Taxonomy:** dentist (`1223*`) and physician (`207*`/`208*`) codes are NUCC *Individual*-section codes, yet about half of Type 2 orgs use them as their primary code. Only a minority of dental orgs use `261QD0000X` alone. A candidate list for dental, medical, urgent care, derm/ophtho/optometry and ABA (NUCC v26.1) is in the findings. Which ones to include is the developer's call.
- **API:** `https://npiregistry.cms.hhs.gov/api/?version=2.1`, no key. Limit is 1–200 and skip goes up to 1000, so at most 1,200 records per query. Throttled by an unpublished per-hour limit since 6/25/2024; "Bulk NPI Registry queries must use the DDS file." `organization_name` searches LBN, DBA, former LBN and other names.
- **Terms:** FOIA-disclosable data, no charge, and no license or attribution text found for NPPES data. The **NUCC taxonomy code set** requires a license for commercial use (AMA copyright).
- Open items: download-site status, monthly row counts, whether bulk ever fills the group-taxonomy field, the API's hourly limit number, and NUCC license scope.

[findings](../research/nppes.md)
