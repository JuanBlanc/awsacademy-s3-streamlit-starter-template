---
title: Dashboard IoT sobre S3 privado
description: App Streamlit desplegada en EC2 que lee sensores desde un bucket S3 que nunca se abre a internet.
slug: dashboard-iot-s3
tags: [AWS, S3, EC2, Streamlit, Plotly, Python]
cover: docs/imgs/27_grafica-datos.png
order: 7
---

Dashboard de sensores IoT desplegado en una EC2 Ubuntu y alimentado desde un
bucket S3 **privado**: filtros por estado del sensor y rango de temperatura, tabla
filtrada, serie temporal, CO₂ medio por sensor y mapa por coordenadas. El
ejercicio de fondo no es la gráfica, es cómo lee datos privados una máquina sin
que la credencial toque el repositorio.

## El recorrido

```
Notebook ──▶ S3 (bucket privado, acceso público bloqueado)
                    │
                    ▼
             EC2 Ubuntu 24.04  ──▶  Streamlit :8501
```

Un cuaderno sube el JSON de sensores al bucket; la app, ya en la EC2, lo lee con
boto3 y lo convierte en DataFrame. El bucket no se abre nunca: la app entra por
credencial, no por URL pública.

## Decisiones

- **Credenciales por rol de instancia**, con las variables de entorno como
  alternativa y nada en el repositorio: ni claves, ni `.pem`, ni un `.env`
  versionado. La app recibe región, bucket y clave por entorno y no sabe de dónde
  salen.
- **La descarga va en caché por bucket, clave y región.** Streamlit reejecuta el
  script entero en cada interacción; sin caché, mover el slider de temperatura
  sería una llamada a S3 por gesto. Con ella, filtrar es trabajo local sobre el
  DataFrame que ya está en memoria.
- **Carga y preprocesado viven en `app/services/`**, separados del dashboard.
  `dashboard.py` decide qué se pinta; leer de S3, normalizar columnas y parsear
  los timestamps son funciones aparte, que es lo que hace que se puedan probar sin
  levantar Streamlit ni tener AWS delante.
- **Arranque desatendido y healthcheck** como scripts (`ec2_setup.sh`,
  `run_streamlit_nohup.sh`, `healthcheck.sh`): un despliegue que dependa de dejar
  una terminal SSH abierta no es un despliegue.

## Nota de honestidad

El repositorio parte de la plantilla de la asignatura; lo mío es la
implementación del dashboard, el despliegue y las evidencias. Las treinta
capturas de `docs/imgs/` recorren el proceso completo, desde la creación del
bucket hasta el filtro funcionando en la instancia.

## Probarlo en local

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export AWS_REGION=... S3_BUCKET=... S3_KEY=...
streamlit run app/dashboard.py
```
