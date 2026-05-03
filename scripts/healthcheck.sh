#!/usr/bin/env bash
set -euo pipefail

PORT="${PORT:-8501}"
curl -fsS "http://127.0.0.1:${PORT}" >/dev/null
echo "Streamlit responde en localhost:${PORT}"
