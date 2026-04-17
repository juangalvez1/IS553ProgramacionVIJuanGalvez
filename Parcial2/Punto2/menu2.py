from .sistema import *
from .datos import *

def MostrarMenu():
    print("\n" + "=" * 54)
    print("\t  SISTEMA DE ATENCION DE CLINICA")
    print("=" * 54)
    print("1. Registrar paciente")
    print("2. Mostrar todos los pacientes")
    print("3. Buscar paciente por documento")
    print("4. Atender siguiente paciente")
    print("5. Guardar en JSON")
    print("6. Cargar desde JSON")
    print("-" * 54)
    print("  0. Salir")
    print("=" * 54)

def Menu2():
    sistema = SistemaPacientes()

    #  Esto es para ingresar por primera vez los productos que estan en el archivo 'datos.py'
    # listaPacientes = []

    # for lista in pacientes.values():
    #     listaPacientes.extend(lista)

    # for p in listaPacientes:
    #     sistema.registrarPaciente(p)

    while True:
        MostrarMenu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            paciente = IngresarNuevoPaciente()
            sistema.registrarPaciente(paciente)

        elif opcion == "2":
            sistema.mostrarPacientes()

        elif opcion == "3":
            documento = int(input("Documento del paciente a buscar: "))
            try:
                paciente = sistema.buscarPaciente(documento)
                print(paciente)
            except (KeyError, ValueError) as error:
                print(f"{error}")

        elif opcion == "4":
            sistema.atenderPacienteSiguiente()

        elif opcion == "5":
            sistema.guardarPacientes()

        elif opcion == "6":
            print("\n    ADVERTENCIA: Al cargar el archivo, el estado actual en memoria")
            print("    se perderá. Asegúrate de haber guardado antes si tienes cambios.")
            respuesta = input("    ¿Deseas continuar con la carga? (s/n): ").strip().lower()

            if respuesta != "s":
                print("   Carga cancelada.")
                continue
            cargados = sistema.cargarPacientes()
            print(f"    {cargados} pacientes(s) cargados en memoria.")

        # probar la funcion del punto 4
        # elif opcion == "7":
        #     PacienteMasCritico(sistema)

        elif opcion == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

# Menu2()