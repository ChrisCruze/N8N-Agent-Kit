# Airtable Integration Guide

Use this checklist to connect Airtable bases to the Knowledge and Tasks agents.

## Prerequisites
- Airtable account with a base for automations.
- Personal access token (PAT) with `data.records:read` and `data.records:write` scopes.
- Table schema with `Status`, `Owner`, and `SourceWorkflow` fields.

## Setup Steps
1. **Store credentials**: In n8n, create a new Airtable credential using the PAT. Name it `airtable-agentkit` to align with the workflow templates.
2. **Configure base metadata**:
   - Capture the Base ID from the Airtable URL.
   - Record table IDs and view IDs for each automation pipeline.
3. **Map fields in workflows**:
   - Update `examples/content-repurpose.json` nodes `Airtable - Upsert Approved Copy` and `examples/knowledge-sync.json` nodes `Airtable - Dataset Index` with your Base ID.
   - For Tasks agent flows, map `Status` to `In Progress/Done` options expected by internal SLAs.
4. **Enable rate limiting**:
   - Set `Max concurrent` in relevant HTTP Request nodes to `2`.
   - Add a Wait node (e.g., 250 ms) in loops that create or update multiple records.
5. **Testing**:
   - Use the `scripts/validate_workflows.py` script before deploying to ensure schema parity.
   - Trigger the workflow in n8n test mode and verify new rows appear with the expected `SourceWorkflow` label.

## Maintenance
- Rotate the PAT every 90 days and update it in n8n credentials.
- Monitor Airtable API usage dashboards for spikes.
- Keep a shared "Field Catalog" document within Knowledge agent documentation.
