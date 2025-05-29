import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from simulacion import generar_datos_simulacion
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def graficar_llenado(volumen, caudal):
    """Tiempo del graficoo de llenado del tanque."""
    tiempos, volumenes = generar_datos_simulacion(volumen, caudal, duracion=200)

    fig, ax = plt.subplots()
    ax.plot(tiempos, volumenes, label="Volumen acumulado")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Volumen (L)")
    ax.set_title("Llenado del Tanque")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

def graficar_dispersión():
    """Generaa dispersion y regresion ."""
    np.random.seed(0)
    
    # Caaudal: de 1 a 20 L/s
    x = np.random.uniform(1, 20, 50)

    # Tiempo estimado mayor caudal → menor tiempo
    y = 10000 / x + np.random.normal(0, 50, 50)

    df = pd.DataFrame({'Caudal (L/s)': x, 'Tiempo (s)': y})

    # Ajuste lineal
    model = LinearRegression()
    model.fit(df[['Caudal (L/s)']], df['Tiempo (s)'])
    pred = model.predict(df[['Caudal (L/s)']])

    # Graficar
    fig, ax = plt.subplots()
    sns.scatterplot(x='Caudal (L/s)', y='Tiempo (s)', data=df, ax=ax)
    sns.lineplot(x=df['Caudal (L/s)'], y=pred, color='red', label="Regresion", ax=ax)
    ax.set_title("Dispersioon: Caudal vs. Tiempo de llenado")
    ax.grid(True)
    st.pyplot(fig)

