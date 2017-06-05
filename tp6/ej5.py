from functions import avg_rec, interval
from random import random
from math import sqrt


def cae_adentro():
    """
    Calcula si la variable generada cae dentro del circulo unitario
    """

    V1, V2 = 2 * random() - 1, 2 * random() - 1
    return int(V1 ** 2 + V2 ** 2 <= 1)


def experiment():
    D = (0.1 / (1.96 * 2)) ** 2
    n = 0
    S2 = 0
    X = 0
    Xn = []

    while S2 / (n+1) > D or n < 100:
        Xn.append(cae_adentro())
        Xnew = avg_rec(X, n+1, Xn)
        S2 = (1 - 1 / (n + 1)) * S2 + (n + 2) * (Xnew - X) ** 2
        X = Xnew
        n += 1
    return S2, X, n


if __name__ == "__main__":
    S2, X, n = experiment()
    print("Iter: {}".format(n))
    print("Varianza: {}".format(S2 * 4))
    print("Media: {}".format(X * 4))
    cons = 1.96
    S = sqrt(S2)
    a, b = interval(X, cons, S, n)
    print("Intervalo: [{}, {}]".format(4 * a, 4 * b))
