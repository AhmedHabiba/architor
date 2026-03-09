# Continue Component Design for a Logistics Route Optimisation Platform

## Problem Description

FleetRoute is a logistics platform that optimises delivery routes for a national courier network. Phase 1 requirements and Phase 2 architecture methodology have been accepted. Phase 3 component design is now underway.

Your task is to act as the architecture agent and continue the Phase 3 component design process. Refer to the state file for the current status of each component and to the methodology document for architectural context. Produce the appropriate design output and update the project state accordingly.

## Output Specification

Produce the following files:

- A component design document placed under `.arch/components/` for the appropriate component
- `.arch/state.json` — updated to reflect progress after this design step

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
    {"id": 1, "name": "API Gateway", "status": "accepted"},
    {"id": 2, "name": "Auth Service", "status": "in_progress"},
    {"id": 3, "name": "Notification Service", "status": "pending"}
  ],
  "decision_count": 15,
  "reopens": {"count": 0, "max": 2}
}

=============== FILE: .arch/phase2-methodology.md ===============
# Phase 2: Architecture Methodology — FleetRoute

## Architecture Pattern
Modular monolith with clearly bounded modules. Each module may be extracted to an independent service if its scaling or release cadence needs diverge from the rest. Chosen because the team of 6 engineers with 1 DevOps engineer cannot sustain many independently deployed services in production.

## High-Level Component Map
1. **API Gateway** — Routes all external requests; handles rate limiting and request logging (ACCEPTED)
2. **Auth Service** — JWT-based authentication and RBAC authorisation; manages driver, dispatcher, and admin user sessions
3. **Notification Service** — Delivers email and SMS alerts for dispatch events, delivery confirmations, and SLA breaches

## Technology Stack
- **Language:** Python (FastAPI) — team's primary language
- **Database:** PostgreSQL — ACID compliance required for route and order data integrity
- **Cache:** Redis — session tokens and rate-limit counters
- **Infrastructure:** AWS ECS Fargate — chosen to avoid Kubernetes operational overhead with a single DevOps engineer
- **Auth mechanism:** JWT with refresh token rotation; no third-party identity provider (data privacy constraint from Phase 1)
