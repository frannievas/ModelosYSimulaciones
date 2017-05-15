from random import random
from math import exp

N = 10000
ITER = 100


def udiscrete(m, k):
    """
    Uniform discrete variable in interval [m, k]
    """
    u = random()
    return int(u*(k-m+1))+m


def experiment():
    s = [exp(udiscrete(1, N) / N) for x in range(ITER)]
    return (sum(s) / ITER) * N


def real_value():
    s = [exp(x/N) for x in range(1, N+1)]
    return sum(s)


if __name__ == '__main__':
    s = experiment()
    r = real_value()
    print("Estimate: {}".format(s))
    print("Real value: {}".format(r))
    print("Diference: {}".format(abs(r-s)))
