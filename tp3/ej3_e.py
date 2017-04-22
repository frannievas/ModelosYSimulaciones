from random import random
from math import exp
N = [1000, 10000,100000, 1000000]

for n in N:
    tita = 0.0
    for i in range(n):
        x = random()
        y = random()
        tita += exp(-(x + y))
    tita = tita / n
    print("N:{} Tita:{}".format(n, tita))
