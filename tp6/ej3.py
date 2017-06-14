from functions import interval, all_interval
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
    X = N()
    Xi = [X]

    for i in range(1, ITER + 1):
        Xi.append(N())
        Xnew = X + (Xi[i] - X) / (i + 1)
        S2 = (1 - 1 / i) * S2 + (i + 1) * (Xnew - X) ** 2
        X = Xnew
        i += 1

    return S2, X, i


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

    print("Media muestral: {}".format(X))
    print("Varianza {}".format(S2))
    # ===================================================================== #
    # Intervalo de confianza
    # X(barra) = 1.96 * (S / sqrt(N))
    cons = 1.96
    S = sqrt(S2)
    a, b = interval(X, cons, S, n)
    print("Estimación de e mediante un intervalo")
    print("Intervalo: [{}, {}] Confianza: 95\n".format(a, b))

    print("Todos los intervalos:")
    INTERVALS = all_interval(X, S, n)
