from functions import avg_sample, udiscrete


def experiment(sample, N, A, B):
    n = len(sample)
    success = 0
    sum_xi = 0
    avg_empirical = avg_sample(sample)

    for _ in range(N):
        sum_xi = sum([sample[udiscrete(0, n - 1)] for _ in range(n)])
        avg = sum_xi / n
        value = (avg - avg_empirical)

        if A < value < B:
            success += 1

    return(success / N)


if __name__ == '__main__':
    VALUES = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
    SORTED_VALUES = [56, 64, 67, 69, 72, 78, 80, 87, 93, 101]
    ITER = 1000
    A = -5
    B = 5

    print("Estimación de p: {}".format(experiment(VALUES, ITER, A, B)))
