from random import random
from math import log2, exp


def gamma(n, lamda):
    """
    Gamma distribution with parameters n, lambda
    """
    u = 1
    for _ in range(n):
        u *= random()
    return - log2(u) / lamda


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


def eventosPoisson(T):
    U = [ random() for x in range(T+1)]
    U.sort()
    return [ T * x for x in U]


if __name__ == '__main__':
    T = 10
    lamda = 2
    print(Nexponenciales(T, lamda))
