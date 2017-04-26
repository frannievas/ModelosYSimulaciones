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
    f = Poisson_acum(l, i)
    u = random()
    if u >= f:
        # generar X haciendo búsqueda ascendente
        while u >= f:
            i += 1
            f *= l / i
        i -= 1
    else:
        # generar X haciendo búsqueda descendente.
        while u < f:
            i -= 1
            f *= (l / i)
        i += 1

    return i

def experiment(l, k):
    """
    Desarrollar dos métodos para generar una variable aleatoria X.
    """
    u = random()
    i = 0
    f = Poisson(l) / sum([Poisson(l) for i in range(k)])
    while u > f:
        i += 1
        f *= l / i
    if f == 0:
        return 0
   else:
        return i
