from functions import rejection, sim_ks, exponential
from math import exp


def expAcum(x, lamda):
    return 1 - exp(-lamda * x)


def ks_sample(sample):
    n = len(sample)
    D1 = max([((i+1)/n) - expAcum(sample[i], 1) for i in range(n)])
    D2 = max([expAcum(sample[i], 1) - (i/n) for i in range(n)])
    return max(D1, D2)


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

    d = ks_sample(values)

    print("Estadisitico: {}".format(d))
    n = len(values)

    p_value = sim_ks(n, Iter, d)

    print("P_Value: {}".format(p_value))
    rejection(p_value)
