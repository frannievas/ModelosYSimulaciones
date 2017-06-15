from functions import Range, range_small, range_normal, range_simulation


if __name__ == '__main__':
    """
    Enunciado: Un experimento diseñado para comparar dos tratamientos contra la
    corrosión arrojó los siguientes datos (los cuales representan la máxima
    profundidad de los agujeros en unidades de milésima de pulgada) en pedazos
    de alambre sujetos a cada uno de los tratamientos por separado:

    Tratamiento 1: 65.2 67.1 69.4 78.4 74.0 80.3
    Tratamiento 2: 59.4 72.1 68.0 66.2 58.5

    a) Calcular el p−valor exacto de este conjunto de datos, correspondiente a
       la hipótesis de que ambos tratamientos tienen resultados idénticos.
    b) Calcular el p−valor aproximado en base a una aproximación normal,
    c) Calcular el p−valor aproximado en base a una simulación.
    """

    # Sample2 es mas chica
    sample_1 = [65.2, 67.1, 69.4, 78.4, 74.0, 80.3]
    sample_2 = [59.4, 72.1, 68.0, 66.2, 58.5]

    r = Range(sample_1, sample_2)
    print("Rango: {}".format(r))

    n = len(sample_2)
    m = len(sample_1)

    p_value_1 = range_small(n, m, r)
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
