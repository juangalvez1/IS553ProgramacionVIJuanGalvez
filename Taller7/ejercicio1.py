import math

class Figura:
    def CalcularArea(self):
        raise NotImplementedError("Debe implementarse en la subclase")


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def SetBase(self, base):
        if base > 0:
            self.__base = base
        else:
            raise ValueError("La base debe ser positiva")

    def SetAltura(self, altura):
        if altura > 0:
            self.__altura = altura
        else:
            raise ValueError("La altura debe ser positiva")

    def CalcularArea(self):
        return (self.__base * self.__altura) / 2


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def SetBase(self, base):
        if base > 0:
            self.__base = base
        else:
            raise ValueError("La base debe ser positiva")

    def SetAltura(self, altura):
        if altura > 0:
            self.__altura = altura
        else:
            raise ValueError("La altura debe ser positiva")

    def CalcularArea(self):
        return self.__base * self.__altura


class Circulo(Figura):
    def __init__(self, radio):
        self.__radio = radio

    def SetRadio(self, radio):
        if radio > 0:
            self.__radio = radio
        else:
            raise ValueError("El radio debe ser positivo")

    def CalcularArea(self):
        return math.pi * (self.__radio ** 2)


class Trapecio(Figura):
    def __init__(self, baseMayor, baseMenor, altura):
        self.__baseMayor = baseMayor
        self.__baseMenor = baseMenor
        self.__altura = altura

    def SetBaseMayor(self, baseMayor):
        if baseMayor > 0:
            self.__baseMayor = baseMayor
        else:
            raise ValueError("La base mayor debe ser positiva")

    def SetBaseMenor(self, baseMenor):
        if baseMenor > 0:
            self.__baseMenor = baseMenor
        else:
            raise ValueError("La base menor debe ser positiva")

    def SetAltura(self, altura):
        if altura > 0:
            self.__altura = altura
        else:
            raise ValueError("La altura debe ser positiva")

    def CalcularArea(self):
        return ((self.__baseMayor + self.__baseMenor) * self.__altura) / 2


def Main():
    triangulo = Triangulo(10, 5)
    rectangulo = Rectangulo(4, 6)
    circulo = Circulo(3)
    trapecio = Trapecio(8, 5, 4)

    print("Área triángulo:", triangulo.CalcularArea())
    print("Área rectángulo:", rectangulo.CalcularArea())
    print("Área círculo:", circulo.CalcularArea())
    print("Área trapecio:", trapecio.CalcularArea())


    triangulo.SetAltura(12)
    triangulo.SetBase(25)

    rectangulo.SetAltura(15)
    rectangulo.SetBase(9)

    circulo.SetRadio(7)

    trapecio.SetAltura(6)
    trapecio.SetBaseMayor(14)
    trapecio.SetBaseMenor(8)

    print("Área triángulo:", triangulo.CalcularArea())
    print("Área rectángulo:", rectangulo.CalcularArea())
    print("Área círculo:", circulo.CalcularArea())
    print("Área trapecio:", trapecio.CalcularArea())
    
Main()