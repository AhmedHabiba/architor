Read `.arch/state.json` first.

**GATE CHECK:**
- If `current_phase` is `finalization` and `phases.finalization.document_generated` is true: Say "Document already generated. Do you want to regenerate? Say 'yes' to regenerate or review the existing document at `output/architecture-document.md`."
- If `current_phase` is not `components` and `current_phase` is not `finalization`, STOP: "Cannot generate documentation. Current phase is [phase]."
- If `current_phase` is `components` and `phases.components.all_accepted` is not `true`, STOP: "All components must be accepted before generating documentation. Use /status to check which components are pending."

Read ALL architecture files:
- `.arch/phase1-evaluation.md`
- `.arch/phase2-methodology.md`
- `.arch/phase2-components-overview.md`
- `.arch/phase2-cross-cutting.md` (if exists)
- All files in `.arch/components/`
- All files in `.arch/reviews/` (if any)
- `.arch/decisions.md`
- `.arch/org-context.md`

## Pre-Generation Validation

Before generating the document, perform these validation steps:

### 1. End-to-End Request Simulation
Trace 3 critical user journeys through the accepted component designs:
- **Happy path**: The most common user action — trace through every component it touches
- **Error path**: What happens when a key dependency fails — verify fallback/circuit breaker coverage
- **Scale path**: What happens at 10x expected load — verify scaling strategy holds

For each journey, verify:
- Every integration point between components is specified in both directions
- Data formats match (producer format = consumer expected format)
- Authentication/authorization is checked at every boundary
- Error handling is specified at every failure point

### 2. Risk Register
Create a risk register with probability x impact scoring:

| # | Risk | Probability (1-5) | Impact (1-5) | Score | Mitigation | Owner |
|---|------|-------------------|--------------|-------|------------|-------|

Include at minimum: technology risks, integration risks, operational risks, scale risks, security risks.

### 3. Cross-Component Consistency Check
Verify across ALL accepted components:
- Technology version consistency (no conflicting versions of shared libraries)
- Authentication approach consistency (same token format, same auth provider)
- Logging format consistency (same structured log format, same correlation ID propagation)
- Error code consistency (no overlapping error codes between components)
- If `.arch/phase2-cross-cutting.md` exists, verify each component adheres to those decisions

Report findings:
- If validation passes: "Pre-generation validation complete. No blocking issues found."
- If validation fails: List each issue with the specific component and conflict. Ask user to /reopen affected components or acknowledge the inconsistency.

Update `.arch/state.json`: set `phases.finalization.validation_complete` = true

---

## Generate Comprehensive Architecture Document

Write to `output/architecture-document.md` with the following structure:

### 1. Executive Summary
One page maximum. State:
- What system is being built and why
- The architecture approach chosen (pattern name, one-line rationale)
- Total number of components
- Key technology choices (top 5)
- Estimated overall complexity
- Critical risks and mitigations

### 2. PRD Analysis Summary
Condensed from Phase 1. Key requirements, constraints, and identified risks.

### 3. Architecture Methodology
- Pattern selected with full rationale
- Patterns considered and why rejected
- Key architectural decisions (numbered list)
- Architecture principles adopted

### 4. System Overview — Holistic Component Architecture
- Component map (table format from Phase 2)
- End-to-end flow description
- Component interaction summary
- Mermaid diagram code for system overview:
  ```mermaid
  graph TD
    [generate appropriate component diagram]
  ```

### 5. Cross-Cutting Architecture
From Phase 2C decisions:
- Authentication & authorization strategy
- Observability strategy
- Deployment strategy
- Error handling & resilience
- Data management cross-cuts

### 6. Detailed Component Designs
For each component (from Phase 3), include the full specification:
- Technology and version
- Role and bounded context
- Integration points (inputs, outputs, protocols)
- API contracts
- Scalability approach
- Security measures
- Monitoring strategy
- Failure modes and recovery

### 7. Technology Stack Summary
Table format:
| Layer | Technology | Version | Component(s) | Justification |
|-------|-----------|---------|---------------|---------------|

### 8. Integration Architecture
- Service-to-service communication patterns
- Data flow diagrams (Mermaid code)
- API gateway routing
- Event/message flows

### 9. Risk Register
From pre-generation validation (probability x impact table).

### 10. Implementation Roadmap
- Suggested build order (which components first, dependencies)
- Phase breakdown with milestones
- Risk mitigation per phase
- Team allocation suggestions

### 11. Decision Log
Complete chronological log from `.arch/decisions.md`

### 12. Open Items & Recommendations
- Unresolved gaps from Phase 1
- Concerns flagged during component reviews
- Recommendations for implementation team
- Areas requiring load testing or proof-of-concept
- Future considerations

### 13. Document Metadata
- Generated: [date]
- Architecture pattern: [name]
- Components: [count]
- Decisions recorded: [count]
- Reopens used: [count] of [max]
- Review findings addressed: [count]

---

After generating:
- Update `.arch/state.json`: `current_phase` = "finalization", `phases.finalization.status` = "awaiting_acceptance", `document_generated` = true
- Append to `.arch/decisions.md`: Document generation complete

Flag any consistency issues found during validation: "During document assembly, I found [N] consistency issues that should be addressed: [list]"

Ask the user:
"The architecture document has been generated at `output/architecture-document.md`.
Please review it. You can:
1. **ACCEPT** — Approve the final document (completes the process)
2. **REVISE** — Request specific changes to sections
3. **EXPAND** — Ask me to add more detail to specific areas"

$ARGUMENTS
