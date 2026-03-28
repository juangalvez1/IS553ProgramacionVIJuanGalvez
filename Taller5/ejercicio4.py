class Transporte:
    def __init__(self, capacidad, tarifa):
        self.capacidad = capacidad
        self.tarifa = tarifa

    def calcular_pasaje(self, km):
        return 0


class Bus(Transporte):
    def calcular_pasaje(self, km):
        return self.tarifa + (100 * km)

class Taxi(Transporte):
    def calcular_pasaje(self, km):
        return 500 * km

class Metro(Transporte):
    def calcular_pasaje(self, km):
        return self.tarifa


def main():
    bus = Bus(40, 2000)
    taxi = Taxi(4, 0)
    metro = Metro(100, 2500)

    transportes = [bus, taxi, metro]

    km = 10

    print("Costo para un trayecto de 10 km:\n")

    for t in transportes:
        print(f"{type(t).__name__}: ${t.calcular_pasaje(km)} pesos")

main()