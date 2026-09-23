##########################################################
# MÓDULO 3: INTERFAZ GRÁFICA TKINTER
##########################################################

import tkinter as tk
from tkinter import messagebox

from benchmark import ejecutar_benchmark


def ejecutar():
    try:

        elemento_inicial = int(entrada_inicial.get())
        incremento = int(entrada_incremento.get())
        elementos_maximos = int(entrada_maximos.get())

       
        if elemento_inicial <= 0:
            raise ValueError(
                "El elemento inicial debe ser mayor que 0."
            )

        if incremento <= 0:
            raise ValueError(
                "El incremento debe ser mayor que 0."
            )

        if elementos_maximos < elemento_inicial:
            raise ValueError(
                "Los elementos máximos deben ser mayores "
                "o iguales al elemento inicial."
            )

        
        ejecutar_benchmark(
            elemento_inicial,
            incremento,
            elementos_maximos
        )

    except ValueError as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            f"Ocurrió un error:\n{e}"
        )




ventana = tk.Tk()

ventana.title(
    "Comparación de algoritmos de ordenamiento"
)

ventana.geometry("550x500")




titulo = tk.Label(
    ventana,
    text="Comparación de algoritmos",
    font=("Arial", 20)
)

titulo.pack(pady=25)


subtitulo = tk.Label(
    ventana,
    text="Fuerza bruta - 6 algoritmos",
    font=("Arial", 12)
)

subtitulo.pack(pady=5)



etiqueta_inicial = tk.Label(
    ventana,
    text="Elemento inicial:",
    font=("Arial", 11)
)

etiqueta_inicial.pack(pady=(20, 5))


entrada_inicial = tk.Entry(
    ventana,
    width=20,
    font=("Arial", 11)
)

entrada_inicial.pack()





etiqueta_incremento = tk.Label(
    ventana,
    text="Incremento:",
    font=("Arial", 11)
)

etiqueta_incremento.pack(pady=(15, 5))


entrada_incremento = tk.Entry(
    ventana,
    width=20,
    font=("Arial", 11)
)

entrada_incremento.pack()




etiqueta_maximos = tk.Label(
    ventana,
    text="Elementos máximos:",
    font=("Arial", 11)
)

etiqueta_maximos.pack(pady=(15, 5))


entrada_maximos = tk.Entry(
    ventana,
    width=20,
    font=("Arial", 11)
)

entrada_maximos.pack()



boton = tk.Button(
    ventana,
    text="Ejecutar comparación",
    font=("Arial", 12),
    command=ejecutar
)

boton.pack(pady=30)




ventana.mainloop()
