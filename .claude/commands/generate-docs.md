Read `.arch/state.json` first.

**GATE CHECK:**
- If `current_phase` is not `components` or `finalization`, STOP: "Cannot generate documentation. Current phase is [phase]."
- If `phases.components.all_accepted` is not `true`, STOP: "All components must be accepted before generating documentation. Use /status to check which components are pending."

Read ALL architecture files:
- `.arch/phase1-evaluation.md`
- `.arch/phase2-methodology.md`
- `.arch/phase2-components-overview.md`
- All files in `.arch/components/`
- All files in `.arch/reviews/` (if any)
- `.arch/decisions.md`
- `.arch/org-context.md`

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

### 5. Detailed Component Designs
For each component (from Phase 3), include the full specification:
- Technology and version
- Role and bounded context
- Integration points (inputs, outputs, protocols)
- API contracts
- Scalability approach
- Security measures
- Monitoring strategy
- Failure modes and recovery

### 6. Cross-Cutting Concerns
Synthesize from all component designs:
- **Security Architecture:** Authentication flow, authorization model, encryption standards, secrets management
- **Observability Strategy:** Monitoring stack, logging standards, distributed tracing, alerting
- **Deployment Strategy:** CI/CD approach, environments, rollback procedures
- **Disaster Recovery:** Backup strategy, RTO/RPO targets, failover approach

### 7. Technology Stack Summary
Table format:
| Layer | Technology | Version | Component(s) | Justification |
|-------|-----------|---------|---------------|---------------|

### 8. Integration Architecture
- Service-to-service communication patterns
- Data flow diagrams (Mermaid code)
- API gateway routing
- Event/message flows

### 9. Implementation Roadmap
- Suggested build order (which components first, dependencies)
- Phase breakdown with milestones
- Risk mitigation per phase
- Team allocation suggestions

### 10. Decision Log
Complete chronological log from `.arch/decisions.md`

### 11. Open Items & Recommendations
- Unresolved gaps from Phase 1
- Concerns flagged during component reviews
- Recommendations for implementation team
- Areas requiring load testing or proof-of-concept
- Future considerations

### 12. Document Metadata
- Generated: [date]
- Architecture pattern: [name]
- Components: [count]
- Decisions recorded: [count]
- Review findings addressed: [count]

---

After generating:
- Update `.arch/state.json`: `current_phase` = "finalization", `phases.finalization.status` = "awaiting_acceptance", `document_generated` = true
- Append to `.arch/decisions.md`: Document generation complete

**CONSISTENCY CHECK before presenting:**
Review the entire document for:
- Technology version conflicts between components
- Integration contract mismatches
- Security gaps (components without auth mentioned)
- Missing monitoring for any component

Flag any issues found: "⚠️ During document assembly, I found [N] consistency issues that should be addressed: [list]"

Ask the user:
"The architecture document has been generated at `output/architecture-document.md`. 
Please review it. You can:
1. **ACCEPT** — Approve the final document (completes the process)
2. **REVISE** — Request specific changes to sections
3. **EXPAND** — Ask me to add more detail to specific areas"

$ARGUMENTS
