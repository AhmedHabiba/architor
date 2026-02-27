# Changelog

All notable changes to the Architecture Agent are documented here.

## [1.0.0] — 2026-02-27

### Initial Release

**Core System**
- CLAUDE.md with adversarial reviewer identity and phase discipline rules
- File-based state management via `.arch/state.json`
- Four-phase methodology: Evaluate → Decide → Design → Document

**Slash Commands (11)**
- `/analyze-prd` — Phase 1: PRD evaluation
- `/propose-methodology` — Phase 2: Architecture pattern + component overview
- `/design-component` — Phase 3: Detailed component design
- `/generate-docs` — Phase 4: Final architecture document generation
- `/accept` — Accept current proposal with adversarial challenge
- `/refine` — Request changes to current proposal
- `/alternative` — Request different approach or technology
- `/review-component` — Adversarial design review
- `/status` — Show project state and progress
- `/decision-log` — Show decision history
- `/help` — Command reference

**Auto-Activating Skills (4)**
- `architecture-methodology` — Phase orchestration and boundary enforcement
- `architecture-patterns` — Pattern selection knowledge (team-aware)
- `challenge-assumptions` — Adversarial reviewer personality
- `state-manager` — State read/write logic and transition rules

**Hard Enforcement (2 hooks)**
- `validate-transition.py` — PreToolUse hook blocks illegal phase transitions
- `log-decision.py` — PostToolUse hook auto-records state changes

**Templates**
- `org-context.md` — Organizational constraints template (team profile, tech stack, compliance, lessons learned)
- `prd.md` — PRD input placeholder
- `state.json` — Clean state machine template

**Documentation**
- Comprehensive README with step-by-step walkthrough
- Architecture design document with system diagrams
- Methodology guide for the four-phase process
- Contributing guide
- SVG diagrams: system architecture, enforcement model, phase workflow, component lifecycle
