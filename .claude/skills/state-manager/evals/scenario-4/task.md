# Record a Technology Decision During Component Design

## Problem Description

The FreightFlow architecture project is in Phase 3. The team is currently designing the Order Service component. After evaluating several options, the team has agreed to use PostgreSQL as the primary data store for the Order Service. This decision needs to be formally recorded in the project decision log before design continues.

Your task is to record this technology decision in the project decision log.

## Output Specification

Produce the following file:

- `.arch/decisions.md` — with the technology decision appended

## Input Files

The following files are provided as inputs. Extract them before beginning.

=============== FILE: .arch/state.json ===============
{
  "current_phase": "components",
  "phases": {
    "evaluation": {"status": "accepted"},
    "methodology": {"status": "accepted"},
    "components": {"status": "in_progress"},
    "finalization": {"status": "not_started"}
  },
  "components": [
    {"id": 1, "name": "Order Service", "status": "in_progress"},
    {"id": 2, "name": "Payment Service", "status": "pending"}
  ],
  "requirements_accepted": true,
  "methodology_accepted": true,
  "decision_count": 12,
  "reopens": {"count": 0, "max": 2}
}

=============== FILE: .arch/decisions.md ===============
### [DEC-001] Phase 1 | Requirements
- **Decision:** Scope FreightFlow to domestic routes only in v1
- **Rationale:** International routing adds regulatory complexity beyond v1 scope
- **Alternatives:** Include international from day one (rejected — timeline risk)
- **Trade-offs:** Limits total addressable market at launch
- **Risk:** Customers with international needs may choose competitors
- **Date:** 2026-02-10T09:00:00Z

### [DEC-002] Phase 2 | Pattern
- **Decision:** Adopt a modular monolith architecture for FreightFlow v1
- **Rationale:** Team of 5 engineers with 1 DevOps cannot sustain many independently deployed services
- **Alternatives:** Microservices (rejected — operational overhead too high for team size)
- **Trade-offs:** Less granular scaling; single deployment unit
- **Risk:** Module coupling may increase over time if boundaries are not enforced
- **Date:** 2026-02-18T11:00:00Z
