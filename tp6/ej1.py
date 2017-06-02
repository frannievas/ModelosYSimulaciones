from random import random
from math import log2


def experiment():
    D = 0.1 ** 2
    i = 0
    S2 = 0
    Xi = []
    X = 0

    while S2 / (i+1) > D or i < 100:
        Xi.append(normal_estandar())
        Xnew = prom(X, i+1, Xi)
        S2 = (1 - 1 / (i + 1)) * S2 + (i + 2) * (Xnew - X) ** 2
        X = Xnew
        i += 1
    return S2, i


if __name__ == "__main__":
    variance, n = experiment()
    print("Numero de corridas:{}".format(n))
    print("Varianza: {}".format(variance))
