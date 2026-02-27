# Changelog

All notable changes to Architor are documented here.

## [2.0.0] — 2026-02-27

### npm CLI Distribution

Architor is now an npm package. Install and scaffold with:
```bash
npx architor init
npx architor init --name "My Project"
```

New CLI commands:
- `architor init` — Scaffold `.arch/` and `.claude/` into any project
- `architor verify` — Check prerequisites (Claude Code, Python 3, git)
- `architor reset` — Reset state.json to initial state (with backup)
- `architor --version` — Show version

### Phase 2 Split (2A/2B/2C)

Phase 2 now has three independently-acceptable sub-phases:
- **Phase 2A**: Architecture Pattern — accept the pattern before component mapping
- **Phase 2B**: Component Map — accept component boundaries before cross-cutting decisions
- **Phase 2C**: Cross-Cutting Decisions — auth, observability, deployment, error handling as system-wide constraints for Phase 3

### Controlled Reopen

New `/reopen` command allows reopening accepted phases or components:
- Maximum 2 reopens per project (prevents thrashing, preserves forward-only pressure)
- Cascading: reopening Phase 2A un-accepts 2B, 2C, and marks all Phase 3 components as "needs-review"
- Fully logged with justification in the decision log

### Discovery Interview

When `.arch/org-context.md` is empty, `/analyze-prd` offers a structured interview:
- 3 blocks of 5 questions (Scale & Complexity, Team Reality, Constraints)
- Auto-generates org-context.md from answers
- Derives complexity tier (Startup/Growth/Enterprise/Specialized)
- Skip option with explicit assumptions marked `[ASSUMED CONTEXT]`

### Phase 4 Validation

`/generate-docs` now includes a validation step before document generation:
- End-to-end request simulation through all components
- Risk register with probability x impact scoring
- Expanded cross-component consistency check against Phase 2C decisions

### Bug Fixes

- Fixed: Empty stdin to validate-transition.py allowed writes (now blocks)
- Fixed: First write to state.json skipped all validation (now validates schema)
- Fixed: New components could be injected as "accepted" (must start as "pending")
- Fixed: Accepted components could be silently deleted (now blocked)
- Fixed: Gate logic errors in propose-methodology and generate-docs commands
- Fixed: /accept auto-advance duplicated /design-component logic (now references it)
- Fixed: Triple challenge before acceptance (unified to /accept flow only)

### Template Improvements

- `decisions.md` now includes an example DEC-001 entry
- `architecture-document.md` now has a 13-section skeleton structure
- `org-context.md` sections marked as REQUIRED/RECOMMENDED/OPTIONAL
- State.json schema updated with sub_phase, reopens, cross_cutting fields

---

## [1.0.0] — 2026-02-27

### Initial Release

**Core System**
- CLAUDE.md with adversarial reviewer identity and phase discipline rules
- File-based state management via `.arch/state.json`
- Four-phase methodology: Evaluate, Decide, Design, Document

**Slash Commands (11)**
- `/analyze-prd` — Phase 1: PRD evaluation
- `/propose-methodology` — Phase 2: Architecture pattern + component overview
- `/design-component` — Phase 3: Detailed component design
- `/generate-docs` — Phase 4: Final architecture document generation
- `/accept`, `/refine`, `/alternative` — Decision commands
- `/review-component` — Adversarial design review
- `/status`, `/decision-log`, `/help` — Status commands

**Auto-Activating Skills (4)**
- `architecture-methodology`, `architecture-patterns`, `challenge-assumptions`, `state-manager`

**Hard Enforcement (2 hooks)**
- `validate-transition.py` — PreToolUse hook blocks illegal phase transitions
- `log-decision.py` — PostToolUse hook auto-records state changes

**Documentation**
- README, Architecture, Methodology, Contributing guides
- SVG diagrams: system architecture, enforcement model, phase workflow, component lifecycle
