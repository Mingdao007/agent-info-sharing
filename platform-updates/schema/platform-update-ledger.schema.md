# Platform Update Ledger Schema

The canonical ledger is a Markdown file at:

```text
ledger/platform-update-ledger.md
```

## Required Top-Level Fields

- `Last run:`
- `Default local implication lookback:`
- `Historical Source Catalog`
- `Recent Checked Entries`

## Required Source Groups

The ledger must include these source groups:

- `openai`
- `anthropic-claude`
- `hermes-agent`

Each source group must include:

- coverage baseline
- first official source
- `Checked through: YYYY-MM-DD`
- canonical source families
- engineer or maintainer watchlist when useful
- current high-signal per-run source subset
- recent checked entries table

## Watchlist Fields

Engineer or maintainer watchlist entries must include:

- `identity_status: verified | candidate | conflict`
- `source_type: <kind>`
- `evidence_url: <url or public evidence phrase>`
- `trust_rule: <how this source may be used>`

Candidate and conflict entries are discovery-only.

## Public-Safety Rules

Do not include:

- machine-local absolute paths such as `/home/...` or `/Users/...`
- private repository paths
- `.codex` session, memory, replay, telemetry, or skill state paths
- credentials, private tokens, or account identifiers
- private conversation/session excerpts

Allowed references to local source drops must be abstract and stable, for
example:

```text
local_source_drop: claude-code-src-snapshot
snapshot_role: fixed historical evidence, not an incremental update source
```

## Update Rules

- Incremental scans update checked-through dates only when sources were
  reachable or a concrete unavailability status was recorded.
- Public architecture implications stay proposal-only until the user explicitly
  approves a local implementation.
- Social posts alone do not justify local architecture changes.
- A direct source URL should be verified openable before being added as a
  normal public ledger link.

