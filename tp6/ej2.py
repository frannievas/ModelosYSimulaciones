from math import exp
from random import random
from functions import avg_rec


def experiment():
    D = 0.01 ** 2
    i = 0
    S2 = 0
    X = 0
    Xi = []

    while S2 / (i+1) > D or i < 100:
        Xi.append(exp(random() ** 2))
        Xnew = avg_rec(X, i+1, Xi)
        S2 = (1 - 1 / (i + 1)) * S2 + (i + 2) * (Xnew - X) ** 2
        X = Xnew
        i += 1
    return X, i


if __name__ == "__main__":
    X, n = experiment()
    print("Numero de corridas:{}".format(n))
    print("Estimacion: {}".format(X))
