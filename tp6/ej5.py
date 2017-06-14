from functions import interval
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
    i = 1
    S2 = 0
    X = cae_adentro()
    Xi = [X]

    while S2 / i > D or i < 100:
        Xi.append(cae_adentro())
        Xnew = X + (Xi[i] - X) / (i + 1)
        S2 = (1 - 1 / i) * S2 + (i + 1) * (Xnew - X) ** 2
        X = Xnew
        i += 1

    return S2, X, i

if __name__ == "__main__":
    """
    Estimar π sorteando puntos uniformemente distribuíos en el cuadrado cuyos
    vértices son:
    (1, 1), (−1, 1), (−1, −1), (1, −1), y contabilizando la fracción que cae
    dentro del círculo inscripto de radio 1.
    Obtener un intervalo de ancho menor que 0.1, el cual contenga a π con el
    95% de confianza.
    ¿Cuántas ejecuciones son necesarias?
    """
    S2, X, n = experiment()
    print("Estimacion de π: {}".format(X * 4))
    print("Cantidad de iteraciones: {}\n".format(n))

    # Dato extra
    print("Varianza: {}".format(S2))
    print("Desviación estandar: {}\n".format(sqrt(S2)))

    # Intervalo de confianza
    # X(barra) = 1.96 * (S / sqrt(N))
    cons = 1.96
    S = sqrt(S2)
    a, b = interval(X, cons, S, n)
    print("Intervalo: [{}, {}] Confianza 95 %\n".format(4 * a, 4 * b))
