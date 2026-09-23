import tkinter as tk
from tkinter import messagebox
import random
import time

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ==========================================================
# SELECTION SORT
# ==========================================================

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# ==========================================================
# BUBBLE SORT
# ==========================================================

def bubble_sort_brute_force(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# ==========================================================
# GENERAR DATOS
# ==========================================================

def generar_datos(n):
    return [random.randint(1, 100000) for _ in range(n)]


# ==========================================================
# MEDIR TIEMPO
# ==========================================================

def medir_tiempo(algoritmo, datos):

    copia = datos.copy()

    inicio = time.perf_counter()

    algoritmo(copia)

    fin = time.perf_counter()

    return fin - inicio


# ==========================================================
# EJECUTAR ANÁLISIS
# ==========================================================

def ejecutar_analisis():

    try:

        # Obtener valores de la interfaz
        inicial = int(entrada_inicial.get())
        incremento = int(entrada_incremento.get())
        maximo = int(entrada_maximo.get())

        # Validaciones
        if inicial <= 0:
            messagebox.showerror(
                "Error",
                "El tamaño inicial debe ser mayor que 0."
            )
            return

        if incremento <= 0:
            messagebox.showerror(
                "Error",
                "El incremento debe ser mayor que 0."
            )
            return

        if maximo < inicial:
            messagebox.showerror(
                "Error",
                "El tamaño máximo debe ser mayor o igual "
                "al tamaño inicial."
            )
            return

        # ==================================================
        # CREAR TAMAÑOS DE ENTRADA
        # ==================================================

        tamanios = []

        n = inicial

        while n <= maximo:
            tamanios.append(n)
            n += incremento

        # ==================================================
        # LISTAS PARA TIEMPOS
        # ==================================================

        tiempos_selection = []
        tiempos_bubble = []

        # ==================================================
        # REALIZAR EXPERIMENTO
        # ==================================================

        for n in tamanios:

            # Misma entrada para ambos algoritmos
            datos = generar_datos(n)

            tiempo_selection = medir_tiempo(
                selection_sort,
                datos
            )

            tiempo_bubble = medir_tiempo(
                bubble_sort_brute_force,
                datos
            )

            tiempos_selection.append(
                tiempo_selection
            )

            tiempos_bubble.append(
                tiempo_bubble
            )

        # ==================================================
        # CALCULAR ASÍNTOTA O(n²)
        # ==================================================

        ultimo_n = tamanios[-1]

        c_selection = (
            tiempos_selection[-1]
            / (ultimo_n ** 2)
        )

        c_bubble = (
            tiempos_bubble[-1]
            / (ultimo_n ** 2)
        )

        asintota_selection = []

        asintota_bubble = []

        for n in tamanios:

            asintota_selection.append(
                c_selection * (n ** 2)
            )

            asintota_bubble.append(
                c_bubble * (n ** 2)
            )

        # ==================================================
        # LIMPIAR GRÁFICA ANTERIOR
        # ==================================================

        ax.clear()

        # ==================================================
        # GRAFICAR TIEMPOS REALES
        # ==================================================

        ax.plot(
            tamanios,
            tiempos_selection,
            marker="o",
            label="Selection Sort"
        )

        ax.plot(
            tamanios,
            tiempos_bubble,
            marker="o",
            label="Bubble Sort"
        )

        # ==================================================
        # GRAFICAR ASÍNTOTAS
        # ==================================================

        ax.plot(
            tamanios,
            asintota_selection,
            linestyle="--",
            label="O(n²) Selection"
        )

        ax.plot(
            tamanios,
            asintota_bubble,
            linestyle="--",
            label="O(n²) Bubble"
        )

        # ==================================================
        # CONFIGURACIÓN DE LA GRÁFICA
        # ==================================================

        ax.set_title(
            "Comparación de tiempos de ejecución"
        )

        ax.set_xlabel(
            "Tamaño de entrada n"
        )

        ax.set_ylabel(
            "Tiempo de ejecución (segundos)"
        )

        ax.legend()

        ax.grid()

        # Mostrar gráfica
        canvas.draw()

        # ==================================================
        # MOSTRAR RESULTADOS EN LA INTERFAZ
        # ==================================================

        resultados.delete(
            "1.0",
            tk.END
        )

        resultados.insert(
            tk.END,
            "RESULTADOS DEL EXPERIMENTO\n"
        )

        resultados.insert(
            tk.END,
            "=" * 60 + "\n"
        )

        resultados.insert(
            tk.END,
            "n\tSelection Sort\tBubble Sort\n"
        )

        resultados.insert(
            tk.END,
            "-" * 60 + "\n"
        )

        for i in range(len(tamanios)):

            resultados.insert(
                tk.END,
                f"{tamanios[i]}\t"
                f"{tiempos_selection[i]:.8f}\t"
                f"{tiempos_bubble[i]:.8f}\n"
            )

        resultados.insert(
            tk.END,
            "\nComplejidad teórica:\n"
        )

        resultados.insert(
            tk.END,
            "Selection Sort: O(n²)\n"
        )

        resultados.insert(
            tk.END,
            "Bubble Sort: O(n²)\n"
        )

    except ValueError:

        messagebox.showerror(
            "Error",
            "Introduce únicamente números enteros."
        )


# ==========================================================
# VENTANA PRINCIPAL
# ==========================================================

ventana = tk.Tk()

ventana.title(
    "Análisis de Algoritmos - Selection Sort vs Bubble Sort"
)

ventana.geometry("1100x750")


# ==========================================================
# TÍTULO
# ==========================================================

titulo = tk.Label(
    ventana,
    text="ANÁLISIS EXPERIMENTAL DE ALGORITMOS",
    font=("Arial", 18, "bold")
)

titulo.pack(
    pady=10
)


# ==========================================================
# FRAME PARA LOS DATOS
# ==========================================================

frame_entrada = tk.Frame(
    ventana
)

frame_entrada.pack(
    pady=10
)


# Tamaño inicial
tk.Label(
    frame_entrada,
    text="Tamaño inicial:",
    font=("Arial", 11)
).grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)

entrada_inicial = tk.Entry(
    frame_entrada,
    width=10
)

entrada_inicial.grid(
    row=0,
    column=1,
    padx=5
)


# Incremento
tk.Label(
    frame_entrada,
    text="Incremento:",
    font=("Arial", 11)
).grid(
    row=0,
    column=2,
    padx=5
)

entrada_incremento = tk.Entry(
    frame_entrada,
    width=10
)

entrada_incremento.grid(
    row=0,
    column=3,
    padx=5
)


# Tamaño máximo
tk.Label(
    frame_entrada,
    text="Tamaño máximo:",
    font=("Arial", 11)
).grid(
    row=0,
    column=4,
    padx=5
)

entrada_maximo = tk.Entry(
    frame_entrada,
    width=10
)

entrada_maximo.grid(
    row=0,
    column=5,
    padx=5
)


# ==========================================================
# BOTÓN
# ==========================================================

boton = tk.Button(
    ventana,
    text="EJECUTAR ANÁLISIS",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    command=ejecutar_analisis
)

boton.pack(
    pady=10
)


# ==========================================================
# RESULTADOS
# ==========================================================

resultados = tk.Text(
    ventana,
    height=8,
    width=90,
    font=("Courier", 10)
)

resultados.pack(
    pady=5
)


# ==========================================================
# CREAR FIGURA DE MATPLOTLIB
# ==========================================================

fig, ax = plt.subplots(
    figsize=(9, 4.5)
)


canvas = FigureCanvasTkAgg(
    fig,
    master=ventana
)

canvas.draw()

canvas.get_tk_widget().pack(
    fill=tk.BOTH,
    expand=True
)


# ==========================================================
# INICIAR INTERFAZ
# ==========================================================

ventana.mainloop()