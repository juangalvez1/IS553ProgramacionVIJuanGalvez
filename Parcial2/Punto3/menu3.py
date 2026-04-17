from .inventario import *
from .datos import *

def MostrarMenu():
    print("\n" + "=" * 54)
    print("\t  SISTEMA DE TIENDA TECNOLOGICA")
    print("=" * 54)
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Vender producto")
    print("4. Reabastecer producto")
    print("5. Consultar producto")
    print("-" * 54)
    print("  0. Salir")
    print("=" * 54)

def Menu3(inventario):
    # inventario = Inventario()
    
    # Esto es para ingresar por primera vez los productos que estan en el archivo 'datos.py'

    # listaProductos = []

    # for lista in productos.values():
    #     listaProductos.extend(lista)

    # for p in listaProductos:
    #     inventario.registrarProducto(p)
    
    while True:
        # print("{")
        # for p in inventario.productos.values():
        #     print(p)
        # print("}")

        MostrarMenu()
        opcion = input("  Selecciona una opción: ").strip()

        if opcion == "1":
            codigo = int(input("Código: "))
            nombre = input("Nombre: ")

            try:
                precio = float(input("Precio: "))
                if precio <= 0:
                    print("Precio inválido")
                    continue
            except:
                print("Precio inválido")
                continue

            try:
                cantidad = int(input("Cantidad: "))
                if cantidad <= 0:
                    print("Cantidad inválida")
                    continue
            except:
                print("Cantidad inválida")
                continue

            tipo = input("\nTipo \n1. Computador\n2. Celular\n3. Accesorio\nOpción: ")
            print()

            if tipo == "1":
                ram = input("RAM (GB): ")
                cpu = input("CPU: ")
                producto = Computador(codigo, nombre, precio, cantidad, ram, cpu)

            elif tipo == "2":
                almacenamiento = input("Almacenamiento (GB): ")
                camaras = input("Numero de camaras: ")
                producto = Celular(codigo, nombre, precio, cantidad, almacenamiento, camaras)

            elif tipo == "3":
                categoria = input("Categoria del accesorio: ")
                producto = Accesorio(codigo, nombre, precio, cantidad, categoria)

            else:
                print("Opción no válida")
                continue

            inventario.registrarProducto(producto)

        elif opcion == "2":
            inventario.mostrarInventario()

        elif opcion == "3":
            codigo = int(input("Código del producto a vender: "))
            try:
                cantidad = int(input("Cantidad a vender: "))
                if cantidad <= 0:
                    print("Cantidad inválida")
                    continue
            except:
                print("Cantidad inválida")
                continue

            inventario.venderProducto(codigo, cantidad)

        elif opcion == "4":
            codigo = int(input("Código: "))
            try:
                cantidad = int(input("Cantidad: "))
                if cantidad <= 0:
                    print("Cantidad inválida")
                    continue
            except:
                print("Cantidad inválida")
                continue

            inventario.reabastecer(codigo, cantidad)

        elif opcion == "5":
            codigo = int(input("Código: "))
            inventario.consultarProducto(codigo)

        # Probando funcion del punto 4
        # elif opcion == "6":
        #     CategoriaMasVendida(inventario)

        elif opcion == "0":
            print("\n  ¡Hasta luego!\n")
            break

        else:
            print("Opción no válida")


# Menu3()