from random import random
from math import log2, exp


def udiscrete(m, k):
    """
    Uniform discrete variable in interval [m, k]
    """
    u = random()
    return int(u*(k-m+1))+m


def Nexponenciales(n, lamda):
    t = gamma(n, lamda)
    U = [random() for x in range(n+1)]
    U.sort()
    V = [t * U[0]]
    for i in range(1, n-1):
        V.append(t * (V[i] - V[i - 1]))
    V.append(t * V[n - 1])  # Agrego el último valor
    return(V)


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
