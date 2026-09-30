import time
import tracemalloc
import matplotlib.pyplot as plt

from Fibonacci1 import fibonacci
from Fibonacci2 import fibonacci_dp


def medir_tiempo_y_espacio(algoritmo, n):
    """
    Mide el tiempo de ejecucion y la memoria pico utilizada.
    """
    tracemalloc.start()

    inicio = time.perf_counter()
    resultado = algoritmo(n)
    fin = time.perf_counter()

    memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tiempo = fin - inicio
    memoria_kb = memoria_pico / 1024

    return resultado, tiempo, memoria_kb


def ejecutar_pruebas(elemento_inicial, incremento, elementos_maximos):
    """
    Genera los valores de N y mide tiempo y espacio
    para Fibonacci con y sin programacion dinamica.
    """

    N = []

    tiempos_sin_dp = []
    espacios_sin_dp = []

    tiempos_dp = []
    espacios_dp = []

    for n in range(
        elemento_inicial,
        elementos_maximos + 1,
        incremento
    ):
        N.append(n)

        _, tiempo, espacio = medir_tiempo_y_espacio(
            fibonacci, n
        )
        tiempos_sin_dp.append(tiempo)
        espacios_sin_dp.append(espacio)

        _, tiempo, espacio = medir_tiempo_y_espacio(
            fibonacci_dp, n
        )
        tiempos_dp.append(tiempo)
        espacios_dp.append(espacio)

    print("\nTAMAÑOS DE N:")
    print(N)

    print("\nTIEMPOS SIN PROGRAMACION DINAMICA:")
    print(tiempos_sin_dp)

    print("\nTIEMPOS CON PROGRAMACION DINAMICA:")
    print(tiempos_dp)

    print("\nESPACIO SIN PROGRAMACION DINAMICA (KB):")
    print(espacios_sin_dp)

    print("\nESPACIO CON PROGRAMACION DINAMICA (KB):")
    print(espacios_dp)

    return (
        N,
        tiempos_sin_dp,
        espacios_sin_dp,
        tiempos_dp,
        espacios_dp
    )


def grafica_resultados_dp(N, tiempos_dp, espacios_dp):
    """
    Punto 2 de la actividad:
    resultados de Fibonacci con programacion dinamica,
    mostrando tiempo y espacio.
    """

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(
        N,
        tiempos_dp,
        marker="o",
        label="Con P. Dinamica"
    )
    plt.xlabel("N")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Tiempo de ejecucion")
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(
        N,
        espacios_dp,
        marker="o",
        label="Con P. Dinamica"
    )
    plt.xlabel("N")
    plt.ylabel("Memoria pico (KB)")
    plt.title("Uso de memoria")
    plt.legend()
    plt.grid(True)

    plt.suptitle(
        "Fibonacci con Programacion Dinamica",
        fontsize=14
    )
    plt.tight_layout()
    plt.show()


def grafica_comparativa(N, tiempos_sin_dp, espacios_sin_dp,
                        tiempos_dp, espacios_dp):
    """
    Punto 3 de la actividad:
    comparacion de Fibonacci con y sin programacion dinamica,
    mostrando tiempo y espacio.
    """

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)

    plt.plot(
        N,
        tiempos_sin_dp,
        marker="o",
        label="Sin P. Dinamica"
    )

    plt.plot(
        N,
        tiempos_dp,
        marker="o",
        label="Con P. Dinamica"
    )

    plt.xlabel("N")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparacion de tiempo")
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)

    plt.plot(
        N,
        espacios_sin_dp,
        marker="o",
        label="Sin P. Dinamica"
    )

    plt.plot(
        N,
        espacios_dp,
        marker="o",
        label="Con P. Dinamica"
    )

    plt.xlabel("N")
    plt.ylabel("Memoria pico (KB)")
    plt.title("Comparacion de espacio")
    plt.legend()
    plt.grid(True)

    plt.suptitle(
        "Comparacion de Fibonacci: con y sin Programacion Dinamica",
        fontsize=14
    )
    plt.tight_layout()
    plt.show()


def ejecutar_benchmark(
    elemento_inicial,
    incremento,
    elementos_maximos
):
    """
    Ejecuta las pruebas y genera las graficas.
    """

    resultados = ejecutar_pruebas(
        elemento_inicial,
        incremento,
        elementos_maximos
    )

    N = resultados[0]
    tiempos_sin_dp = resultados[1]
    espacios_sin_dp = resultados[2]
    tiempos_dp = resultados[3]
    espacios_dp = resultados[4]

    # Grafica correspondiente al punto 2.
    grafica_resultados_dp(
        N,
        tiempos_dp,
        espacios_dp
    )

    # Graficas correspondientes al punto 3.
    grafica_comparativa(
        N,
        tiempos_sin_dp,
        espacios_sin_dp,
        tiempos_dp,
        espacios_dp
    )


if __name__ == "__main__":
    ejecutar_benchmark(5, 5, 35)
