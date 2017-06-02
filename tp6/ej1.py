from random import random
from math import log2
from functions import normal, S, prom


def experiment():
    D = 0.1 ** 2
    n = 0
    S2 = 0
    Xn = []
    X = 0

    while S2 / (n+1) > D or n < 100:
        Xn.append(normal(0,1))
        Xnew = prom(X, n+1, Xn)
        S2 = (1 - 1 / (n + 1)) * S2 + (n + 2) * (Xnew - X) ** 2
        X = Xnew
        n += 1
    return S2, X, n


if __name__ == "__main__":
    variance, X, n = experiment()
    print("Numero de corridas:{}".format(n))
    print("Varianza: {}".format(variance))
    print("Promedio: {}".format(X))
