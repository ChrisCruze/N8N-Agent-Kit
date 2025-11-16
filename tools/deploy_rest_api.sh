#!/usr/bin/env bash
set -euo pipefail

COMPOSE_FILE="$(cd "$(dirname "$0")" && pwd)/api.docker-compose.yml"

usage() {
  cat <<USAGE
Deploy or teardown the n8n REST API stack.

Usage:
  $(basename "$0") up   # start the stack
  $(basename "$0") down # stop and remove containers

Environment overrides:
  N8N_BASIC_AUTH_USER, N8N_BASIC_AUTH_PASSWORD, WEBHOOK_URL, GENERIC_TIMEZONE
USAGE
}

if [[ $# -ne 1 ]]; then
  usage
  exit 1
fi

action="$1"

if [[ "$action" != "up" && "$action" != "down" ]]; then
  usage
  exit 1
fi

docker compose -f "$COMPOSE_FILE" "$action" -d

echo "Stack '$action' command executed using $COMPOSE_FILE"
