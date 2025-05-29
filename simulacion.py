import numpy as np
import math

def calcular_volumen(radio_m, altura_m):
    """Calcula el volumen en litros de un cilindro."""
    volumen_m3 = math.pi * (radio_m**2) * altura_m  # metros cubicos
    return volumen_m3 * 1000  # Convertir a litros

def calcular_tiempo_llenado(volumen_litros, caudal_litros_segundo):
    """Tiempo en segundos para llenar el tanque."""
    if caudal_litros_segundo <= 0:
        return float('inf')
    return volumen_litros / caudal_litros_segundo

def generar_datos_simulacion(volumen_total, caudal, duracion=100):
    """Simula datos de llenado hasta cierto tiempo o volumen."""
    tiempos = np.arange(0, duracion, 1)
    volumenes = np.minimum(caudal * tiempos, volumen_total)
    return tiempos, volumenes
