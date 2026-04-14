class Vehiculo:
    def __init__(self, color, ruedas):
        self.__color = color
        self.__ruedas = ruedas

    def __str__(self):
        return f"Color: {self.__color}, Ruedas: {self.__ruedas}"

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if type(color).__name__ == "str":
            self.__color = color
        else:
            raise ValueError("El color debe ser una str.")

    @property
    def ruedas(self):
        return self.__ruedas
    
    @ruedas.setter
    def ruedas(self, ruedas):
        if ruedas > 0:
            self.__ruedas = ruedas
        else:
            raise ValueError("El # de ruedas debe ser un numero entero positivo.")


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.__velocidad = velocidad
        self.__cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", Velocidad: {self.__velocidad} km/h, Cilindrada: {self.__cilindrada} cc"

    @property
    def velocidad(self):
        return self.__velocidad
    
    @velocidad.setter
    def velocidad(self, velocidad):
        if velocidad > 0:
            self.__velocidad = velocidad
        else:
            raise ValueError("La velocidad debe ser un numero entero positivo.")

    @property
    def cilindrada(self):
        return self.__cilindrada
    
    @cilindrada.setter
    def cilindrada(self, cilindrada):
        if cilindrada > 0:
            self.__cilindrada = cilindrada
        else:
            raise ValueError("La cc debe ser un numero entero positivo.")


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.__carga = carga

    def __str__(self):
        return super().__str__() + f", Carga: {self.carga}kg"

    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, carga):
        if carga > 0:
            self.__carga = carga
        else:
            raise ValueError("La carga debe ser un numero entero positivo.")


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.__tipo = tipo

    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo}"

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        if type(tipo).__name__ == "str":
            self.__tipo = tipo
        else:
            raise ValueError("El tipo debe ser una str.")


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.__velocidad = velocidad
        self.__cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada}cc"

    @property
    def velocidad(self):
        return self.__velocidad
    
    @velocidad.setter
    def velocidad(self, velocidad):
        if velocidad > 0:
            self.__velocidad = velocidad
        else:
            raise ValueError("La velocidad debe ser un numero entero positivo.")

    @property
    def cilindrada(self):
        return self.__cilindrada
    
    @cilindrada.setter
    def cilindrada(self, cilindrada):
        if cilindrada > 0:
            self.__cilindrada = cilindrada
        else:
            raise ValueError("La cc debe ser un numero entero positivo.")

    
def catalogar(vehiculos, ruedas = None):
    contador = 0

    for v in vehiculos:
        if ruedas is None or v.ruedas == ruedas:
            print(f"{type(v).__name__} => {v}")
            contador += 1
    print("")
    if ruedas is not None:
        print(f"Se han encontrado {contador} vehículos con {ruedas} ruedas.\n\n")