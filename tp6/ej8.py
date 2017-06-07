from functions import Poisson, exponential


def simulation():
    # Guardamos los tiempos de atencion de c/ cliente
    customers = []

    # Tiempo de espera de cada cliente, para poder calcular los promedios
    time_wasted = []

    time = 0  # El dia termina cuando T = 8

    # Cantidad de clientes atendidos
    customers_attended = 0

    time_new_customer = exponential(4)
    atention_time = exponential(4.2)
    time += time_new_customer

    while time != 8:

        # Tiempo en que llega el nuevo cliente
        time_new_customer = exponential(4)
        time += time_new_customer

        # Tiempo que va a demorar en atender el nuevo cliente
        atention_time_new_customer = exponential(4.2)

        if len(customers) == 0:
            atention_time = atention_time_new_customer

        tmp_time = time_new_customer
        while tmp_time >= 0:

            if len(customers) == 0:
                break

            # Si alcance a atender a alguien en el tiempo que pasó
            if atention_time < tmp_time:
                tmp_time -= atention_time

                # Avanzar la fila
                atention_time = customers[0]
                customers.remove(customers[0])
            else:
                # Atendi un poco pero no termine
                atention_time -= tmp_time
                tmp_time = 0


        # Si hay 3 o menos clientes
        if customers <= 3:
            customers_attended += 1
            customers.append(atention_time_new_customer)

    return customers_attended

if __name__ == '__main__':
    """
    Enunciado: Considerar un sistema con un único servidor en el cual los clientes
    potenciales llegan de acuerdo con un proceso de Poisson de razón 4.0.
    Un cliente potencial entrará al sistema sólo si hay tres o menos clientes
    en el sistema al momento de su llegada. El tiempo de servicio de cada
    cliente está distribuído según una exponencial de parámetro 4.2.
    Despues del instante T = 8 no entran más clientes al sistema (los tiempos
    están dados en horas).
    Realizar un estudio de simulación para estimar el tiempo promedio que
    un cliente pasa en el sistema.
    Aplicar el método “bootstrap” para estudiar el error cuadrático medio de su
    estimador.
    """
