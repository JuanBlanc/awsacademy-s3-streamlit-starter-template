import os

import pandas as pd
import streamlit as st
import plotly.express as px

from app.services.s3_loader import load_json_from_s3
from app.services.preprocessing import to_dataframe, ensure_columns, parse_time

st.set_page_config(page_title="RA2 · IoT Dashboard", layout="wide")

st.title("RA2 · Dashboard IoT (S3 privado + Streamlit)")
st.caption("Dashboard de sensores IoT con datos desde S3.")

# --- Config ---
AWS_REGION = os.getenv("AWS_REGION", "")
S3_BUCKET = os.getenv("S3_BUCKET", "")
S3_KEY = os.getenv("S3_KEY", "")

with st.sidebar:
    st.header("Configuración")
    st.write("Configura por variables de entorno (recomendado) o escribe aquí para pruebas.")
    aws_region = st.text_input("AWS_REGION", value=AWS_REGION, placeholder="eu-west-1")
    s3_bucket = st.text_input("S3_BUCKET", value=S3_BUCKET, placeholder="mi-bucket-privado")
    s3_key = st.text_input("S3_KEY", value=S3_KEY, placeholder="data/sensores/iabdXX_sensores.json")

    st.divider()
    st.header("Filtros")
    sensor_state = st.selectbox("Estado del sensor", ["(todos)", "OK", "WARN", "FAIL"])
    temp_min, temp_max = st.slider("Rango temperatura (°C)", -20.0, 80.0, (0.0, 40.0), 0.5)

    st.divider()
    reload_btn = st.button("🔄 Recargar datos", type="primary")


@st.cache_data(show_spinner=False)
def load_data(bucket: str, key: str, region: str) -> pd.DataFrame:
    """Carga datos desde S3 y devuelve un DataFrame listo para usar."""
    raw = load_json_from_s3(bucket, key, region)
    df = to_dataframe(raw)
    df = ensure_columns(df)
    df = parse_time(df)
    return df


def apply_filters(df: pd.DataFrame, sensor_state: str, temp_min: float, temp_max: float) -> pd.DataFrame:
    """Aplica filtros del sidebar."""
    filtered = df.copy()
    if sensor_state != "(todos)":
        filtered = filtered[filtered["sensor_state"].astype(str).str.upper() == sensor_state.upper()]
    filtered = filtered[(filtered["temperature_c"] >= temp_min) & (filtered["temperature_c"] <= temp_max)]
    return filtered


def plot_temperature(df: pd.DataFrame):
    """Devuelve una figura Plotly de línea: temperatura vs tiempo."""
    return px.line(
        df.sort_values("timestamp"),
        x="timestamp",
        y="temperature_c",
        color="sensor_id",
        title="Temperatura vs Tiempo"
    )


def plot_co2(df: pd.DataFrame):
    """Devuelve una figura Plotly de barras: CO2 agregado por sensor."""
    agg = df.groupby("sensor_id", as_index=False)["co2_ppm"].mean()
    return px.bar(
        agg,
        x="sensor_id",
        y="co2_ppm",
        title="CO₂ promedio por sensor"
    )


def render_map(df: pd.DataFrame):
    """Muestra el mapa con st.map() usando lat/lon."""
    map_df = df.dropna(subset=["lat", "lon"])[["lat", "lon"]]
    if len(map_df):
        st.map(map_df, latitude="lat", longitude="lon")
    else:
        st.info("No hay coordenadas disponibles para mostrar en el mapa.")


# --- Control recarga cache ---
if reload_btn:
    load_data.clear()

# --- Carga ---
if not s3_bucket or not s3_key or not aws_region:
    st.warning("Define AWS_REGION, S3_BUCKET y S3_KEY (por variables o en la barra lateral).")
    st.stop()

try:
    with st.spinner("Cargando JSON desde S3..."):
        df = load_data(s3_bucket, s3_key, aws_region)
except NotImplementedError as e:
    st.error("Esta es la plantilla starter: aún faltan TODOs por implementar.")
    st.exception(e)
    st.stop()
except Exception as e:
    st.error("No se pudo cargar desde S3. Revisa permisos, región y ruta del objeto.")
    st.exception(e)
    st.stop()

# --- Filtrado ---
try:
    fdf = apply_filters(df, sensor_state, temp_min, temp_max)
except NotImplementedError as e:
    st.error("Faltan TODOs por implementar en apply_filters().")
    st.exception(e)
    st.stop()

# --- Métricas ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("Registros (total)", len(df))
c2.metric("Registros (filtrado)", len(fdf))
c3.metric("Sensores únicos", fdf["sensor_id"].nunique() if len(fdf) else 0)
c4.metric("Última lectura", fdf["timestamp"].max().isoformat() if len(fdf) else "—")

# --- Tabla ---
st.subheader("Tabla (filtrada)")
st.dataframe(
    fdf.sort_values("timestamp", ascending=False) if "timestamp" in fdf.columns else fdf,
    use_container_width=True,
    height=320
)

left, right = st.columns(2)

with left:
    st.subheader("Temperatura en el tiempo")
    if len(fdf):
        try:
            fig = plot_temperature(fdf)
            st.plotly_chart(fig, use_container_width=True)
        except NotImplementedError as e:
            st.info("Implementa plot_temperature() para mostrar esta gráfica.")
    else:
        st.info("Sin datos con el filtro actual.")

with right:
    st.subheader("CO₂ por sensor (agregado)")
    if len(fdf):
        try:
            fig2 = plot_co2(fdf)
            st.plotly_chart(fig2, use_container_width=True)
        except NotImplementedError as e:
            st.info("Implementa plot_co2() para mostrar esta gráfica.")
    else:
        st.info("Sin datos con el filtro actual.")

st.subheader("Mapa de sensores")
if len(fdf):
    try:
        render_map(fdf)
    except NotImplementedError:
        st.info("Implementa render_map() para mostrar el mapa.")
else:
    st.info("Sin datos con el filtro actual.")
