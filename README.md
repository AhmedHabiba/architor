# Architecture Agent for Claude Code

A complete workflow toolkit that turns Claude Code into a rigorous, phase-gated solution architecture assistant. It enforces a 4-phase methodology — from PRD analysis to architecture document — with deterministic state management, adversarial design reviews, and hard enforcement of phase transitions.

This is not a chatbot. It is an opinionated architecture review process encoded into Claude Code's building blocks: CLAUDE.md memory, slash commands, auto-activating skills, hooks, and validation scripts.

**25 files · 4 phases · Zero auto-acceptance**

### Documentation

| Document | Description |
|----------|-------------|
| **[README.md](README.md)** | This guide — setup, step-by-step walkthrough, command reference |
| **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** | System design — enforcement layers, state management, design decisions |
| **[docs/METHODOLOGY.md](docs/METHODOLOGY.md)** | The four-phase methodology — what happens at each phase and why |
| **[docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)** | How to contribute — project structure, testing, guidelines |
| **[CHANGELOG.md](CHANGELOG.md)** | Version history |

### System Diagrams

| Diagram | What it shows |
|---------|---------------|
| **[System Architecture](docs/diagrams/system-architecture.svg)** | How CLAUDE.md, commands, skills, hooks, and state files connect |
| **[Enforcement Model](docs/diagrams/enforcement-model.svg)** | Soft → medium → hard enforcement layers |
| **[Phase Workflow](docs/diagrams/phase-workflow.svg)** | Four phases with gates, refinement loops, and acceptance criteria |
| **[Component Lifecycle](docs/diagrams/component-lifecycle.svg)** | State machine for individual component design in Phase 3 |

---

## What's in the Box

```
arch-agent/
├── CLAUDE.md                              # Persistent behavior rules + identity
├── README.md                              # This guide
├── LICENSE                                # MIT License
├── CHANGELOG.md                           # Version history
├── .gitignore
│
├── docs/
│   ├── ARCHITECTURE.md                    # System design document
│   ├── METHODOLOGY.md                     # Four-phase methodology guide
│   ├── CONTRIBUTING.md                    # Contribution guidelines
│   └── diagrams/
│       ├── system-architecture.svg        # System layers and connections
│       ├── enforcement-model.svg          # Soft → hard enforcement
│       ├── phase-workflow.svg             # 4 phases with gates
│       └── component-lifecycle.svg        # Phase 3 state machine
│
├── .claude/
│   ├── settings.json                      # Hooks + permissions configuration
│   ├── commands/                          # Slash commands (user-invoked)
│   │   ├── analyze-prd.md                 # /analyze-prd         → Phase 1
│   │   ├── propose-methodology.md         # /propose-methodology  → Phase 2
│   │   ├── design-component.md            # /design-component     → Phase 3
│   │   ├── generate-docs.md               # /generate-docs        → Phase 4
│   │   ├── accept.md                      # /accept               → Accept current
│   │   ├── refine.md                      # /refine               → Request changes
│   │   ├── alternative.md                 # /alternative          → Different approach
│   │   ├── review-component.md            # /review-component     → Adversarial review
│   │   ├── status.md                      # /status               → Project state
│   │   ├── decision-log.md                # /decision-log         → All decisions
│   │   └── help.md                        # /help                 → Command reference
│   │
│   └── skills/                            # Auto-activating skills (model-invoked)
│       ├── architecture-methodology/
│       │   └── SKILL.md                   # Orchestration: phase enforcement
│       ├── architecture-patterns/
│       │   └── SKILL.md                   # Knowledge: pattern selection
│       ├── challenge-assumptions/
│       │   └── SKILL.md                   # Personality: adversarial reviewer
│       └── state-manager/
│           └── SKILL.md                   # Task: state read/write logic
│
├── .arch/                                 # Working directory (architecture state)
│   ├── state.json                         # Phase state machine (single source of truth)
│   ├── prd.md                             # Your PRD goes here
│   ├── org-context.md                     # Organizational constraints template
│   ├── decisions.md                       # Running decision log
│   ├── scripts/
│   │   ├── validate-transition.py         # Hook: blocks illegal phase transitions
│   │   └── log-decision.py                # Hook: auto-logs state changes
│   ├── components/                        # Phase 3 outputs (one file per component)
│   └── reviews/                           # Adversarial review findings
│
└── output/
    └── architecture-document.md           # Phase 4 final deliverable
```

### How the Pieces Work Together

| Layer | What | Control Level |
|-------|------|--------------|
| **CLAUDE.md** | Identity, rules, file references | Soft — Claude follows these instructions probabilistically |
| **Slash Commands** | Phase workflows triggered by `/command` | Medium — structured prompts with gate checks |
| **Skills** | Auto-activate for architecture conversations | Medium — behavioral nudges that activate by context |
| **Hooks + Scripts** | Python validation on state.json writes | **Hard** — deterministic code that blocks illegal transitions |
| **state.json** | Phase state machine on disk | **Hard** — survives /clear, session restarts, compaction |

The key insight: Claude may drift on instructions over a long conversation, but it cannot bypass a Python script that exits with code 1. The hooks are your hard safety net.

---

## Prerequisites

You need:
1. **Claude Code** installed and working (Claude Pro, Max, or API subscription)
2. **Python 3** available in your terminal (for hook scripts)
3. A **PRD document** (text content — not a scanned PDF)
4. Optionally, organizational context (team profile, tech stack, constraints)

Verify your setup:
```bash
claude --version        # Claude Code installed
python3 --version       # Python 3 available
```

---

## Step-by-Step: PRD to Architecture Document

### Step 0 — Set Up the Project

**0.1 Clone or copy the arch-agent directory to your workspace:**

```bash
# If distributed as a git repo:
git clone <repo-url> my-project-architecture
cd my-project-architecture

# Or copy manually:
cp -r arch-agent/ my-project-architecture/
cd my-project-architecture
```

**0.2 Make hook scripts executable:**

```bash
chmod +x .arch/scripts/validate-transition.py
chmod +x .arch/scripts/log-decision.py
```

**0.3 Add your PRD:**

Open `.arch/prd.md` and replace the template content with your actual PRD. If your PRD is in PDF or DOCX, extract the text and paste it here.

```bash
# Option A: paste directly
nano .arch/prd.md

# Option B: copy from another file
cp ~/documents/my-project-prd.txt .arch/prd.md
```

**0.4 Fill in organizational context (recommended):**

Open `.arch/org-context.md` and fill in your team profile, tech stack, constraints, and lessons learned. This is optional but dramatically improves the quality of recommendations.

The more honest you are about team limitations and past failures, the better the architecture recommendations will be. If you skipped MongoDB because your team couldn't operate it, say so.

**0.5 Start Claude Code in the project directory:**

```bash
cd my-project-architecture
claude
```

Claude will automatically load `CLAUDE.md` and discover the skills and commands.

**0.6 Verify everything is loaded:**

```
You: /help
```

You should see the full command reference. If commands don't appear, verify the `.claude/commands/` directory exists and files have `.md` extension.

---

### Step 1 — Phase 1: PRD Evaluation

**What happens:** Claude analyzes your PRD, extracts requirements, identifies gaps, assesses risks, and rates the PRD quality. It will challenge vague requirements and ask hard questions.

**Start it:**

```
You: /analyze-prd
```

**What to expect:**
- Functional requirements extracted with IDs (FR-001, FR-002...)
- Non-functional requirements identified (or flagged as missing)
- Gaps rated by severity (Critical / Important / Minor)
- Specific questions — not vague asks, but pointed questions with concrete expected answers
- Risk assessment covering integration, scalability, security, operations, and team capability
- Overall PRD quality rating

**Your job in Phase 1:**

Don't just accept the first analysis. This is where you establish the foundation.

- **Answer the gap questions.** If Claude asks "What's the expected peak concurrent users?", provide a number. Vague answers lead to vague architecture.
- **Challenge the analysis.** If Claude missed something, say so: "You didn't mention the regulatory requirement for data residency in Saudi Arabia."
- **Add context.** If you know things the PRD doesn't say, provide them: "The PRD doesn't mention it, but this system replaces a legacy Oracle system we need to migrate data from."

**Refine if needed:**
```
You: /refine The security analysis is too shallow. We handle PCI-DSS card data 
     and you didn't address PCI scope at all. Also, the PRD assumes cloud 
     deployment but our compliance team hasn't approved AWS yet — only Azure 
     is approved.
```

**Accept when ready:**
```
You: /accept
```

Claude will confirm what you're accepting and ask for explicit confirmation. The state machine transitions to Phase 2.

**State after Step 1:**
```
.arch/state.json        → current_phase: "methodology"
.arch/phase1-evaluation.md  → Full analysis document
.arch/decisions.md      → DEC-001: Phase 1 accepted
```

---

### Step 2 — Phase 2: Architecture Methodology

**What happens:** Claude proposes an architecture pattern (e.g., Event-Driven Microservices, Modular Monolith) with rationale tied to your specific requirements and team. It also presents a holistic component overview — the complete system map showing all components, their roles, and how they connect.

**Start it:**

```
You: /propose-methodology
```

**What to expect:**

**Part A — Architecture Pattern:**
- Recommended pattern with requirement-specific justification (not generic benefits)
- Trade-offs: what you sacrifice with this choice
- Comparison table: recommended vs 2+ alternatives scored on fit, team capability, operational cost, delivery time, and future flexibility
- Key architectural decisions this pattern implies

**Part B — Holistic Component Overview:**
- Complete component table: name, role, why it exists, connections, technology direction
- End-to-end flow: how a user request travels through the system
- Self-challenge: Claude will question its own proposal (too many components? god service? missing cross-cutting concerns?)

**Your job in Phase 2:**

This is the highest-leverage phase. A wrong architecture pattern compounds into every component decision. Push hard here.

- **Question the pattern choice.** "Why microservices for a team of 4? Convince me this isn't over-engineering."
- **Challenge component count.** "You proposed 9 components. We have 6 developers. Can we consolidate?"
- **Ask about alternatives.** "What would this look like as a modular monolith instead?"
- **Check against org context.** "You recommended Kafka, but we've never operated a message broker. What's the operational burden?"

**Important constraint:** You cannot refine individual components in Phase 2. The point is to accept or reject the big picture before drilling into details. If you try to refine a specific component's implementation, Claude will redirect you.

**Request an alternative approach:**
```
You: /alternative I want to see this designed as a modular monolith instead of 
     microservices. Our team is too small for the operational overhead.
```

**Refine the overall approach:**
```
You: /refine I like the pattern, but the component overview is missing a 
     dedicated audit service. Given our compliance requirements, audit 
     logging can't be a cross-cutting concern — it needs its own bounded 
     context with immutable storage.
```

**Accept when ready:**
```
You: /accept
```

This accepts BOTH the methodology AND the component overview. Claude will list the components that will be designed in Phase 3 and ask for explicit confirmation.

**State after Step 2:**
```
.arch/state.json                   → current_phase: "components"
.arch/phase2-methodology.md        → Architecture pattern + rationale
.arch/phase2-components-overview.md → Holistic component map
.arch/decisions.md                 → DEC-002: Pattern accepted, DEC-003: Components finalized
```

---

### Step 3 — Phase 3: Component Design (Iterative)

**What happens:** Claude designs each component in detail, one at a time. The component list comes from the accepted Phase 2 overview. Order follows dependency logic — foundational components (databases, auth, core services) before dependent services.

**Start the first component:**

```
You: /design-component
```

(Claude picks the first component in dependency order. You can also specify: `/design-component api-gateway`)

**What to expect for each component:**
- Component specification: name, detailed role, bounded context
- Technology recommendation with version, rationale, and 2 alternatives considered
- Integration specification: inputs, outputs, protocols, data formats, API contracts
- Consistency check against previously accepted components
- Scalability analysis: scaling approach, bottleneck identification, data growth projection
- Security: authentication, authorization, data sensitivity, attack surface
- Monitoring: key metrics, alerting thresholds, logging strategy, distributed tracing
- Failure modes: what happens when it dies, dependency failures, fallback strategy, recovery
- Complexity assessment with build estimate

**Before acceptance, Claude will challenge you:** "Before you accept, I want to flag these concerns: [specific issues]. Are you comfortable with these?"

**Your job in Phase 3:**

This is the longest phase. For each component:

1. **Read the full design.** Don't skim.
2. **Check integration points.** Does this match what the previous component expects? Claude checks automatically, but verify.
3. **Question the technology.** "Why Redis 7 for caching instead of the built-in caching our framework provides?"
4. **Probe failure modes.** "What happens to in-flight orders if this component crashes during a database write?"
5. **Consider operations.** "Who's going to be on-call for this at 3am? Is the monitoring sufficient for them to diagnose issues?"

**Launch an adversarial review (optional but recommended for critical components):**
```
You: /review-component api-gateway
```

This triggers a separate review where Claude acts as a skeptical principal architect reviewing someone else's design. It rates the component on requirements alignment, technology fitness, integration integrity, failure analysis, security, operational readiness, and scalability — then presents specific findings.

**Refine a component:**
```
You: /refine The failure mode analysis assumes the message queue is always 
     available. That's not realistic. Add a dead letter queue and a 
     circuit breaker pattern for when the queue is down.
```

**Suggest a different technology:**
```
You: /alternative Use RabbitMQ instead of Kafka. We have RabbitMQ operational 
     experience and the message volume doesn't justify Kafka's complexity.
```

**Accept and auto-advance to next:**
```
You: /accept
```

After confirmation, Claude automatically designs the next component — no need to run `/design-component` again. The flow becomes:

```
/design-component → review → /accept → [auto-advances] → review → /accept → [auto-advances] → ...
```

You only need `/design-component` once to start Phase 3. After that, `/accept` chains through all remaining components. You can still `/refine` or `/alternative` at any point to break the chain and adjust before accepting.

**Check progress anytime:**
```
You: /status
```

This shows the component scorecard (3 of 7 complete, current component, etc.).

**Repeat** for every component. The hook script ensures you cannot skip components or work on two at once.

**State after Step 3 (all components done):**
```
.arch/state.json              → current_phase: "components", all_accepted: true
.arch/components/*.md         → One detailed design per component
.arch/reviews/*.md            → Any review findings
.arch/decisions.md            → Full history of technology choices + rationale
```

---

### Step 4 — Phase 4: Finalization

**What happens:** Claude consolidates everything into a comprehensive architecture document. It reads all phase outputs, checks for cross-component consistency, generates Mermaid diagrams, and produces the final deliverable.

**Start it:**

```
You: /generate-docs
```

**What to expect:**

The generated document at `output/architecture-document.md` includes:
1. Executive summary (one page)
2. PRD analysis summary
3. Architecture methodology with full rationale
4. System overview with Mermaid component diagram
5. Detailed component designs (all of them)
6. Cross-cutting concerns (security, observability, deployment, DR)
7. Technology stack summary table
8. Integration architecture with data flow diagrams
9. Implementation roadmap with build order and team allocation
10. Complete decision log
11. Open items and recommendations
12. Document metadata

**Consistency check:** Before presenting, Claude reviews the entire document for technology version conflicts, integration contract mismatches, security gaps, and missing monitoring coverage. It flags any issues found.

**Your job in Phase 4:**

- **Read the executive summary.** Does it accurately represent the architecture?
- **Check the technology stack table.** Any conflicts or missing entries?
- **Review the implementation roadmap.** Is the build order realistic? Are dependencies correct?
- **Verify the decision log.** Does it capture all the key decisions and rationale?

**Request revisions:**
```
You: The implementation roadmap puts the notification service in Phase 1, 
     but it depends on the message queue which is in Phase 2. Fix the 
     ordering. Also, expand the disaster recovery section — it doesn't 
     address multi-region failover.
```

**Approve the final document:**
```
You: /accept
```

**You're done.** The architecture document is at `output/architecture-document.md`.

---

## Command Quick Reference

| Command | Phase | Purpose |
|---------|-------|---------|
| `/analyze-prd` | 1 | Evaluate the PRD |
| `/propose-methodology` | 2 | Propose architecture pattern + component overview |
| `/design-component [name]` | 3 | Design one component in detail |
| `/generate-docs` | 4 | Generate final architecture document |
| `/accept` | Any | Accept current proposal |
| `/refine [feedback]` | Any | Request changes |
| `/alternative [request]` | 2, 3 | Request different approach or technology |
| `/review-component [name]` | 3 | Adversarial design review |
| `/status` | Any | Show project state and progress |
| `/decision-log [filter]` | Any | Show decision history |
| `/help` | Any | Show command reference |

---

## How Enforcement Works

### Soft Enforcement (CLAUDE.md + Skills)

Claude's behavior rules in CLAUDE.md and auto-activating skills create strong behavioral guidance. Claude will:
- Read state.json before every response
- Refuse to discuss component details during Phase 2
- Challenge assumptions instead of agreeing
- Flag anti-patterns (over-engineering, resume-driven development)

**Limitation:** Over very long conversations (100+ exchanges), Claude may drift from these instructions. Use `/clear` and resume — CLAUDE.md is reloaded fresh. State persists in files.

### Hard Enforcement (Hooks + Scripts)

The `validate-transition.py` script runs as a PreToolUse hook every time Claude attempts to write to `state.json`. It blocks:
- Illegal phase transitions (e.g., jumping from evaluation to finalization)
- Backward transitions (going from components back to methodology)
- Starting Phase 2 without Phase 1 acceptance
- Starting Phase 3 without Phase 2 acceptance (both pattern AND component overview)
- Starting Phase 4 without all components accepted
- Working on multiple components simultaneously
- Reverting accepted components

**No prompt, no matter how creative, can bypass a Python script that exits with code 1.**

### What Can't Be Enforced

Be honest about the limits:
- Claude may become too agreeable over long sessions (use `/review-component` to inject tension)
- The quality of Claude's architecture advice depends on the model — Opus is significantly better than Haiku for this
- "Accept" detection relies on Claude interpreting the word, not a button click
- If you manually edit `state.json`, you bypass the hooks (don't do this)

---

## Tips for Best Results

### Before You Start
- **Write a real PRD.** Garbage in, garbage out. A two-paragraph description won't produce useful architecture.
- **Fill in org-context.md honestly.** If your team has never operated Kubernetes, say so. If you tried event sourcing and it failed, say so. The most valuable advice comes from knowing your constraints.
- **Use Claude Opus.** For architecture decisions, model quality matters enormously. Sonnet is adequate for straightforward systems. Opus handles complex trade-offs, subtle integration concerns, and adversarial challenges significantly better.

### During the Process
- **Don't rush acceptance.** The cost of a bad Phase 2 decision compounds into every component. Spend time here.
- **Argue back.** If you disagree with a recommendation, say why. Claude is designed to defend its position or adapt — not just comply.
- **Use /review-component for critical services.** The adversarial review catches real issues. Use it for anything that handles money, PII, authentication, or is on the critical path.
- **Run /status frequently.** It's your dashboard.
- **Use /clear when conversations get long.** State lives in files, not in conversation context. Clearing gives Claude a fresh context window with the same project state.

### After Completion
- **The document is a starting point, not a finished product.** Share it with your team. Use it as the basis for sprint planning.
- **The decision log is the most valuable artifact.** When someone asks "why did we choose Kafka?", the answer is in there with rationale, alternatives, and trade-offs.
- **Convert Mermaid diagrams.** The document includes Mermaid code blocks for system diagrams. Render them using mermaid.live, VS Code Mermaid plugin, or GitHub's built-in rendering.

---

## Adapting for Different Scenarios

### Quick Feasibility Assessment (Phases 1-2 Only)

If you just need to evaluate a PRD and propose an architecture approach without detailed component design:

```
You: /analyze-prd
[review and accept]
You: /propose-methodology
[review — stop here, don't accept]
```

Use the Phase 2 output as a feasibility discussion document.

### Legacy System Modernization

Add to `.arch/org-context.md`:
```markdown
## Legacy System Details
- Current system: [description, age, technology]
- What must be preserved: [APIs, data, integrations]
- Migration constraints: [zero downtime? phased? parallel run?]
- Data volume to migrate: [size, complexity]
```

Then in Phase 1, tell Claude:
```
You: /analyze-prd
     This is a modernization project. The PRD describes the target state 
     but doesn't cover the migration from the legacy Oracle system. Factor 
     in the migration path in your analysis.
```

### Multiple Architecture Options

Use Phase 2 to generate alternatives before committing:

```
You: /propose-methodology
[Claude proposes Option A]
You: /alternative Design this as a serverless-first architecture instead
[Claude proposes Option B]
You: /alternative Now show me a hybrid — serverless for ingestion, 
     containers for processing
[Claude proposes Option C]
You: Compare all three options in a table
[Claude compares]
You: Go with Option B
You: /accept
```

### Team Review Workflow

After generating the architecture document:

1. Share `output/architecture-document.md` with your team
2. Collect feedback offline (email, Slack, meeting)
3. Start a new Claude Code session in the same directory
4. Use `/refine` to incorporate team feedback into specific components
5. Re-run `/generate-docs` to produce an updated document

The state files and decision log persist between sessions.

---

## Troubleshooting

**Commands don't appear:** Verify `.claude/commands/` directory exists with `.md` files. Restart Claude Code.

**Hooks don't fire:** Run `/hooks` in Claude Code to verify hooks are registered. Check that Python 3 is available.

**Claude skips phases:** The hook should block this. If it doesn't, check that `settings.json` is in `.claude/` and the matcher pattern is correct. You can test the validator manually:
```bash
cat .arch/state.json | python3 .arch/scripts/validate-transition.py
```

**Claude becomes too agreeable:** Over long conversations, the adversarial personality skill may lose influence. Run `/review-component` to inject structured criticism, or `/clear` to reset the conversation with a fresh context window.

**State gets corrupted:** If `state.json` gets into an inconsistent state, you can reset it:
```bash
# Nuclear option — reset to beginning of current phase
python3 -c "
import json
state = json.load(open('.arch/state.json'))
print(json.dumps(state, indent=2))
"
# Then manually edit if needed — but you lose hook protection doing this
```

**Context window fills up:** For large projects with many components, the conversation may hit context limits. Use `/clear` between components. Claude reads state from files, not conversation history.

---

## Customization

### Adding New Commands

Create a new `.md` file in `.claude/commands/`:
```bash
echo 'Your prompt template here. Use $ARGUMENTS for parameters.' \
  > .claude/commands/my-command.md
```

### Adding New Skills

Create a directory in `.claude/skills/` with a `SKILL.md`:
```
.claude/skills/my-skill/
  └── SKILL.md    # Must include YAML frontmatter with name and description
```

### Modifying Phase Rules

Edit the `LEGAL_TRANSITIONS` and `PREREQUISITES` dictionaries in `.arch/scripts/validate-transition.py` to change what transitions are allowed.

### Adding a New Phase

1. Add the phase to `state.json` template
2. Update `LEGAL_TRANSITIONS` in `validate-transition.py`
3. Create a new slash command for the phase
4. Update CLAUDE.md phase rules
5. Update `/help` and `/status` commands

---

## Design Philosophy

This toolkit encodes a specific philosophy about architecture design:

1. **Methodology before technology.** Choose the right architecture pattern before picking technologies. Pattern decisions constrain everything downstream.

2. **Big picture before details.** Accept the holistic component architecture before designing individual components. You can't evaluate a component without understanding where it fits.

3. **One decision at a time.** Don't design all components in parallel. Each component's integration points depend on previously accepted designs.

4. **Challenge before accept.** The AI is designed to push back, not agree. If every component gets accepted on first proposal, you're not getting value from the process.

5. **Record everything.** Decisions without rationale are arbitrary. The decision log captures not just what was decided, but why, what alternatives were considered, and what was sacrificed.

6. **Hard gates, not suggestions.** Phase transitions are enforced by code, not instructions. You cannot skip ahead even if you want to.
