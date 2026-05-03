#!/usr/bin/env bash
set -euo pipefail

echo "[1/5] Instalando dependencias del sistema..."
sudo apt update
sudo apt install -y python3-pip python3-venv git

echo "[2/5] Creando entorno virtual..."
python3 -m venv .venv
source .venv/bin/activate

echo "[3/5] Instalando dependencias Python..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[4/5] Verificación Streamlit..."
python -c "import streamlit; print('streamlit OK')"

echo "[5/5] Listo. Ahora exporta variables AWS_REGION/S3_BUCKET/S3_KEY y ejecuta run_streamlit_nohup.sh"
