from functions import stadistic, rejection, normal, range_sample
from scipy.stats import expon
from scipy.special import ndtr
from random import random
from math import exp


def ks_sample(sample, mu, sigma):
    n = len(sample)
    D1 = max([((i+1)/n) - ndtr((sample[i] - mu) / sigma) for i in range(n)])
    D2 = max([ndtr((sample[i] - mu) / sigma) - (i/n) for i in range(n)])
    return max(D1, D2)


def sim_ks(n, ITER, d, mu, sigma):
    """
    """
    success = 0

    for _ in range(ITER):
        distribution = [normal(mu, sigma) for _ in range(n)]
        distribution.sort()
        mu_new, sigma_new = estimate_mu_sigma_normal(distribution, n)

        D = ks_sample(distribution, mu_new, sigma_new)

        if D >= d:
            success += 1

    return success / ITER



if __name__ == '__main__':
    """
    Enunciado: Un experimento diseñado para comparar dos tratamientos contra la
    corrosión arrojó los siguientes datos (los cuales representan la máxima
    profundidad de los agujeros en unidades de milésima de pulgada) en pedazos
    de alambre sujetos a cada uno de los tratamientos por separado:

    Tratamiento 1: 65.2 67.1 69.4 78.4 74.0 80.3
    Tratamiento 2: 59.4 72.1 68.0 66.2 58.5
    """

    sample_1 = [65.2, 67.1, 69.4, 78.4, 74.0, 80.3]
    sample_2 = [59.4, 72.1, 68.0, 66.2, 58.5]

    sample_1.sort()
    sample_2.sort()

    n = len(sample)
    Iter = 10000
    mu, sigma = estimate_mu_sigma_normal(sample, n)

    d = ks_sample(sample, mu, sigma)
    print("Estadisitico: {}".format(d))

    p_value = sim_ks(n, Iter, d, mu, sigma)
    print("P_Value: {}\n".format(p_value))

    rejection(p_value)
