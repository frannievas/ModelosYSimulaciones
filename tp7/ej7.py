from functions import rejection, exponential, p_value
from functions import estimate_lamda_exponential, d_value_exponential, p_value_exponential
from math import exp


if __name__ == '__main__':
    """
    Enunciado: En un estudio de vibraciones, una muestra aleatoria de 15
    componentes del avión fueron sometidos a fuertes vibraciones hasta que se
    evidenciaron fallas estructurales. Los datos proporcionados son los minutos
    transcurridos hasta que se evidenciaron dichas fallas.
    1.6 10.3 3.5 13.5 18.4 7.7 24.3 10.7 8.4 4.9 7.9 12 16.2 6.8 14.7
    Pruebe la hipótesis nula de que estas observaciones pueden ser consideradas
    como una muestra de la población exponencial.
    """

    sample = [1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12,
              16.2, 6.8, 14.7]
    sample.sort()

    n = len(sample)
    Iter = 10000
    lamda = estimate_lamda_exponential(sample, n)

    d = d_value_exponential(sample, lamda)
    print("Estadisitico: {}".format(d))

    p_value_1 = p_value(n, Iter, d)
    print("P_Value (randoms): {}\n".format(p_value_1))
    rejection(p_value_1)

    p_value_2 = p_value_exponential(n, Iter, d, lamda)
    print("P_Value (exponential): {}\n".format(p_value_2))
    rejection(p_value_2)
