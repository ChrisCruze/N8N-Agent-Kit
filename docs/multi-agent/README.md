# Multi-Agent Automation Patterns

This directory captures composable patterns for the four core agents described in the repository AGENTS.md. Each pattern lists:
- **Purpose**: Business outcome or user journey automated by the agent.
- **Workflow Building Blocks**: Required n8n nodes, triggers, and shared resources.
- **Observability Hooks**: Metrics, logging, and alerting expectations.

## Content Agent
- **Purpose**: Automate campaign content repurposing across blog, social, and knowledge-base channels.
- **Workflow Building Blocks**:
  - HTTP Request nodes for LLM endpoints.
  - AI Text Generation nodes for rewriting prompts.
  - Airtable or Notion nodes to store approved copy.
  - Git or CMS integrations for final publishing.
- **Observability Hooks**: capture latency per LLM call, success/failure of publishing, and approval timestamps.

## Email Agent
- **Purpose**: Govern transactional, lifecycle, and notification emails triggered via API or CRM webhooks.
- **Workflow Building Blocks**:
  - Webhook triggers guarded by signed secrets.
  - Email Send nodes (SMTP, Resend, SendGrid, etc.).
  - Feature flag checks stored in Redis or Airtable.
  - Shared "Message Templates" data resource defined in `examples/email-lifecycle.json`.
- **Observability Hooks**: send metrics to Prometheus via HTTP node, log bounce events into Airtable.

## Tasks Agent
- **Purpose**: Provide internal automations such as escalations, standup digests, or Jira synchronizations.
- **Workflow Building Blocks**:
  - Cron or Schedule trigger nodes.
  - Task management connectors (Linear, Jira, Asana).
  - Slack or Teams message nodes for human-in-the-loop confirmations.
  - Access to `scripts/validate_workflows.py` during CI to guard against malformed workflows.
- **Observability Hooks**: Slack logging channel, Run status posted to Notion/Confluence.

## Knowledge Agent
- **Purpose**: Synchronize structured knowledge (Airtable, Dropbox documents, Confluence) with AI-ready stores.
- **Workflow Building Blocks**:
  - Airtable list/create nodes.
  - Dropbox download/upload nodes.
  - Vector database integrations (Supabase, Pinecone) through HTTP or native nodes.
  - File preprocessing helpers from `examples/knowledge-sync.json`.
- **Observability Hooks**: dataset freshness metrics, doc count parity checks, and Slack alerts on checksum drift.
