import math

class Figura:
    def area(self):
        return 0


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)
    
def main():
    figuras = [
    Rectangulo(10, 5),
    Triangulo(8, 4),
    Circulo(3)
    ]

    areas = []

    for f in figuras:
        areas.append(f"{type(f).__name__} => {f.area():.2f}")

    print(areas)

main()