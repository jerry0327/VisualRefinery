---
name: visual-refinery
description: Transform raw information into polished, evidence-grounded, publication-grade visual artifacts through research, editorial synthesis, information architecture, visual design, full-page QA, and technical validation. Use whenever the user asks to create, redesign, improve, or visually package reports, presentations, slide decks, PDFs, one-pagers, posters, guides, handbooks, decision aids, research communication, executive communication, technical explainers, educational materials, or other high-stakes visual deliverables—even when they only ask to “make it look better” or “turn this into a professional document.”
---

# VisualRefinery

VisualRefinery is a domain-agnostic production workflow for turning source material into finished visual communication.

The goal is not merely to generate a file. The goal is to create an artifact that is accurate, coherent, readable, visually intentional, technically sound, and suitable for its audience.

Apply this workflow silently. Do not insert production notes, prompt logic, chain-of-thought, internal QA instructions, or model commentary into the finished artifact.

## 1. Start with the decision, not the template

Before designing anything, determine internally:

- What is the artifact trying to help the reader understand, decide, remember, compare, approve, or do?
- Who will read or view it, in what context, and under what time or attention constraints?
- What would make the artifact misleading, unusable, or expensive to misunderstand?
- Which parts need precision, which need explanation, and which can be simplified?

Do not announce an inferred audience profile unless the user asked for it. Use the audience constraints to guide the work.

If the user supplied source files, preserve their factual boundaries, terminology, and intended meaning unless correction or reinterpretation was explicitly requested.

## 2. Build evidence before layout

Research and source-check before committing to visual structure.

For substantial work, create an internal source map with these layers as relevant:

1. user-supplied material;
2. authoritative primary sources;
3. reliable independent evaluation or secondary sources;
4. contextual or lived-experience evidence where appropriate.

For load-bearing claims, track:

- the claim;
- source and date/version;
- whether it is fact, synthesis, or inference;
- whether it may have changed;
- where it will appear in the artifact.

Use `assets/templates/claim-ledger.md` when a formal ledger is useful.

Verify unstable information such as prices, schedules, laws, policies, product specifications, software behavior, scientific guidance, clinical guidance, organizational details, and current statistics.

Never invent missing studies, prices, specifications, people, services, assignments, quotations, results, citations, or practical details.

When reliable sources disagree, represent the disagreement or uncertainty instead of silently selecting the most convenient version.

## 3. Synthesize instead of stacking sources

Do not turn the artifact into disconnected facts, quotations, review snippets, citations, or cards.

A strong section usually explains:

- what the evidence establishes;
- how pieces of evidence relate to each other;
- what the practical implication is;
- what uncertainty remains;
- what the reader should conclude or do next.

Prefer concrete mechanisms, comparisons, numbers, consequences, and examples over generic claims such as “important,” “excellent,” “robust,” or “high value.”

Use conclusions as headings when possible. Prefer a heading that communicates the finding over a label that merely names the topic.

## 4. Build information architecture before styling

Choose a narrative that fits the job. Do not force every artifact into a fixed teaching or consulting template.

Common structures include:

- question → evidence → interpretation → action;
- context → options → trade-offs → recommendation;
- problem → mechanism → diagnosis → decision → management;
- situation → sequence → exceptions → checklist;
- overview → regional or thematic sections → comparison → conclusion;
- thesis → supporting evidence → counterpoints → implication.

Each page or slide should have one dominant job.

A page may contain multiple elements, but the reader should be able to answer: **Why does this page exist?**

When revising an existing artifact, preserve working structure and design. Correct the smallest coherent set of defects unless the user requests a redesign.

Read `references/artifact-branches.md` when the requested format is a slide deck, report/PDF, one-pager, poster, guide, handbook, or data-led visual artifact.

## 5. Design for comprehension

Use visual design to clarify meaning, not to decorate empty content.

Apply these defaults:

- establish a clear typographic hierarchy;
- keep margins, spacing, and alignment consistent;
- use a restrained palette unless the context calls for something expressive;
- preserve whitespace where it creates hierarchy;
- avoid accidental large empty zones that make a page feel unfinished;
- prefer native editable charts, tables, diagrams, and shapes when editability matters;
- preserve image aspect ratios and crop deliberately;
- keep captions, footnotes, and citations legible;
- do not solve overflow by shrinking body text until it becomes uncomfortable to read.

Every major visual should answer a reader question. Examples:

- What does the system look like?
- Where does the process branch?
- How large is the difference?
- What changed over time?
- What does the environment or product actually look like?
- Which option dominates on the decision criteria?
- What sign, mechanism, structure, or pattern is being taught?

Prefer real subject-specific visuals, original charts, meaningful diagrams, maps, screenshots, or licensed imagery over generic stock imagery or decorative filler when suitable material is available.

Do not use watermarked assets.

Read `references/visual-design.md` for detailed layout, typography, imagery, accessibility, and chart guidance.

## 6. Adapt to the domain without contaminating the core

The core workflow is the same across subjects, but some domains have additional constraints.

Read `references/domain-profiles.md` only when relevant. It contains optional profiles for areas such as:

- academic and research communication;
- business and strategy;
- education and training;
- technical and engineering communication;
- data and analytics;
- policy and public information;
- medical and clinical communication;
- travel and hospitality;
- product and service comparison.

Treat profiles as overlays. Do not make domain-specific conventions universal unless they genuinely improve all artifacts.

## 7. Control density instead of hiding it

When content does not fit comfortably, choose among these remedies:

- remove redundancy;
- split the page by argument, not arbitrarily;
- merge sparse adjacent pages;
- convert prose into a diagram or table when the structure is genuinely visual;
- move secondary methodological detail to notes or an appendix;
- enlarge or simplify a chart;
- re-balance the grid;
- shorten labels while preserving meaning;
- add meaningful evidence or imagery to a sparse page when useful.

Do not:

- use tiny text as the default solution;
- create a wall of equally weighted cards;
- fill empty space with meaningless shapes, oversized numerals, or slogans;
- rasterize an entire editable slide merely to preserve layout;
- delete important content simply because layout is difficult.

## 8. Make uncertainty proportional and local

Include limitations that materially change interpretation.

Put caveats where they affect the claim rather than repeating generic warnings across the artifact.

Examples:

- place a study limitation beside the affected result;
- put date or price variability in a compact methodology note;
- mark unavailable details as “not specified” rather than inventing them;
- distinguish evidence, local practice, assumptions, and expert judgment when the distinction matters.

Do not bury the reader in defensive prose before presenting the substance.

## 9. Perform full-page visual QA

Never approve a visual artifact from source code, text extraction, cropped snippets, or automated checks alone.

For substantial deliverables:

1. render every page or slide;
2. inspect a contact sheet or montage for rhythm, hierarchy, and consistency;
3. inspect every complete page or slide at readable scale;
4. enlarge dense or complex pages as a supplemental check;
5. correct defects;
6. re-render every corrected page;
7. re-inspect the complete artifact for regressions.

Look for:

- clipped or hidden text;
- truncated table cells;
- overlapping objects;
- off-canvas elements;
- bad line breaks;
- unreadable citations;
- poor contrast;
- text placed over bright or visually noisy imagery;
- distorted or pixelated images;
- accidental empty areas;
- inconsistent spacing or alignment;
- charts that cannot be interpreted at normal viewing size;
- visual emphasis that contradicts the message.

Read `references/qa-checklist.md` for the complete preflight checklist.

Use `assets/templates/qa-log.md` when the project benefits from a page-by-page record.

## 10. Run technical validation

Where the format allows, check:

- text extraction for corrupted or missing glyphs;
- fonts for embedding or safe substitution;
- links and bookmarks;
- citations and page numbers;
- image effective resolution;
- file opening in an independent viewer;
- editable source integrity;
- export consistency between editable source and final PDF/image output.

Automated validation complements manual inspection. It does not replace it.

## 11. Preserve provenance and recoverability

For substantial projects, maintain as appropriate:

- editable source files;
- final delivery files;
- asset manifest with source and usage notes;
- claim/source ledger;
- QA log;
- stable descriptive filenames;
- a known-good prior version until the new one passes QA.

Use `assets/templates/asset-manifest.md` when external imagery or third-party assets are used.

Do not overwrite a known-good artifact before the revision has passed the relevant checks.

## 12. Deliver honestly

Never claim that research verification, full-page visual inspection, accessibility review, technical validation, or source comparison was completed unless it was actually performed.

If a required check could not be completed, say what was completed and what remains unverified.

The final artifact should not mention AI, prompts, internal workflow stages, hidden reasoning, or production instructions unless the user explicitly wants process documentation.

## Completion standard

Before calling the artifact finished, ask internally:

- Is the evidence sufficient for the claims?
- Does the structure help the reader reach the intended conclusion?
- Does every page have a reason to exist?
- Does the visual hierarchy match the information hierarchy?
- Are visuals informative rather than ornamental?
- Is the artifact readable at its real viewing size?
- Did I inspect the complete rendered pages?
- Did I recheck corrected pages?
- Is the delivered file technically sound and recoverable?
- Am I describing the QA truthfully?

If any answer is no, the work is not finished.
