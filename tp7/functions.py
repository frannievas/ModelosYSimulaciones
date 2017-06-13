from collections import Counter
from random import random
from math import log2, log, sqrt, factorial
from scipy.special import ndtr


def range_simulation(sample_1, sample_2, r, N):
    # sample_1 es la mas chica siempre, cambio de nombre si es necesario.
    if len(sample_2) <= len(sample_1):
        tmp = sample_1
        sample_1 = sample_2
        sample_2 = tmp

    all_sample = sample_1 + sample_2
    success_min = 0
    success_max = 0

    for _ in range(N):
        per = permutation(all_sample)
        R = range_sample(sample_1, sample_2, per)

        if R >= r:
            success_max += 1
        else:
            success_min += 1

    return 2 * min(success_min / N, success_max / N)

def range_normal(n, m, r):
    num = r - n * (n + m + 1) / 2
    den = sqrt(n * m * (n + m + 1) / 12)
    R = num / den
    if r <= n * ((n + m + 1) / 2):
        return 2 * ndtr(R)
    else:
        return 2 * (1 - ndtr(R))


def range_sample(sample_1, sample_2, all_sample=None):
    if all_sample is None:
        all_sample = sample_1 + sample_2
        all_sample.sort()
    # Si la sample_2 es la mas chica
    if len(sample_2) < len(sample_1):
        tmp = sample_1
        sample_1 = sample_2
        sample_2 = tmp

    # Si hay repeticiones
    repetition = [(i, count) for i, count in Counter(all_sample).items() if count > 1]

    if len(repetition) > 0:
        val_rep_s1 = [i for i, c in repetition if i in sample_1 and i in sample_2]
        R = 0

        # Sumo todos los que se repiten
        for i in val_rep_s1:
            index = [j+1 for j in range(len(all_sample)) if all_sample[j] in val_rep_s1]
            R += sum(index) / len(index)
        # Sumo todos los que no se repiten
        R += sum([k+1 for k in range(len(all_sample)) if all_sample[k] in sample_1 and all_sample[k] not in val_rep_s1])
        return R
    return sum([i+1 for i in range(len(all_sample)) if all_sample[i] in sample_1])

def rangos(n, m, r):
    if n == 1 and m == 0:
        if r <= 0:
            return 0
        else:
            return 1
    elif n == 0 and m == 1:
        if r < 0:
            return 0
        else:
            return 1
    else:
        if n == 0:
            return rangos(0, m-1, r)
        elif m == 0:
            return rangos(n-1, 0, r-n)
        else:
            return n / (n+m) *rangos(n-1,m,r-n-m)+m/(n+m)*rangos(n,m-1,r)


def permutation(x):
    """
    Random permutation
    """
    N = len(x)

    for i in range(N-1, 0, -1):
        # Uniform in [0,i]
        index = udiscrete(0, i)
        tmp = x[index]
        x[index] = x[i]
        x[i] = tmp
    return x


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

def estimate_mu_sigma_normal(sample, n):
    n = len(sample)
    mu = sum(sample) / n
    sum_xi = sum([(value - mu) ** 2 for value in sample])

    return(mu, sqrt(sum_xi / n))



def estimate_p_binomial(sample, n):
    return (sum(sample) / len(sample)) / n


def estimate_lamda_exponential(sample, n):
    return (len(sample) / sum(sample))


def nCr(n,r):
    return factorial(n) / factorial(r) / factorial(n-r)


def binomial(n, p):
    return [binomial_pi(n, p, i) for i in range(n + 1)]


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
