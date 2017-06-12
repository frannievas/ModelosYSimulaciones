from functions import stadistic, rejection, exponential, estimate_lamda_exponential
from scipy.stats import expon
from random import random
from math import exp


def expAcum(x, lamda):
    return 1 - exp(-lamda * x)


def ks_sample(sample, lamda):
    n = len(sample)
    D1 = max([((i+1)/n) - expAcum(sample[i], lamda) for i in range(n)])
    D2 = max([expAcum(sample[i], lamda) - (i/n) for i in range(n)])
    return max(D1, D2)


def sim_ks(n, ITER, d, lamda):
    """
    """
    success = 0

    for _ in range(ITER):
        distribution = [exponential(lamda) for _ in range(n)]
        # XXX: BIQUERFUL! HAY QUE ORDENAR
        distribution.sort()
        lamda_new = estimate_lamda_exponential(distribution, n)

        D = ks_sample(distribution, lamda_new)

        if D >= d:
            success += 1

    return success / ITER

if __name__ == '__main__':
    """
    Enunciado: En un estudio de vibraciones, una muestra aleatoria de 15
    componentes del avión fueron sometidos a fuertes vibraciones hasta que se
    evidenciaron fallas estructurales. Los datos proporcionados son los minutos
    transcurridos hasta que se evidenciaron dichas fallas.
    1.6 10.3 3.5 13.5 18.4 7.7 24.3 10.7 8.4 4.9 7.9 12 16.2 6.8 14.7
    Pruebe la hipótesis nula de que estas observaciones pueden ser consideradas
    como una muestra de la población exponencial.
    """

    sample = [1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12, 16.2, 6.8, 14.7]
    sample.sort()

    n = len(sample)
    Iter = 10000
    lamda = estimate_lamda_exponential(sample, n)

    d = ks_sample(sample, lamda)
    print("Estadisitico: {}".format(d))

    p_value = sim_ks(n, Iter, d, lamda)
    print("P_Value: {}\n".format(p_value))

    rejection(p_value)
