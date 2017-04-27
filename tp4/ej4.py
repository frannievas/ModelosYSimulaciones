from random import random
from math import exp


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
    Desarrollar dos métodos para generar una variable aleatoria X.
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


def experiment_naive(l, k):
    """
    Desarrollar dos métodos para generar una variable aleatoria X.
    """
    u = random()
    i = 0
    denom = sum([ Poisson_acum(l,x) for x in range(k+1)])
    p = exp(-l) / denom
    f = p
    while u >= f:
        i += 1
        p *= l / i
        f += p

    return i


def experiment(l, k):
    i = int(l)
    denom = sum([ Poisson_acum(l,x) for x in range(k+1)])
    # Calcular F(I) usando la definición recursiva de p_i
    p = Poisson_acum(l, i) / denom
    u = random()
    f = p
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
            p *= (i / l)
            f -= p
        i += 1

    return i

if __name__ == '__main__':
    l = 2
    k = 10
    print(experiment_naive(l, k))
