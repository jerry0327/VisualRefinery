#!/usr/bin/env python3
"""Lightweight structural validation for the VisualRefinery skill repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "visual-refinery"
SKILL_MD = SKILL_DIR / "SKILL.md"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def check_exists(path: Path) -> None:
    if not path.exists():
        fail(f"missing required path: {path.relative_to(ROOT)}")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")

    values: dict[str, str] = {}
    for raw in match.group(1).splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            fail(f"invalid frontmatter line: {raw!r}")
        key, value = raw.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def main() -> int:
    required = [
        SKILL_MD,
        SKILL_DIR / "references" / "visual-design.md",
        SKILL_DIR / "references" / "artifact-branches.md",
        SKILL_DIR / "references" / "domain-profiles.md",
        SKILL_DIR / "references" / "qa-checklist.md",
        SKILL_DIR / "assets" / "templates" / "claim-ledger.md",
        SKILL_DIR / "assets" / "templates" / "asset-manifest.md",
        SKILL_DIR / "assets" / "templates" / "qa-log.md",
        SKILL_DIR / "evals" / "evals.json",
        ROOT / "README.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "LICENSE",
    ]
    for path in required:
        check_exists(path)

    skill_text = SKILL_MD.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(skill_text)

    if frontmatter.get("name") != "visual-refinery":
        fail("frontmatter name must be 'visual-refinery'")
    if not frontmatter.get("description"):
        fail("frontmatter description is required")
    if len(frontmatter["description"]) < 80:
        fail("description is too short to communicate purpose and trigger conditions")

    line_count = len(skill_text.splitlines())
    if line_count > 500:
        fail(f"SKILL.md is {line_count} lines; keep it at or below 500 and use references")

    referenced = [
        "references/artifact-branches.md",
        "references/domain-profiles.md",
        "references/visual-design.md",
        "references/qa-checklist.md",
        "assets/templates/claim-ledger.md",
        "assets/templates/asset-manifest.md",
        "assets/templates/qa-log.md",
    ]
    for rel in referenced:
        if rel not in skill_text:
            fail(f"SKILL.md does not reference bundled resource: {rel}")
        check_exists(SKILL_DIR / rel)

    eval_path = SKILL_DIR / "evals" / "evals.json"
    try:
        payload = json.loads(eval_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"evals.json is invalid JSON: {exc}")

    if payload.get("skill_name") != "visual-refinery":
        fail("evals.json skill_name must be 'visual-refinery'")
    evals = payload.get("evals")
    if not isinstance(evals, list) or len(evals) < 6:
        fail("evals.json should contain at least 6 cross-domain eval cases")

    names = set()
    for item in evals:
        if not isinstance(item, dict):
            fail("each eval must be an object")
        for field in ("id", "name", "prompt", "expected_output"):
            if not item.get(field):
                fail(f"eval missing required field: {field}")
        if item["name"] in names:
            fail(f"duplicate eval name: {item['name']}")
        names.add(item["name"])

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for marker in (
        "npx skills add jerry0327/VisualRefinery --skill visual-refinery",
        "skills/visual-refinery/SKILL.md",
        "Full-page QA",
    ):
        if marker not in readme:
            fail(f"README is missing expected project entry point: {marker!r}")

    print("PASS: VisualRefinery structure and core metadata are valid")
    print(f"PASS: SKILL.md line count = {line_count}")
    print(f"PASS: cross-domain eval cases = {len(evals)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
