from functions import S, prom, interval
from random import random
from math import sqrt


def N():
    """
    Calcula la variable aleatoria N del ejercicio
    """
    Ui = 0
    n = 0
    while Ui < 1:
        Ui += random()
        n += 1
    return n


def experiment():
    D = 0.01 ** 2
    S2 = 0
    X = 0
    Xn = []

    for n in range(1000):
        Xn.append(N())
        Xnew = prom(X, n+1, Xn)
        S2 = (1 - 1 / (n + 1)) * S2 + (n + 2) * (Xnew - X) ** 2
        X = Xnew
        n += 1
    return S2, X, n


if __name__ == "__main__":
    S2, X, n = experiment()
    variance = S2 / n
    print("Varianza del estimador: {}".format(variance))
    cons = 1.96
    S = sqrt(S2)
    a, b = interval(X, cons, S, n)
    print("Intervalo: {} {}".format(a,b))´
