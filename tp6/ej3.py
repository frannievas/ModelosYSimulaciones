from functions import avg_rec, interval
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


def experiment(ITER):
    S2 = 0
    X = 0
    Xn = []

    for n in range(ITER):
        Xn.append(N())
        Xnew = avg_rec(X, n+1, Xn)
        S2 = (1 - 1 / (n + 1)) * S2 + (n + 2) * (Xnew - X) ** 2
        X = Xnew
        n += 1
    return S2, X, n


if __name__ == "__main__":
    """
    Calcular la varianza del estimador N̄ correspondiente a 1000 ejecuciones
    de la simulación y dar una estimación de e mediante un intervalo de
    confianza de 95%.
    """
    ITER = 1000
    S2, X, n = experiment(ITER)
    # La varianza del estimador en este caso es  S**2 / N
    variance = S2 / n
    print("Varianza del estimador: {}".format(variance))

    # ====================================================================== #
    # Intervalo de confianza
    # X(barra) = 1.96 * (S / sqrt(N))
    cons = 1.96
    S = sqrt(S2)
    a, b = interval(X, cons, S, n)
    print("Intervalo: [{}, {}]".format(a, b))
