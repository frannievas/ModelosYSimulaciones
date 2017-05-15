from random import random
from math import exp, log2

def exponential(lamda):
    """
    Exponential distribution with lambda parameter
    """
    return - (1/lamda) * log2(random())


def PoissonNoHomogenea(lamdaT, lamda, T):
    """
    :param l: lambda function
    """
    I = 0
    S = [0]
    t = 0

    while True:
        exp = exponential(lamda)
        if t + exp > T:
            break
        else:
            t = t + exp
        v = random()
        if v < (lamdaT(t) / lamda):
            I += 1
            S.append(t)

    return I, S

def lamdaT(t):
    return(3 + (4 / (t + 1)))


if __name__ == '__main__':
    lamda, T = 2, 5
    I, S = PoissonNoHomogenea(lamdaT, lamda, T)
    print("Las valores generados son: I = {}, \n S = {}".format(I, S))
