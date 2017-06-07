from functions import avg_rec, interval
from random import random
from math import sqrt, factorial


def M():
    """
    Calcula la variable aleatoria M del ejercicio
    """
    U_Old = random()
    U_new = random()
    n = 1
    while U_Old <= U_new:
        U_Old = U_new
        U_new = random()
        n += 1
    return n


def experiment(ITER):
    S2 = 0
    X = 0
    Xn = []

    for n in range(ITER):
        Xn.append(M())
        Xnew = avg_rec(X, n+1, Xn)
        S2 = (1 - 1 / (n + 1)) * S2 + (n + 2) * (Xnew - X) ** 2
        X = Xnew
    return S2, X, n


# XXX: NO ANDA, PREGUNTAR
def experiment2(ITER):
    return sum([1 / factorial(M()) for _ in range(ITER)]) / ITER


if __name__ == "__main__":
    """
    Considere una sucesón de números aleatorios y sea M de la siguiente forma:
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

    # X = experiment2(ITER)
    # print("Media2: {}".format(X))

    # d)
    # XXX: La varianza del estimador en este caso es  S**2 / N
    variance = S2 / n
    print("Varianza del estimador: {}".format(S2))
    # print("Varianza del estimador: {}".format(variance))

    # Intervalo de confianza
    # X(barra) = 1.96 * (S / sqrt(N))
    cons = 1.96
    S = sqrt(S2)
    a, b = interval(X, cons, S, n)
    print("Intervalo: [{}, {}]".format(a, b))
