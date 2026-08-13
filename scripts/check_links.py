from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LINK = re.compile(r"\]\(([^)]+)\)")


def main() -> int:
    missing: list[str] = []
    for source in DOCS.rglob("*.md"):
        text = source.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), 1):
            for match in LINK.finditer(line):
                target = match.group(1).split("#", 1)[0]
                if not target or "://" in target or target.startswith(
                    ("mailto:", "#", "/")
                ):
                    continue
                resolved = (source.parent / target).resolve()
                if resolved.suffix == "":
                    resolved = resolved.with_suffix(".md")
                if not resolved.exists():
                    missing.append(
                        f"{source.relative_to(ROOT)}:{line_number}: {target}"
                    )
    if missing:
        print("Missing local links:", *missing, sep="\n")
        return 1
    print("Local Markdown links are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
