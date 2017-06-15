from functions import rejection, p_value, d_value_exponential
from math import exp


if __name__ == '__main__':
    """
    Enunciado: Calcular una aproximación del p−valor de la hipótesis:
    “Los siguientes 13 valores provienen de una distribución
    exponencial con media 50”:
    86, 133, 75, 22, 11, 144, 78, 122, 8, 146, 33, 41, 99.
    """

    values = [86, 133, 75, 22, 11, 144, 78, 122, 8, 146, 33, 41, 99]
    values.sort()

    Iter = 10000

    d_1 = d_value_exponential(values, 1/50)

    print("Estadisitico: {}".format(d_1))

    n = len(values)

    p_value_1 = p_value(n, Iter, d_1)

    print("P_Value_1: {}".format(p_value_1))
    rejection(p_value_1)
