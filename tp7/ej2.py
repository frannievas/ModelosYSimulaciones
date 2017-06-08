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
    Enunciado: Para verificar que cierto dado no estaba trucado, se registraron
    1000 lanzamientos, resultando que el número de veces que el dado arrojó
    el valor i (i = 1, 2, 3, 4, 5, 6) fue, respectivamente, 158, 172, 164,
    181, 160, 165. Aproximar el p−valor de la prueba: “el dado es honesto”

    a) utilizando un aproximación ji-cuadrada,
    b) realizando una simulación.
    """

    # a)
    probs = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
    frecuency = [158, 172, 164, 181, 160, 165]
    n = sum(frecuency)
    T = stadistic(probs, frecuency, n)
    print("a)")
    print("==========")
    print("Estadisitico: {}".format(T))
    k = 6
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
