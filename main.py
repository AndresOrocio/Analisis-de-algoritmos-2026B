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
                "El maximo debe ser mayor o igual al elemento inicial."
            )

        # Para la version recursiva conviene no usar valores demasiado grandes.
        if elementos_maximos > 40:
            raise ValueError(
                "Para esta comparacion usa un maximo de 40 o menor."
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
            f"Ocurrio un error:\n{e}"
        )


ventana = tk.Tk()

ventana.title(
    "Comparacion de Fibonacci"
)

ventana.geometry("550x500")


titulo = tk.Label(
    ventana,
    text="Comparacion de Fibonacci",
    font=("Arial", 20)
)

titulo.pack(pady=25)


subtitulo = tk.Label(
    ventana,
    text="Con y sin Programacion Dinamica",
    font=("Arial", 12)
)

subtitulo.pack(pady=5)


etiqueta_inicial = tk.Label(
    ventana,
    text="N inicial:",
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
    text="N maximo:",
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
    text="Ejecutar comparacion",
    font=("Arial", 12),
    command=ejecutar
)

boton.pack(pady=30)


ventana.mainloop()
