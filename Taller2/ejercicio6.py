from io import *

class Animal:
    especie = ""
    nombre = ""
    edad = 0

    def save(self):
        file = open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller2\archivos\animales.txt", "a")

        file.write(f"{self.especie},{self.nombre},{self.edad}\n")

        file.close()



    def average_age(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller2\archivos\animales.txt", "r") as file:
            sumOfAges = 0
            counterOfRecords = 0
            
            for line in file:
                data = line.strip().split(",")

                sumOfAges += int(data[2])
                counterOfRecords += 1
            
        return sumOfAges / counterOfRecords
    
def main():
    tam = int(input("Ingrese la cantidad de animales a guardar en el archivo: "))

    temp = Animal()
    for i in range(tam):
        print(f"\nAnimal {i+1}")
        temp.especie = input(f"Ingrese la especie del animal {i+1}: ")
        temp.nombre = input(f"Ingrese el nombre del animal {i+1}: ")
        temp.edad = int(input(f"Ingerse la edad del animal {i+1}: "))

        temp.save()

    averageAge = temp.average_age()

    print(f"\nLa edad promedio de los animales ingresados es de {averageAge}\nA continuacion estan los animales que superan ese promedio:")
    with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller2\archivos\animales.txt", "r") as file:
        for linea in file:
            data = linea.strip().split(",")

            if float(data[2]) > averageAge:
                print(f"{data[0]} - {data[1]} - {data[2]}")
            else:
                pass

main()