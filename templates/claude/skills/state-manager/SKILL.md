---
name: state-manager
description: Manages architecture project state in .arch/state.json and .arch/decisions.md. Activates when reading or updating project phase state, tracking component acceptance, logging decisions, or validating phase transitions.
---

# State Manager

## State File: `.arch/state.json`

This file is the single source of truth for project progress. ALWAYS read it before responding to architecture queries. ALWAYS update it after state changes.

### Reading State
- Parse the JSON file
- Check `current_phase` to know where we are
- Check phase-specific status fields for detail
- For Phase 2, check `sub_phase` and individual acceptance flags (pattern_accepted, components_overview_accepted, cross_cutting_accepted)
- For Phase 3, check `components` object for per-component status
- Check `reopens.count` and `reopens.max` for reopen availability

### Valid Phase Transitions
```
not_started → evaluation     (when /analyze-prd runs)
evaluation → methodology     (when Phase 1 is accepted)
methodology → components     (when Phase 2 is fully accepted: pattern + components + cross-cutting)
components → finalization    (when ALL components accepted)
```

Backward transitions are ONLY allowed via /reopen (max 2 per project).

### Phase 2 Sub-Phases
```
pattern → components_overview → cross_cutting
```
Each sub-phase is accepted independently via /accept. All three must be accepted for Phase 2 to be complete.

### Component Status Values
```
pending → in_progress        (when /design-component starts)
in_progress → awaiting_acceptance  (when design is presented)
awaiting_acceptance → accepted     (when user accepts)
awaiting_acceptance → in_progress  (when user refines)
needs-review → in_progress         (after a reopen cascades)
```

### Updating State
When updating state.json:
1. Read current state
2. Validate the transition is legal
3. Write the updated state
4. Increment `decision_count` if a decision was made

## Decision Log: `.arch/decisions.md`

Append-only file. Never edit previous entries. Format:

```markdown
### [DEC-NNN] Phase X | Category
- **Decision:** [What was decided]
- **Rationale:** [Why this choice]
- **Alternatives:** [What else was considered]
- **Trade-offs:** [What was sacrificed]
- **Risk:** [Any residual risk]
- **Date:** [ISO timestamp]
```

Categories: Requirements | Pattern | Technology | Integration | Security | Infrastructure | Process | Reopen

### Automatic Logging Events
Log a decision entry for:
- Phase acceptance
- Phase transition
- Sub-phase acceptance (2A, 2B, 2C)
- Technology selection (per component)
- Refinement requests (what changed and why)
- Alternative requests (what was replaced)
- Review findings (significant concerns raised)
- Reopen operations (with cascade details)
