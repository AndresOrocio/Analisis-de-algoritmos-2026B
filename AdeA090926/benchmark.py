##########################################################
# MÓDULO 2: MEDICIÓN DE TIEMPOS Y GRÁFICA
##########################################################

import random
import time
import matplotlib.pyplot as plt

from ordenamientos import (
    selection_sort,
    bubble_sort_brute_force,
    insertion_sort,
    gnome_sort,
    stooge_sort,
    exchange_sort
)


def genera(n, minimo, maximo):
    """
    Genera una lista aleatoria de tamaño n.
    """
    lista = []

    for i in range(n):
        lista.append(random.randint(minimo, maximo))

    return lista


def medir_tiempo(algoritmo, lista):
    """
    Mide el tiempo que tarda un algoritmo
    en ordenar una lista.
    """

    inicio = time.time()

    algoritmo(lista)

    fin = time.time()

    return fin - inicio


def ejecutar_pruebas(elemento_inicial, incremento, elementos_maximos):
    """
    Genera las listas y mide los tiempos
    de los 6 algoritmos.
    """

    N = []

    # Lista de listas
    listas = []

    
    tiempos_selection = []
    tiempos_bubble = []
    tiempos_insertion = []
    tiempos_gnome = []
    tiempos_stooge = []
    tiempos_exchange = []

    
    for n in range(
        elemento_inicial,
        elementos_maximos + 1,
        incremento
    ):

        lista = genera(n, 1, 100)

        listas.append(lista)
        N.append(n)

    print("\nTAMAÑOS DE LAS LISTAS:")
    print(N)

    print("\nLISTA DE LISTAS:")
    print(listas)

   
    for lista in listas:

        tiempos_selection.append(
            medir_tiempo(selection_sort, lista)
        )

        tiempos_bubble.append(
            medir_tiempo(bubble_sort_brute_force, lista)
        )

        tiempos_insertion.append(
            medir_tiempo(insertion_sort, lista)
        )

        tiempos_gnome.append(
            medir_tiempo(gnome_sort, lista)
        )

        tiempos_stooge.append(
            medir_tiempo(stooge_sort, lista)
        )

        tiempos_exchange.append(
            medir_tiempo(exchange_sort, lista)
        )

    return (
        N,
        tiempos_selection,
        tiempos_bubble,
        tiempos_insertion,
        tiempos_gnome,
        tiempos_stooge,
        tiempos_exchange
    )


def grafica(
    N,
    tiempos_selection,
    tiempos_bubble,
    tiempos_insertion,
    tiempos_gnome,
    tiempos_stooge,
    tiempos_exchange
):
    """
    Genera la gráfica comparativa.
    """

    plt.figure(figsize=(10, 6))

    plt.plot(
        N,
        tiempos_selection,
        marker="o",
        label="Selection Sort"
    )

    plt.plot(
        N,
        tiempos_bubble,
        marker="o",
        label="Bubble Sort"
    )

    plt.plot(
        N,
        tiempos_insertion,
        marker="o",
        label="Insertion Sort"
    )

    plt.plot(
        N,
        tiempos_gnome,
        marker="o",
        label="Gnome Sort"
    )

   #plt.plot(
   #    N,
   #    tiempos_stooge,
   #    marker="o",
   #    label="Stooge Sort"
   #)

    plt.plot(
        N,
        tiempos_exchange,
        marker="o",
        label="Exchange Sort"
    )

    plt.xlabel("Número de elementos")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de algoritmos de ordenamiento")

    plt.legend()
    plt.grid(True)

    plt.show()


def ejecutar_benchmark(
    elemento_inicial,
    incremento,
    elementos_maximos
):
    """
    Ejecuta las pruebas y genera la gráfica.
    """

    resultados = ejecutar_pruebas(
        elemento_inicial,
        incremento,
        elementos_maximos
    )

    grafica(*resultados)


if __name__ == "__main__":

    ejecutar_benchmark(20, 20, 100)