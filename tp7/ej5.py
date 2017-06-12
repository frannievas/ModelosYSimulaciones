from functions import stadistic, rejection, sim_ks, Ni, binomial,binomial_naive, estimate_p_binomial
from math import exp
from random import random
from scipy.stats import expon
from scipy.special import chdtrc


def simulation(n, ITER, T, k, Pi, p):
    """
    :param n: Tamaño de las muestras
    :param ITER: Cantidad de iteraciones
    :param t: T = t, calculado con la muestra original
    :param k: Cantidad de valores que toma la variable aleatoria
    :param Pi: Probabilidades
    :param fun: Funcion de probabilidad de la v.a
    """
    success = 0

    for _ in range(ITER):

        distribution = [binomial_naive(n, p) for _ in range(n)]
        distribution.sort()
        Ni = [distribution.count(i) for i in range(k)]

        pnew = estimate_p_binomial(distribution, n)
        Pi = binomial(n, pnew)

        if stadistic(Pi, Ni, n) >= T:
            success += 1


    return success / ITER


if __name__ == '__main__':
    """
    Enunciado: Calcular una aproximación del p−valor de la prueba de que los
    siguientes datos corresponden a una distribución binomial con parámetros
    (n = 8, p), donde p no se conoce:
    6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7.
    """

    sample = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]

    n = 8
    # Estimamos p = media / n
    sample_mean = sum(sample) / len(sample)
    p = sample_mean / n

    Ni = Ni(sample)
    Pi = binomial(n, p)
    T = stadistic(Pi, Ni, n)
    print("Estadisitico: {} \n".format(T))

    # Estimamos un parametro entonces tomamos chi2 k- 1 - m
    k = 8
    m = 1
    p_value = chdtrc(k-1-m, T)

    print("chi-cuadrado {}".format(chdtrc(7, T)))
    print("P-Valor ji-cuadrada: {}".format(p_value))
    rejection(p_value)

    print("")
    # b)
    ITER = 10000
    p_value_simulation = simulation(n, ITER, T, k, Pi, p)
    print("P-Valor simulacion: {}".format(p_value_simulation))
    rejection(p_value_simulation)
