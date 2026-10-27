# Edge lifecycle: ending, retraction and staleness

Type: grilling
Status: open
Blocked by: 20, 25  (Document storage, fetch log and last-confirmed; Conflict, succession and co-investors)
Map: [api-spec](../map.md)

## Question

How do edges start, end, get retracted, go stale and get re-confirmed — and how do we stop re-derivation from resurrecting a retracted edge?

## Context

- **Ended vs retracted**: one column `retracted_at` (evidence_layer_plan.md:114–119); "end-dated" used both for wrong facts and true-but-ended facts (ADR 0001:15; research_flows.md:162). Needs start date ("formerly PE-owned {years}"), end date, last_confirmed_at, status; current value for PC edges.
- **Mutation policy**: on confidence change (reported→verified, research_flows.md:101) update in place + event, or new row? stack_fastapi.md:44 says "edge upsert". Unique per (from, to, relation) or per ownership period (sold then re-acquired)?
- **Retraction**: build_roadmap.md:157 = "end-date edge, claims untouched" — but edges are derived, so accepted claims re-create it; evidence_layer_plan.md:111 has claim status `retracted`; :134 "retract and add a new one". A manual `POST /internal/edges/{id}/retract` contradicts ADR 0002:17 (no hand-editing facts). Who triggers a retraction, which automated cases exist, what is the reason vocabulary? (A takedown/dispute intake is out of scope but the likeliest real trigger.)
- **Disappearance**: departed loans (research_flows.md:162), removed roster locations (:103), plans missing from a 5500 reload (:164). Absence can't be quoted — what records the end, after how many consecutive misses?
- **Staleness**: what makes a `reported` edge stale; "hunt for 2nd source" undefined (research_flows.md:113,166; build_roadmap.md:129). The 18-month last-confirmed sweep (ADR 0001:15) is in no Beat table.
- **Append-only vs "claim updates"** (CLAUDE.md:25 vs research_flows.md:162).
- Concurrency (advisory lock per business or a single-concurrency publish queue) and incremental re-derivation (recompute touched (s,p,o) groups, emit events only on change) — defaultable.
