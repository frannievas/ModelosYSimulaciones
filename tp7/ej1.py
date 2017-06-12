from functions import stadistic, rejection, simulation
from scipy.special import chdtrc
from random import random


def F():
    u = random()
    if u <= 1/4:
        return 1
    elif u <= (1/4) + (1/2):
        return 2
    else:
        return 3


if __name__ == '__main__':
    """
    Enunciado: De acuerdo con la teoría genética de Mendel, cierta planta de
    guisantes debe producir flores blancas, rosas o rojas con probabilidad
    1/4, 1/2 y 1/4, respectivamente. Para verificar experimentalmente la
    teoría, se estudió una muestra de 564 guisantes, donde se encontró que 141
    produjeron flores blancas, 291 flores rosas y 132 flores rojas.
    Aproximar el p−valor de esta muestra:

    a) utilizando un aproximación ji-cuadrada,
    b) realizando una simulación.
    """

    # a)
    probs = [1/4, 1/2, 1/4]
    frecuency = [141, 291, 132]
    n = sum(frecuency)
    T = stadistic(probs, frecuency, n)
    k = 3
    
    print("a)")
    print("==========")
    print("Estadisitico: {}".format(T))
    # Tomar chi_cuadrado con k-1 grados de libertad
    p_value = chdtrc(k-1, T)
    print("P-Valor ji-cuadrada: {}".format(p_value))
    alpha = 0.05
    rejection(p_value, alpha)

    # b)
    print("b)")
    print("==========")
    ITER = 1000
    p_value_simulation = simulation(n, ITER, T, k, probs, F)
    print("P-Valor simulacion: {}".format(p_value_simulation))
    rejection(p_value_simulation, alpha)
