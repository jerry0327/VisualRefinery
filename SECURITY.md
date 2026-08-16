# Security Policy

VisualRefinery is primarily an instruction-based Agent Skill, but skill repositories can still create security and trust risks because agents may follow bundled instructions or scripts automatically.

## Reporting a concern

Please report security-sensitive concerns privately to the repository maintainer through GitHub's private vulnerability reporting feature when available.

Avoid opening a public issue that contains active exploit details, credentials, private data, or instructions that would make abuse materially easier.

## In scope

Examples include:

- hidden or misleading agent instructions;
- instructions that attempt to obtain or expose credentials;
- unexpected network or file-system behavior in bundled scripts;
- dependency or workflow changes that introduce avoidable supply-chain risk;
- content that materially differs from the behavior described to the user;
- unsafe handling of source material or generated artifacts.

## Design principles

VisualRefinery should follow the principle of least surprise:

- bundled behavior must be consistent with the documented purpose;
- scripts should be deterministic and narrowly scoped;
- network access should not be required by hidden implementation details;
- user-provided material should not be uploaded or transmitted merely for telemetry;
- examples and assets should have clear provenance;
- new dependencies require a concrete justification.

## Supported versions

Security fixes are applied to the current main branch and the latest released version unless otherwise stated.
