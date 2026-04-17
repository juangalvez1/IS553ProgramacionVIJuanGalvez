# from Punto1.menu1 import *
# from Punto2.menu2 import *
# from Punto3.menu3 import *

from Parcial2.Punto1.menu1 import *
from Parcial2.Punto2.menu2 import *
from Parcial2.Punto3.menu3 import *

def MostrarMenu():
    print("\n" + "=" * 54)
    print("\t  SISTEMA DE ATENCION DE CLINICA")
    print("=" * 54)
    print("1. Ejecutar Punto 1")
    print("2. Ejecutar Punto 2")
    print("3. Ejecutar Punto 3")
    print("4. Ver vehiculo mas costoso")
    print("5. Ver paciente mas critico")
    print("6. Ver categoria mas vendido")
    print("-" * 54)
    print("  0. Salir")
    print("=" * 54)


def Main():
    sistema1 = SistemaAlquiler()
    sistema2 = SistemaPacientes()
    sistema3 = Inventario()

    while True:
        MostrarMenu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            Menu1()

        elif opcion == "2":
            Menu2()

        elif opcion == "3":
            Menu3(sistema3)

        elif opcion == "4":
            sistema1.vehiculoCostoso()

        elif opcion == "5":
            sistema2.pacienteMasCritico()

        elif opcion == "6":
            CategoriaMasVendida(sistema3)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

Main()