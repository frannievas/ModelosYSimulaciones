from functions import rejection, p_value, exponential, d_value_exponential
from math import exp


if __name__ == '__main__':
    """
    Enunciado: Generar los valores correspondientes a 10 variables aleatorias
    exponenciales independientes,cada una con media 1. Luego, en base al
    estadístico de prueba de Kolmogorov-Smirnov, aproxime el p−valor de la
    prueba de que los datos realmente provienen de una distribución exponencial
    con media 1.
    """

    n = 10
    values = [exponential(1) for _ in range(n)]
    values.sort()

    Iter = 10000

    d = d_value_exponential(values, 1)

    print("Estadisitico: {}".format(d))
    n = len(values)

    p_value = p_value(n, Iter, d)

    print("P_Value: {}".format(p_value))
    rejection(p_value)
