#Capitulo 4. Ejercicio resuelto 7

import tkinter as tk
from tkinter import messagebox

def comparar_numeros():
    try:
        valor_a = float(entry_a.get())
        valor_b = float(entry_b.get())
        
        if valor_a > valor_b:
            resultado = "A es mayor que B"
        elif valor_a < valor_b:
            resultado = "A es menor que B"
        else:
            resultado = "A es igual a B"
        
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Ingrese números válidos.")

ventana = tk.Tk()
ventana.title("Comparar Números")

tk.Label(ventana, text="Ingrese el valor de A:").pack(padx=10, pady=5)
entry_a = tk.Entry(ventana)
entry_a.pack(padx=10, pady=5)

tk.Label(ventana, text="Ingrese el valor de B:").pack(padx=10, pady=5)
entry_b = tk.Entry(ventana)
entry_b.pack(padx=10, pady=5)

tk.Button(ventana, text="Comparar", command=comparar_numeros).pack(padx=10, pady=20)

ventana.mainloop()
