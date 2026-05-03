#!/usr/bin/env bash
set -euo pipefail

# Activa venv si existe
if [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
fi

# Necesario para que Python encuentre el modulo 'app'
export PYTHONPATH="${PYTHONPATH:-}:$(pwd)"

PORT="${PORT:-8501}"
ADDR="${ADDR:-0.0.0.0}"

echo "Arrancando Streamlit en segundo plano en ${ADDR}:${PORT} ..."
nohup streamlit run app/dashboard.py --server.address "${ADDR}" --server.port "${PORT}" > streamlit.log 2>&1 &

echo "OK. Revisa logs con: tail -f streamlit.log"
echo "Abre: http://IP_PUBLICA_EC2:${PORT}"
