from io import *

class Vehiculo:
    def __init__(self, color, ruedas, tipo):
        self.color = color
        self.ruedas = ruedas
        self.tipo = tipo.lower()

    def info(self):
        if self.tipo == "coche":
            return f"Para un {self.tipo}, las llantas duran 3-5 años. Marcas: Michelin, Bridgestone, Goodyear, Continental y Pirelli"
        elif self.tipo == "moto":
            return f"Para una {self.tipo}, las llantas duran 1-4 años. Marcas: Michelin, Pirelli, Bridgestone, Continental y Dunlop"
        elif self.tipo == "camion":
            return f"Para un {self.tipo}, las llantas duran 2-3 años. Marcas: Michelin, Bridgestone, Goodyear, Continental y Pirelli"
        return "Sin información"

    def tipoDeCombustible(self):
        if self.tipo == "coche":
            return f"Para un tipo {self.tipo} el combustible es: Gasolina, Diesel, Electrico o hibrido"
        elif self.tipo == "moto":
            return f"Para un tipo {self.tipo} el combustible es: Gasolina o Electrica"
        elif self.tipo == "camion":
            return f"Para un tipo {self.tipo} el combustible es: Diesel, Electrico o Hibrido"
        return "Desconocido"

    def save(self):
        with open(r"C:\JuanJose\utp\Semestre5\Programacion4\Taller5\files\vehiculos.txt", "a", encoding = "utf-8") as file:
            file.write(f"{self.info()}\n{self.tipoDeCombustible()}\n\n")
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas, "coche")
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def tiempoDesplazamiento(self, ciudad):
        ciudad = ciudad.lower()

        if ciudad == "bogota":
            tiempo = (
                "8 horas" if self.tipo == "coche" else
                "6 horas" if self.tipo == "moto" else
                "10 horas" if self.tipo == "camion" else
                None
            )

        elif ciudad == "medellin":
            tiempo = (
                "6 horas" if self.tipo == "coche" else
                "4 horas" if self.tipo == "moto" else
                "8 horas" if self.tipo == "camion" else
                None
            )

        elif ciudad == "cali":
            tiempo = (
                "4 horas" if self.tipo == "coche" else
                "3 horas" if self.tipo == "moto" else
                "6 horas" if self.tipo == "camion" else
                None
            )

        elif ciudad == "cartagena":
            tiempo = (
                "18 horas" if self.tipo == "coche" else
                "15 horas" if self.tipo == "moto" else
                "20 horas" if self.tipo == "camion" else
                None
            )

        elif ciudad == "barranquilla":
            tiempo = (
                "16 horas" if self.tipo == "coche" else
                "14 horas" if self.tipo == "moto" else
                "18 horas" if self.tipo == "camion" else
                None
            )

        else:
            return "Ciudad no válida (validas: bogota, medellin, cali, cartagena, barranquilla)."

        if tiempo:
            articulo = "una" if self.tipo == "moto" else "un"
            return f"Para {articulo} {self.tipo}, el tiempo de desplazamiento a {ciudad} es de {tiempo}."
        else:
            return f"No hay información para un/a {self.tipo} hacia {ciudad}."

    def gastoCombustible(self):
        return "300000 pesos mensuales"
    
    def save(self):
        with open(r"C:\JuanJose\utp\Semestre5\Programacion4\Taller5\files\vehiculos.txt", "a", encoding = "utf-8") as file:
            file.write(f"{self.info()}\n{self.tipoDeCombustible()}\n{self.gastoCombustible()}\n\n")
    
def main():
    vehicle1 = Vehiculo("negro", 2, "moto")
    vehicle2 = Vehiculo("blanco", 8, "camion")
    car1 = Coche("rojo", 4, 180, 2000)

    print(vehicle1.info())
    print(vehicle2.info())
    print(car1.tiempoDesplazamiento("bogota"))

    vehicle1.save()
    vehicle2.save()
    car1.save()

main()