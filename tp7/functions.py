from collections import Counter
from random import random
from math import log2, log, sqrt, factorial, exp
from scipy.special import ndtr
from scipy.stats import binom


"""
======= 2 MUESTRAS =========
"""
def range_simulation(sample_1, sample_2, r, N):
    n, m, sample_1, sample_2 = correct_order(sample_1, sample_2)
    all_sample = sample_1 + sample_2
    success_min = 0
    success_max = 0

    for _ in range(N):
        per = permutation(all_sample)
        R = Range(sample_1, sample_2, per)

        if R >= r:
            success_max += 1
        if R <= r:
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

#
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


def correct_order(sample_1, sample_2):
    """
    Dadas dos muestras, la función devuelve el arreglo menor y su longitud en
    las variables sample_1 y n y el mayor con su longitud en sample_2, m
    respectivamente.
    """

    if len(sample_1) > len(sample_2):
        tmp = sample_1
        sample_1 = sample_2
        sample_2 = tmp

    return(len(sample_1), len(sample_2), sample_1, sample_2)


def Range(sample_1, sample_2, sample=None):
    """
    Calcula el rango de una muestra aleatoria, para los casos en los que haya
    o no repeticiones.
    """
    R, repetitions_values = 0, []

    if sample is None:
        sample = sample_1 + sample_2
        sample.sort()

    _, _, sample_1, sample_2 = correct_order(sample_1, sample_2)
    repetitions = [(sample.index(value), counter, value) for value, counter in
                   Counter(sample).items() if counter > 1]

    if len(repetitions) > 0:
        for index, count, value in repetitions:
            repetitions_values.append(value)
            R += sum([j for j in range(index + 1, index + count + 1)]) / count

    R += sum([(i + 1) for i in range(len(sample)) if sample[i] in sample_1 and
             sample[i] not in repetitions_values])

    return(R)


def range_rec(n, m, r):
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
            return range_rec(0, m-1, r)
        elif m == 0:
            return range_rec(n-1, 0, r-n)
        else:
            return n / (n+m) *range_rec(n-1,m,r-n-m)+m/(n+m)*range_rec(n,m-1,r)


def range_small(n, m, r):
    return 2 * min(1 - range_rec(n, m, r - 1), range_rec(n, m, r))

"""
================= ESTIMAR PARAMETROS ==========================
"""


def estimate_mu_sigma_normal(sample):
    n = len(sample)
    mu = sum(sample) / n
    sum_xi = sum([(value - mu) ** 2 for value in sample])

    return(mu, sqrt(sum_xi / n))


def estimate_p_binomial(sample, n):
    return (sum(sample) / len(sample)) / n


def estimate_lamda_exponential(sample, n):
    return (len(sample) / sum(sample))


"""
========== D_SAMPLE Y P_VALUES GENERICO ==========
"""

def p_value(n, Iter, d):
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

        Di = max(D_values)
        if Di >= d:
            success += 1

    return success / Iter


"""
========== D_SAMPLE Y P_VALUES  NORMAL, EXPONENTIAL ==========
"""


def d_value_normal(sample, mu, sigma):
    n = len(sample)
    D1 = max([((i+1)/n) - ndtr((sample[i] - mu) / sigma) for i in range(n)])
    D2 = max([ndtr((sample[i] - mu) / sigma) - (i/n) for i in range(n)])
    return max(D1, D2)


def p_value_normal(n, ITER, d, mu, sigma):
    """
    Calcula el p_valor partiendo de mu, sigma de una muestra original
    Y estima el parametro en cada iteracion
    """
    success = 0

    for _ in range(ITER):
        distribution = [normal(mu, sigma) for _ in range(n)]
        distribution.sort()
        mu_new, sigma_new = estimate_mu_sigma_normal(distribution)

        D = d_value_normal(distribution, mu_new, sigma_new)

        if D >= d:
            success += 1

    return success / ITER


def expAcum(x, lamda):
    return 1 - exp(-lamda * x)


def d_value_exponential(sample, lamda):
    n = len(sample)
    D1 = max([((i+1)/n) - expAcum(sample[i], lamda) for i in range(n)])
    D2 = max([expAcum(sample[i], lamda) - (i/n) for i in range(n)])
    return max(D1, D2)


def p_value_exponential(n, ITER, d, lamda):
    """
    Calcula el p_valor partiendo de lamda de una muestra original
    Y estima el parametro en cada iteracion
    """
    success = 0

    for _ in range(ITER):
        distribution = [exponential(lamda) for _ in range(n)]
        # XXX: BIQUERFUL! HAY QUE ORDENAR
        distribution.sort()
        lamda_new = estimate_lamda_exponential(distribution, n)

        D = d_value_exponential(distribution, lamda_new)

        if D >= d:
            success += 1

    return success / ITER


"""
==========  VIEJAS ==========
"""


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

"""
==========  === ==========
"""


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


def nCr(n,r):
    return factorial(n) / factorial(r) / factorial(n-r)


def binomial(n, p):
    return [binomial_pi(n, p, i) for i in range(n + 1)]


def binomial_pi(n, p, i):
  return binom.pmf(i, n, p)
    # return nCr(n, i) * (p**i) * ((1 - p) ** (n-i))


def Ni(sample):
    return list(Counter(sample).values())


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
        # XXX: No importa ordenar porque es la frecuencia absoluta
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


def mean_sample(Xi):
    """Calcula el promedio de los Xi"""
    return sum(Xi) / len(Xi)


def mean_rec(X, n, Xi):
    """
    :param X: Promedio con n-1 valores
    :param n:
    :param Xn: Valor n-esimo
    """
    return X + (Xi[n] - X) / (n + 1)


def var_sample(Xi):
    X = mean_sample(Xi)
    result = [(i - X) ** 2 for i in Xi]
    return sum(result) / (len(Xi) - 1)


def var_sample_rec(Xi):
    """
    Calcula la varianza muestral
    """
    S2 = 0
    X = Xi[0]
    for i in range(1, len(Xi)):
        Xnew = X + (Xi[i] - X) / (i + 1)
        Xnew = mean_rec(X, i, Xi)
        S2 = (1 - 1 / i) * S2 + (i + 1) * (Xnew - X) ** 2
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
