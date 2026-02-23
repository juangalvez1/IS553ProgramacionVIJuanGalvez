from io import *

class Producto:
    codigo = 0
    nombre = ""
    cantidad = 0
    precio = 0
    categoria = ""

    def save(self):
        file = open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller2\archivos\almacen.txt", "a")

        file.write(f"{self.codigo},{self.nombre},{self.cantidad},{self.precio},{self.categoria}\n")

        file.close()

    def stock_value_category(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller2\archivos\almacen.txt", "r") as file:
            categories = []

            for line in file:
                data = line.strip().split(",")

                if data[4] not in categories:
                    categories.append(data[4])
                else:
                    pass
            
            stockValue = [["", 0] for _ in range(len(categories))]
            for i in range(len(categories)):
                stockValue[i][0] = categories[i]

            file.seek(0)
            for line in file:
                data = line.strip().split(",")

                index = categories.index(data[4])

                stockValue[index][1] += int(data[2]) * int(data[3])

            print("Valores en stock por categoria: \n")
            for elem in stockValue:
                print(f"{elem[0]}: ${elem[1]}")
            print()
            
def main():
    tam = int(input("Ingrese la cantidad de productos a guardar en el archivo: "))

    temp = Producto()
    for i in range(tam):
        print(f"\nProducto {i+1}")
        temp.codigo = int(input(f"Ingrese el codigo del producto {i+1}: "))
        temp.nombre = input(f"Ingrese el nombre del producto {i+1}: ")
        temp.cantidad = int(input(f"Ingerse la cantidad del producto {i+1}: "))
        temp.precio = int(input(f"Ingerse el precio del producto {i+1}: "))
        temp.categoria = input(f"Ingrese la categoria del producto {i+1}: ")

        temp.save()

    temp.stock_value_category()

main()
