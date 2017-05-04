from random import random
from math import log2, exp


def exponential(lamda):
    """
    Exponential distribution with lambda parameter
    """
    return - (1/lamda) * log2(random())


def experiment():
    return random() ** (1/ exponential(1))


if __name__ == '__main__':
    print(experiment())
