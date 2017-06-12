from collections import Counter
from random import random
from math import log2, log, sqrt, factorial


def binomial_naive(n, p):
    """
    Binomial distribution with parameters n, p
    """
    U = random()
    i = 0
    c = p / (1 - p)  # Constant
    F = prob = (1 - p) ** n  # P0

    while U >= F:
        prob *= c * (n - i) / (i + 1)
        F += prob
        i += 1
    return i


def estimate_p_binomial(sample, n):
    return (sum(sample) / len(sample)) / n


def nCr(n,r):
    return factorial(n) / factorial(r) / factorial(n-r)


def binomial(n, p):
    return [binomial_pi(n, p, i) for i in range(n)]


def binomial_pi(n, p, i):
    return nCr(n, i) * (p**i) * ((1 - p) ** (n-i))


def Ni(sample):
    return list(Counter(sample).values())

def sim_ks(n, Iter, d):
    success = 0

    for _ in range(Iter):
        randoms = [random() for _ in range(n)]
        randoms.sort()

        D_values = []
        for j in range(n):
            # j / n - F(Y(j))
            D_values.append((j + 1) / n - randoms[j])
            # F(Y(j)) - (j - 1) / n
            D_values.append(randoms[j] - j / n)

        # D1 = max([(i+1/n) - randoms[i] for i in range(n)])
        # D2 = max([randoms[i] - (i/n) for i in range(n)])
        # # Di = [(i+1/n) - randoms[i] for i in range(n)] + [randoms[i] - (i/n) for i in range(n)]
        # Di = max(D1, D2)
        Di = max(D_values)
        if Di >= d:
            success += 1

    return success / Iter


def rejection(p_value):
    alphas = [0.05, 0.01, 0.1]
    for alpha in alphas:
        print("Alpha:{}".format(alpha))
        if p_value < alpha:
            print("Se rechaza la hipotesis")
        else:
            print("No se rechaza la hipotesis")


def simulation(n, ITER, T, k, Pi, fun):
    """
    :param n: Tamaño de las muestras
    :param ITER: Cantidad de iteraciones
    :param t: T = t, calculado con la muestra original
    :param k: Cantidad de valores que toma la variable aleatoria
    :param Pi: Probabilidades
    :param fun: Funcion de probabilidad de la v.a
    """
    success = 0

    for _ in range(ITER):
        distribution = [fun() for _ in range(n)]
        Ni = [distribution.count(i + 1) for i in range(k)]

        if stadistic(Pi, Ni, n) >= T:
            success += 1

    return success / ITER


def stadistic(Pi, Ni, n):
    """
    Pi: Probabilidades
    Ni: frecuencia absoluta
    """
    T = sum([((Ni[i] - Pi[i] * n) ** 2) / (n * Pi[i]) for i in range(len(Pi))])

    return T


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


def prom_sample(Xi):
    """Calcula el promedio de los Xi"""
    return sum(Xi) / len(Xi)


def avg_rec(X, n, Xi):
    """
    :param X: Promedio con n-1 valores
    :param n:
    :param Xn: Valor n-esimo
    """
    return X + (Xi[n-1] - X) / (n + 1)


def var(Xi, X):
    result = [(i - X) ** 2 for i in Xi]
    return sum(result) / (len(Xi) - 1)


def var_sample(Xi):
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
    values.sort()

    n = len(values)
    if x < values[0]:
        return 0

    for i in range(len(values) - 1):
        if (x >= values[i]) and (x < values[i+1]):
            return (i+1) / n

    return 1
