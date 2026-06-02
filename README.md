# Agent Info Sharing

Public shared information used by agents on multiple machines.

This repository is for facts and coordination data that should not drift
between Ubuntu and Mac. It is intentionally public: keep only public source
facts, public update ledgers, shared schemas, and validation scripts here.

## Current Modules

- [platform-updates](platform-updates/) - shared OpenAI, Anthropic/Claude, and
  Hermes Agent platform update ledger used by `skill-sync`.

## Rules

- Do not include private sessions, memories, replay ledgers, telemetry, tokens,
  credentials, or machine-local state.
- Do not include machine-local absolute paths.
- If a machine has a fixed local source snapshot, record it as an abstract
  evidence label in the public ledger, then resolve the machine path locally.
- Validate before committing.
- Push updates when validation passes and the upstream branch is fast-forward
  safe.

## Machine Setup

Each machine should keep this checkout at:

```text
~/agent-info-sharing
```

Before a sync run:

```bash
cd ~/agent-info-sharing
git pull --ff-only
python3 platform-updates/scripts/validate_platform_ledger.py
```

After adding public source updates:

```bash
cd ~/agent-info-sharing
python3 platform-updates/scripts/validate_platform_ledger.py
git status --short --branch
git add platform-updates
git commit -m "Update platform ledger"
git push
```

