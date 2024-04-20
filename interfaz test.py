#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox

class TiendaConveniencia:
    def __init__(self, master):
        self.master = master
        master.title("Tienda de Conveniencia")

        self.label = tk.Label(master, text="Bienvenido a la Tienda de Conveniencia")
        self.label.pack()

        self.comprar_button = tk.Button(master, text="Comprar", command=self.comprar)
        self.comprar_button.pack()

        self.salir_button = tk.Button(master, text="Salir", command=master.quit)
        self.salir_button.pack()

    def comprar(self):
        top = tk.Toplevel(self.master)
        top.title("Compra")

        self.label = tk.Label(top, text="¿Qué deseas comprar?")
        self.label.pack()

        self.compra_entry = tk.Entry(top)
        self.compra_entry.pack()

        self.comprar_button = tk.Button(top, text="Realizar Compra", command=self.realizar_compra)
        self.comprar_button.pack()

    def realizar_compra(self):
        producto = self.compra_entry.get()
        # Lista de productos permitidos
        productos_permitidos = [
            "arma de alto calibre",
            "chalecos antibalas",
            "pistola 9mm",
            "arsenal móvil",
            "linterna táctica",
            "kit de supervivencia",
            "navaja suiza",
            "cuerda resistente",
            "botiquín de primeros auxilios",
            "radiocomunicador"
        ]

        if producto.lower() in productos_permitidos:
            mensaje = f"Compra realizada: {producto}"
            messagebox.showinfo("Compra Realizada", mensaje)
        else:
            mensaje = "Lo sentimos, este producto no está disponible en nuestra tienda."
            messagebox.showerror("Error", mensaje)

def main():
    root = tk.Tk()
    mi_tienda = TiendaConveniencia(root)
    root.mainloop()

if __name__ == "__main__":
    main()
