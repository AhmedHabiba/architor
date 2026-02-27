# Methodology — The Four-Phase Architecture Review

## The Problem This Solves

AI-assisted development tools enable developers to produce working code at unprecedented speed. But working code is not the same as production-ready architecture. The gap between "it runs" and "it runs reliably at scale" is where architecture discipline lives.

Traditional architecture review — TOGAF, review boards, enterprise tools — was designed for a slower pace. When development takes weeks, a two-week review cycle is proportional. When AI generates a working system in hours, the same review cycle becomes a bottleneck that teams bypass under pressure.

The Architecture Agent provides a middle path: structured review that matches AI-accelerated development speed, without sacrificing the rigor that production systems demand.

## Core Principle

> **AI proposes and challenges. Human decides at every gate.**

The AI never auto-accepts. The AI never skips a phase. The AI actively challenges proposals and flags risks. But every decision — from architecture pattern selection to individual technology choices — requires explicit human acceptance.

## Phase 1: Evaluate

**Purpose**: Understand what we're building before deciding how to build it.

**Input**: PRD document (`.arch/prd.md`) + organizational context (`.arch/org-context.md`)

**What the agent does**:
- Extracts functional requirements with IDs (FR-001, FR-002...)
- Identifies non-functional requirements or flags them as missing
- Finds gaps rated by severity (Critical / Important / Minor)
- Asks specific, pointed questions — not vague asks
- Assesses risks across integration, scalability, security, operations, and team capability
- Rates overall PRD quality

**What the architect does**:
- Answers gap questions with concrete details
- Challenges the analysis if something was missed
- Adds context the PRD doesn't capture (legacy systems, regulatory, team history)
- Iterates with `/refine` until satisfied
- Explicitly accepts with `/accept`

**Gate**: PRD analysis accepted → proceed to Phase 2

**Anti-patterns caught here**:
- Vague requirements ("high availability" without a number)
- Missing non-functional requirements (no mention of monitoring, DR, security)
- Implicit assumptions the PRD doesn't state

## Phase 2: Decide

**Purpose**: Choose the right architecture pattern and map the complete system before designing individual parts.

**What the agent does**:
- Proposes an architecture pattern (microservices, modular monolith, serverless, event-driven, hybrid) with rationale tied to specific requirements and team constraints
- Presents trade-offs honestly — what this approach sacrifices
- Provides a **holistic component overview**: complete list of all system components, their roles, how they integrate, and high-level technology suggestions
- Compares alternatives when requested

**What the architect does**:
- Evaluates whether the pattern fits the team's operational reality (not just technical elegance)
- Reviews the component map for completeness — are all integrations covered? Any missing components?
- Requests alternatives with `/alternative` if the approach doesn't feel right
- Accepts the overall approach and component map (not individual components)

**Gate**: Both architecture pattern AND component overview accepted → proceed to Phase 3

**Why holistic before detailed**: You cannot evaluate a component without understanding where it fits in the system. The holistic overview ensures everyone sees the same big picture before drilling down. This prevents the common failure mode where individually-designed components don't integrate cleanly.

**Anti-patterns caught here**:
- Resume-Driven Development (choosing Kubernetes for a 3-person team)
- Cargo Cult Architecture (microservices because Netflix does it)
- Missing integration points (components that don't connect to anything)

## Phase 3: Design

**Purpose**: Design each component in detail, one at a time, with technology choices tied to team skills and operational reality.

**What the agent does (per component)**:
- Provides detailed design including technology recommendation with version
- Explains technology rationale and alternatives considered
- Details integration points — inputs, outputs, protocols, data formats
- Specifies API contracts and interfaces
- Addresses failure modes and fallback strategies
- Covers operational concerns: monitoring, alerting, scaling approach
- Challenges the architect on weak points before acceptance

**What the architect does**:
- Reviews technology choice against team skills and organizational constraints
- Validates integration points match what adjacent components expect
- Ensures failure modes are addressed (not just happy path)
- Requests adversarial review with `/review-component` for critical components
- Accepts each component individually

**Gate**: ALL components accepted → proceed to Phase 4

**Component lifecycle**:
```
pending → in_progress → awaiting_acceptance → accepted (locked)
                ↑              ↓
                └── /refine ───┘
```

Only one component is active at a time. Accepted components are locked and cannot be reverted. This prevents late changes from cascading through already-accepted designs.

**Anti-patterns caught here**:
- Over-engineering (distributed cache for 100 users)
- Under-engineering (no circuit breaker on external API calls)
- Integration wishful thinking (assuming services will "just work" together)
- Missing operational story (who pages at 2am when this breaks?)

## Phase 4: Document

**Purpose**: Consolidate all decisions into a comprehensive, auditable architecture document.

**What the agent does**:
- Reads all phase outputs and cross-checks for consistency
- Generates a comprehensive document including:
  - Executive summary
  - PRD analysis summary
  - Architecture methodology and rationale
  - System overview with component diagram
  - Detailed component designs
  - Cross-cutting concerns (security, observability, deployment, DR)
  - Technology stack summary table
  - Integration architecture with data flows
  - Implementation roadmap with build order
  - Complete decision log
- Flags inconsistencies found during consolidation

**What the architect does**:
- Reviews the executive summary for accuracy
- Checks the technology stack table for conflicts
- Validates the implementation roadmap ordering
- Verifies the decision log captures all key decisions
- Requests revisions or approves the final document

**Output**: `output/architecture-document.md`

## Decision Log

Every decision throughout all four phases is recorded with:

- **Decision ID**: Sequential (DEC-001, DEC-002...)
- **Phase**: Which phase it was made in
- **Category**: Technology, pattern, integration, NFR, etc.
- **What was decided**: The actual decision
- **Rationale**: Why this choice was made
- **Alternatives considered**: What else was evaluated
- **Trade-offs**: What was sacrificed
- **Residual risk**: What risk remains
- **Timestamp**: When the decision was made

The decision log is the most valuable artifact of the process. When someone asks "why did we choose Kafka over RabbitMQ?" six months later, the answer — with full context — is in the log.

## Adapting the Methodology

### For Startups

Ship the MVP first. Add architecture discipline when customers start expecting reliability. The four-phase process is most valuable at the transition from "it works on my machine" to "it runs in production with SLAs."

Watch for three traps:
- **Resume-Driven Development**: Choosing technologies to improve your CV rather than to solve the problem
- **Cargo Cult Architecture**: Copying patterns from companies 1000x your scale
- **Integration Wishful Thinking**: Assuming five services will integrate cleanly without designing the contracts

### For Enterprises

Speed up the review to match AI-accelerated development. The four phases encode what a good architecture review board does — but in hours instead of weeks.

Key adjustments:
- Encode organizational standards as inputs in `org-context.md`
- Use the decision log as an audit trail for compliance
- Start with one team, validate the process, then roll out
- The decision log replaces the PowerPoint deck that nobody reads
