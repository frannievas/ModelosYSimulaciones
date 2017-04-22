from random import random

N1 = 100
N2 = 1000
N3 = 10000
N4 = 100000
N = [N1, N2, N3, N4]


def udiscrete(m, k):
    """
    Uniform discrete variable in interval [m, k]
    """
    u = random()
    return int(u*(k-m+1))+m


def experiment():
    """
    Se lanzan simultáneamente un par de dados legales y se anota el resultado
    de la suma de ambos. El proceso se repite hasta que todos los resultados
    posibles: 2,3,...,12 hayan aparecido al menos una vez.
    """
    result = set()
    i = 0
    while len(result) != 11:
        dice1 = udiscrete(1, 6)
        dice2 = udiscrete(1, 6)
        result.add(dice1 + dice2)
        i += 1

    return i


if __name__ == '__main__':
    for n in N:
        results = [experiment() for x in range(n)]
        print("Mean: {}".format(sum(results) / n))
