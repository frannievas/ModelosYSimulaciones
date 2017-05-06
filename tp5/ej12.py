from random import random
from math import exp, log2


def PoissonNoHomogenea(lamdaT, lamda, T):
    """
    :param l: lambda function
    """
    I = 0
    S = [0]
    t = 0

    while True:
        exp = exponential(t)
        if t + exp > T:
            break
        else:
            t = t + exp
        v = random()
        if v < (lamdaT(t) / lamda):
            I += 1
            S.append(t)

    return I, S


if __name__ == '__main__':
    
