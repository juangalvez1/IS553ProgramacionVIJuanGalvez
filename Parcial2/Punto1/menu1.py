from .sistemaGestor import *
from .datos import *

def MostrarMenu():
    print("\n" + "=" * 54)
    print("\t  SISTEMA DE ALQUILER DE VEHÍCULOS")
    print("=" * 54)
    print("  1. Cargar datos desde archivo JSON")
    print("  2. Guardar estado actual en archivo JSON")
    print("  3. Ver todos los vehículos")
    print("  4. Ver vehículos disponibles")
    print("  5. Ver vehículos alquilados")
    print("  6. Alquilar un vehículo")
    print("  7. Devolver un vehículo")
    print("  8. Calcular costo de alquiler")
    print("  9. Agregar nuevo vehículo")
    print("-" * 54)
    print("  0. Salir")
    print("=" * 54)

def Menu1():
    sistema = SistemaAlquiler()

    # Esto es para ingresar por primera vez los vehiculos que estan en el archivo 'datos.py'

    # listaVehiculos = []

    # for lista in vehiculos.values():
    #     listaVehiculos.extend(lista)

    # for v in listaVehiculos:
    #     sistema.agregarVehiculo(v)

    while True:
        MostrarMenu()
        opcion = input("  Selecciona una opción: ").strip()

        if opcion == "1":
            print("\n    ADVERTENCIA: Al cargar el archivo, el estado actual en memoria")
            print("    se perderá. Asegúrate de haber guardado antes si tienes cambios.")
            respuesta = input("    ¿Deseas continuar con la carga? (s/n): ").strip().lower()

            if respuesta != "s":
                print("   Carga cancelada.")
                continue
            cargados = sistema.cargarVehiculos()
            print(f"    {cargados} vehículo(s) cargados en memoria.")

        elif opcion == "2":
            sistema.guardarVehiculos()

        elif opcion == "3":
            sistema.mostrarTodos()

        elif opcion == "4":
            sistema.mostrarDisponibles()

        elif opcion == "5":
            sistema.mostrarAlquilados()

        elif opcion == "6":
            placa = PedirPlaca()
            dias  = PedirDias()
            try:
                sistema.alquilarVehiculo(placa, dias)
            except (KeyError, ValueError) as error:
                print(f"{error}")

        elif opcion == "7":
            placa = PedirPlaca()
            try:
                sistema.devolverVehiculo(placa)
            except (KeyError, ValueError) as error:
                print(f"{error}")

        elif opcion == "8":
            placa = PedirPlaca()
            dias  = PedirDias()
            try:
                sistema.calcularCosto(placa, dias)
                sistema.calcular
            except KeyError as error:
                print(f"{error}")

        elif opcion == "9":
            vehiculoNuevo = CrearNuevoVehiculo()
            sistema.agregarVehiculo(vehiculoNuevo)

        # Prueba de la funcion de este punto que se usa en el punto 4 del parcial

        # elif opcion == "10":
        #     sistema.vehiculoCostoso()

        elif opcion == "0":
            print("\n  ¡Hasta luego!\n")
            break

        else:
            print("\tOpción no válida. Intenta de nuevo.")


# Menu1()