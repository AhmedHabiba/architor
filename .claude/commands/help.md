Read `.arch/state.json` to determine current phase.

Display available commands and contextual guidance:

```
╔══════════════════════════════════════════════════════╗
║  ARCHITECTURE AGENT — COMMAND REFERENCE              ║
╠══════════════════════════════════════════════════════╣

WORKFLOW COMMANDS:
  /analyze-prd            Phase 1: Evaluate the PRD
  /propose-methodology    Phase 2: Propose architecture pattern + components
  /design-component [n]   Phase 3: Design a specific component in detail
  /generate-docs          Phase 4: Generate final architecture document

DECISION COMMANDS:
  /accept                 Accept current proposal (phase or component)
  /refine [feedback]      Request changes to current proposal
  /alternative [request]  Request a completely different approach

REVIEW COMMANDS:
  /review-component [n]   Launch adversarial review of a component
  /decision-log [filter]  Show all decisions (optional: filter by topic)
  /status                 Show current project state and progress

SETUP:
  /help                   Show this reference

╚══════════════════════════════════════════════════════╝
```

Then based on current phase, show contextual guidance:

**If not_started:** "Start by placing your PRD in `.arch/prd.md` and filling out `.arch/org-context.md`. Then run `/analyze-prd`."

**If evaluation:** "You're in Phase 1. Review the PRD analysis and either `/accept`, `/refine`, or ask questions."

**If methodology:** "You're in Phase 2. Review the architecture pattern and component overview. `/accept` both to proceed, or `/refine` / `/alternative`."

**If components:** "You're in Phase 3, designing components one at a time. Use `/design-component`, `/review-component`, `/accept`, or `/refine`."

**If finalization:** "You're in Phase 4. Review the generated document. `/accept` to complete, or request revisions."

$ARGUMENTS
