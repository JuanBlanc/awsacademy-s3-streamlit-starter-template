# Rúbrica · RA2 SBD (10 puntos)

> Puede ajustarse según el curso. Esta rúbrica está pensada para AWS Academy.

## 1) S3 privado + datos (2.0)
- 1.0: Bucket privado correctamente configurado y evidenciado
- 1.0: JSON subido en `data/sensores/` con esquema razonable

## 2) Ingesta (notebook/script) (1.5)
- 1.0: Notebook/script genera/transforma datos correctamente
- 0.5: Subida a S3 reproducible y documentada

## 3) EC2 + despliegue (2.0)
- 1.0: EC2 Ubuntu 22.04 + SG correcto + acceso por SSH
- 1.0: Streamlit desplegado en `http://IP:8501` y mantenido en segundo plano

## 4) Dashboard Streamlit (3.5)
- 1.0: Lectura desde S3 por variables de entorno (sin secretos en código)
- 1.0: Filtros (estado + rango temperatura) + tabla filtrada
- 1.0: Plotly (línea temperatura, barras CO₂)
- 0.5: Mapa (st.map con lat/lon)

## 5) Buenas prácticas GitHub (1.0)
- 0.5: README claro + estructura de repo correcta
- 0.5: Evidencias completas + tag `v1.0-entrega`

### Bonus (hasta +1.0)
- +1.0: Variante A (IAM Role mínimo privilegio) documentada y evidenciada
