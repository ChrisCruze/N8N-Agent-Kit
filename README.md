# N8N-Agent-Kit

Production-ready n8n automation toolkit for orchestrating LLM-driven agents, REST API workflows, and integrations.

## Repository Map
- `AGENTS.md` – governance for Content, Email, Tasks, and Knowledge agents.
- `docs/multi-agent/` – patterns, observability hooks, and shared conventions.
- `docs/integrations/` – Airtable and Dropbox playbooks for onboarding credentials.
- `examples/` – validated JSON workflow templates for each agent.
- `schema/` – JSON Schema definitions for template validation.
- `scripts/` – automation helpers (validation, CI hooks, etc.).
- `tools/` – deployment tooling for REST API hosting and gateways.

## Workflow Validation
Use the validation script before committing or deploying workflows.

```bash
python scripts/validate_workflows.py            # validate all templates
python scripts/validate_workflows.py "content-*" # validate subset
```

The script enforces the schema in `schema/workflow.schema.json` and fails fast on missing required fields.

## REST API Deployment
Deploy a hardened n8n REST stack plus an OpenAPI-compatible proxy using Docker Compose.

```bash
cd tools
./deploy_rest_api.sh up
# ... deploys n8n on :5678 and proxy on :8080
./deploy_rest_api.sh down
```

Override defaults with environment variables (e.g., `N8N_BASIC_AUTH_USER`, `WEBHOOK_URL`).

## Integrations
Follow the integration guides in `docs/integrations/` for Airtable and Dropbox to keep Knowledge and Tasks agents synchronized with external systems. Each guide lists prerequisites, configuration steps, and maintenance tips.
