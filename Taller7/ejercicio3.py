import tkinter as tk

def ejemplo1():
    def cambiar_texto():
        etiqueta.config(text="¡Botón presionado!")

    ventana = tk.Tk()
    ventana.title("Ejemplo 2 - Botón")
    ventana.geometry("300x200")

    etiqueta = tk.Label(ventana, text="Texto inicial")
    etiqueta.pack()

    boton = tk.Button(ventana, text="Presionar", command=cambiar_texto)
    boton.pack()

    ventana.mainloop()

def ejemplo2():
    def calcular_area():
        base = float(entry_base.get())
        altura = float(entry_altura.get())

        if base > 0 and altura > 0:
            area = (base * altura) / 2
            resultado.config(text=f"Área del triángulo: {area}")
        else:
            resultado.config(text="Los valores deben ser positivos")

    ventana = tk.Tk()
    ventana.title("Calculadora de Área del triangulo")
    ventana.geometry("400x250")

    tk.Label(ventana, text="Base:").pack()
    entry_base = tk.Entry(ventana)
    entry_base.pack()

    tk.Label(ventana, text="Altura:").pack()
    entry_altura = tk.Entry(ventana)
    entry_altura.pack()

    tk.Button(ventana, text="Calcular", command=calcular_area).pack()

    resultado = tk.Label(ventana, text="")
    resultado.pack()

    ventana.mainloop()

def Main():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Ejecutar Ejemplo 1")
        print("2. Ejecutar Ejemplo 2")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejemplo1()
        elif opcion == "2":
            ejemplo2()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo")
Main()