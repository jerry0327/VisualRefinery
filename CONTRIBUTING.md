# Contributing to VisualRefinery

VisualRefinery aims to remain a compact, domain-agnostic production skill rather than grow into an unstructured collection of preferences.

Contributions are welcome when they make the workflow more reliable, more portable, easier to evaluate, or useful to a broader set of people.

## Good contributions

Especially useful contributions include:

- stronger visual QA heuristics;
- accessibility improvements;
- cross-domain eval cases;
- new artifact branches such as maps, infographics, posters, or data stories;
- optional domain profiles with genuinely domain-specific constraints;
- reproducible before/after examples;
- deterministic preflight or validation tooling;
- Agent Skills host compatibility improvements;
- clearer documentation and installation guidance.

## Before adding a rule

Ask where the rule belongs:

### Core `SKILL.md`

Add a rule to the core only if it is broadly useful across domains and artifact types.

### `references/artifact-branches.md`

Use this for behavior that depends primarily on the output format.

### `references/domain-profiles.md`

Use this for constraints that arise from a particular discipline or industry.

### `references/visual-design.md`

Use this for general design, typography, imagery, chart, layout, or accessibility guidance.

### `references/qa-checklist.md`

Use this for verifiable completion and preflight criteria.

If a new rule merely repeats an existing principle in different words, do not add it.

## Adding a domain profile

A good profile is short and answers:

1. What does this domain make unusually important?
2. Which mistakes have unusually high consequences?
3. Which values, conditions, or distinctions must remain explicit?
4. Which visual patterns are especially useful or misleading?

Do not duplicate the complete VisualRefinery workflow inside a profile.

## Adding an example

Examples should be reproducible and based on source material that can be shared publicly.

Include, where applicable:

- source material;
- final artifact;
- preview images;
- claim ledger;
- asset manifest;
- QA log;
- a short explanation of design decisions and limitations.

Do not fabricate an impressive-looking artifact and present it as a validated example.

## Adding an eval

Eval prompts should sound like real user requests.

Prefer evals that test whether VisualRefinery changes behavior in a meaningful way, such as:

- preserving uncertainty;
- resisting fixed templates;
- choosing the correct artifact architecture;
- avoiding tiny type;
- preserving working structure during revision;
- adapting to an unfamiliar domain;
- performing full-page QA rather than relying only on code checks.

Cross-domain coverage is important. A general skill should not be evaluated only on the domains that motivated its first version.

## Pull request checklist

Before opening a PR:

- [ ] Run `python scripts/validate_skill.py`.
- [ ] Keep `SKILL.md` at or below 500 lines; move specialized detail into references.
- [ ] Confirm all links and referenced resource paths work.
- [ ] Update `CHANGELOG.md` for user-visible behavior changes.
- [ ] Add or update eval cases when behavior changes materially.
- [ ] Avoid adding personal preferences to the domain-agnostic core.
- [ ] Avoid unnecessary dependencies.
- [ ] Explain why the change belongs in the selected file.

## Style

Write instructions for the agent in clear imperative language.

Explain the reason behind important constraints when that improves generalization.

Prefer specific, observable guidance over vague phrases such as “make it professional” or “use good design.”

Avoid excessive `MUST` language when a reasoned rule is clearer, but use explicit prohibitions for failure modes that should never occur.

## Security and trust

Skills influence agent behavior. Contributions must not contain hidden data-exfiltration behavior, credential collection, destructive actions unrelated to the documented purpose, or instructions that would surprise a reasonable user.

See [`SECURITY.md`](SECURITY.md) for reporting security concerns.
