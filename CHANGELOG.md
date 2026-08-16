# Changelog

All notable user-visible changes to VisualRefinery will be documented here.

The project uses semantic versioning for released behavior.

## [0.1.0] - 2026-08-16

### Added

- Initial public release of the `visual-refinery` Agent Skill.
- Domain-agnostic evidence → synthesis → architecture → design → QA → delivery workflow.
- Progressive-disclosure reference files for:
  - visual design;
  - artifact-specific branches;
  - optional domain profiles;
  - full-page and technical QA.
- Reusable claim-ledger, asset-manifest, and QA-log templates.
- Cross-domain eval set spanning strategy, research, engineering, education, travel, clinical teaching, public policy, and artifact revision.
- Lightweight structural validator and GitHub Actions workflow.
- Agent Plugins metadata for portable discovery.
- Contributor and security guidance.

### Changed from the original private workflow

- Removed user-specific defaults and personal preferences.
- Moved medical and travel guidance out of the core and into optional domain profiles.
- Generalized the workflow to arbitrary subjects and visual artifact types.
- Reorganized the project around the self-contained `skills/<name>/SKILL.md` convention.
- Reduced core context by moving specialized detail into on-demand references.
- Added explicit accessibility, cross-domain evaluation, portability, and contribution rules.
