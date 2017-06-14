from functions import range_sample, rangos, range_normal, range_simulation


if __name__ == '__main__':
    """
    Enunciado:
    Catorce ciudades, aproximadamente del mismo tamaño, se eligen para un
    estudio de seguridad vial. Siete de ellas se eligen al azar y durante un
    mes aparecen en los periódicos locales artículos relativos a la seguridad
    vial. Los números de accidentes de tránsito del mes posterior a la campaña
    son los siguientes:

    Grupo de tratamiento: 19 31 39 45 47 66 75
    Grupo de control: 28 36 44 49 52 72 72

    a) Calcular el p−valor exacto de este conjunto de datos, correspondiente a
       la hipótesis de que en ambos grupos se tienen resultados idénticos
       (es decir, los artículos no tuvieron ningún efecto).
    b) Calcular el p−valor aproximado en base a una aproximación normal,
    c) Calcular el p−valor aproximado en base a una simulación.
    """

    # Sample1 es mas chica
    sample_1 = [19, 31, 39, 45, 47, 66, 75]
    sample_2 = [28, 36, 44, 49, 52, 72, 72]

    r = range_sample(sample_1, sample_2)
    print("Rango: {}".format(r))

    n = len(sample_2)
    m = len(sample_1)

    p_value_1 = rangos(n, m, r)
    print("a) p-valor exacto")
    print("P_Value: {}\n".format(p_value_1))
    Iter = 10000

    p_value_2 = range_normal(n, m, r)
    print("b) p-valor normal")
    print("P_Value: {}\n".format(p_value_2))

    N = 10000
    p_value_3 = range_simulation(sample_1, sample_2, r, N)
    print("b) p-valor simulación")
    print("P_Value: {}\n".format(p_value_3))
