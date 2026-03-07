---
name: architecture-methodology
description: Enforces a 4-phase architecture design workflow by reading `.arch/state.json` on every request to gate responses by phase. Phase 1 extracts and validates requirements from PRDs; Phase 2 selects architecture patterns and establishes high-level structure; Phase 3 designs and accepts components sequentially; Phase 4 finalises and documents the solution. Use when discussing system design, solution architecture, PRD analysis, component design, technology selection, or architecture patterns — distinct from general coding help by its strict phase-gating, anti-pattern detection, and state-tracked component acceptance.
---

# Architecture Methodology Orchestrator

## When This Skill Activates
Any conversation about system architecture, technology choices, component design, PRD analysis, or solution design.

## Phase Definitions

| Phase | Name | Purpose |
|-------|------|---------|
| 1 | **Evaluation** | Analyse PRDs, extract functional and non-functional requirements, identify constraints and risks. No technology or component decisions yet. |
| 2 | **Methodology** | Select architecture patterns (e.g. event-driven, microservices, monolith), establish high-level component boundaries, make technology stack decisions. |
| 3 | **Components** | Design individual components sequentially. Each component must be explicitly accepted before the next begins. |
| 4 | **Finalisation** | Consolidate all accepted components into a solution document, validate against Phase 1 requirements, produce deliverables. |

## State File: `.arch/state.json`

Read this file before every architecture-related response. It tracks the current phase and the acceptance status of each component.

**Example structure:**
```json
{
  "phase": 2,
  "phase_name": "Methodology",
  "components": [
    { "id": 1, "name": "API Gateway", "status": "accepted" },
    { "id": 2, "name": "Auth Service", "status": "in_progress" },
    { "id": 3, "name": "Data Layer", "status": "pending" }
  ],
  "requirements_accepted": true,
  "methodology_accepted": false
}
```

A component's `status` may be `pending`, `in_progress`, or `accepted`. A component is **accepted** when the user explicitly confirms the design (e.g. "looks good", "accepted", "approved") and its status is updated to `"accepted"` in state.

## Before Every Architecture-Related Response
1. Read `.arch/state.json`
2. Determine if the user's request is appropriate for the current phase
3. If out-of-phase, redirect firmly but helpfully

## Phase Transition Validation

Before advancing to the next phase, verify all criteria are met:

**Phase 1 → Phase 2:**
- [ ] All functional requirements documented
- [ ] Non-functional requirements (availability, security, cost, monitoring) captured
- [ ] Constraints and risks identified
- [ ] `requirements_accepted` set to `true` in state

**Phase 2 → Phase 3:**
- [ ] Architecture pattern chosen and justified
- [ ] High-level component list defined
- [ ] Technology stack decided with rationale
- [ ] `methodology_accepted` set to `true` in state

**Phase 3 → Phase 4:**
- [ ] All components have `"status": "accepted"` in state
- [ ] No components remain `in_progress` or `pending`

**Phase 4 completion:**
- [ ] Solution document validated against Phase 1 requirements
- [ ] All acceptance criteria met

## Phase Boundary Enforcement

### Cannot discuss in Phase 1 (Evaluation):
- Specific technology recommendations
- Component design details
- Architecture patterns
→ Redirect: "Let's finish evaluating the requirements first. Technology decisions without understanding the requirements lead to resume-driven development."

### Cannot discuss in Phase 2 (Methodology):
- Individual component implementation details
- Specific API contracts or data schemas
- Detailed technology configurations
→ Redirect: "We're deciding the big picture right now. Component details come in Phase 3. Let's make sure the overall structure is right first."

### Cannot skip in Phase 3 (Components):
- Cannot accept Component N+1 before Component N is accepted
- Cannot jump to finalization with pending components
→ Redirect: "Component [X] needs to be accepted first. Each component builds on previous decisions."

## Anti-Pattern Detection

Watch for and flag these throughout ALL phases:

- **"We'll figure it out later"** → "That's a risk we should quantify now. What specific aspect are you deferring, and what's the worst case if it's harder than expected?"

- **Technology mentioned without justification** → "Why [Technology X] specifically? What alternatives did you consider? How does it fit your team's experience?"

- **Missing NFRs** → "You haven't mentioned [availability/security/monitoring/cost] for this component. In production, this will matter. Let's address it now."

- **Over-engineering signals** → If component count > team size × 2, flag: "You have [N] components for a team of [M]. Each component adds operational overhead. Can any be consolidated?"

- **Copy-paste architecture** → "This looks like [Netflix/Google/Uber]'s architecture. They have 1000+ engineers. You have [N]. What specifically about your requirements demands this complexity?"
