from functions import normal, avg_rec


def experiment():
    D = 0.1 ** 2
    n = 0
    S2 = 0
    Xn = []
    X = 0

    while S2 / (n+1) > D or n < 100:
        Xn.append(normal(0, 1))
        Xnew = avg_rec(X, n+1, Xn)
        S2 = (1 - 1 / (n + 1)) * S2 + (n + 2) * (Xnew - X) ** 2
        X = Xnew
        n += 1
    return S2, X, n


if __name__ == "__main__":
    """
    Generar n valores de una variable aleatoria normal estándar de manera tal
    que se cumplan las condiciones: n >= 30 y S/ n < 0.1,
    siendo S la desviación estándar muestral de los n datos generados.
    a) ¿Cuál es el número esperado de datos que deben generarse para cumplir
       las condiciones?
    b) ¿Cuál es el número de datos generados efectivamente?
    c) ¿Cuál es la media muestral de los datos generados?
    d) ¿Cuál es la varianza muestral de los datos generados?
    e) Comente los resultados de los items (c) y (d). ¿Son sorprendentes?
    """
    variance, X, n = experiment()
    # a)
    """
    (1 / 0.01) * E(S**2) < E(N) == 100 * E(S**2) < E(N)
    El numero esperado de datos es mayor que 100 veces la esperanza de la
    varianza muestral
    """

    # b)
    print("Numero de corridas:{}".format(n))

    # c)
    print("Media Muestral: {}".format(X))

    # d)
    print("Varianza muestral: {}".format(variance))

    # e)
    # Los datos son sorprendentes
