# Enunciado · Tarea Evaluable RA2 (SBD) — AWS Academy Lab

## Contexto
En esta actividad desplegarás un **servidor de visualización** (Streamlit) en **EC2 Ubuntu 22.04** que consumirá datos IoT almacenados en un **bucket S3 privado**.

El objetivo es reproducir un flujo realista:
- **Ingesta** (subida JSON a S3)
- **Procesamiento** (lectura y filtrado)
- **Visualización** (dashboard Streamlit)
- **Despliegue** accesible desde navegador.

---

## Restricciones del entorno AWS Academy
En AWS Academy los permisos pueden estar limitados (IAM, roles, políticas). Por ello hay **dos variantes válidas** para acceder a S3 desde EC2:

### Variante A (recomendada): IAM Role / Instance Profile
- La instancia EC2 tiene un **rol** con permisos mínimos de lectura sobre el prefijo `data/sensores/`.

### Variante B (fallback): AWS CLI configure en EC2
- Si no se permite crear/adjuntar roles, se aceptará:
  - configurar credenciales en EC2 con `aws configure`
  - y que `boto3` las consuma desde `~/.aws/credentials`.
- **Prohibido** subir claves al repositorio, README o capturas.

En `docs/evidencias.md` debes indicar qué variante has usado.

---

## Parte 1 — S3 (bucket privado)
1. Crea un bucket S3 en una región disponible en el lab.
2. Debe ser **privado** (sin acceso público a objetos).
3. Crea el prefijo:
   - `data/sensores/`

---

## Parte 2 — Generar y subir datos (JSON)
Genera (o transforma) un dataset IoT con el siguiente **esquema mínimo recomendado**:

- `timestamp` (ISO8601 o epoch)
- `sensor_id` (string)
- `sensor_state` (OK/WARN/FAIL)
- `temperature_c` (float)
- `co2_ppm` (float)
- `lat`, `lon` (float)

Sube al bucket S3 con una clave como:
- `data/sensores/iabdXX_sensores.json`

El notebook/script debe quedar en `notebooks/` dentro del repositorio.

---

## Parte 3 — EC2 Ubuntu 22.04
1. Crea una instancia EC2 Ubuntu 22.04 (tipo t2.micro o equivalente del lab).
2. Configura el **Security Group**:
   - SSH (22) desde tu IP (o según permita el lab).
   - Streamlit (8501) desde tu IP o `0.0.0.0/0` (solo para el lab).
3. Conéctate por SSH e instala dependencias:
   - Puedes usar `scripts/ec2_setup.sh`.

**Comprobación mínima:** `streamlit hello` debe funcionar.

---

## Parte 4 — Dashboard Streamlit (obligatorio)
Implementa una app en `app/dashboard.py` que:

### 4.1 Carga datos desde S3
- Lee el JSON desde S3 (bucket+key) usando variables de entorno:
  - `AWS_REGION`, `S3_BUCKET`, `S3_KEY`

### 4.2 Añade filtros en barra lateral
- Filtro por **estado** (`sensor_state`)
- Slider de **rango de temperatura**

### 4.3 Muestra una tabla
- Tabla con los registros filtrados (ordenada por timestamp, recomendación).

### 4.4 Gráficas (Plotly)
- Línea: temperatura vs tiempo (color por sensor o similar)
- Barras: CO₂ agregado por sensor (media o suma)

### 4.5 Mapa
- Mapa con `st.map()` usando lat/lon.

---

## Parte 5 — Despliegue en EC2
- Arranca el dashboard para que siga ejecutándose tras cerrar SSH.
- Recomendación: `scripts/run_streamlit_nohup.sh`
- Debe ser accesible desde tu equipo:
  - `http://IP_PUBLICA_EC2:8501`

---

## Reglas de seguridad (obligatorias)
- Prohibido subir al repo:
  - claves AWS, tokens, `.pem`, `.env` con secretos.
- Debes usar:
  - IAM Role (Variante A) **o**
  - `aws configure` en EC2 (Variante B).
- El repositorio debe contener **pasos claros** en `README.md`.

---

## Entrega
Ver `docs/entrega.md`.
