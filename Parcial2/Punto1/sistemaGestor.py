import json
from .vehiculos import *

direccionArchivo = r"Parcial2\Punto1\files\vehiculos.json"

class SistemaAlquiler:
    def __init__(self):
        # Diccionario que guarda todos los vehiculos de la empresa
        self.flota = {}

    def __leerVehiculo(self, tipo, data):
        # Del diccionario 'data' arma un objeto segun el tipo de vehiculo

        tipo = tipo.lower()
        vehiculoBase = (data["placa"], data["marca"], data["modelo"], data["precioPorDia"], data["disponible"])

        # El '*' desempaqueta la tupla y excluye el ultimo elemento
        if tipo == "automovil":
            return Automovil(*vehiculoBase[:-1], data["numeroPuertas"], vehiculoBase[-1])
        elif tipo == "motocicleta":
            return Motocicleta(*vehiculoBase[:-1], data["cilindraje"], vehiculoBase[-1])
        elif tipo == "camion":
            return Camion(*vehiculoBase[:-1], data["capacidadCarga"], vehiculoBase[-1])
        else:
            raise ValueError(f"Tipo de vehículo desconocido: '{tipo}'.")
        
    def __buscarVehiculo(self, placa):
        # Retorna el objeto que tenga la placa a buscar, o salta un eror si no existe
        vehiculo = self.flota.get(placa.upper())

        if vehiculo is None:
            raise ValueError(f"NO hay ningun vehiculo con la placa '{placa.upper()}' en el sistema")
        
        return vehiculo
    
    def guardarVehiculos(self):
        # Sobreescribe el JSON con el estado actual de la flota en memoria.

        datos = {"automovil": [], "motocicleta": [], "camion": []}

        for vehiculo in self.flota.values():
            tipo = type(vehiculo).__name__.lower()
            if tipo in datos:
                datos[tipo].append(vehiculo.toDict())

        with open(direccionArchivo, "w", encoding="utf-8") as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)

        print(f"    Datos guardados correctamente en '{direccionArchivo}'.")

    def cargarVehiculos(self):
        try:
            with open(direccionArchivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            print(f"    No se encontró '{direccionArchivo}'. Genera los datos primero (opción 2).")
            return
        except json.JSONDecodeError:
            print(f"    El archivo '{direccionArchivo}' tiene un formato inválido.")
            return
        
        self.flota.clear()
        cargados = 0
        
        for tipo, lista in datos.items():
            for v in lista:
                placa = v["placa"].upper()

                if placa in self.flota:
                    print(f"    Placa duplicada '{placa}' ignorada.")
                    continue
                self.flota[placa] = self.__leerVehiculo(tipo, v)
                cargados += 1

        return cargados

    def mostrarTodos(self):
        if not self.flota:
            print("    No hay vehículos registrados en el sistema.")
            return
        
        print(f"\n{'-' * 10} TODOS LOS VEHICULOS ({len(self.flota)}) {'-' * 10}")
        for vehiculo in self.flota.values():
            print(vehiculo)

    def mostrarDisponibles(self):
        disponibles = [v for v in self.flota.values() if v.disponible]
        if not disponibles:
            print("   No hay vehículos disponibles en este momento.")
            return
        print(f"\n{'─'*10} VEHÍCULOS DISPONIBLES ({len(disponibles)}) {'─'*10}")
        for vehiculo in disponibles:
            print(vehiculo)

    def mostrarAlquilados(self):
        alquilados = [v for v in self.flota.values() if not v.disponible]
        if not alquilados:
            print("   No hay vehículos alquilados en este momento.")
            return
        print(f"\n{'─'*10} VEHÍCULOS ALQUILADOS ({len(alquilados)}) {'─'*10}")
        for vehiculo in alquilados:
            print(vehiculo)

    def agregarVehiculo(self, vehiculo):
        placa = vehiculo.placa.upper()

        if placa in self.flota:
            raise ValueError(f"Ya existe un vehículo con la placa '{placa}'.")
        self.flota[placa] = vehiculo
        print(f"    Vehículo '{placa}' agregado correctamente.")

    def alquilarVehiculo(self, placa, dias):
        # Valida que el vehiculo este disponible y lo alquila, retornando el costo por x dias

        vehiculo = self.__buscarVehiculo(placa)

        if vehiculo is None:
            raise ValueError(f"No existe vehiculo con placa '{placa.upper()}'.")

        if not vehiculo.disponible:
            raise ValueError(f"El vehículo '{placa.upper()}' ya está alquilado. Elige otro vehículo disponible.")

        vehiculo.disponible = 0
        costo = vehiculo.precioPorDia * dias

        print(f"\n    Vehículo '{placa.upper()}' alquilado por {dias} día(s).")
        print(f"    Costo total: ${costo:,.0f}")
        return costo
    
    def devolverVehiculo(self, placa):
        # Devuelve un vehículo alquilado. Valida que esté efectivamente alquilado.

        vehiculo = self.__buscarVehiculo(placa)

        if vehiculo.disponible:
            raise ValueError(f"El vehículo '{placa.upper()}' no está actualmente alquilado.")

        vehiculo.disponible = True
        print(f"    Vehículo '{placa.upper()}' devuelto. Ya está disponible.")

    def calcularCosto(self, placa, dias):
        vehiculo = self.__buscarVehiculo(placa)
        costo = vehiculo.precioPorDia * dias

        print(f"\    Vehículo : {vehiculo.placa} — {vehiculo.marca} {vehiculo.modelo}")
        print(f"    Días     : {dias}")
        print(f"    Costo    : ${costo:,.0f}")

        return costo
    
    def vehiculoCostoso(self):
        self.cargarVehiculos()
    
        if not self.flota:
            print("No hay vehiculos registrados en el sistema.")
            return
    
        vehiculoCostoso = max(self.flota.values(), key=lambda v: v.precioPorDia)
    
        print("El vehiculo más costoso de alquilar es:")
        print(vehiculoCostoso)


def PedirPlaca():
    return input("    Placa del vehículo: ").strip().upper()

def PedirDias():
    while True:
        try:
            dias = int(input("    Cantidad de días: "))
            if dias <= 0:
                print("    Ingresa un número mayor a 0.")
                continue
            return dias
        except ValueError:
            print("    Ingresa un número entero válido.")

def PedirFloat(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("    El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("    Ingresa un número válido.")

def PedirInt(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("    El valor debe ser mayor a 0.")
                continue
            return valor
        except ValueError:
            print("    Ingresa un número entero válido.")

def CrearNuevoVehiculo():
    print("\n─── AGREGAR NUEVO VEHÍCULO ───")
    print("    Tipos:  1) Automóvil   2) Motocicleta   3) Camión")
    tipoOpcion = input("    Selecciona el tipo: ").strip()

    if tipoOpcion not in ("1", "2", "3"):
        print("    Tipo no válido.")
        return

    placa  = input("    Placa  : ").strip()
    marca  = input("    Marca  : ").strip()
    modelo = input("    Modelo : ").strip()
    precio = PedirFloat("    Precio por día: ")

    try:
        if tipoOpcion == "1":
            puertas  = PedirInt("    Número de puertas: ")
            vehiculo = Automovil(placa, marca, modelo, precio, puertas)
        elif tipoOpcion == "2":
            cilindros = PedirInt("    Cilindraje (cc): ")
            vehiculo  = Motocicleta(placa, marca, modelo, precio, cilindros)
        else:
            carga    = PedirFloat("    Capacidad de carga (toneladas): ")
            vehiculo = Camion(placa, marca, modelo, precio, carga)

        return vehiculo

    except ValueError as error:
        print(f"{error}")