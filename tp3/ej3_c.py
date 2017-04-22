from random import random
from math import exp
N = [1000, 10000,100000, 1000000]

for n in N:
    tita = 0.0
    for i in range(n):
        x = random()
        tita += 2. * exp(- ( 1. / x - 1.) ** 2 )  / (x ** 2)
    tita = tita / n
    print("N:{} Tita:{}".format(n, tita))
