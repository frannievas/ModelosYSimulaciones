from functions import estadistic

if __name__ == '__main__':
    probs = [ 1/4, 1/2, 1/4]
    frecuency = [141, 291, 132]
    n = sum(frecuency)
    print(estadistic(probs, frecuency, n))

    # Tomar chi_cuadrado con k-1 grados de libertad
