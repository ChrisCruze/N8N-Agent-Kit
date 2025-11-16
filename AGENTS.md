# Repository Agent Guidelines

This repository encodes a production-ready n8n automation stack optimized for multi-agent orchestration. When contributing, follow the conventions below:

## Multi-Agent Patterns
- **Content Agent**: owns creative generation workflows (long-form, short-form, and asset repurposing). Workflows and docs for this agent live under `docs/multi-agent` and `examples/content-*`.
- **Email Agent**: maintains transactional and lifecycle messaging flows. Store artifacts under `examples/email-*` and document new playbooks in `docs/multi-agent`.
- **Tasks Agent**: coordinates internal automations such as ticket routing or standup reports. Use `examples/tasks-*` naming and keep supporting scripts in `scripts/`.
- **Knowledge Agent**: synchronizes knowledge bases (wikis, Airtable, etc.). Related workflows live in `examples/knowledge-*`.

## Coding & Documentation Rules
1. Prefer declarative JSON workflow templates and ensure they validate using `scripts/validate_workflows.py`.
2. Place automation tooling (CLI, deployment, validators) under `scripts/` or `tools/`.
3. Integrations must be documented inside `docs/integrations/` using clear checklists.
4. Reference this AGENTS file in new directories unless a more specific AGENTS.md overrides it.
