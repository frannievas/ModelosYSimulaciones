from random import random
from math import log


def experiment(beta, alpha):

    return (-log(random()) / alpha) ** (1/beta)

if __name__ == '__main__':
    print(experiment(3, 5))
