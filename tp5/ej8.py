from random import random
from math import log2, sqrt


def normal(mu, sigma):
    while True:
        Y1 = -log2(random())
        Y2 = -log2(random())
        if Y2 >= (Y1 - 1) ** 2:
            break
    if random() < 0.5:
        return Y1 * sigma + mu
    else:
        return -Y1 * sigma + mu


def polar():
    # Generar un punto aleatorio en el circulo unitario
    while True:
        V1, V2 = random(), random()
        if V1 ** 2 + V2 ** 2 <= 1:
            break
    S = V1 ** 2 + V2 ** 2
    const = sqrt(-2 * log2(S)/S)
    X = V1 * const
    Y = V2 * const

    return (X, Y)

def normal_abs(z):
    u = random()
    if u <= 0.5:
        return z
    else:
        return -z

def experiment():
    N = 10000
    mu = 0
    sigma = 1

    print("")
    print("Experiment normal:")
    print("================")
    results = [normal(mu,sigma) for x in range(N)]
    mean = sum(results) / N
    print("Mean: {}".format(mean))

    results = [normal(mu,sigma) ** 2 for x in range(N)]
    mean2 = sum(results) / N
    print("Mean2: {}".format(mean2))

    variance = mean2 - mean ** 2
    sigma_estimated = sqrt(variance)
    print("Variance: {}".format(sigma_estimated))

def experiment_polar():
    N = 5000
    mu = 0
    sigma = 1

    print("")
    print("Experiment polar:")
    print("================")
    results = [ normal_abs(x[0]) + normal_abs(x[1]) for x in [polar() for _ in range(N)]]
    mean = sum(results) / N
    print("Mean: {}".format(mean))

    results = [ normal_abs(x[0]) ** 2 + normal_abs(x[1]) ** 2 for x in [polar() for _ in range(N)]]
    mean2 = sum(results) / N
    print("Mean2: {}".format(mean2))

    variance = mean2 - mean ** 2
    sigma_estimated = sqrt(variance)
    print("Variance: {}".format(sigma_estimated))


if __name__ == '__main__':
    experiment()
    experiment_polar()
