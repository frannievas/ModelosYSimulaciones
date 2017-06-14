from functions import mean_sample, udiscrete


def experiment(sample, N, A, B):
    n = len(sample)
    success = 0
    sum_xi = 0
    avg_empirical = mean_sample(sample)

    for _ in range(N):
        sum_xi = sum([sample[udiscrete(0, n - 1)] for _ in range(n)])
        avg = sum_xi / n
        value = (avg - avg_empirical)

        if A < value < B:
            success += 1

    return success / N


if __name__ == '__main__':
    """
    Enunciado: Ejercicio 6. Sean X 1 , . . . , X n variables aleatorias
    independientes e idénticamente distribuías con media μ desconocida.
    Para a y b constantes dadas, a < b, nos interesa estimar
    P ( a < SUM(Xi)/n - μ < b)

    a) Explicar como utilizar el método “bootstrap” para estimar p.

    b) Estimar p asumiendo que para n = 10, los valores de las variables Xi
    resultan 56, 101, 78, 67, 93, 87, 64, 72, 80 y 69.
    Sean a = −5 y b = 5.
    """
    VALUES = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
    SORTED_VALUES = [56, 64, 67, 69, 72, 78, 80, 87, 93, 101]
    ITER = 1000
    A = -5
    B = 5

    print("Estimación de p: {}".format(experiment(VALUES, ITER, A, B)))
