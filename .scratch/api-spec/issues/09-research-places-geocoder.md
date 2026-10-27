# Research: Google Places terms, pricing and a free geocoder

Type: research
Status: resolved
Map: [api-spec](../map.md)

## Question

What may we store from Google Places, what does a lookup cost today, and which free geocoder could supply coordinates for the map?

## Find out

- Current Places API generation (Places API (New)?), Text Search SKUs, field masks and their prices; is the docs' $0.017/call (research_flows.md:30) current?
- Terms: storage/caching rules — `place_id` only (ADR 0003:12) or also name/address/lat-lng under some caching window? Phone numbers?
- Free geocoders for US addresses: US Census Geocoder (batch limits, terms, accuracy), others; whether storing results is permitted.


## How to resolve

AFK. A subagent invokes the `research` skill and writes findings, every claim cited to its primary source, to `.scratch/api-spec/research/places-geocoder.md`. No branches, commits or pushes (map scope ruling 2026-10-26). Then append `## Answer` here: a short summary + link to the findings file.

## Answer

- Places API (New) is the current generation. Places API (Legacy) has been closed to new Cloud projects since 2025-03-01. Text Search (New) requires a field mask, and each request is billed at the highest SKU any requested field triggers.
- The $0.017/call figure is stale for Text Search. Name, address and location are Text Search **Pro** at $32/1k ($0.032) after 5,000 free calls a month. Phone and website are **Enterprise** at $35/1k after 1,000 free. An IDs-only Text Search is free. $17/1k is the price of Place Details Pro and legacy Find Place.
- Terms: `place_id` may be stored indefinitely (refreshing after 12 months is recommended and free). Places lat/lng may be cached for at most 30 days. Name, address, phone and all other Places content may not be stored: ToS §3.2.3(a)(iii) says "copy and save business names, addresses". ADR 0003:12 holds, with the 30-day lat/lng nuance.
- Places content also may not be used on a non-Google map, and Places lat/lng may not feed point-in-polygon analysis. A persistent map therefore needs another coordinate source.
- US Census Geocoder: free, no API key in its docs, batches of up to 10,000 records. Coordinates are interpolated along TIGER address ranges, not rooftop. The FAQ lists "non-residential or commercial" addresses as a no-match cause, and batch match counts vary between runs. The Bureau publishes no terms page; the output is federal work under 17 U.S.C. §105.
- Nominatim's public server allows 1 req/s, discourages bulk use (4 req/min for long or recurring jobs) and requires caching results. Its data is ODbL share-alike.
- Open: Census rate limits and terms (census.gov timed out), the real Census match rate on business addresses, and the scope of the ToS "listings or directory service" clause.

[findings](../research/places-geocoder.md)
