# Skill Sync Platform Update Ledger

Public canonical ledger for incremental OpenAI, Anthropic/Claude, Hermes
Agent, and Superpowers platform update checks.

Last run: `2026-06-25T20:40+08:00`
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
- Checked through: `2026-06-25`
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
  - <https://developers.openai.com/codex/changelog>
  - <https://developers.openai.com/codex/config-reference>
  - <https://developers.openai.com/apps-sdk/changelog>

Recent checked entries:

| Date | Title | Source | Local relevance | Status |
|---|---|---|---|---|
| 2026-06-24 | OpenAI API changelog: Safety Usage Dashboard and `chat-latest` snapshot update | <https://developers.openai.com/api/docs/changelog> | Relevant to future safety-monitoring and model-routing guidance. Keep as proposal-only evidence; no local Codex skill, registry, MCP, or permission architecture mutation without a specific user request. | checked |
| 2026-06-22 | Codex changelog after Jun 11: Record & Replay, thread handoff, SSH connection deep links, Browser Use routing, workspace file/path UX, MCP approval choices, and subagent progress visibility | <https://developers.openai.com/codex/changelog> | Relevant to future skill-capture, handoff, SSH diagnostics, browser reliability, local path prompting, approval-state UX, and subagent observability proposals. Do not change local skill packages or runtime policy automatically. | checked |
| 2026-06-20 | Incremental check through Jun 20: no newer OpenAI API changelog entry after Jun 9; Codex changelog has post-Jun 11 app and CLI updates | <https://developers.openai.com/api/docs/changelog>; <https://developers.openai.com/codex/changelog> | The API changelog still showed Jun 9 Responses web-search image results as the newest June 2026 API entry. Codex app/CLI updates on Jun 15 and Jun 18 are relevant as proposal-only evidence for local app/CLI behavior, plugin MCP exposure, remote executor paths, hook trust handling, terminal backgrounding, and skill/marketplace routing. No immediate local skill registry, lifecycle, MCP, or permission mutation is authorized by this scan alone. | checked |
| 2026-06-18 | Codex app 26.616 and Codex CLI 0.141.0: Record & Replay, host handoff, encrypted remote relay channels, plugin MCP exposure, request-input auto-resolution, hook and plugin routing fixes | <https://developers.openai.com/codex/changelog> | Relevant as proposal-only context for future skill recording/replay, local/remote handoff policy, plugin MCP capability routing, request_user_input auto-resolution expectations, and hook trust diagnostics. Existing local hard gates remain unchanged without explicit follow-up approval. | checked |
| 2026-06-15 | Codex Mobile and CLI updates: MCP approval scope choices, LaTeX rendering, subagent status fixes, `/usage`, goal attachment preservation, session deletion, Claude import, unified mentions, Bedrock auth, encrypted MCP OAuth credentials, SQLite recovery, and MCP reliability fixes | <https://developers.openai.com/codex/changelog> | Relevant as proposal-only context for mobile review behavior, MCP approval-scope language, goal artifact preservation, credential storage, SQLite/state recovery, and cross-tool migration expectations. No local architecture write without a targeted user request. | checked |
| 2026-06-12 | Apps SDK changelog: app permission controls in ChatGPT | <https://developers.openai.com/apps-sdk/changelog> | Relevant to future connector/app permission-policy comparisons. Proposal-only; no local app, MCP, or approval-rule mutation without explicit approval. | checked |
| 2026-06-10 | Codex changelog: performance improvements, Computer Use startup readiness, appshot error reporting, and UI fixes | <https://developers.openai.com/codex/changelog> | Relevant as proposal-only evidence for local diagnostics and visual/browser reliability expectations. No immediate skill registry mutation needed; keep this as context for agent-doctor and browser/appshot troubleshooting checks. | checked |
| 2026-06-11 | Incremental check: no OpenAI architecture update after Jun 9 | <https://developers.openai.com/api/docs/changelog> | OpenAI API changelog was reachable. The latest listed item remained the Jun 9 Responses web-search image-result update; no new post-`2026-06-09` local Codex skill, registry, MCP, permission, or safety-gate architecture change was found. | checked |
| 2026-06-09 | Incremental check: no new OpenAI architecture update after Jun 8 | <https://developers.openai.com/api/docs/changelog>; <https://developers.openai.com/codex/subagents> | Changelog and Codex subagent docs were reachable. No new post-`2026-06-08` local Codex skill, registry, MCP, permission, or safety-gate architecture change was found. | checked |
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
- Checked through: `2026-06-25`
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
  - <https://code.claude.com/docs/en/changelog>
  - <https://code.claude.com/docs/en/whats-new/>
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
| 2026-06-24 | Claude Code 2.1.191: `/rewind`, persistent permission approvals, sandbox network permission memory, MCP retry reliability, and managed-settings refresh fixes | <https://code.claude.com/docs/en/changelog> | Relevant comparison material for local permission-prompt fatigue, resumable conversations, MCP transient-error handling, and stale managed-config diagnostics. Proposal-only; no Codex config, skill, or permission-rule mutation. | checked |
| 2026-06-23 | Claude Code 2.1.187/2.1.186: sandbox credential blocking, org model restrictions, CLI MCP login/logout, subagent depth fixes, and skill frontmatter tolerance | <https://code.claude.com/docs/en/changelog> | Relevant comparison material for secret isolation, model allowlist policy, headless MCP auth, nested-agent safety, and skill metadata resilience. Proposal-only; no direct local registry or skill-package write. | checked |
| 2026-06-20 | Incremental check through Jun 20: Claude Code changelog reachable through 2.1.183; What's New root still provides weekly digest context | <https://code.claude.com/docs/en/changelog>; <https://code.claude.com/docs/en/whats-new/> | Relevant as proposal-only comparison material for local subagent depth/observability, permission modes, fallback-model design, safe-mode troubleshooting, and version-normalization hygiene. No Codex skill registry, lifecycle, or permission write is authorized by this scan alone. | checked |
| 2026-06-08..12 | Claude Code Week 24 digest: `/cd`, nested subagents, `--safe-mode`, and fallback model configuration | <https://code.claude.com/docs/en/whats-new/> | Relevant as comparison material for local directory-switching semantics, delegated-agent depth limits, troubleshooting profiles, and fallback-model policy. Existing local subagent and approval boundaries remain adequate; no immediate local architecture mutation needed. | checked |
| 2026-06-12 | Claude Code Week 24 and 2.1.174-2.1.175: `/cd`, nested subagents, safe mode, fallback models, and managed available-model enforcement | <https://code.claude.com/docs/en/whats-new/>; <https://code.claude.com/docs/en/changelog> | Relevant to future working-directory handoff, subagent-depth policy, troubleshooting boot modes, fallback-model routing, and managed model allowlists. Proposal-only unless the user asks for a local policy update. | checked |
| 2026-06-09 | New in Claude Managed Agents: scheduled agents and environment variable vaults | <https://claude.com/blog> | Relevant as proposal-only comparison material for future automation governance, scheduled agent review, secret handling, and agent-doctor monitoring. Do not create or migrate local automations without explicit user approval and local safety review. | checked |
| 2026-06-11 | Claude Code 2.1.173: Fable 5 1M suffix normalization and Windows sandbox warning fix | <https://code.claude.com/docs/en/changelog> | Relevant only as comparison material for model-name normalization and startup warning hygiene. No local Codex skill, registry, or robot-workflow mutation needed. | checked |
| 2026-06-10 | Claude Code 2.1.172: nested subagents, model/permission fixes, and subagent observability fixes | <https://code.claude.com/docs/en/changelog> | Relevant as proposal-only comparison material for delegated-agent depth limits, subagent status visibility, model allowlists, permission-rule precision, and memory lookup in remote sessions. Existing local `subagent-goal` authority boundaries remain adequate; no immediate local architecture write required. | checked |
| 2026-06-09 | Incremental check: no new Anthropic/Claude architecture update after Jun 8 | <https://www.anthropic.com/news>; <https://github.com/karpathy> | Anthropic Newsroom and Karpathy GitHub were reachable. No new post-`2026-06-08` local skill, subagent, MCP, memory, permission, or workflow architecture change was found. | checked |
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
- Checked through: `2026-06-25`
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
| 2026-06-25 | Incremental check: no Hermes release newer than v2026.6.19 found | <https://github.com/NousResearch/hermes-agent/releases>; <https://hermes-agent.nousresearch.com/docs/llms.txt> | Confirms the Jun 19 Reach Release is the latest release-level signal observed in this pass. Continue treating Hermes runtime features as proposal-only comparison material. | checked |
| 2026-06-19 | Hermes Agent v0.17.0 / v2026.6.19 Reach Release | <https://github.com/NousResearch/hermes-agent/releases/tag/v2026.6.19>; <https://github.com/NousResearch/hermes-agent/tags> | Relevant as proposal-only comparison material for iMessage/WhatsApp/Telegram reach, async subagents, image editing, dashboard profile builders, memory tool upgrades, and curator cost optimization. Do not adopt Hermes runtime behavior, state trees, messaging gateways, or auto-writing loops into local Codex without explicit user approval and local safety review. | checked |
| 2026-06-16 | Hermes backup tags include OpenTUI parser cache and remote grammar fetch refactors | <https://github.com/NousResearch/hermes-agent/tags> | Relevant only as low-confidence implementation context for UI parser cache and graceful fallback patterns. Because these are backup/pre-release tags rather than the main release line, keep as discovery-only and do not use them to justify local architecture mutation. | checked |
| 2026-06-11 | Incremental check: no Hermes release newer than v2026.6.5 found | <https://github.com/NousResearch/hermes-agent/releases>; <https://hermes-agent.nousresearch.com/docs/> | Confirms no new release-level local architecture signal beyond the already recorded Surface Release. Continue treating Hermes features as proposal-only comparison material. | checked |
| 2026-06-09 | Incremental check: no Hermes release update after Jun 8 | <https://github.com/NousResearch/hermes-agent/releases> | GitHub releases page was reachable. No new post-`2026-06-08` Hermes release-level signal requiring local Codex skill, registry, memory, or automation changes was found. | checked |
| 2026-06-06 | Hermes Agent v0.16.0 / v2026.6.5 Surface Release | <https://github.com/NousResearch/hermes-agent/releases/tag/v2026.6.5>; <https://hermes-agent.nousresearch.com/docs/llms.txt> | Relevant as proposal-only comparison material for desktop surfaces, remote gateway auth, browser admin panels, MCP/credential management UI, trimmed default skill sets, trusted skill taps, fuzzy model pickers, and `/undo`. No local Codex runtime migration or auto-writing loop is justified without explicit approval. | checked |
| 2026-06-05 | Incremental check: no release/tag newer than `v2026.5.29.2` | <https://github.com/NousResearch/hermes-agent/releases>; <https://github.com/NousResearch/hermes-agent/tags> | Confirms no new release-level migration signal after the prior ledger boundary. No local Codex skill, registry, or safety-gate change. | checked |
| 2026-06-02 | Dashboard refresh-token sessions, Skills & Tools pane consolidation, and default streaming config discoverability | <https://github.com/NousResearch/hermes-agent/commit/c10ccaaf51a7146c7079e318cc20e4ab3f1a190d>; <https://github.com/NousResearch/hermes-agent/commit/a2b8e430e851bd7c77600fbafe3bc6cd5035e616>; <https://github.com/NousResearch/hermes-agent/commit/d78d77e46053e65cf8960760a1438a33553377ab> | Relevant as proposal-only comparison material for auth refresh flows, combined skills/tool management UI, and explicit streaming configuration. No local Codex skill, registry, or safety-gate write is justified by these commits alone. | checked |
| 2026-06-02 | Incremental check: no release/tag newer than `v2026.5.29.2` | <https://github.com/NousResearch/hermes-agent/releases>; <https://github.com/NousResearch/hermes-agent/tags> | Confirms no new release-level migration signal after the `2026-06-01` ledger boundary; only unreleased main-branch commits were considered as proposal-only signals. | checked |
| 2026-06-01 | Hermes Agent source group added to skill-sync ledger | <https://hermes-agent.nousresearch.com/docs/llms.txt> | Relevant to future comparisons around self-improving skills, persistent memory, context files, subagent delegation, hooks, MCP, checkpoints, and agent runtime safety. Keep as proposal-only; do not migrate Hermes runtime state or auto-writing behavior into Codex without explicit approval. | checked |

### superpowers

- Coverage baseline:
  - Public GitHub repository observed: `2026-06-22`
  - First official source:
    <https://github.com/obra/Superpowers>
- Checked through: `2026-06-22`
- Canonical source families:
  - GitHub repository: <https://github.com/obra/Superpowers>
  - README / install docs:
    <https://github.com/obra/Superpowers#readme>
  - Raw README:
    <https://raw.githubusercontent.com/obra/Superpowers/main/README.md>
  - Release notes:
    <https://github.com/obra/Superpowers/blob/main/RELEASE-NOTES.md>
  - GitHub releases/tags:
    <https://github.com/obra/Superpowers/releases>
    <https://github.com/obra/Superpowers/tags>
  - Skills directory:
    <https://github.com/obra/Superpowers/tree/main/skills>
  - Codex plugin metadata:
    <https://github.com/obra/Superpowers>
  - Claude plugin metadata:
    <https://github.com/obra/Superpowers/tree/main/.claude-plugin>
  - Engineer / maintainer watchlist:
    - obra / Superpowers maintainers
      identity_status: verified
      source_type: official_project_maintainer
      evidence_url: <https://github.com/obra/Superpowers>
      trust_rule: official repo, release notes, plugin metadata, and skills directory can inform proposal-only comparisons for agent skills, workflow methodology, TDD gates, and plugin packaging; do not import Superpowers methodology, hooks, or skill behavior into local Codex without explicit user approval and local validation
      notes: project-level maintainer identity is verified through the public GitHub repository; individual social or third-party commentary still needs separate verification.
- Current high-signal per-run source subset:
  - <https://github.com/obra/Superpowers>
  - <https://raw.githubusercontent.com/obra/Superpowers/main/README.md>
  - <https://github.com/obra/Superpowers/blob/main/RELEASE-NOTES.md>
  - <https://github.com/obra/Superpowers/tree/main/skills>
  - <https://github.com/obra/Superpowers>
  - <https://github.com/obra/Superpowers/releases>
  - <https://github.com/obra/Superpowers/tags>

Recent checked entries:

| Date | Title | Source | Local relevance | Status |
|---|---|---|---|---|
| 2026-06-22 | Superpowers source group added to skill-sync ledger | <https://github.com/obra/Superpowers> | Relevant as proposal-only comparison material for agentic skills methodology, multi-harness plugin packaging, subagent-driven development, TDD workflow gates, and Codex/Claude/Cursor/Gemini skill portability. Do not import Superpowers methodology, hooks, or skill behavior into local Codex without explicit approval and local validation. | checked |

### robotics-ecosystem

- Coverage baseline:
  - Optional source registry added on `2026-06-22` for broad robotics stacks,
    simulator projects, ROS/MoveIt foundations, robot-learning frameworks, and
    planning/dynamics libraries.
  - Registry purpose: reusable source coverage for future robotics work; this
    is not a new active skill and does not authorize local architecture writes.
- Checked through: `2026-06-22`
- Registry entries:
  - id: universal-robots
    category: manipulator-control-stack
    official_docs:
      - <https://www.universal-robots.com/developer/communication-protocol/ros-and-ros2-driver/>
    official_github:
      - <https://github.com/UniversalRobots>
    community_repos: []
    maturity: mature-official
    trust_rule: use UR official docs and the UniversalRobots GitHub org as official sources; treat third-party UR forks and wrappers as community evidence only
    checked_through: 2026-06-22
    notes: official ROS/ROS2 driver and UR client library coverage.
  - id: franka
    category: manipulator-control-stack
    official_docs:
      - <https://frankarobotics.github.io/docs/>
    official_github:
      - <https://github.com/frankarobotics>
    community_repos: []
    maturity: mature-official
    trust_rule: use Franka FCI/libfranka/ROS2 docs and frankarobotics GitHub as official; verify robot-mode, safety, and torque-control claims against hardware docs before operational guidance
    checked_through: 2026-06-22
    notes: covers FCI, libfranka, and Franka ROS/ROS2 sources.
  - id: kinova-kortex
    category: manipulator-control-stack
    official_docs:
      - <https://github.com/Kinovarobotics/ros2_kortex#readme>
    official_github:
      - <https://github.com/Kinovarobotics/ros2_kortex>
    community_repos: []
    maturity: official-ros2-driver
    trust_rule: treat Kinovarobotics GitHub repositories as official Kinova Kortex ROS2 sources; verify firmware/API compatibility before local robot instructions
    checked_through: 2026-06-22
    notes: Gen3/Kortex ROS2 entry point.
  - id: kuka-lbr-iiwa
    category: manipulator-control-stack
    official_docs:
      - <https://my.kuka.com/s/product/kuka-sunrisefri-25/01t1i000000tTEpAAM?language=en_US>
    official_github: []
    community_repos:
      - <https://github.com/lbr-stack/lbr_fri_ros2_stack>
    maturity: official-fri-community-ros2
    trust_rule: KUKA Sunrise.FRI is the official source; lbr-stack and other iiwa ROS/ROS2 integrations must remain community_repos and must not be labeled official
    checked_through: 2026-06-22
    notes: official FRI availability plus community ROS2 integration; KUKA official GitHub driver source not recorded.
  - id: ufactory-xarm
    category: manipulator-control-stack
    official_docs:
      - <https://github.com/xArm-Developer/xarm_ros2#readme>
    official_github:
      - <https://github.com/xArm-Developer/xarm_ros2>
    community_repos: []
    maturity: official-ros2-driver
    trust_rule: treat xArm-Developer GitHub as UFactory official source; verify hardware generation, firmware, and ROS distro support before operational guidance
    checked_through: 2026-06-22
    notes: xArm ROS2 developer package source.
  - id: agilex-piper
    category: manipulator-control-stack
    official_docs:
      - <https://github.com/agilexrobotics/piper_sdk#readme>
      - <https://github.com/agilexrobotics/piper_ros#readme>
    official_github:
      - <https://github.com/agilexrobotics/piper_sdk>
      - <https://github.com/agilexrobotics/piper_ros>
    community_repos: []
    maturity: emerging-official
    trust_rule: AgileX SDK/ROS repos are usable official sources, but SDK, ROS, and LeRobot pipelines require local validation before operational claims
    checked_through: 2026-06-22
    notes: PiPER source coverage is available but newer than the mature industrial-arm stacks.
  - id: trossen-interbotix
    category: manipulator-control-stack
    official_docs:
      - <https://docs.trossenrobotics.com/interbotix_xsarms_docs/>
    official_github:
      - <https://github.com/Interbotix>
    community_repos: []
    maturity: mature-official
    trust_rule: use Trossen docs and Interbotix GitHub as official for X-Series/ViperX/ALOHA-related sources; verify product line because Trossen AI Arms and X-Series docs differ
    checked_through: 2026-06-22
    notes: covers Interbotix X-Series arms and related ROS/ROS2 packages.
  - id: mujoco
    category: simulator
    official_docs:
      - <https://mujoco.readthedocs.io/en/stable/>
    official_github:
      - <https://github.com/google-deepmind/mujoco>
    community_repos: []
    maturity: mature-official
    trust_rule: use MuJoCo docs and google-deepmind/mujoco as official; distinguish MuJoCo/MJX behavior by version before simulator claims
    checked_through: 2026-06-22
    notes: core physics simulator and MJX-adjacent source.
  - id: gazebo
    category: simulator
    official_docs:
      - <https://gazebosim.org/libs/sim/>
    official_github:
      - <https://github.com/gazebosim/gz-sim>
    community_repos: []
    maturity: mature-official
    trust_rule: use Gazebo docs and gazebosim GitHub as official; distinguish modern Gazebo from Gazebo classic in guidance
    checked_through: 2026-06-22
    notes: modern Gazebo simulation stack.
  - id: isaac-sim
    category: simulator
    official_docs:
      - <https://docs.isaacsim.omniverse.nvidia.com/latest/index.html>
    official_github:
      - <https://github.com/isaac-sim/IsaacSim>
    community_repos: []
    maturity: official-open-source-with-licensing-caveats
    trust_rule: use NVIDIA Isaac Sim docs and isaac-sim GitHub as official, while preserving licensing, binary dependency, and contribution caveats
    checked_through: 2026-06-22
    notes: GitHub visibility does not remove Isaac Sim license and NVIDIA Omniverse dependency constraints.
  - id: isaac-lab
    category: robot-learning-framework
    official_docs:
      - <https://github.com/isaac-sim/IsaacLab#readme>
    official_github:
      - <https://github.com/isaac-sim/IsaacLab>
    community_repos: []
    maturity: mature-official
    trust_rule: use Isaac Lab docs and isaac-sim/IsaacLab as official; verify Isaac Sim version compatibility before reproducing training examples
    checked_through: 2026-06-22
    notes: robot-learning framework built on Isaac Sim.
  - id: newton
    category: simulator
    official_docs:
      - <https://newton-physics.github.io/newton/stable/>
    official_github:
      - <https://github.com/newton-physics/newton>
    community_repos: []
    maturity: emerging-official
    trust_rule: use Newton docs and newton-physics GitHub as official, but treat adoption guidance as emerging until local examples and release maturity are validated
    checked_through: 2026-06-22
    notes: GPU-accelerated physics engine source coverage.
  - id: ros2
    category: core-robotics-stack
    official_docs:
      - <https://docs.ros.org/en/rolling/>
    official_github:
      - <https://github.com/ros2/ros2>
    community_repos: []
    maturity: mature-official
    trust_rule: use docs.ros.org and ros2 GitHub as official; verify ROS distro, REP, and package-release status before instructions
    checked_through: 2026-06-22
    notes: docs.ros.org may block automated readers, but remains the official docs source.
  - id: moveit2
    category: core-robotics-stack
    official_docs:
      - <https://moveit.ai/>
    official_github:
      - <https://github.com/moveit/moveit2>
    community_repos: []
    maturity: mature-official
    trust_rule: use MoveIt docs and moveit/moveit2 as official; verify ROS distro and planning plugin versions before implementation claims
    checked_through: 2026-06-22
    notes: MoveIt 2 motion planning and manipulation stack.
  - id: drake
    category: dynamics-planning-foundation
    official_docs:
      - <https://drake.mit.edu/>
    official_github:
      - <https://github.com/RobotLocomotion/drake>
    community_repos: []
    maturity: mature-official
    trust_rule: use Drake docs and RobotLocomotion/drake as official; verify bindings, solver availability, and ROS2 support status by version
    checked_through: 2026-06-22
    notes: model-based design, dynamics, planning, and control toolbox.
  - id: pinocchio
    category: dynamics-planning-foundation
    official_docs:
      - <https://stack-of-tasks.github.io/pinocchio/>
    official_github:
      - <https://github.com/stack-of-tasks/pinocchio>
    community_repos: []
    maturity: mature-official
    trust_rule: use Stack-of-Tasks Pinocchio docs and GitHub as official; verify major-version API before dynamics code guidance
    checked_through: 2026-06-22
    notes: rigid-body dynamics algorithms and analytical derivatives.
  - id: ruckig
    category: dynamics-planning-foundation
    official_docs:
      - <https://docs.ruckig.com/>
    official_github:
      - <https://github.com/pantor/ruckig>
    community_repos: []
    maturity: mature-official
    trust_rule: use Ruckig docs and pantor/ruckig as official; verify community/pro feature boundaries before deployment recommendations
    checked_through: 2026-06-22
    notes: jerk-limited online trajectory generation.
  - id: ompl
    category: dynamics-planning-foundation
    official_docs:
      - <https://ompl.kavrakilab.org/>
    official_github:
      - <https://github.com/ompl/ompl>
    community_repos: []
    maturity: mature-official
    trust_rule: use OMPL docs and ompl/ompl as official; distinguish OMPL planner library behavior from MoveIt integration behavior
    checked_through: 2026-06-22
    notes: Open Motion Planning Library source coverage.
  - id: lerobot
    category: robot-learning-framework
    official_docs:
      - <https://huggingface.co/docs/lerobot/index>
    official_github:
      - <https://github.com/huggingface/lerobot>
    community_repos: []
    maturity: mature-official
    trust_rule: use Hugging Face LeRobot docs and huggingface/lerobot as official; verify hardware adapters, dataset format, and policy version before physical-robot guidance
    checked_through: 2026-06-22
    notes: real-world robotics learning framework and dataset/tooling source.
  - id: maniskill
    category: robot-learning-framework
    official_docs:
      - <https://maniskill.readthedocs.io/en/latest/>
    official_github:
      - <https://github.com/mani-skill/ManiSkill>
    community_repos: []
    maturity: mature-official
    trust_rule: use ManiSkill docs and mani-skill GitHub as official; verify SAPIEN/GPU backend compatibility before benchmark or environment claims
    checked_through: 2026-06-22
    notes: manipulation benchmark and simulator framework.
  - id: robosuite
    category: robot-learning-framework
    official_docs:
      - <https://robosuite.ai/docs/overview.html>
    official_github:
      - <https://github.com/ARISE-Initiative/robosuite>
    community_repos: []
    maturity: mature-official
    trust_rule: use robosuite docs and ARISE-Initiative/robosuite as official; verify MuJoCo version and controller support before implementation claims
    checked_through: 2026-06-22
    notes: MuJoCo-based robot-learning simulation framework.
  - id: sapien-genesis
    category: simulator
    official_docs:
      - <https://sapien.ucsd.edu/docs/latest/>
      - <https://genesis-world.readthedocs.io/en/latest/>
    official_github:
      - <https://github.com/haosulab/SAPIEN>
      - <https://github.com/Genesis-Embodied-AI/genesis-world>
    community_repos: []
    maturity: official-mixed-maturity
    trust_rule: use SAPIEN and Genesis official docs/GitHub sources separately; do not merge API, physics, or rendering claims across them without version-specific verification
    checked_through: 2026-06-22
    notes: grouped first-pass registry entry because ManiSkill depends on SAPIEN while Genesis is a related emerging simulation platform.
- Current high-signal per-run source subset:
  - <https://www.universal-robots.com/developer/communication-protocol/ros-and-ros2-driver/>
  - <https://frankarobotics.github.io/docs/>
  - <https://github.com/Kinovarobotics/ros2_kortex>
  - <https://github.com/lbr-stack/lbr_fri_ros2_stack>
  - <https://github.com/agilexrobotics/piper_sdk>
  - <https://github.com/isaac-sim/IsaacSim>
  - <https://github.com/isaac-sim/IsaacLab>
  - <https://newton-physics.github.io/newton/stable/>
  - <https://github.com/huggingface/lerobot>

Recent checked entries:

| Date | Title | Source | Local relevance | Status |
|---|---|---|---|---|
| 2026-06-22 | Robotics ecosystem source registry added | <https://www.universal-robots.com/developer/communication-protocol/ros-and-ros2-driver/>; <https://github.com/UniversalRobots>; <https://frankarobotics.github.io/docs/>; <https://github.com/frankarobotics>; <https://github.com/Kinovarobotics/ros2_kortex>; <https://github.com/xArm-Developer/xarm_ros2>; <https://github.com/agilexrobotics/piper_sdk>; <https://github.com/agilexrobotics/piper_ros>; <https://docs.trossenrobotics.com/interbotix_xsarms_docs/>; <https://github.com/Interbotix>; <https://my.kuka.com/s/product/kuka-sunrisefri-25/01t1i000000tTEpAAM?language=en_US>; <https://github.com/lbr-stack/lbr_fri_ros2_stack>; <https://mujoco.readthedocs.io/en/stable/>; <https://github.com/google-deepmind/mujoco>; <https://gazebosim.org/libs/sim/>; <https://github.com/gazebosim/gz-sim>; <https://github.com/isaac-sim/IsaacSim>; <https://github.com/isaac-sim/IsaacLab>; <https://newton-physics.github.io/newton/stable/>; <https://github.com/newton-physics/newton>; <https://docs.ros.org/en/rolling/>; <https://github.com/ros2/ros2>; <https://moveit.ai/>; <https://github.com/moveit/moveit2>; <https://drake.mit.edu/>; <https://github.com/RobotLocomotion/drake>; <https://stack-of-tasks.github.io/pinocchio/>; <https://github.com/stack-of-tasks/pinocchio>; <https://docs.ruckig.com/>; <https://github.com/pantor/ruckig>; <https://ompl.kavrakilab.org/>; <https://github.com/ompl/ompl>; <https://huggingface.co/docs/lerobot/index>; <https://github.com/huggingface/lerobot>; <https://maniskill.readthedocs.io/en/latest/>; <https://github.com/mani-skill/ManiSkill>; <https://robosuite.ai/docs/overview.html>; <https://github.com/ARISE-Initiative/robosuite>; <https://sapien.ucsd.edu/docs/latest/>; <https://github.com/haosulab/SAPIEN>; <https://genesis-world.readthedocs.io/en/latest/>; <https://github.com/Genesis-Embodied-AI/genesis-world> | Adds source coverage for future robotics work without creating a new active skill. Official GitHub fields are restricted to vendor/project organizations; KUKA LBR community ROS2 support is recorded only under community_repos; Isaac Sim caveats and PiPER validation requirements are preserved. | checked |
