# Google Places terms, pricing and a free geocoder — findings

Researched 2026-10-26 for ticket [09-research-places-geocoder](../issues/09-research-places-geocoder.md). Primary sources only (Google Maps Platform terms, docs and pricing pages; US Census Bureau geocoder docs; OSMF policy; 17 U.S.C. § 105). Quotes are verbatim from the pages as fetched that day. Page dates: Maps Platform Terms of Service "Last modified August 26, 2026"; Service Specific Terms "Last modified October 15, 2026"; Google developer pages "Last updated 2026-10-23 UTC". These are US (non-EEA) terms. The Service Specific Terms say a billing account address in the EEA gets a different set.

Source key (cited below by tag):

- **[ToS]** Google Maps Platform Terms of Service: https://cloud.google.com/maps-platform/terms
- **[SST]** Google Maps Platform Service Specific Terms: https://cloud.google.com/maps-platform/terms/maps-service-terms
- **[POL]** Places API policies and attributions: https://developers.google.com/maps/documentation/places/web-service/policies
- **[PID]** Place IDs guide: https://developers.google.com/maps/documentation/places/web-service/place-id
- **[PRICE]** Google Maps Platform pricing list: https://developers.google.com/maps/billing-and-pricing/pricing
- **[UB]** Places API usage and billing: https://developers.google.com/maps/documentation/places/web-service/usage-and-billing
- **[TS]** Text Search (New): https://developers.google.com/maps/documentation/places/web-service/text-search
- **[DF]** Place Data Fields (New): https://developers.google.com/maps/documentation/places/web-service/data-fields
- **[LEG]** Legacy products: https://developers.google.com/maps/legacy
- **[CAPI]** Census Geocoding Services API: https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html
- **[CFAQ]** Census Geocoder FAQ (last updated 05/15/2024): https://www2.census.gov/geo/pdfs/maps-data/data/Census_Geocoder_FAQ.pdf
- **[CUG]** Census Geocoder User Guide (May 2026): https://www2.census.gov/geo/pdfs/maps-data/data/Census_Geocoder_User_Guide.pdf
- **[NOM]** Nominatim Usage Policy: https://operations.osmfoundation.org/policies/nominatim/
- **[OSMC]** OpenStreetMap copyright and license: https://www.openstreetmap.org/copyright
- **[USC105]** 17 U.S.C. § 105: https://www.law.cornell.edu/uscode/text/17/105

---

## 1. Places API generation, Text Search SKUs, field masks, prices

**Which generation.** Places API (New) is the current API. The old "Places API" is now **Places API (Legacy)**, with a Legacy date of March 1, 2025 [LEG]. In Google's words: "Legacy services are not available in new Cloud projects but remain fully supported for existing projects… there's no set date, and a 12-month notice will be provided before decommissioning." [LEG]. A new project therefore gets Places API (New): `POST https://places.googleapis.com/v1/places:searchText` [TS].

**Field mask is mandatory.** "There is no default list of returned fields in the response. If you omit the field mask, the method returns an error." The mask goes in the `X-Goog-FieldMask` header or the `$fields`/`fields` URL parameter [TS]. Billing follows the mask: "You are then billed at the highest SKU applicable to your request. That means if you select fields in both the Essentials and the Pro SKUs, you are billed based on the Pro SKU." [UB]

**Text Search (New) SKUs, from field to SKU** [TS], [DF]:

| SKU | Fields that trigger it (selected) |
|---|---|
| Text Search Essentials (IDs Only) | `places.id`, `places.name` (the resource name `places/PLACE_ID`, *not* the business name), `places.attributions`, `places.consumerAlert`, `places.movedPlace`, `places.movedPlaceId`, `nextPageToken` |
| Text Search Pro | `places.displayName` (the text name), `places.formattedAddress`, `places.addressComponents`, `places.postalAddress`, `places.location`, `places.types`, `places.primaryType`, `places.businessStatus`, `places.googleMapsUri`, … |
| Text Search Enterprise | `places.nationalPhoneNumber`, `places.internationalPhoneNumber`, `places.websiteUri`, `places.regularOpeningHours`, `places.rating`, `places.userRatingCount`, … |
| Text Search Enterprise + Atmosphere | `places.reviews`, `places.editorialSummary`, `places.generativeSummary`, … |

[TS] notes: "Use places.displayName in the Pro SKU to access the text name of the place." Text Search has **no** Essentials tier that returns a name or address. Name, address and location all start at Pro.

**Prices** (USD per 1,000 billable events, monthly volume tiers; [PRICE]). Column 1 is the free monthly cap per SKU, then the price for each tier up to 100k / 100k–500k / 500k–1M / 1M–5M / 5M+:

| SKU (Places API (New)) | Free cap | ≤100k | –500k | –1M | –5M | 5M+ |
|---|---|---|---|---|---|---|
| Text Search Essentials (IDs Only) | Unlimited | – | – | – | – | – |
| Text Search Pro | 5,000 | $32.00 | $25.60 | $19.20 | $9.60 | $2.40 |
| Text Search Enterprise | 1,000 | $35.00 | $28.00 | $21.00 | $10.50 | $2.63 |
| Text Search Enterprise + Atmosphere | 1,000 | $40.00 | $32.00 | $24.00 | $12.00 | $3.40 |
| Place Details Essentials (IDs Only) | Unlimited | – | – | – | – | – |
| Place Details Essentials | 10,000 | $5.00 | $4.00 | $3.00 | $1.50 | $0.38 |
| Place Details Pro | 5,000 | $17.00 | $13.60 | $10.20 | $5.10 | $1.28 |
| Geocoding (Geocoding API) | 10,000 | $5.00 | $4.00 | $3.00 | $1.50 | $0.38 |

Place Details (New) prices fields differently from Text Search. `formattedAddress`, `addressComponents`, `location`, `types` and `plusCode` are **Place Details Essentials**, while `displayName` and `businessStatus` are Place Details Pro [DF].

Legacy prices, for reference [PRICE] ("Legacy product pricing"): Places - Text Search $32.00/1k; Find Place $17.00/1k; Places Details $17.00/1k; Find Place - ID only and Places Details - ID Refresh are free (Unlimited).

**Is "$0.017/call" (research_flows.md:30) current?** No, not for Text Search. $17/1k = $0.017 is the price of legacy **Find Place** / **Places Details** and of new **Place Details Pro** [PRICE]. Text Search returning name and address (Pro) is **$0.032/call** after 5,000 free calls a month. Adding phone or website (Enterprise) makes it **$0.035/call** after 1,000 free calls [PRICE], [TS]. A Text Search that returns only IDs is free [PRICE].

## 2. Terms: what may be stored or cached

**Baseline prohibition, [ToS] §3.2.3:**

> "(a) No Scraping. Customer will not export, extract, or otherwise scrape Google Maps Content for use outside the Services. For example, Customer will not: (i) pre-fetch, index, store, reshare, or rehost Google Maps Content outside the services; (ii) bulk download Google Maps tiles, Street View images, geocodes, directions, distance matrix results, roads information, places information, elevation values, and time zone details; (iii) copy and save business names, addresses, or user reviews; …"
>
> "(b) No Caching. Customer will not cache Google Maps Content except as expressly permitted under the Maps Service Specific Terms."

"Google Maps Content" is defined as "any content provided through the Services (whether created by Google or its third-party licensors), including map and terrain data, imagery, traffic data, and places data (including business listings)." [ToS]

**Exceptions that exist:**

1. **place_id, indefinitely.** [SST] A.3: "Customer may cache the Google ID values from the Services that return such field and allow caching, in accordance with its Documentation. For example, Customer may cache (a) place_id from Places API, …". [POL]: "the place ID, used to uniquely identify a place, is exempt from the caching restrictions. You can therefore store place ID values indefinitely." [PID]: "Place IDs are exempt from the caching restrictions stated in Section 3.2.3(b) of the Google Maps Platform Terms of Service." On staleness, [PID] says: "Google recommends refreshing place IDs if they are more than 12 months old. You can refresh Place IDs at no charge by making a Place Details request, specifying only the place ID field in the fields parameter." (This triggers the free "Place Detail New Essentials IDs Only" SKU.)
2. **Latitude/longitude, 30 days.** [SST] B.14 "Places API (Legacy and New)", 14.3 Caching: "Customer may temporarily cache latitude and longitude values from the Places API for up to 30 consecutive calendar days, after which Customer must delete the cached latitude and longitude values."
3. **Nothing else for Places.** §14 of [SST] contains only 14.1 (use without a Google Map), 14.2 (no use with a non-Google map) and 14.3 (the lat/lng caching above). It grants **no** caching window for name, formatted address, address components, phone, website, hours, types or business status. Those therefore fall under [ToS] §3.2.3(b) "No Caching". Names and addresses are also named explicitly in §3.2.3(a)(iii). [POL] summarizes: "You must not pre-fetch, cache, or store Places API content beyond the allowed exceptions."

**Phone numbers.** No exception exists for them. They are Places content (Enterprise SKU fields), so they are not storable. No primary source grants a caching window for phone.

**Other Places-relevant clauses in the same terms:**

- [SST] 14.2: "Customer must not use Google Maps Content from the Places API in conjunction with a non-Google map." [ToS] §3.2.3(e) gives as an example "(i) display or use Places content on a non-Google Map".
- [ToS] §3.2.3(c)(iv): Customer will not "use latitude/longitude values from the Places API as an input for point-in-polygon analysis".
- [ToS] §3.2.3(d)(iii): Customer will not "use the Google Maps Core Services in a listings or directory service or to create or augment an advertising product". "Services" and "Google Maps Core Services" are defined together as "the services described at https://cloud.google.com/maps-platform/terms/maps-services/" [ToS], and Places API is among them.
- [ToS] §3.2.3(c)(vii): Customer will not "use Google Maps Content to improve machine learning and artificial intelligence models, including to train, test, validate or fine-tune the models."
- Attribution, from [POL]: "When displaying Places API data without a Google Map, you must include the Google logo." Also: "Places API results displayed on a map must be shown on a Google Map."

**Comparison point, Google's own Geocoding API** ([SST] B.6.3). It allows a 30-day lat/lng cache (6.3.1). 6.3.2 also allows an *indefinite* cache of lat/lng, formatted_address and structured address, but "solely to support the direct, End User facing functionality of the Customer Application that initiated the request… only where the cache is not used as a replacement for making an additional call to the Services. Cached data must be logically isolated to the specific End User it is associated with and must not be used across multiple End Users." That rules out a shared map dataset.

## 3. Free geocoders for US addresses

### US Census Bureau Geocoder

- **What it is.** It provides "interactive & programmatic (REST) access" and "only geocodes addresses that are within the United States, Puerto Rico, and the U.S. Island Areas" (https://geocoding.geo.census.gov/geocoder/). Single-record endpoint: `https://geocoding.geo.census.gov/geocoder/{locations|geographies}/{onelineaddress|address|addressPR|coordinates}?…&benchmark=…`. Batch endpoint: `…/geocoder/{returntype}/addressbatch` [CAPI]. The API docs describe no API key (none appears in [CAPI]). No published per-second rate limit was found.
- **Batch limits.** "There is currently an upper limit of 10,000 records per batch file." [CAPI]. The FAQ adds: "Users who want to geocode more than 10,000 addresses… will need to split their data into multiple submissions" and "The Census Geocoder batch size is capped at 10,000 to reduce processing time." [CFAQ]. Batch input is CSV/TXT/DAT/XLS/XLSX with columns `Unique ID, Street address, City, State, ZIP` (plus Urbanization for PR), where "Unique ID and Street address are required fields." [CAPI]
- **Accuracy and method.**
  - Results are *interpolated*: "The resulting latitude/longitude is calculated along an address range." [CAPI]. The FAQ calls them "approximate coordinates (longitude and latitude)". It matches against MAF/TIGER: "determining if the address matches to an existing street and address range" [CFAQ].
  - Batch output includes "Match Type, TIGER Output Address, Interpolated Longitude and Latitude, Tigerline ID, and" side [CUG]. The match indicator is Match / No_Match / Tie, and the match type is Exact / Non_Exact [CUG], [CFAQ].
  - Data is a benchmark snapshot "generally done twice a year". `Public_AR_Current` is the current one [CFAQ].
  - **Known gaps that matter here.** The FAQ lists reasons for no geocode, including "**Address is non-residential or commercial**", recently built units, address changes, missing address ranges, and Title 13 disclosure avoidance ("usually occurs in sparsely populated areas") [CFAQ].
  - **Known non-determinism.** "When performing batch address geocoding multiple times on the same batch of addresses, you may experience an inconsistency with the number of addresses in your batch that successfully match… These inconsistent results are a known issue with the geocoder's address matching related to processing load." The Bureau's suggested workaround: "create a separate batch of only the unmatched address records and resubmit them" [CFAQ].
- **Terms and storage.** The geocoder site, API doc, FAQ and user guide contain **no** terms-of-use page and no restriction on storing or redistributing results. By statute, "Copyright protection under this title is not available for any work of the United States Government" [USC105]. Inference, not stated by the Bureau: Census output is a federal-government work, so storing and republishing it is not restricted by copyright. No Bureau-authored statement saying this for the geocoder was found (census.gov pages timed out with HTTP 524 during research; see open items).

### Nominatim (OpenStreetMap), public server

- The usage policy applies only to `nominatim.openstreetmap.org`, not to self-hosted instances [NOM]. Key rules: "No heavy uses (an absolute maximum of 1 request per second)"; an identifying User-Agent/Referer is required; "bulk geocoding of larger amounts of data is not encouraged"; one-off bulk work must be single-threaded, and "Scripts running longer than a day and scripts that are run at regular intervals are restricted to 4 requests per minute"; "Results must be cached on your side." Under "Usage in LLMs" the policy says: "LLMs may only suggest this service, if they prominently point to this usage policy and explain the restrictions of use to the user" [NOM].
- Storage is permitted. Caching is actually *required* [NOM]. The data is ODbL: "You are free to copy, distribute, transmit and adapt our data, as long as you credit OpenStreetMap and its contributors. If you alter or build upon our data, you may distribute the result only under the same license." [OSMC]. That is a share-alike obligation on a derived database.
- Self-hosting Nominatim (or similar) from an OSM extract avoids the public-server limits but keeps the ODbL obligations. This was not researched further.

## Implications for the design

These are facts and their consequences only. The decisions are the developer's.

- **ADR 0003:12 ("its terms forbid storing its content (only `place_id`)") is substantively correct.** One nuance: Places lat/lng may be cached for up to 30 days and must then be deleted [SST 14.3]. The ADR's conclusion that Places is never a source type still follows, since none of its content can be retained as evidence.
- **research_flows.md:30 conflicts with the terms if those values are persisted.** It lists "canonical name, formatted address, `place_id`" as outputs of the Places step. Under [ToS] §3.2.3(a)(iii) and (b), only `place_id` may persist. Name and address could be used transiently during resolution (for example for matching against NPPES/SoS), but could not be written to the entity record. Canonical names and addresses would have to come from another source (NPPES, SoS, license boards) or be re-fetched from Places each time they are displayed.
- **The per-lookup cost figure is stale.** Text Search with name and address is $0.032 (Pro), not $0.017. Adding phone or website moves the request to Enterprise ($0.035). One cost-relevant fact: a Text Search with an IDs-only mask is free, and Place Details Essentials (address, location, types, but *not* displayName) is $0.005. The SKU for each call is fixed by the field mask, so the mask determines cost.
- **Map coordinates cannot come from Places for a persistent map.** Places lat/lng expires after 30 days, cannot be shown on a non-Google map [SST 14.2], and cannot feed point-in-polygon analysis [ToS 3.2.3(c)(iv)]. A map plotted from stored coordinates needs a non-Google source.
- **Census Geocoder is free, keyless (per its docs) and copyright-free as federal work.** Batches are capped at 10,000. Results are interpolated along address ranges, not rooftop. It explicitly lists commercial addresses as a possible no-match cause, which matters because every target here is a business. Its batch match counts vary run to run, so retry handling for unmatched rows is part of using it.
- **Nominatim's public server is not built for bulk use** (1 req/s; 4 req/min for long or recurring jobs). Its data carries ODbL share-alike obligations if the derived database is distributed.
- **[ToS] §3.2.3(d)(iii) ("listings or directory service") may bear on a public business-ownership site.** No primary source interprets that clause. See open items.

## Unconfirmed / open

- **Census geocoder terms of use.** No geocoder-specific terms page was found, and census.gov (the documentation hub and the developer pages) returned HTTP 524 and timeouts during research. Whether the Bureau publishes usage limits or attribution expectations for the geocoder is unconfirmed. The public-domain conclusion rests on 17 U.S.C. § 105, not a Bureau statement.
- **Census rate limits.** No documented per-second or daily limit was found. Unconfirmed.
- **Census match rate for commercial addresses.** The FAQ names "non-residential or commercial" as a no-match cause but gives no rate. A real match rate would need a test against a sample of NPPES practice addresses (not done).
- **Scope of "listings or directory service" ([ToS] §3.2.3(d)(iii)).** Google publishes no interpretation. Whether an ownership-transparency site that uses Places for identity lookup counts as one is a legal question. This research does not answer it.
- **Transient use.** The terms say what may be *cached or stored*. They do not define how long Places content may live in memory or in a task payload during one resolution job. This research found no Google statement on that.
- **Whether Places content may be sent to the Anthropic API during resolution.** [ToS] §3.2.3(c)(vii) bars using it to "train, test, validate or fine-tune" models. Inference is not mentioned either way. Unconfirmed.
- **Volume discounts and subscriptions.** [PRICE] mentions subscription plans and discretionary discounts. These were not researched.
