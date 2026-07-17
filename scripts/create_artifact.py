#!/usr/bin/env python3
"""Create a non-overwriting Markdown shell for an Unknowns Workflow artifact."""

from __future__ import annotations

import argparse
from pathlib import Path


TEMPLATES = {
    "discovery": """# Discovery brief: {title}\n\n## Goal and non-goals\n\n## Evidence inspected\n\n## Unknown unknowns\n\n## Unknown knowns\n\n## Known unknowns\n\n## Prioritized actions\n\n## Assumptions and decisions\n\n## Revised task brief / next step\n""",
    "implementation-notes": """# Implementation notes: {title}\n\n## Original plan\n\n## Deviations\n\n### [Milestone]\n- Planned approach:\n- Discovered fact and evidence:\n- Conservative decision:\n- Impact:\n- Follow-up:\n""",
    "merge-review": """# Merge review: {title}\n\n## Outcome\n\n## Scope and non-scope\n\n## Key behavior paths and evidence\n\n## Decisions and deviations\n\n## Risks, rollback, and remaining unknowns\n\n## Verification performed\n\n## Verification not performed\n\n## Comprehension quiz\n1. \n2. \n3. \n\n## Answers and explanations\n""",
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=sorted(TEMPLATES))
    parser.add_argument("--title", default="Untitled task")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    output = args.output.resolve()
    if output.exists():
        parser.error(f"refusing to overwrite existing file: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEMPLATES[args.kind].format(title=args.title), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
