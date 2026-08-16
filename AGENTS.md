# AGENTS.md

This repository contains an Agent Skill. Changes should preserve both human readability and machine usefulness.

## Repository goal

VisualRefinery teaches AI agents how to turn raw source material into polished, evidence-grounded visual artifacts through editorial judgment, visual design, full-page QA, and technical validation.

The core must remain domain-agnostic.

## Before changing the skill

1. Read `skills/visual-refinery/SKILL.md` completely.
2. Read only the reference file(s) relevant to the proposed change.
3. Check whether the change belongs in the core, an artifact branch, a domain profile, visual design guidance, or QA.
4. Avoid duplicating an existing rule.
5. Update evals when behavior changes materially.
6. Run `python scripts/validate_skill.py` before completion.

## Structural rules

- Keep the installable skill under `skills/visual-refinery/`.
- Keep `SKILL.md` at or below 500 lines.
- Put specialized detail in `references/`.
- Put reusable working templates in `assets/templates/`.
- Keep eval prompts realistic and cross-domain.
- Do not add a dependency unless it creates clear deterministic value.

## Core design rule

Do not make a domain-specific convention universal.

If a new requirement is specific to medicine, finance, travel, law, education, engineering, or another field, place it in the domain profiles unless the underlying principle applies broadly.

## Documentation rule

README content should answer, in this order:

1. What is VisualRefinery?
2. Why would someone use it?
3. How can they install or try it quickly?
4. How does it work?
5. What does the repository contain?
6. How can they contribute?

Do not let project philosophy bury the quick start.

## Trust rule

Never add hidden behavior, credential collection, data exfiltration, destructive actions unrelated to the documented purpose, or instructions that would surprise a reasonable user who read the project description.
