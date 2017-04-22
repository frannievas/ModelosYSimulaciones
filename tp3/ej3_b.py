from random import random
N = [1000, 10000,100000, 1000000]

for n in N:
    tita = 0
    for i in range(n):
        x = random()
        tita += ((1. / x ** 3 ) - (1. / x ** 2 )) / ( ( (1. / x ** 2 ) - (2. / x ) + 2. ) ** 2 ) 
    tita = tita / n
    print("N:{} Tita:{}".format(n, tita))
