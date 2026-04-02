from datetime import datetime

class Persona:
    def __init__(self, nombre, id, telefono, direccion, correo):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}, ID: {self.id}")


class Pedido:
    def __init__(self, codigo, fecha, monto, direccionEntrega, estado):
        self.codigo = codigo
        self.fecha = fecha
        self.monto = monto
        self.direccionEntrega = direccionEntrega
        self.estado = estado

    def mostrarPedido(self):
        print(f"Pedido {self.codigo} - Estado: {self.estado}")



class Cliente(Persona):
    def __init__(self, nombre, id, telefono, direccion, correo, metodoPago):
        Persona.__init__(self, nombre, id, telefono, direccion, correo)
        self.metodoPago = metodoPago

    def hacerPedido(self):
        print(f"{self.nombre} realizó un pedido")

class Repartidor(Persona):
    def __init__(self, nombre, id, telefono, direccion, correo, vehiculo):
        Persona.__init__(self, nombre, id, telefono, direccion, correo)
        self.vehiculo = vehiculo

    def entregarPedido(self):
        print(f"{self.nombre} está entregando el pedido en {self.vehiculo}")

class PedidoComida(Pedido):
    def __init__(self, codigo, fecha, monto, direccionEntrega, estado, restaurante):
        super().__init__(codigo, fecha, monto, direccionEntrega, estado)
        self.restaurante = restaurante

    def prepararComida(self):
        print(f"Pedido preparado en {self.restaurante}")


class PedidoMercado(Pedido):
    def __init__(self, codigo, fecha, monto, direccionEntrega, estado, supermercado):
        super().__init__(codigo, fecha, monto, direccionEntrega, estado)
        self.supermercado = supermercado

    def comprarProductos(self):
        print(f"Compra realizada en {self.supermercado}")


class RepartidorCliente(Cliente, Repartidor):
    def __init__(self, nombre, id, telefono, direccion, correo, metodoPago, vehiculo):
        Cliente.__init__(self, nombre, id, telefono, direccion, correo, metodoPago)
        Repartidor.__init__(self, nombre, id, telefono, direccion, correo, vehiculo)

    def dobleRol(self):
        print(f"{self.nombre} puede pedir y repartir pedidos")



def Main():
    listaPersonas = []

    cliente1 = Cliente("Ana", 1, "123", "Calle 1", "ana@mail.com", "Tarjeta")
    repartidor1 = Repartidor("Luis", 2, "456", "Calle 2", "luis@mail.com", "Moto")
    repartidorCliente1 = RepartidorCliente("Carlos", 3, "789", "Calle 3", "carlos@mail.com", "Efectivo", "Bicicleta")

    pedido1 = PedidoComida("P001", "2026-01-01", 25000, "Calle 10", "En camino", "McDonald's")
    pedido2 = PedidoMercado("P002", "2026-01-02", 80000, "Calle 20", "Pendiente", "Éxito")

    listaPersonas.extend([cliente1, repartidor1, repartidorCliente1])

    for persona in listaPersonas:
        persona.mostrarInfo()

    cliente1.hacerPedido()
    repartidor1.entregarPedido()
    repartidorCliente1.dobleRol()

    pedido1.prepararComida()
    pedido2.comprarProductos()

    with open(r"C:\JuanJose\utp\Semestre5\Programacion4\Taller6\files\pedidos.txt", "a", encoding="utf8") as file:
        for persona in listaPersonas:
            file.write(f"{persona.nombre},{persona.id}\n")

Main()