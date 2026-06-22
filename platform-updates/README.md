# Platform Updates

Canonical public ledger for platform updates that may affect local AI-agent
workflow architecture.

Tracked source groups:

- OpenAI and Codex
- Anthropic, Claude, and Claude Code
- Hermes Agent by Nous Research
- Superpowers by obra

The ledger tracks:

- source catalogs and checked-through dates
- recent relevant updates
- local architecture implications
- proposal-only notes before any local skill, registry, hook, or agent change

## Files

- [ledger/platform-update-ledger.md](ledger/platform-update-ledger.md) -
  canonical public ledger.
- [schema/platform-update-ledger.schema.md](schema/platform-update-ledger.schema.md) -
  required structure and publication rules.
- [scripts/validate_platform_ledger.py](scripts/validate_platform_ledger.py) -
  validation for required sections and public-safety checks.

## `skill-sync` Integration

`skill-sync` should read:

```text
~/agent-info-sharing/platform-updates/ledger/platform-update-ledger.md
```

Machine-local fallbacks may exist, but this public ledger is the canonical
shared source.
