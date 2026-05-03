from __future__ import annotations

import pandas as pd

REQUIRED_COLUMNS = [
    "timestamp",
    "sensor_id",
    "sensor_state",
    "temperature_c",
    "co2_ppm",
    "lat",
    "lon",
]

def flatten_ubicacion(records: list) -> list:
    """Extrae lat/lon de objeto anidado 'ubicacion' si existe."""
    for r in records:
        if isinstance(r.get("ubicacion"), dict):
            r["lat"] = r["ubicacion"].get("latitud")
            r["lon"] = r["ubicacion"].get("longitud")
    return records

def to_dataframe(raw: object) -> pd.DataFrame:
    """Convierte JSON (lista/dict) a DataFrame."""
    if isinstance(raw, list):
        return pd.DataFrame(flatten_ubicacion(raw))
    if isinstance(raw, dict):
        # Si viene como { "data": [...] } o similar, intenta extraer
        for k in ("data", "records", "items"):
            if k in raw and isinstance(raw[k], list):
                return pd.DataFrame(flatten_ubicacion(raw[k]))
        # Si no, lo tratamos como un único registro
        return pd.DataFrame(flatten_ubicacion([raw]))
    raise ValueError("Formato JSON no soportado")

def ensure_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Asegura columnas mínimas; si faltan, las crea a NaN."""
    for c in REQUIRED_COLUMNS:
        if c not in df.columns:
            df[c] = pd.NA
    # normaliza nombres típicos
    rename_map = {
        "temp": "temperature_c",
        "temperature": "temperature_c",
        "co2": "co2_ppm",
        "state": "sensor_state",
        "id": "sensor_id",
        "longitude": "lon",
        "latitude": "lat",
        "time": "timestamp",
    }
    for old, new in rename_map.items():
        if old in df.columns and new in df.columns and df[new].isna().all():
            df[new] = df[old]
    # tipado
    for num in ("temperature_c", "co2_ppm", "lat", "lon"):
        df[num] = pd.to_numeric(df[num], errors="coerce")
    return df

def parse_time(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte timestamp a datetime."""
    # acepta epoch, ISO8601, etc.
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)
    # si todo es NaT, no rompemos
    if df["timestamp"].isna().all():
        # crea una marca para que la app no falle
        df["timestamp"] = pd.Timestamp.utcnow()
    return df
