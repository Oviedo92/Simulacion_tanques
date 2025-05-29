import streamlit as st
from simulacion import calcular_tiempo_llenado, calcular_volumen
from graficos import graficar_llenado, graficar_dispersión
from optimizacion import optimizar_modelo

st.set_page_config(page_title="Simulacion de Tanques", layout="wide")

st.title("Simulacion de llenado y vaciado de taanques de agua")
st.markdown("Parcial 3 - Modelos y Simulación - Universidad Popular del Cesar")

# PUNTO 1: VARIABLES DE ENTRADA
st.header("1️. Paarametros del Tanque y Simulacion")

col1, col2 = st.columns(2)
with col1:
    radio = st.slider("Radio del tanque (m)", 0.5, 5.0, 2.0)
    altura = st.slider("Altura del tanque (m)", 1.0, 10.0, 5.0)
with col2:
    caudal_entrada = st.slider("Caudal de entrada (L/s)", 1.0, 50.0, 10.0)
    caudal_salida = st.slider("Caudal de salida (L/s)", 0.0, 30.0, 5.0)

# Calculos para determinar el volumen y tiempo de llenado
volumen = calcular_volumen(radio, altura)
tiempo_llenado = calcular_tiempo_llenado(volumen, caudal_entrada)

st.success(f"Volumen total: {volumen:.2f} litros")
st.info(f"Tiempo estimado de llenado: {tiempo_llenado:.2f} segundos")

# PUNTO 2: ECUACIONES Y MODELO HIDRAAULICO
st.header("2️.  Modelo Hidraulico")
st.latex(r"V = \pi r^2 h")
st.latex(r"t = \frac{V}{Q}")
st.markdown("Donde **V** es el volumen, **Q** es el caudal, **t** el tiempo, **r** el radio, y **h** la altura.")

# PUNTO 3: GRAFICA DE LLENADO
st.header("3️. Grafica del llenado del Tanque")
graficar_llenado(volumen, caudal_entrada)

# PUNTO 4: DISPERSION Y REGRESION
st.header("4️. Grafica de dispersion y regresion")
graficar_dispersión()

# PUNTO 5: OPTIMIZACION DEL SISTEMA
st.header("5️. Optimizacion del Modelo")
optimo = optimizar_modelo(radio, altura)
if optimo is not None:
    st.success(f" Caudal optimo sugerido: {optimo:.2f} L/s")
else:
    st.warning("No se pudo calcular un caudal optimo.")
