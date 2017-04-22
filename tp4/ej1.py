from random import random

DECK = list(range(1, 101))
N = 100
ITER = 100


def udiscrete(m, k):
    """
    Uniform discrete variable in interval [m, k]
    """
    u = random()
    return int(u*(k-m+1))+m

def permutation(x):
    """
    Random permutation
    """
    for i in range(N-1,0,-1):
        # Uniform in [0,i]
        index = udiscrete(0, i)
        tmp = x[index]
        x[index] = x[i]
        x[i] = tmp
    return x

def experiment():
    """
    Shuffles a deck of size n = 100, and draw a card one by one.
    Success: If the i-th card is the card N° = i
    """
    shuffle_deck = permutation(DECK)
    success = [1 for i in range(len(shuffle_deck)) if shuffle_deck[i] == i + 1]

    return sum(success)

if __name__ == '__main__':

    # Estimate the mean of the succes experiments
    success = []
    for i in range(ITER):
        success.append(experiment())
    mean = sum(success) / ITER
    print("Mean: {}".format(mean))

    # Estimate the mean of the succes experiments
    success = []
    for i in range(ITER):
        success.append(experiment() ** 2)
    mean2 = sum(success) / ITER
    print("Mean2: {}".format(mean2))

    varianza = mean2 -  (mean ** 2)
    print("varianza: {}".format(varianza))
