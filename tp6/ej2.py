from math import exp
from random import random
from math import sqrt


def experiment():
    D = 0.01 ** 2
    i = 1
    S2 = 0
    X = exp(random() ** 2)
    Xi = [X]

    while S2 / i > D or i < 100:
        Xi.append(exp(random() ** 2))
        Xnew = X + (Xi[i] - X) / (i + 1)
        S2 = (1 - 1 / i) * S2 + (i + 1) * (Xnew - X) ** 2
        X = Xnew
        i += 1

    return S2, X, i


if __name__ == "__main__":
    """
    Estimar mediante el método de Monte Carlo la integral:
    Integral[0][1] e(x**2) dX
    Generar al menos 100 valores y detenerse cuando la desviación estándar
    del estimador sea menor que 0.01.
    """
    S2, X, n = experiment()
    print("Numero de corridas: {}".format(n))
    print("Desviación estándar: {}".format(sqrt(S2)))
    print("Varianza: {}".format(S2))
    print("Estimación: {}".format(X))
