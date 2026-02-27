Read `.arch/state.json` and display a comprehensive status report.

Format the output as:

```
ARCHITECTURE AGENT — PROJECT STATUS

Project: [project_name]
Started: [created_at]
Current Phase: Phase [N] — [Name]

Phase 1: Evaluation        [Accepted / In Progress / Not Started]
Phase 2: Methodology
  2A Pattern:              [Accepted / Awaiting Acceptance / Not Started]
  2B Component Map:        [Accepted / Awaiting Acceptance / Not Started]
  2C Cross-Cutting:        [Accepted / Awaiting Acceptance / Not Started]
Phase 3: Components        [X of Y / Not Started]
Phase 4: Finalization      [Not Started]

Reopens: [count] of [max] used
Decisions: [decision_count]
```

If in Phase 3, show component breakdown:
```
Component Progress:
  [status] 1. API Gateway          — Accepted
  [status] 2. Auth Service          — Accepted
  [status] 3. Core Database         — Accepted
  [status] 4. Message Queue         — Awaiting Acceptance <- CURRENT
  [status] 5. Notification Service  — Pending
  [status] 6. Analytics Engine      — Pending
  [status] 7. CDN / Static Assets   — Pending
```

Use these status indicators:
- Accepted: check mark
- In Progress / Awaiting Acceptance: in progress indicator
- Pending: empty indicator
- Needs Review: warning indicator (after a reopen)

Also show:
- Architecture pattern: [if decided]
- Org context source: [file / interview / assumed / not loaded]
- Open gaps/risks from Phase 1: [count]
- Key files generated: [list of .arch files that exist]

If there's a pending action, prompt the user:
"**Next action:** [what the user should do next, e.g., 'Run /accept to accept the current component, or /refine to request changes']"

$ARGUMENTS
