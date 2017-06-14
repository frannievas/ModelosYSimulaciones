from functions import var_sample, udiscrete


def experiment(sample, N):
    var_empirical = var_sample(sample)
    n = len(sample)
    var = 0

    for _ in range(N):
        values = [sample[udiscrete(0, n - 1)] for _ in range(n)]
        mean_tmp = sum(values) / n

        var_tmp = 0
        for value in values:
            var_tmp += (value - mean_tmp) ** 2
        var_tmp /= (n - 1)

        var += (var_tmp - var_empirical) ** 2
    return var / N


if __name__ == '__main__':
    """
    Enunciado: Ejercicio 7. Sean X1 , ... , Xn variables aleatorias
    independientes e idénticamente distribuías con varianza σ2 desconocida.
    Se planea estimar σ2 mediante la varianza muestral
    """
    VALUES = [1, 3]
    ITER = 1000

    print("Formula normal")
    print("Estimación de varianza: {}".format(experiment(VALUES, ITER)))
