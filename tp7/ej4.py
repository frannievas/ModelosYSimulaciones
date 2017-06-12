from functions import stadistic, rejection, simulation, sim_ks
from scipy.stats import expon
from random import random
from math import exp


def expAcum(x, lamda):
    return 1 - exp(-lamda * x)


def ks_sample(sample):
    n = len(sample)
    D1 = max([((i+1)/n) - expAcum(sample[i], 1/50) for i in range(n)])
    D2 = max([expAcum(sample[i], 1/50) - (i/n) for i in range(n)])
    return max(D1, D2)


def ks_sample2(sample):
    n = len(sample)
    D1 = max([((i+1)/n) - expon.cdf(sample[i], 1/50) for i in range(n)])
    D2 = max([expon.cdf(sample[i], 1/50) - (i/n) for i in range(n)])
    return max(D1, D2)


if __name__ == '__main__':
    """
    Enunciado: Calcular una aproximación del p−valor de la hipótesis:
    “Los siguientes 13 valores provienen de una distribución
    exponencial con media 50”:
    86, 133, 75, 22, 11, 144, 78, 122, 8, 146, 33, 41, 99.
    """

    values = [86, 133, 75, 22, 11, 144, 78, 122, 8, 146, 33, 41, 99]
    values.sort()

    Iter = 100

    d_1 = ks_sample(values)
    # d_2 = ks_sample2(values)

    print("Estadisitico: {}".format(d_1))
    # print("Estadisitico 2: {}".format(d_2))

    n = len(values)

    p_value_1 = sim_ks(n, Iter, d_1)
    # p_value_2 = sim_ks(n, Iter, d_2)

    print("P_Value_1: {}".format(p_value_1))
    rejection(p_value_1)

    # print("\n---\n")

    # print("P_Value_2: {}".format(p_value_2))
    # rejection(p_value_2)
