#!/usr/bin/env python3
"""Sync governed public artifacts from omsp-bootstrap into the docs tree.

Single-source-of-truth rule (ADR-0003): the website never stores standards
content. This script runs at build time, walks an omsp-bootstrap checkout,
and copies ONLY Markdown artifacts whose YAML front matter carries
`Classification: Public` into the target docs directory, preserving the
repository's directory structure.

Usage: sync_content.py <bootstrap-checkout> <target-dir>
"""

import re
import shutil
import sys
from pathlib import Path

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(\n|\Z)", re.S)
PUBLIC = re.compile(r"^Classification:\s*Public\s*$", re.M)

# Never publish from these top-level directories, whatever their metadata.
EXCLUDED_TOP_LEVEL = {".claude", ".github", "tests", "build"}


def is_public(text: str) -> bool:
    match = FRONT_MATTER.match(text)
    return bool(match and PUBLIC.search(match.group(1)))


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    source, target = Path(sys.argv[1]), Path(sys.argv[2])
    if not source.is_dir():
        print(f"source checkout not found: {source}", file=sys.stderr)
        return 2

    if target.exists():
        shutil.rmtree(target)

    synced = 0
    for path in sorted(source.rglob("*.md")):
        rel = path.relative_to(source)
        if rel.parts[0] in EXCLUDED_TOP_LEVEL or rel.parts[0].startswith("."):
            continue
        text = path.read_text(encoding="utf-8")
        if not is_public(text):
            continue
        out = target / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        synced += 1

    print(f"synced {synced} public artifacts -> {target}")
    if synced == 0:
        print("refusing to publish an empty content set", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
