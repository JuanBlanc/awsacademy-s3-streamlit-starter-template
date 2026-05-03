# RA2 SBD · Dashboard IoT en Streamlit con datos en S3 (AWS Academy) — Plantilla Profesor

Este repositorio es la **plantilla oficial** para la *Tarea Evaluable RA2* del curso de especialización (Sistemas de Big Data) en entorno **AWS Academy Lab**.

## Objetivo
Implementar un **pipeline sencillo**:
1. Generar/obtener datos IoT (JSON) y **subirlos a un bucket S3 privado**.
2. Desplegar una app **Streamlit** en una **EC2 Ubuntu 24.04** que **lee el JSON desde S3**.
3. Construir un dashboard con:
   - filtros (estado del sensor + rango de temperatura),
   - tabla filtrada,
   - gráficas Plotly,
   - mapa (lat/lon),
   - despliegue accesible por `http://IP_PUBLICA:8501`.

> El enunciado completo, evidencias y rúbrica están en `docs/`.

> Pistas opcionales: ver `docs/pistas.md`.


---

## Flujo de trabajo (alumnado)
1. Haced **Fork** de este repo a vuestra cuenta de GitHub.
2. Trabajad solo en vuestro fork (commits frecuentes).
3. Entrega: **enlace al repo** + **tag** `v1.0-entrega` (ver `docs/entrega.md`).

---

## Quickstart (local, opcional)
> Puede ejecutarse en local si tenéis credenciales AWS configuradas (o si usáis un JSON local de prueba).

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # opcional (no se sube)
streamlit run app/dashboard.py
```

---

## Quickstart (EC2 Ubuntu 24.04 en AWS Academy)
En la EC2:

```bash
sudo apt update
sudo apt install -y git
git clone <URL_DE_VUESTRO_FORK>
cd <repo>
bash scripts/ec2_setup.sh
bash scripts/run_streamlit_nohup.sh
```

Abrir:
- `http://IP_PUBLICA_EC2:8501`

---

## Configuración por variables de entorno
La app usa estas variables (en EC2 es recomendable exportarlas en `~/.bashrc` o en un `.env` **no versionado**):

- `AWS_REGION` (ej. `us-west-1`)
- `S3_BUCKET` (nombre del bucket)
- `S3_KEY` (ruta del objeto, ej. `data/sensores/iabdXX_sensores.json`)

Ejemplo:

```bash
export AWS_REGION=us-west-1
export S3_BUCKET=mi-bucket-privado
export S3_KEY=data/sensores/iabd01_sensores.json
```

**Importante:** No subáis claves (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `.pem`, etc.) al repo.

---

## Estructura del repo
- `app/` → Streamlit + servicios de carga/procesado
- `scripts/` → setup EC2 y arranque en segundo plano
- `docs/` → enunciado, entrega, evidencias, rúbrica
- `notebooks/` → aquí irá vuestro notebook/script de subida a S3

---

## Licencia
Uso docente.
