def normal_estandar():
    while True:
        Y1 = -log2(random())
        Y2 = -log2(random())
        if Y2 >= (Y1 - 1) ** 2:
            return Y1


def S(Xi, X):
    result = [(i - X) ** 2 for i in Xi]
    return sum(result) / (len(Xi) - 1)

def experiment():
