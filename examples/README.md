# Examples

This directory is for reproducible examples built from source material that can be shared publicly.

The initial release avoids invented showcase artifacts. Examples should demonstrate a real source-to-artifact transformation and make the quality process inspectable.

## Suggested structure

```text
examples/<example-name>/
├── README.md
├── source/
├── output/
├── claim-ledger.md
├── asset-manifest.md
└── qa-log.md
```

Each example should explain:

1. the input material;
2. the intended reader and objective;
3. the design challenge;
4. the chosen information architecture;
5. important visual decisions;
6. the QA steps performed;
7. known limitations.

## Good early examples

To demonstrate generalization, prefer examples from unrelated domains, such as:

- an executive decision brief;
- a research poster or conference deck;
- a technical architecture explainer;
- an educational field guide;
- a data-led report;
- a destination comparison;
- a professional teaching deck.

The goal is to show that VisualRefinery is a general visual-artifact workflow rather than a single-domain template.

## Contribution note

Only contribute source material and assets that you have permission to redistribute publicly.
