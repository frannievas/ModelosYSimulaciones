from random import random
from math import exp, log2


def exponential(lamda):
    """
    Exponential distribution with lambda parameter
    """
    return - (1/lamda) * log2(random())


def h(x):
    return (x * exp(-(x / 2)) * exp(1)) / 2


def acceptRejection():
    Y = exponential(1/2)
    U = random()

    while U >= h(Y):
        Y = exponential(1/2)
        U = random()

    return Y


if __name__ == '__main__':
    print(acceptRejection())
