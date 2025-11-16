# Dropbox Integration Guide

Dropbox powers the Knowledge agent's document synchronization workflows.

## Prerequisites
- Dropbox Business account with app folder access.
- Generated short-lived OAuth token (PKCE) or long-lived refresh token.
- Folder taxonomy mirroring `/{team}/KnowledgeBase/{topic}`.

## Setup Steps
1. **Create Dropbox app**:
   - Visit the Dropbox App Console and provision a Scoped Access app with `files.content.read`, `files.content.write`, and `files.metadata.read` scopes.
   - Enable the refresh token feature if using long-lived automations.
2. **Store credentials in n8n**:
   - Add a Dropbox credential named `dropbox-knowledge-sync`.
   - Paste the app key/secret and refresh token, or configure OAuth 2.0 callback to your n8n instance.
3. **Map workflow parameters**:
   - Update the `Source Folder` field in `examples/knowledge-sync.json` to point to your root folder.
   - Configure the `Dropbox - Upload Processed Asset` node to write into `/KnowledgeBase/Processed`.
4. **Checksum enforcement**:
   - Use the Function node `Compute Dropbox Checksum` from the template to hash file contents before uploading.
   - Store the checksum in Airtable or a dedicated SQLite DB for drift detection.
5. **Monitoring**:
   - Add the `Dropbox - Activity Log` node output to an n8n error workflow to capture throttling events.
   - Send alert notifications via Slack when the Dropbox API returns HTTP 429.

## Maintenance
- Review app permissions quarterly.
- Rotate refresh tokens every 6 months.
- Archive obsolete folders to cold storage to keep sync loops fast.
