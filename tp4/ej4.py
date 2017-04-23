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
        p = f
        while u >= f:
            p *= l * i
            i += 1
            f += p
    else:
        # generar X haciendo búsqueda descendente.
        p = f
        while u >= f:
            p *= (l / i)
            i += 1
            f += p
    return i
