#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_GROUPS = ("openai", "anthropic-claude", "hermes-agent", "superpowers")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FORBIDDEN_PATTERNS = (
    re.compile(r"/home/[A-Za-z0-9_.-]+"),
    re.compile(r"/Users/[A-Za-z0-9_.-]+"),
    re.compile(r"\.codex"),
    re.compile(r"codex-private-skills"),
    re.compile(r"replay-ledger"),
    re.compile(r"history\.jsonl"),
    re.compile(r"sessions/"),
)


def section_for_group(text: str, group: str) -> str:
    marker = f"### {group}"
    start = text.find(marker)
    if start == -1:
        return ""
    next_start = text.find("\n### ", start + len(marker))
    if next_start == -1:
        return text[start:]
    return text[start:next_start]


def checked_through(section: str) -> str | None:
    match = re.search(r"^- Checked through: `([^`]+)`", section, re.MULTILINE)
    if not match:
        return None
    return match.group(1)


def validate(path: Path) -> tuple[list[str], list[str]]:
    issues: list[str] = []
    warnings: list[str] = []
    if not path.exists():
        return [f"missing ledger: {path}"], warnings

    text = path.read_text(encoding="utf-8")
    for required in (
        "Last run:",
        "Default local implication lookback:",
        "## Publication Contract",
        "## Historical Source Catalog",
        "Recent checked entries:",
    ):
        if required not in text:
            issues.append(f"missing required marker: {required}")

    for pattern in FORBIDDEN_PATTERNS:
        for match in pattern.finditer(text):
            line_no = text.count("\n", 0, match.start()) + 1
            issues.append(f"forbidden public ledger token at line {line_no}: {match.group(0)}")

    for group in REQUIRED_GROUPS:
        section = section_for_group(text, group)
        if not section:
            issues.append(f"missing source group: {group}")
            continue
        date_value = checked_through(section)
        if not date_value:
            issues.append(f"{group}: missing checked-through date")
        elif not DATE_RE.match(date_value):
            issues.append(f"{group}: checked-through is not YYYY-MM-DD: {date_value}")
        if "Recent checked entries:" not in section:
            issues.append(f"{group}: missing recent checked entries section")
        for field in ("identity_status:", "source_type:", "evidence_url:", "trust_rule:"):
            if "watchlist" in section.lower() and field not in section:
                warnings.append(f"{group}: watchlist exists but field may be missing: {field}")

    if "local_source_drop:" in text and "snapshot_role:" not in text:
        issues.append("local source drop reference must include snapshot_role")

    return issues, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the public AI platform update ledger.")
    parser.add_argument(
        "--ledger",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "ledger" / "platform-update-ledger.md",
    )
    args = parser.parse_args()

    issues, warnings = validate(args.ledger)
    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)
    if issues:
        for issue in issues:
            print(f"error: {issue}", file=sys.stderr)
        return 1
    print(f"ok: {args.ledger}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
