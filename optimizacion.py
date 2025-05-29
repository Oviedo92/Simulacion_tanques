import sympy as sp

def optimizar_modelo(radio, altura):
    """
    Retorna un valor sugerido de caudal optimo.
    """
    V = sp.pi * (radio**2) * altura * 1000  # litros

    # Tiempo a llenarse en 5 minutos su conversion a (300s)
    tiempo_deseado = 300  # segundos

    Q_optimo = V / tiempo_deseado
    return round(Q_optimo, 2)
