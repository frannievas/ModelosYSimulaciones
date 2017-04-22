from random import random
N = [1000, 10000,100000, 1000000]

for n in N:
    tita = 0
    for i in range(n):
        tita += (1. - random() ** 2) ** (3/2)
    tita = tita / n
    print("N:{} Tita:{}".format(n, tita))
