class Vehiculo:
    def __init__(self, placa: str, marca: str, modelo: str, precioDia: float, estado: str = "disponible"):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.precioDia = precioDia
        self.estado = estado

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa: str):
        if not isinstance(placa, str):
            raise TypeError("La placa debe ser un string")
        self.__placa = placa

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca: str):
        if not isinstance(marca, str):
            raise TypeError("La marca debe ser un string")
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo: str):
        if not isinstance(modelo, str):
            raise TypeError("El modelo debe ser un string")
        self.__modelo = modelo

    @property
    def precioDia(self):
        return self.__precioDia

    @precioDia.setter
    def precioDia(self, precioDia: float):
        if not isinstance(precioDia, (int, float)):
            raise TypeError("El precio por día debe ser numérico")
        if precioDia < 0:
            raise ValueError("El precio por día no puede ser negativo")
        self.__precioDia = float(precioDia)

    @property
    def estado(self):
        return self.__estado

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado: str):
        if not isinstance(estado, str):
            raise TypeError("El estado debe ser un string")

        estadosValidos = ["disponible", "alquilado"]

        if estado.lower() not in estadosValidos:
            raise ValueError(f"El estado debe ser uno de: {estadosValidos}")

        self.__estado = estado.lower()

    def alquilar(self):
        self.__estado = ""


    def costoAlquiler(self, numDias: int):
        if numDias > 0:
            raise ValueError("El número de dias a alquilar debe ser un entero positivo")
        else:
            return self.__precioDia * numDias



class Automovil(Vehiculo):
    def __init__(self, placa: str, marca: str, modelo: str, precioDia: float, estado: str, numPuertas: int):
        super().__init__(placa, marca, modelo, precioDia, estado)
        self.numPuertas = numPuertas

    @property
    def numPuertas(self):
        return self.__numPuertas

    @numPuertas.setter
    def numPuertas(self, numPuertas: int):
        if not isinstance(numPuertas, int):
            raise TypeError("El número de puertas debe ser entero")
        if numPuertas <= 0:
            raise ValueError("El número de puertas debe ser positivo")
        self.__numPuertas = numPuertas


class Motocicleta(Vehiculo):
    def __init__(self, placa: str, marca: str, modelo: str, precioDia: float, estado: str, cilindraje: int):
        super().__init__(placa, marca, modelo, precioDia, estado)
        self.cilindraje = cilindraje

    @property
    def cilindraje(self):
        return self.__cilindraje

    @cilindraje.setter
    def cilindraje(self, cilindraje: int):
        if not isinstance(cilindraje, int):
            raise TypeError("El cilindraje debe ser entero")
        if cilindraje <= 0:
            raise ValueError("El cilindraje debe ser positivo")
        self.__cilindraje = cilindraje


class Camion(Vehiculo):
    def __init__(self, placa: str, marca: str, modelo: str, precioDia: float, estado: str, capacidadCarga: float):
        super().__init__(placa, marca, modelo, precioDia, estado)
        self.capacidadCarga = capacidadCarga

    @property
    def capacidadCarga(self):
        return self.__capacidadCarga

    @capacidadCarga.setter
    def capacidadCarga(self, capacidadCarga: float):
        if not isinstance(capacidadCarga, (int, float)):
            raise TypeError("La capacidad de carga debe ser numérica")
        if capacidadCarga <= 0:
            raise ValueError("La capacidad de carga debe ser positiva")
        self.__capacidadCarga = float(capacidadCarga)

