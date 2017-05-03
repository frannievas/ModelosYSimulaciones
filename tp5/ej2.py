from random import random
from math import log2


def experiment(beta, alpha):

    return (-log2(random()) / alpha) ** (1/beta)
