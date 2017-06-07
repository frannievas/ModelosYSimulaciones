from random import random
from math import log2, log, sqrt


def udiscrete(m, k):
    """
    Uniform discrete variable in interval [m, k]
    """
    u = random()
    return int(u*(k-m+1))+m


def interval(X, c, S, n):
    """
    Calcula los intervalos de confianza para los parametros recibidos

    :param X: Media muestral
    :param C: Constanste Zalfa
    :param S: Varianza muestral
    :param n: Largo de la muestra
    """
    return (X - c * (S/sqrt(n)), X + c * (S/sqrt(n)))


def exponential(lamda):
    """
    Genera una va Exponencial, a partir de su único parámentro lamda,
    utilizando el método de la transformada inversa.
    """
    return(- log(random()) / lamda)


def normal(mu, sigma):
    """
    Esta función devuelve una va normal, utilizando el método de Aceptación y
    Rechazo mediante 2 va exponenciales.
    """
    Y1, Y2 = exponential(1), exponential(1)

    while Y2 < (Y1 - 1) ** 2 / 2:
        Y1, Y2 = exponential(1), exponential(1)

    if random() < 0.5:
        return(Y1 * sigma + mu)
    else:
        return(-Y1 * sigma + mu)


def normal_estandar():
    while True:
        Y1 = -log2(random())
        Y2 = -log2(random())
        if Y2 >= (Y1 - 1) ** 2:
            return Y1


def avg_sample(Xi):
    """Calcula el promedio de los Xi"""
    return sum(Xi) / len(Xi)


def avg_rec(X, n, Xi):
    """
    :param X: Promedio con n-1 valores
    :param n:
    :param Xn: Valor n-esimo
    """
    return X + (Xi[n-1] - X) / (n + 1)


def var_sample(Xi):
    X = avg_sample(Xi)
    result = [(i - X) ** 2 for i in Xi]
    return sum(result) / (len(Xi) - 1)


def var_sample_rec(Xi):
    """
    Calcula la varianza muestral
    """
    S2 = 0
    X = Xi[0]
    for i in range(len(Xi)):
        Xnew = avg_rec(X, i+1, Xi)
        S2 = (1 - 1 / (i + 1)) * S2 + (i + 2) * (Xnew - X) ** 2
        X = Xnew
    return S2


def empiric(x, values):
    """
    Funcion empirica
    :param x: valor en el que se desea evaluar la funcion
    :param values: valores que toma la funcion empirica
    """
    n = len(values)
    if x < values[0]:
        return 0

    for i in range(len(values) - 1):
        if (x >= values[i]) and (x < values[i+1]):
            return (i+1) / n

    return 1


def bootstrap(sample, N):
    """
    :variable: mean: Estimación por boostrap de la media.
    :variable: var: Estimación por boostrap de la varianza.
    """
    empirical_mean = avg_sample(sample)
    empirical_var = var_sample(sample)
    n, mean, var = len(sample), 0, 0

    for _ in range(N):
        sum_xi, values = 0, []
        for _ in range(n):
            index = udiscrete(0, n - 1)
            sum_xi += sample[index]
            values.append(sample[index])
        mean_tmp = sum_xi / n

        var_tmp = 0
        for value in values:
            var_tmp += (value - mean_tmp) ** 2
        var_tmp /= (n - 1)

        mean += (mean_tmp - empirical_mean) ** 2
        var += (var_tmp - empirical_var) ** 2
    return(mean / N, var / N)
