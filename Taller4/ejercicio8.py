class CarritoCompras:
    def __init__(self):
        self.productos = []

    def __len__(self):
        return len(self.productos)

    def __str__(self):
        texto = "Productos en el carrito:\n"
        for producto in self.productos:
            texto += f"- {producto}\n"
        return texto


def main():
    carrito = CarritoCompras()

    carrito.productos.append("Laptop")
    carrito.productos.append("Mouse")
    carrito.productos.append("Teclado")
    carrito.productos.append("Monitor")

    print(f"Cantidad de productos en el carrito: {len(carrito)}")
    print(carrito)

main()