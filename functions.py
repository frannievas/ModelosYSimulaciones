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


def binomial(n, p):
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


def composition(alpha, distributions):
    """
    Composition method
    :param alpha: List with all the alphas
    :param distributions: List with all the distributions
    """
    assert sum(alpha) == 1
    assert len(distributions) == len(alphas)

    alpha_distributions = list(zip(alpha, distributions))
    alpha_distributions.sort(reverse=True)
    u = random()
    prob = 0

    for a, d in alpha_distributions:
        prob += a
        if u <= prob:
            return d


def alias(n, var):
    """
    Alias method
    :param n: size of the alias
    :param var: list of lists
    e.g
    var[0] = [ (0.1, 3), (0.9, 2)]
    0.1 and 0.9 are the probabilities
    3 and 2 are the return values
    """
    i = int(random() * n) # pos
    v = random()

    x = var[i]

    if x[0][0] < v:
        return x[0][1]
    else:
        return x[1][1]

"""
ejemplo del teorico
"""
# n = 3
# x1 = [(5/8, 1), (3/8, 3)]
# x2 = [(9/16, 4), (7/16, 2)]
# x3 = [(11/16, 1), (4/16, 2)]
# var = [x1, x2, x3]
# alias(n, var)


def urna(k, p, r):
    """
    Urn method
    :param k: int. k * Pi must be integer for all Pi
    :param p: List with all the Pi probs
    :param r: List with all the return values
    """
    A = []
    p = p.sort()

    # Create the array
    for i, elem in enumerate(r):
        A += [elem for x in range(int(p[i]*k))]

    i = int(random()*k) + 1

"""
ejemplo de urna
# """
# k = 10
# p = [0.2, 0.8]
# r = [1, 2]
# urna(k, p, r)
