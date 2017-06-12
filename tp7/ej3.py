from functions import stadistic, rejection, simulation, sim_ks
from scipy.special import chdtrc
from random import random

def ks_sample(sample):
    n = len(sample)
    D1 = max([((i+1)/n) - sample[i] for i in range(n)])
    D2 = max([sample[i] - (i/n) for i in range(n)])
    return max(D1, D2)


if __name__ == '__main__':
    """
    Enunciado: Calcular una aproximación del p−valor de la hipótesis:
     “Los siguientes 10 números son aleatorios”:
     0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74.
    """

    values = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
    values.sort()

    D = ks_sample(values)
    print("Estadisitico D: {}".format(D))

    Iter = 1000
    n = len(values)
    p_value_simulation = sim_ks(n, Iter, D)
    print("P-Valor simulacion: {}".format(p_value_simulation))
    rejection(p_value_simulation)
