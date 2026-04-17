import json
from .pacientes import *

direccionArchivo = r"Parcial2\Punto2\files\pacientes.json"

class SistemaPacientes:
    def __init__(self):
        self.pacientes = {}

    def __leerPaciente(self, tipo, data):
        tipo = tipo
        pacienteBase = (data["documento"], data["nombre"], data["edad"], data["estadoDeAtencion"])

        if tipo == "PacienteGeneral":
            return PacienteGeneral(*pacienteBase, data["nombreEps"])
        elif tipo == "PacientePrioritario":
            return PacientePrioritario(*pacienteBase, data["condicionEspecial"])
        elif tipo == "PacienteUrgencia":
            return PacienteUrgencia(*pacienteBase, data["nivelDeGravedad"])
    
    def guardarPacientes(self):
        datos = {"PacienteGeneral": [], "PacientePrioritario": [], "PacienteUrgencia": []}

        for paciente in self.pacientes.values():
            tipo = type(paciente).__name__
            if tipo in datos:
                datos[tipo].append(paciente.toDict())

        with open(direccionArchivo, "w", encoding="utf-8") as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)

        print(f"    Datos guardados correctamente en '{direccionArchivo}'.")

    def cargarPacientes(self):
        try:
            with open(direccionArchivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            print(f"    No se encontró '{direccionArchivo}'. Genera los datos primero (opción 2).")
            return
        except json.JSONDecodeError:
            print(f"    El archivo '{direccionArchivo}' tiene un formato inválido.")
            return
        
        self.pacientes.clear()
        cargados = 0

        for tipo, lista in datos.items():
            for p in lista:
                documento = p["documento"]

                if documento in self.pacientes:
                    print(f"    Documento duplicada '{documento}' ignorada.")
                    continue
                self.pacientes[documento] = self.__leerPaciente(tipo, p)
                cargados += 1

        return cargados

    def registrarPaciente(self, paciente):
        documento = paciente.documento

        if documento in self.pacientes:
            raise ValueError(f"Ya existe un Paciente con el documento '{documento}'.")
        self.pacientes[documento] = paciente
        print(f"    Paciente '{documento}' agregado correctamente.")

    def mostrarPacientes(self):
        if not self.pacientes:
            print("No hay pacientes registrados.")
            return
        for p in self.pacientes.values():
            print(p)

    def buscarPaciente(self, documento):
        paciente = self.pacientes.get(documento)

        if paciente is None:
            raise ValueError(f"\nNO hay ningun paciente con el documento '{documento}' en el sistema")

        return paciente

    def atenderPacienteSiguiente(self):
        orden = [PacienteUrgencia, PacientePrioritario, PacienteGeneral]
        for tipo in orden:
            pendientes = [p for p in self.pacientes.values() if isinstance(p, tipo) and p.estadoDeAtencion != "Atendido"]

            if not pendientes:
                continue

            if tipo == PacienteUrgencia:
                paciente = max(pendientes, key=lambda p: p.nivelDeGravedad)
            else:
                paciente = pendientes[0]

            paciente.estadoDeAtencion = "Atendido"
            print(f"Paciente {paciente.nombre} atendido exitosamente.")
            return

        print("No hay pacientes pendientes.")

    def pacienteMasCritico(self):
        self.cargarPacientes()
        urgencias = [p for p in self.pacientes.values() if isinstance(p, PacienteUrgencia)]

        if not urgencias:
            print("No hay pacientes de urgencias registrados.")
            return

        masCritico = max(urgencias, key=lambda p: p.nivelDeGravedad)

        print("\n--- PACIENTE MÁS CRÍTICO ---")
        print(masCritico)


def validarEdad(self, edad):
        return 0 <= edad <= 120


def IngresarNuevoPaciente():
    print("\n--- REGISTRAR PACIENTE ---")
    print("1) General  2) Prioritario  3) Urgencias")
    tipo = input("Seleccione el tipo: ").strip().lower()
    
    try:
        documento = int(input("Documento: "))
        nombre = input("Nombre: ").strip()
        edad = int(input("Edad: "))
    except ValueError:
        print("Error: documento y edad deben ser números enteros.")
        return
    
    if tipo == "1":
        eps = input("Nombre de la EPS: ").strip()
        paciente = PacienteGeneral(documento, nombre, edad, "Pendiente", eps)
    elif tipo == "2":
        condicion = input("Condición especial: ").strip()
        paciente = PacientePrioritario(documento, nombre, edad, "Pendiente", condicion)
    elif tipo == "3":
        print("\nNiveles de gravedad: 1, 2, 3, 4")
        print("Siendo 1 levemente grave y 4 muy grave")
        gravedad = int(input("Nivel de gravedad: "))
        paciente = PacienteUrgencia(documento, nombre, edad, "Pendiente", gravedad)
    else:
        print("Tipo inválido.")
        return
    return paciente