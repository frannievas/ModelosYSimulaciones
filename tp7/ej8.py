from functions import rejection, normal, estimate_mu_sigma_normal, d_value_normal, p_value_normal, p_value
from scipy.special import ndtr


if __name__ == '__main__':
    """
    Enunciado: Decidir si los siguientes datos corresponden a una distribución
    Normal:
    91.9 97.8 111.4 122.3 105.4 95.0 103.8 99.6 96.6 119.3 104.8 101.7.
    Calcular una aproximación del p-valor.
    """

    sample = [91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3,
              104.8, 101.7]
    sample.sort()

    n = len(sample)
    Iter = 10000
    mu, sigma = estimate_mu_sigma_normal(sample)

    d = d_value_normal(sample, mu, sigma)
    print("Estadisitico: {}".format(d))

    p_value_1 = p_value(n, Iter, d)
    print("P_Value (randoms): {}\n".format(p_value_1))
    rejection(p_value_1)

    p_value_2 = p_value_normal(n, Iter, d, mu, sigma)
    print("P_Value (normal): {}\n".format(p_value_2))
    rejection(p_value_2)
