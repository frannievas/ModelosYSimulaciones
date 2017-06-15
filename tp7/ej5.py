from functions import stadistic, rejection, Ni, binomial, binomial_naive
from functions import estimate_p_binomial
from scipy.special import chdtrc


def simulation(n, ITER, T, k, p):
    """
    :param n: Tamaño de las muestras
    :param ITER: Cantidad de iteraciones
    :param t: T = t, calculado con la muestra original
    :param k: Cantidad de valores que toma la variable aleatoria
    :param p: parametro de la binomial
    """
    success = 0

    for _ in range(ITER):

        distribution = [binomial_naive(8, p) for _ in range(n)]
        Ni = [distribution.count(i) for i in range(k)]

        pnew = estimate_p_binomial(distribution, n)
        Pi = binomial(8, pnew)

        if stadistic(Pi, Ni, n) >= T:
            success += 1

    return success / ITER


if __name__ == '__main__':
    """
    Enunciado: Calcular una aproximación del p−valor de la prueba de que los
    siguientes datos corresponden a una distribución binomial con parámetros
    (n = 8, p), donde p no se conoce:
    6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7.
    """

    sample = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
    n = len(sample)

    N = 8
    p = estimate_p_binomial(sample, N)
    print("Estimacion p: {}".format(p))

    Ni = Ni(sample)
    Pi = binomial(N, p)
    Pi.pop(0)
    T = stadistic(Pi, Ni, n)
    print("==========")
    print("Estadistico: {} \n".format(T))

    k = 9
    m = 1
    p_value = chdtrc(k-1-m, T)
    print("P-Valor ji-cuadrada: {}".format(p_value))
    rejection(p_value)

    # b)
    print("==========")
    ITER = 1000
    p_value_simulation = simulation(n, ITER, T, k, p)
    print("P-Valor simulacion: {}".format(p_value_simulation))
    rejection(p_value_simulation)
