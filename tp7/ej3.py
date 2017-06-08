from functions import stadistic, rejection, simulation
from scipy.special import chdtrc
from random import random


def kolmogorov_smirnov(values):
    n = len(values)
    randoms = [random() for _ in range(n)]
    D1 = max([(i+1/n) - randoms[i] for i in range(n)])
    D2 = max([(i+1/n) - randoms[i] for i in range(n)])
    return max(D1, D2)


def sim_kolmogorov_smirnov(values, k, d):
    success = 0
    n = len(values)

    for _ in range(k):
        Di = kolmogorov_smirnov(values)

        if Di >= d:
            success += 1

    return success / k


if __name__ == '__main__':
    """
    Enunciado: Calcular una aproximación del p−valor de la hipótesis:
     “Los siguientes 10 números son aleatorios”:
     0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74.
    """

    values = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
    values.sort()

    D = kolmogorov_smirnov(values)
    print("Estadisitico D: {}".format(D))

    alpha = 0.05
    k = 1000
    p_value_simulation = sim_kolmogorov_smirnov(values, k, D)
    print("P-Valor simulacion: {}".format(p_value_simulation))
    rejection(p_value_simulation, alpha)
