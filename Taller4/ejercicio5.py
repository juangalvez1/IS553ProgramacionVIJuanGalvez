class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def __add__(self, otro):
        return self.precio + otro.precio


def main():
    producto1 = Producto("Mouse", 25.5)
    producto2 = Producto("Teclado", 40.0)

    total = producto1 + producto2

    print(f"Precio total: {total}")


main()