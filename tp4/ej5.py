from random import random


def p1():
    u = random()
    p = 1 / 2
    i = 1
    while u >= p:
        i += 1
        p += p * (1/2)

    return i


def p2():
    u = random()
    p = 2 / 6
    i = 1
    while u >= p:
        i += 1
        p += p * (2/3)

    return i


def experiment():
    u = random()
    if u < 0.5:
        return p1()
    else:
        return p2()


if __name__ == '__main__':
    print(experiment())
