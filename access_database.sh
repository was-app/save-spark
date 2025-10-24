#!/usr/bin/env bash
# db-access.sh — connect to Postgres running in your docker-compose (with sudo)
# Usage:
#   ./db-access.sh            → open interactive psql shell
#   ./db-access.sh --shell    → open bash shell in db container
#   ./db-access.sh -- -c "SELECT now();" → run SQL command directly

set -euo pipefail

DB_USER="izzy"
DB_NAME="postgres"

# Load .env if present (to read DATABASE_USERNAME / DATABASE_NAME)
if [[ -f .env ]]; then
  while IFS='=' read -r key val; do
    key="$(echo "$key" | tr -d '[:space:]')"
    [[ -z "$key" || "$key" == \#* ]] && continue
    case "$key" in
      DATABASE_USERNAME|POSTGRES_USER|DB_USER) DB_USER="${val//\"/}" ;;
      DATABASE_NAME|POSTGRES_DB|DB_NAME)       DB_NAME="${val//\"/}" ;;
    esac
  done < <(grep -E '^[A-Za-z0-9_]+=.*' .env || true)
fi

# Parse args
MODE="psql"
if [[ "${1:-}" == "--shell" ]]; then
  MODE="shell"
  shift
elif [[ "${1:-}" == "--" ]]; then
  shift
fi

PSQL_ARGS=("$@")

# Choose docker-compose flavor
if command -v docker-compose >/dev/null 2>&1; then
  COMPOSE_CMD="sudo docker-compose"
elif docker compose version >/dev/null 2>&1; then
  COMPOSE_CMD="sudo docker compose"
else
  echo "❌ docker-compose not found" >&2
  exit 1
fi

# Verify service 'db' exists (optional)
if ! grep -qE '^[[:space:]]*db:' docker-compose.yml 2>/dev/null; then
  echo "⚠️  Warning: no 'db' service found in docker-compose.yml" >&2
fi

if [[ "$MODE" == "shell" ]]; then
  # open interactive bash in container
  if [[ -t 0 && -t 1 ]]; then
    $COMPOSE_CMD exec db bash
  else
    $COMPOSE_CMD exec -T db bash
  fi
else
  # run psql inside container
  if [[ ${#PSQL_ARGS[@]} -eq 0 ]]; then
    if [[ -t 0 && -t 1 ]]; then
      $COMPOSE_CMD exec db psql -U "$DB_USER" -d "$DB_NAME"
    else
      $COMPOSE_CMD exec -T db psql -U "$DB_USER" -d "$DB_NAME"
    fi
  else
    $COMPOSE_CMD exec -T db psql -U "$DB_USER" -d "$DB_NAME" "${PSQL_ARGS[@]}"
  fi
fi
