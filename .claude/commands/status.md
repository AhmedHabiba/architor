Read `.arch/state.json` and display a comprehensive status report.

Format the output as:

```
╔══════════════════════════════════════════════════════╗
║  ARCHITECTURE AGENT — PROJECT STATUS                 ║
╠══════════════════════════════════════════════════════╣
║  Project: [project_name]                             ║
║  Started: [created_at]                               ║
║  Current Phase: Phase [N] — [Name]                   ║
╚══════════════════════════════════════════════════════╝

Phase 1: Evaluation        [✅ Accepted / 🔄 In Progress / ⬜ Not Started]
Phase 2: Methodology       [✅ Accepted / 🔄 In Progress / ⬜ Not Started]  
Phase 3: Components        [🔄 3 of 7 / ⬜ Not Started]
Phase 4: Finalization      [⬜ Not Started]
```

If in Phase 3, show component breakdown:
```
Component Progress:
  ✅ 1. API Gateway          — Accepted
  ✅ 2. Auth Service          — Accepted  
  ✅ 3. Core Database         — Accepted
  🔄 4. Message Queue         — Awaiting Acceptance ← CURRENT
  ⬜ 5. Notification Service  — Pending
  ⬜ 6. Analytics Engine      — Pending
  ⬜ 7. CDN / Static Assets   — Pending
```

Also show:
- Total decisions made: [decision_count]
- Open gaps/risks from Phase 1: [count]
- Architecture pattern: [if decided]
- Key files generated: [list of .arch files that exist]

If there's a pending action, prompt the user:
"**Next action:** [what the user should do next, e.g., 'Run /accept to accept the current component, or /refine to request changes']"

$ARGUMENTS
