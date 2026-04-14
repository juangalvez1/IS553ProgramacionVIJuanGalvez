from objetos import *

def Main():
    vehiculos = [coche, camioneta, bicicleta, motocicleta]

    catalogar(vehiculos)
    catalogar(vehiculos, 4)
    catalogar(vehiculos, 2)
    catalogar(vehiculos, 0)

    coche.color = "azul"
    coche.ruedas = 4
    coche.velocidad = 200
    coche.cilindrada = 2200

    camioneta.color = "gris"
    camioneta.ruedas = 4
    camioneta.velocidad = 140
    camioneta.cilindrada = 3000
    camioneta.carga = 1200

    bicicleta.color = "amarillo"
    bicicleta.ruedas = 2
    bicicleta.tipo = "montaña"

    motocicleta.color = "rojo"
    motocicleta.ruedas = 2
    motocicleta.tipo = "racing"
    motocicleta.velocidad = 250
    motocicleta.cilindrada = 750

    for v in vehiculos:
        print(v)

Main()