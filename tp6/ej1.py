from random import random
from math import log2


def normal_estandar():
    while True:
        Y1 = -log2(random())
        Y2 = -log2(random())
        if Y2 >= (Y1 - 1) ** 2:
            return Y1


def S_naive(Xi, X):
    result = [(i - X) ** 2 for i in Xi]
    return sum(result) / (len(Xi) - 1)


def prom(Xi):
    """Calcula el promedio de los Xi"""
    return sum(Xi) / len(Xi)


def prom(X, n, Xi):
    """
    :param X: Promedio con n-1 valores
    :param n: 
    :param Xn: Valor n-esimo 
    """
    return X + (Xi[n-1] - X) / (n + 1)


def S(Xi):
    """
    Calcula la varianza muestral
    """
    S2 = 0
    X = Xi[0]
    for i in range(len(Xi)):
        Xnew = prom(X, i+1, Xi) 
        S2  = (1 - 1 / (i + 1)) * S2 + (i + 2) * (Xnew - X) ** 2
        X = Xnew
    return S2


def experiment():
    D = 0.1 ** 2

    i = 0
    S2 = 0
    Xi = []
    X = 0 

    while S2 / (i+1) > D or i < 100:
        Xi.append(normal_estandar())
        Xnew = prom(X, i+1, Xi) 
        S2  = (1 - 1 / (i + 1)) * S2 + (i + 2) * (Xnew - X) ** 2
        X = Xnew
        i += 1
    return S2, i


if __name__ == "__main__":
    variance, n = experiment()
    print("Numero de corridas:{}".format(n))
    print("Varianza: {}".format(variance))
