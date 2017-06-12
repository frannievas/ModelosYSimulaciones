from functions import stadistic, rejection, normal, estimate_mu_sigma_normal
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
        Ni = [distribution.count(i) for i in range(n)]
        mu_new, sigma_new = estimate_mu_sigma_normal(distribution, n)

        D = ks_sample(distribution, mu_new, sigma_new)

        if D >= d:
            success += 1

    return success / ITER

if __name__ == '__main__':
    """
    Enunciado: Decidir si los siguientes datos corresponden a una distribución
    Normal:
    91.9 97.8 111.4 122.3 105.4 95.0 103.8 99.6 96.6 119.3 104.8 101.7.
    Calcular una aproximación del p-valor.
    """

    sample = [91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7]
    sample.sort()

    n = len(sample)
    Iter = 10000
    mu, sigma = estimate_mu_sigma_normal(sample, n)

    d = ks_sample(sample, mu, sigma)
    print("Estadisitico: {}".format(d))

    p_value = sim_ks(n, Iter, d, mu, sigma)
    print("P_Value: {}\n".format(p_value))

    rejection(p_value)
