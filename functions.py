from random import random
from math import exp, log2


def udiscrete(m, k):
    """
    Uniform discrete variable in interval [m, k]
    """
    u = random()
    return int(u*(k-m+1))+m


def permutation(x):
    """
    Random permutation
    """
    N = len(x)

    for i in range(N-1, 0, -1):
        # Uniform in [0,i]
        index = udiscrete(0, i)
        tmp = x[index]
        x[index] = x[i]
        x[i] = tmp
    return x


def Poisson_acum(l, i):
    prob = exp(-l)
    for j in range(0, i):
        prob *= (l / (j + 1))
    return prob


def Poisson(l):
    i = int(l)
    # Calcular F(I) usando la definición recursiva de p_i
    p = Poisson_acum(l, i)
    f = p
    u = random()
    if u >= f:
        # generar X haciendo búsqueda ascendente
        while u >= f:
            i += 1
            p *= l / i
            f += p
        i -= 1
    else:
        # generar X haciendo búsqueda descendente.
        while u < f:
            i -= 1
            p *= i / l
            f += p
        i += 1

    return i


def Poisson_naive(l, k):
    """
    Metodo naive
    """
    u = random()
    i = 0
    p = exp(-l)
    f = p
    while u >= f:
        i += 1
        p *= l / i
        f += p

    return i


def geometric(p):
    """
    Geometric Distribution
    """
    return(int(log2(1 - random()) / log2(1 - p)) + 1)


def bernoulli_naive(p):
    return random() < p


def binomial_naive(n, p):
    """
    Binomial distribution with parameters n, p
    """
    u = random()
    i = 0
    c = p / (1 - p)  # Constant
    f = prob = (1 - p) ** n  # P0

    while U >= F:
        prob *= c * (n - i) / (i + 1)
        F += prob
        i += 1
    return i
