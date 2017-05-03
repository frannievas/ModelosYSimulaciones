from random import random
from math import sqrt

def experiment():
    u = random()
    if u < 3/4:
        return 6 + 6 * sqrt((1/3) - (1/3) * u)
    else:
        return 2 + 2 * sqrt(u)

if __name__ == '__main__':
    print(experiment())
