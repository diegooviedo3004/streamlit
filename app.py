import streamlit as st
import time
import random
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Monitor de Calidad del Aire", layout="wide")

# Títulos de la aplicación
st.title("Monitor de Calidad del Aire 🌍")
st.markdown("**Simulación de datos en tiempo real para temperatura y humedad.**")

# Datos iniciales
if "data" not in st.session_state:
    st.session_state.data = {
        "timestamp": [],
        "temperature": [],
        "humidity": []
    }

# Función para generar datos simulados
def generate_data():
    current_time = time.strftime("%H:%M:%S")
    temperature = round(random.uniform(20, 30), 1)  # Temperatura entre 20°C y 30°C
    humidity = round(random.uniform(40, 60), 1)     # Humedad entre 40% y 60%

    st.session_state.data["timestamp"].append(current_time)
    st.session_state.data["temperature"].append(temperature)
    st.session_state.data["humidity"].append(humidity)

    # Mantener máximo 20 registros
    if len(st.session_state.data["timestamp"]) > 20:
        for key in st.session_state.data.keys():
            st.session_state.data[key].pop(0)

# Layout de columnas
col1, col2 = st.columns(2)

# Contenedores para los gráficos
with col1:
    st.header("Temperatura (°C)")
    temp_chart_placeholder = st.empty()

with col2:
    st.header("Humedad (%)")
    humidity_chart_placeholder = st.empty()

# Botón de alerta
if st.button("Lanzar Alerta"):
    st.warning("⚠️ ¡Alerta de Calidad del Aire detectada! ⚠️")

# Simulación en tiempo real
while True:
    generate_data()
    
    # Crear un DataFrame con los datos actuales
    df = pd.DataFrame(st.session_state.data)

    # Actualizar gráficos
    with temp_chart_placeholder:
        st.line_chart(df.set_index("timestamp")[["temperature"]], use_container_width=True)

    with humidity_chart_placeholder:
        st.line_chart(df.set_index("timestamp")[["humidity"]], use_container_width=True)

    time.sleep(1)  # Actualización cada segundo
