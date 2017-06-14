from functions import interval, all_interval
from random import random
from math import sqrt, factorial


def M():
    """
    Calcula la variable aleatoria M del ejercicio
    """
    U_Old = random()
    U_new = random()
    n = 2
    while U_Old <= U_new:
        U_Old = U_new
        U_new = random()
        n += 1

    return n


def experiment(ITER):
    S2 = 0
    X = M()
    Xi = [X]

    for i in range(1, ITER + 1):
        Xi.append(M())
        Xnew = X + (Xi[i] - X) / (i + 1)
        S2 = (1 - 1 / i) * S2 + (i + 1) * (Xnew - X) ** 2
        X = Xnew

    return S2, X, i


def experiment2(ITER):
    return sum([1 / factorial(i) for i in range(ITER)])


if __name__ == "__main__":
    """
    Considere una sucesión de números aleatorios y sea M de la siguiente forma:
    M = {n : U1 ≤ U2 ≤ · · · ≤ Un−1 > Un }

    c) Utilizar el resultado del item anterior para estimar e mediante 1000
       ejecuciones de una simulación.
    d) Calcular la varianza del estimador del item (c) y dar una estimación
       de e mediante un intervalo de confianza de 95%.
    """

    # c) Estimar e, E[M] = e
    ITER = 1000
    S2, X, n = experiment(ITER)
    print("Media: {}".format(X))

    X = experiment2(ITER)
    print("Media2: {}".format(X))

    # d)
    # La varianza del estimador en este caso es  S**2 / N
    variance = S2 / n
    print("Varianza del estimador: {}".format(S2))

    # Intervalo de confianza
    # X(barra) = 1.96 * (S / sqrt(N))
    cons = 1.96
    S = sqrt(S2)
    a, b = interval(X, cons, S, n)
    print("Intervalo: [{}, {}] Confianza: 95 %\n".format(a, b))

    print("Todos los intervalos:")
    all_interval(X, S, n)
