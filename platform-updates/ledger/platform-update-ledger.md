# Skill Sync Platform Update Ledger

Public canonical ledger for incremental OpenAI, Anthropic/Claude, and Hermes
Agent platform update checks.

Last run: `2026-06-08T11:20+08:00`
Default local implication lookback: `60d`

## Publication Contract

This ledger contains public source facts and public architecture implications.
It intentionally excludes machine-local paths, private session logs, replay
ledgers, telemetry, and local skill state.

Local source drops are allowed only as abstract fixed evidence labels. They are
not incremental update surfaces and do not participate in checked-through
updates.

## Historical Source Catalog

This catalog is broader than the per-run scan. It records update surfaces to
cover from each company or project's public baseline onward. Per-run work still
uses checked-through boundaries and only inspects newly published items.

Social posts are valid discovery/context sources after account verification,
but do not use a social post alone to justify local architecture changes.
Prefer official docs, changelogs, repo releases, blog/news posts, or direct
product behavior before writing local skills, registries, subagents, hooks, or
config.

Engineer blogs and social posts remain discovery/context sources unless
identity and claim are verified against official docs, source code, release
notes, or reproduction.

### openai

- Coverage baseline:
  - Public announcement: `2015-12-11`
  - Official startup note: OpenAI later described officially getting started in
    early January 2016.
  - First official source:
    <https://openai.com/index/introducing-openai/>
- Checked through: `2026-06-08`
- Canonical source families:
  - News / historical blog archive: <https://openai.com/news/>
  - RSS: <https://openai.com/news/rss.xml>
  - Research index: <https://openai.com/research/>
  - OpenAI API/platform changelog:
    <https://developers.openai.com/api/docs/changelog>
  - OpenAI Developers docs and guides:
    <https://developers.openai.com/>
  - Codex docs:
    <https://developers.openai.com/codex/>
  - Codex config reference:
    <https://developers.openai.com/codex/config-reference>
  - Apps SDK changelog:
    <https://developers.openai.com/apps-sdk/changelog>
  - Platform status: <https://status.openai.com/>
  - GitHub organization: <https://github.com/openai>
  - Official social:
    - <https://x.com/OpenAI>
    - <https://twitter.com/openai>
  - Engineer / maintainer watchlist:
    - Tibo / Tibo Sottiaux
      identity_status: candidate
      source_type: engineer_social
      evidence_url: <https://x.com/thsottiaux>; <https://twitter.com/thsottiaux>
      trust_rule: discovery/context only until cross-checked against official OpenAI/Codex sources or local behavior
      notes: candidate OpenAI/Codex public commentary source.
    - Michael Bolin
      identity_status: verified
      source_type: official_engineering_author
      evidence_url: <https://openai.com/index/unrolling-the-codex-agent-loop/>
      trust_rule: track future Codex architecture posts under official OpenAI News first; use personal/social sources only if identity is verified
      notes: official OpenAI Codex engineering author.
- Current high-signal per-run source subset:
  - <https://developers.openai.com/api/docs/changelog>
  - <https://developers.openai.com/codex/config-reference>

Recent checked entries:

| Date | Title | Source | Local relevance | Status |
|---|---|---|---|---|
| 2026-06-08 | Incremental check: no OpenAI changelog item newer than Jun 4 | <https://developers.openai.com/api/docs/changelog>; <https://developers.openai.com/codex/> | Changelog and Codex docs were reachable; no new post-`2026-06-05` local Codex skill, registry, MCP, permission, or safety-gate architecture change was found. | checked |
| 2026-06-03 | Reusable prompts, Evals platform, and Agent Builder deprecation notices | <https://developers.openai.com/api/docs/deprecations>; <https://developers.openai.com/api/docs/changelog> | Relevant to future OpenAI-platform guidance: avoid new local workflows depending on reusable prompt objects, Evals dashboard/API, or Agent Builder. No immediate local Codex skill/runtime mutation needed. | checked |
| 2026-06-01 | OpenAI models available in Amazon Bedrock through OpenAI-compatible Responses API endpoint | <https://developers.openai.com/api/docs/changelog>; <https://developers.openai.com/api/docs/production-best-practices/amazon-bedrock> | Relevant to future provider-routing or Bedrock deployment discussions. No local Codex skill, registry, MCP, or permission architecture change needed without a user request to use Bedrock. | checked |
| 2026-05 | Secure MCP Tunnel | <https://developers.openai.com/api/docs/changelog> | Relevant to private/on-prem MCP access for Codex, Responses API, and AgentKit; proposal-only for future local MCP architecture. | checked |
| 2026-05-07 | OpenAI Developers plugin for Codex | <https://developers.openai.com/api/docs/changelog> | Relevant to Codex plugin/API setup guidance, but no immediate local skill-package mutation required. | checked |
| 2026-05-06 | Agents SDK TypeScript with sandbox agents | <https://developers.openai.com/api/docs/changelog> | Relevant to future agent-harness architecture; keep as proposal-only unless a user asks to build SDK agents. | checked |
| 2026-05 | Codex config reference updates for granular approvals, hooks, MCP, skills, memories, permissions | <https://developers.openai.com/codex/config-reference> | Relevant to local config and safety-gate skills; no immediate write without a specific config change request. | checked |

### anthropic-claude

- Coverage baseline:
  - Founding: beginning of `2021`
  - First public news/funding post observed: `2021-05-28`
  - Andrej Karpathy publicly reported joining Anthropic: `2026-05-19`
  - First official source:
    <https://www.anthropic.com/news/anthropic-raises-124-million-to-build-more-reliable-general-ai-systems>
- Checked through: `2026-06-08`
- Canonical source families:
  - Anthropic Newsroom: <https://www.anthropic.com/news>
  - Anthropic Research: <https://www.anthropic.com/research>
  - Anthropic Engineering: <https://www.anthropic.com/engineering>
  - Claude blog: <https://claude.com/blog>
  - Claude Code product page:
    <https://claude.com/product/claude-code>
  - Claude Code What's New / changelog:
    <https://code.claude.com/docs/en/whats-new/>
  - Claude/Anthropic platform docs:
    <https://platform.claude.com/docs/>
  - Managed Agents docs:
    <https://platform.claude.com/docs/en/managed-agents/quickstart>
  - Local source drops:
    - local_source_drop: `claude-code-src-snapshot`
      snapshot_role: fixed historical implementation evidence, not an incremental update source
      notes: Use only to verify behavior of the captured Claude Code source snapshot; do not treat it as a live platform source.
  - Anthropic status: <https://status.anthropic.com/>
  - GitHub organization, when relevant:
    <https://github.com/anthropics>
  - Karpathy GitHub as an Anthropic engineer source after the public
    `2026-05-19` Anthropic hire announcement:
    <https://github.com/karpathy>
    - High-signal repositories to sample when relevant:
      <https://github.com/karpathy/llm.c>
      <https://github.com/karpathy/autoresearch>
      <https://github.com/karpathy/nanochat>
      <https://github.com/karpathy/nanoGPT>
      <https://github.com/karpathy/LLM101n>
      <https://github.com/karpathy/rendergit>
  - Engineer / maintainer watchlist:
    - Boris Cherny
      identity_status: candidate
      source_type: engineer_social_interview
      evidence_url: <https://x.com/bcherny>; <https://twitter.com/bcherny>
      trust_rule: use X/interview material for workflow discovery only; verify implementation claims against docs, source snapshots, or release notes before changing local skills
      notes: Claude Code creator / Head of Claude Code candidate source.
    - Barry Zhang
      identity_status: verified
      source_type: official_engineering_author
      evidence_url: <https://www.anthropic.com/engineering/building-effective-agents>; <https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work>
      trust_rule: official sources can inform proposals; personal/social claims still need source-code, docs, release-note, or reproduction corroboration before local architecture changes
      notes: Anthropic official engineering author / Agent Skills source.
    - Barry Zhang personal site candidate
      identity_status: conflict
      source_type: personal_site
      evidence_url: <https://www.barry.ooo/>
      trust_rule: do not treat as an Anthropic Barry source unless later identity verification resolves the conflict
      notes: site appears to describe a Barry Zhang who is co-founder/CEO of Hex, not the Anthropic engineer.
    - Erik Schluntz
      identity_status: verified
      source_type: official_engineering_author
      evidence_url: <https://www.anthropic.com/engineering/building-effective-agents>
      trust_rule: monitor official Anthropic Engineering posts and verified personal/social sources
      notes: official Anthropic engineering co-author for Building effective agents.
    - Andrej Karpathy
      identity_status: verified
      source_type: anthropic_engineer_github
      evidence_url: <https://github.com/karpathy>
      trust_rule: use GitHub activity as Anthropic-adjacent discovery/context for LLM, agent, training, and workflow ideas; corroborate against repo code, README, official Anthropic sources, or reproducible behavior before proposing local architecture changes
      notes: public reporting on `2026-05-19` says Karpathy joined Anthropic's pre-training team; GitHub profile remains a source for technical artifacts, not a standalone approval basis for local writes.
    - Mahesh Murag
      identity_status: candidate
      source_type: conference_talk
      evidence_url: AI Engineer Summit "Don't Build Agents, Build Skills Instead" with Barry Zhang
      trust_rule: monitor official Anthropic/Claude posts, AI Engineer Summit material, and verified personal/social sources
      notes: Agent Skills co-presenter candidate.
- Current high-signal per-run source subset:
  - <https://code.claude.com/docs/en/whats-new/2026-w22>
  - <https://code.claude.com/docs/en/whats-new/2026-w21>
  - <https://code.claude.com/docs/en/whats-new/2026-w20>
  - <https://platform.claude.com/docs/en/managed-agents/quickstart>
  - <https://github.com/karpathy>
  - <https://github.com/karpathy/autoresearch>
  - <https://github.com/karpathy/nanochat>
  - <https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills>

Recent checked entries:

| Date | Title | Source | Local relevance | Status |
|---|---|---|---|---|
| 2026-06-06 | Claude Code 2.1.166/2.1.167: fallback models, deny-rule globbing, and cross-session authority hardening | <https://code.claude.com/docs/en/changelog> | Relevant as comparison material for local model fallback design, permission-rule precision, and subagent/cross-session authority boundaries. Proposal-only; no direct Codex skill or registry write. | checked |
| 2026-06-03 | Claude Code 2.1.162: agents JSON waiting state, explicit Grep/Glob tools, persistent effort confirmation, WebFetch rule precedence | <https://code.claude.com/docs/en/changelog> | Relevant as comparison material for local subagent observability, user-visible default-setting confirmations, and explicit permission-rule precedence. Proposal-only; no direct Codex skill or registry change. | checked |
| 2026-06-03 | Lessons from building Claude Code: How we use skills | <https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills> | Relevant practice evidence for skill folder structure, gotchas, verification, progressive disclosure, functional skill categories, usage logging, and marketplace governance. Treat the nine categories as functional taxonomy, not as lifecycle tier schema. | checked |
| 2026-06-02 | Incremental check: no Week 23 Claude Code digest yet | <https://code.claude.com/docs/en/whats-new> | Official What's New page still surfaced Week 22 (`2026-05-25` to `2026-05-29`) as the newest weekly digest. No new local architecture action. | checked |
| 2026-05-19 | Karpathy joins Anthropic; GitHub source tracked under Anthropic/Claude | <https://github.com/karpathy> | Relevant as an Anthropic engineer source for LLM training, agent workflow, and tooling ideas. Use as discovery/context only unless a specific repo artifact and local need justify a proposal. | checked |
| 2026-05-25..29 | Dynamic workflows and skill reload behavior | <https://code.claude.com/docs/en/whats-new/2026-w22> | Relevant to future workflow/subagent architecture and skill reload expectations; proposal-only for local Codex skills. | checked |
| 2026-05-18..22 | Auto mode, usage attribution for skills/subagents/plugins/MCP, background session scripting | <https://code.claude.com/docs/en/whats-new/2026-w21> | Relevant to local observability of skills and subagents; no immediate local mutation required. | checked |
| 2026-05-11..15 | Agent view, `/goal`, hook exec form, plugin root-level `SKILL.md` surfacing | <https://code.claude.com/docs/en/whats-new/2026-w20> | Relevant to goal-led workflows, hook design, and plugin skill packaging. | checked |
| 2026-05 | Managed Agents core concepts: agents include tools, MCP servers, and skills; environments can be cloud or self-hosted sandboxes | <https://platform.claude.com/docs/en/managed-agents/quickstart> | Relevant to architecture comparison only; no direct Codex runtime change. | checked |

### hermes-agent

- Coverage baseline:
  - Public GitHub repository created: `2025-07-22`
  - First observed version-tag baseline: `v2026.3.12`
  - Official docs confirmed: `2026-06-01`
  - First official sources:
    <https://github.com/NousResearch/hermes-agent>
    <https://hermes-agent.nousresearch.com/docs/>
- Checked through: `2026-06-08`
- Canonical source families:
  - Official docs root: <https://hermes-agent.nousresearch.com/docs/>
  - LLM-readable docs index:
    <https://hermes-agent.nousresearch.com/docs/llms.txt>
  - LLM-readable full docs:
    <https://hermes-agent.nousresearch.com/docs/llms-full.txt>
  - GitHub repository: <https://github.com/NousResearch/hermes-agent>
  - GitHub releases/tags:
    <https://github.com/NousResearch/hermes-agent/releases>
    <https://github.com/NousResearch/hermes-agent/tags>
  - README / install and update docs:
    <https://raw.githubusercontent.com/NousResearch/hermes-agent/main/README.md>
    <https://hermes-agent.nousresearch.com/docs/getting-started/updating>
  - Core feature docs:
    - Skills: <https://hermes-agent.nousresearch.com/docs/user-guide/features/skills>
    - Curator: <https://hermes-agent.nousresearch.com/docs/user-guide/features/curator>
    - Memory: <https://hermes-agent.nousresearch.com/docs/user-guide/features/memory>
    - Context files:
      <https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files>
    - Delegation:
      <https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation>
    - Hooks: <https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks>
    - MCP: <https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp>
  - Developer guide:
    - Architecture:
      <https://hermes-agent.nousresearch.com/docs/developer-guide/architecture>
    - Agent loop:
      <https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop>
    - Creating skills:
      <https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills>
  - Engineer / maintainer watchlist:
    - Nous Research Hermes maintainers
      identity_status: verified
      source_type: official_project_maintainer
      evidence_url: <https://github.com/NousResearch/hermes-agent>; <https://hermes-agent.nousresearch.com/docs/>
      trust_rule: official docs and repo releases can inform proposal-only local architecture comparisons; do not adopt Hermes runtime behavior, state trees, or auto-writing loops without explicit user approval
      notes: project-level maintainer identity is verified through official repository and docs, but individual social accounts still need separate verification.
- Current high-signal per-run source subset:
  - <https://hermes-agent.nousresearch.com/docs/llms.txt>
  - <https://hermes-agent.nousresearch.com/docs/user-guide/features/skills>
  - <https://hermes-agent.nousresearch.com/docs/user-guide/features/memory>
  - <https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files>
  - <https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation>
  - <https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks>
  - <https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp>
  - <https://github.com/NousResearch/hermes-agent/releases>
  - <https://github.com/NousResearch/hermes-agent/tags>

Recent checked entries:

| Date | Title | Source | Local relevance | Status |
|---|---|---|---|---|
| 2026-06-06 | Hermes Agent v0.16.0 / v2026.6.5 Surface Release | <https://github.com/NousResearch/hermes-agent/releases/tag/v2026.6.5>; <https://hermes-agent.nousresearch.com/docs/llms.txt> | Relevant as proposal-only comparison material for desktop surfaces, remote gateway auth, browser admin panels, MCP/credential management UI, trimmed default skill sets, trusted skill taps, fuzzy model pickers, and `/undo`. No local Codex runtime migration or auto-writing loop is justified without explicit approval. | checked |
| 2026-06-05 | Incremental check: no release/tag newer than `v2026.5.29.2` | <https://github.com/NousResearch/hermes-agent/releases>; <https://github.com/NousResearch/hermes-agent/tags> | Confirms no new release-level migration signal after the prior ledger boundary. No local Codex skill, registry, or safety-gate change. | checked |
| 2026-06-02 | Dashboard refresh-token sessions, Skills & Tools pane consolidation, and default streaming config discoverability | <https://github.com/NousResearch/hermes-agent/commit/c10ccaaf51a7146c7079e318cc20e4ab3f1a190d>; <https://github.com/NousResearch/hermes-agent/commit/a2b8e430e851bd7c77600fbafe3bc6cd5035e616>; <https://github.com/NousResearch/hermes-agent/commit/d78d77e46053e65cf8960760a1438a33553377ab> | Relevant as proposal-only comparison material for auth refresh flows, combined skills/tool management UI, and explicit streaming configuration. No local Codex skill, registry, or safety-gate write is justified by these commits alone. | checked |
| 2026-06-02 | Incremental check: no release/tag newer than `v2026.5.29.2` | <https://github.com/NousResearch/hermes-agent/releases>; <https://github.com/NousResearch/hermes-agent/tags> | Confirms no new release-level migration signal after the `2026-06-01` ledger boundary; only unreleased main-branch commits were considered as proposal-only signals. | checked |
| 2026-06-01 | Hermes Agent source group added to skill-sync ledger | <https://hermes-agent.nousresearch.com/docs/llms.txt> | Relevant to future comparisons around self-improving skills, persistent memory, context files, subagent delegation, hooks, MCP, checkpoints, and agent runtime safety. Keep as proposal-only; do not migrate Hermes runtime state or auto-writing behavior into Codex without explicit approval. | checked |
