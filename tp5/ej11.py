from random import random
from math import log2, exp


def udiscrete(m, k):
    """
    Uniform discrete variable in interval [m, k]
    """
    u = random()
    return int(u*(k-m+1))+m


def Nexponenciales(N, lamda):
    """
    Genera N variables aleatorias, mediante la funcion gamma, de manera óptima.
    """
    Vi, array = [], []
    t = gamma(N, lamda)
    Vi = [random() for _ in range(N)]
    Vi.sort()
    intervals = ([t * Vi[0]] +
                 [t * (Vi[i] - Vi[i - 1]) for i in range(1, N-1)] +
                 [t - t * Vi[N - 1]])

    return intervals


def gamma(n, lamda):
    """
    Gamma distribution with parameters n, lambda
    """
    u = 1
    for _ in range(n):
        u *= random()
    return - log2(u) / lamda


def eventosPoisson(T):
    U = [random() for x in range(T+1)]
    U.sort()
    return [T * x for x in U]


def Poisson_naive(lamda):
    """
    Metodo naive
    """
    u = random()
    i = 0
    p = exp(-lamda)
    f = p
    while u >= f:
        i += 1
        p *= lamda / i
        f += p

    return i


def experiment(lamda):
    return sum([udiscrete(20, 40) for x in range(Poisson_naive(lamda))])


if __name__ == '__main__':
    lamda = 5
    print(experiment(lamda))
