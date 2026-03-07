---
name: state-manager
description: Manages architecture project state in .arch/state.json and .arch/decisions.md. Use when reading or updating project phase state, checking architecture status or project progress, asking "what phase are we in", tracking component acceptance, recording or logging decisions, or validating phase transitions.
---

# State Manager

## State File: `.arch/state.json`

This file is the single source of truth for project progress. Read it before responding to architecture queries and update it after state changes.

### Reading State
- Parse the JSON file
- Check `current_phase` to know where we are
- Check phase-specific status fields for detail
- For Phase 2, check `sub_phase` and individual acceptance flags (pattern_accepted, components_overview_accepted, cross_cutting_accepted)
- For Phase 3, check `components` object for per-component status
- Check `reopens.count` and `reopens.max` for reopen availability

**Example – read state:**
```python
import json, pathlib
state = json.loads(pathlib.Path(".arch/state.json").read_text())
print(state["current_phase"])
```

### Valid Phase Transitions
```
not_started → evaluation     (when /analyze-prd runs)
evaluation → methodology     (when Phase 1 is accepted)
methodology → components     (when Phase 2 is fully accepted: pattern + components + cross-cutting)
components → finalization    (when ALL components accepted)
```

Backward transitions are only allowed via /reopen (max 2 per project).

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

**Example – validate and write state:**
```python
import json, pathlib

VALID_TRANSITIONS = {
    "not_started": ["evaluation"],
    "evaluation": ["methodology"],
    "methodology": ["components"],
    "components": ["finalization"],
}

def apply_transition(new_phase):
    p = pathlib.Path(".arch/state.json")
    state = json.loads(p.read_text())
    current = state["current_phase"]
    allowed = VALID_TRANSITIONS.get(current, [])

    if new_phase not in allowed:
        # Invalid transition: do NOT write state.
        # Report the error to the user and stop.
        raise ValueError(
            f"Invalid transition: '{current}' → '{new_phase}'. "
            f"Allowed next phases: {allowed or ['none (use /reopen for backward transitions)']}"
        )

    state["current_phase"] = new_phase
    state["decision_count"] += 1
    p.write_text(json.dumps(state, indent=2))
    return state
```

**If validation fails:**
- Do not write any changes to `state.json`.
- Inform the user of the current phase and the valid next transitions.
- If a backward transition is needed, direct the user to use `/reopen` (subject to `reopens.count < reopens.max`).
- Log a warning entry in `decisions.md` under category `Process` if the invalid attempt was user-initiated.

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

**Example – append a decision entry:**
```python
import pathlib
entry = """
### [DEC-001] Phase 1 | Pattern
- **Decision:** Adopt hexagonal architecture
- **Rationale:** Decouples domain from infrastructure
- **Alternatives:** Layered monolith
- **Trade-offs:** Higher initial complexity
- **Risk:** Team familiarity required
- **Date:** 2024-06-01T10:00:00Z
"""
pathlib.Path(".arch/decisions.md").open("a").write(entry)
```

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
