import tkinter as tk

def saludar():
    nombre = entrada.get().strip()
    if not nombre:
        nombre = "mundo"
    lbl.config(text = f"Hola, {nombre}")

root = tk.Tk()
root.title("Saludador de compas")
root.geometry("360x220")

#Crear etiqueta
lbl = tk.Label(root, text = "Hola, escribe your name y presiona el boton")
lbl.pack(pady = 60)
entrada = tk.Entry(root)

#Entrada de texto
entrada.pack(pady = 5)

#Creacion de boton
btn = tk.Button(root, text = "Saludar", command = saludar)
btn.pack(pady = 10)

root.mainloop()