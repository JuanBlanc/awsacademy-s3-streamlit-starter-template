# Pistas (opcional) · RA2 SBD

## Lectura desde S3 (boto3)
En `load_data()`:
1) `raw = load_json_from_s3(bucket, key, region)`
2) `df = to_dataframe(raw)`
3) `df = ensure_columns(df)`
4) `df = parse_time(df)`

## Filtros
- Estado:
  - `df["sensor_state"].astype(str).str.upper() == sensor_state`
- Temperatura:
  - `df[(df["temperature_c"]>=temp_min) & (df["temperature_c"]<=temp_max)]`

## Plotly
- Línea:
  - `px.line(df.sort_values("timestamp"), x="timestamp", y="temperature_c", color="sensor_id")`
- Barras:
  - `agg = df.groupby("sensor_id", as_index=False)["co2_ppm"].mean()`
  - `px.bar(agg, x="sensor_id", y="co2_ppm")`

## Mapa
- `map_df = df.dropna(subset=["lat","lon"])[["lat","lon"]]`
- `st.map(map_df, latitude="lat", longitude="lon")`

## EC2 / red (AWS Academy)
- Security Group: abrir 8501/TCP.
- Si no carga desde fuera: comprobar que Streamlit está en `--server.address 0.0.0.0`.
