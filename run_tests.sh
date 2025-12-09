#!/usr/bin/env bash
# Simple helper to activate the venv and run the test suite

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_ACTIVATE="$ROOT_DIR/venv/bin/activate"

if [[ ! -f "$VENV_ACTIVATE" ]]; then
  echo "Virtual environment not found at $VENV_ACTIVATE" >&2
  exit 1
fi

# Activate the project virtual environment
source "$VENV_ACTIVATE"

# Run the tests; bubble up the exit code so CI can act on it
pytest -q "$@"
exit $?
