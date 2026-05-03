# Evidencias · RA2 SBD (rellenar por el alumnado)

> Completa este documento con capturas/salidas. No incluyas secretos.
> Indica si has usado **Variante A (IAM Role)** o **Variante B (aws configure)**.

## 0) Identificación
- Alumno/a:juan blanco
- Grupo: a
- Variante usada (A/B): aws configure
- Región AWS: us-east-1
- Bucket S3:juancho-sensores

---

## 1) S3 privado
- [ ] Captura del bucket (nombre y región)
![01 Creación bucket](imgs/01_creacion-bucket.png)
- [ ] Captura/confirmación de que **no es público** (Block Public Access o permisos)
![09 Acceso público bloqueado](imgs/09_acceso-publico-bloqueado.png)
- [ ] Captura del objeto JSON en `data/sensores/`
![03 Prueba datos](imgs/03_prueba-datos.png)
![data-sensores](imgs/data-sensores.png)


**Notas:**
- Key usada (S3_KEY):S1bkkZ8ZFqkNaDB5ne4dsKk/6S3htGFGoFXvObQr

---

## 2) Notebook / Script de subida
- [ ] Captura de la ejecución del notebook/script subiendo a S3
![30-notebook-subida-s3](imgs/30_notebook-subida-s3.png)
- [ ] Enlace o ruta del archivo en el repo (`notebooks/...`)
(notebooks/upload_to_s3.ipynb)

---

## 3) EC2 y red
- [ ] Captura de la instancia EC2 (Ubuntu 22.04)
![07 Verificación instancia](imgs/07_verificacion_instancia.png)
- [ ] Captura del Security Group con puerto 8501 abierto (según reglas del lab)
![06 Config TCP](imgs/06_config-TCP.png)
![05 Config TCP](imgs/05_config-TCP.png)

- [ ] Salida de `ssh` conectando (sin mostrar claves)
![08 Conexión SSH](imgs/08_conexion-instancia-SSH.png)

---

## 4) Acceso a S3 desde EC2 (sin secretos)
Ejecuta en EC2:

```bash
aws sts get-caller-identity
aws s3 ls s3://<BUCKET>/data/sensores/
```

- [ ] Captura/salida de ambos comandos
![17 Comprobación extra](imgs/17_comprobacion-extra.png)
---

## 5) Streamlit en EC2
- [ ] Captura de `streamlit hello` funcionando (o `python -c "import streamlit"`)
- [ ] Captura de instalación de dependencias (`pip install -r requirements.txt`)

---

## 6) Dashboard (funcionalidad)
Incluye capturas donde se vea:

- [ ] Filtro por `sensor_state`
![23 Filtro OK](imgs/23_filtro-ok.png)
![24 Filtro WARN](imgs/24_filtro-warn.png)
![25 Filtro FAIL](imgs/25_filtro-fail.png)

- [ ] Slider de temperatura
![26 Slider temperatura](imgs/26_slider-temp.png)

- [ ] Tabla filtrada
- [ ] Gráfica línea (temperatura vs tiempo)
![27 Gráfica datos](imgs/27_grafica-datos.png)

- [ ] Gráfica barras (CO₂ por sensor)
![28 Gráfica barras](imgs/28_grafica-barras.png)

- [ ] Mapa con sensores
![29 Mapa sensores](imgs/29_mapa-sensores.png)

---

## 7) Despliegue final
- [ ] Comando usado para arrancar en segundo plano (ej. `nohup` o script)

- [ ] Captura del log (`tail -n 50 streamlit.log` o similar)
![20 Activar y arrancar](imgs/20_activar%20y%20arrancar.png)
- [ ] URL final:

**URL:** `http://3.94.93.180:8501`

- [ ] Captura en navegador accediendo a la URL
![22 Prueba final](imgs/22_prueba-final.png)

---

## 8) Observaciones (opcional)
- Problemas encontrados y solución: falo en la ejecucion del script: run_streamlit_nohup.sh por que le faltaba el path de python para encontrar el modulo app.
