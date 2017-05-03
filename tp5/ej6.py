from random import random


def raizN(n):
    return max([random() for x in range(n+1)])


def inverseTransform(n):
    return random() ** (1/n)


def acceptRejection(n):
    Y, U = random(), random()

    while U >= Y ** (n-1):
        Y, U = random(), random()

    return Y


if __name__ == '__main__':
    n = 100
    print(raizN(n))
    print(inverseTransform(n))
    print(acceptRejection(n))
