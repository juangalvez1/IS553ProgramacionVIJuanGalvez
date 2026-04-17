import json
from productos import *

direccionArchivo = r"Parcial2\Punto3\files\inventario.json"

class Inventario:
    def __init__(self):
        self.productos = {}
        self.ventasPorCategoria = {}
        self.cargarProductos()

    def __leerProducto(self, tipo, data):
        # Del diccionario 'data' arma un objeto segun el tipo de vehiculo

        tipo = tipo.lower()
        productoBase = (data["id"], data["nombre"], data["precio"], data["cantidad"])

        # El '*' desempaqueta la tupla y excluye el ultimo elemento
        if tipo == "computador":
            return Computador(*productoBase, data["ram"], data["procesador"])
        elif tipo == "celular":
            return Celular(*productoBase, data["almacenamiento"], data["camaras"])
        elif tipo == "accesorio":
            return Accesorio(*productoBase, data["categoria"])
        else:
            raise ValueError(f"Tipo de vehículo desconocido: '{tipo}'.")

    def guardarProductos(self):
        datos = {"computador": [], "celular": [], "accesorio": []}

        for producto in self.productos.values():
            tipo = type(producto).__name__.lower()
            if tipo in datos:
                if producto.cantidad > 0:
                    datos[tipo].append(producto.toDict())

        with open(direccionArchivo, "w", encoding="utf-8") as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)

        print(f"    Datos guardados correctamente en '{direccionArchivo}'.")

    def cargarProductos(self):
        try:
            with open(direccionArchivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            print(f"    No se encontró '{direccionArchivo}'. Genera los datos primero (opción 2).")
            return
        except json.JSONDecodeError:
            print(f"    El archivo '{direccionArchivo}' tiene un formato inválido.")
            return
        
        self.productos.clear()
        
        for tipo, lista in datos.items():
            for p in lista:
                id = p["id"]

                if id in self.productos:
                    print(f"    ID duplicada '{id}' ignorada.")
                    continue
                self.productos[id] = self.__leerProducto(tipo, p)

    def registrarProducto(self, producto):
        if producto.id in self.productos:
            print("Este producto ya fue registrado.")
            return

        self.productos[producto.id] = producto
        self.guardarProductos()
        print("Producto registrado exitosamente.")
        self.cargarProductos()

    def mostrarInventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        for producto in self.productos.values():
            print(producto)

    def buscarProducto(self, id):
        print("Entro en buscarProducto")
        return self.productos.get(id, None)
    
    def reabastecer(self, id, cantidad):
        producto = self.buscarProducto(id)
        if producto:
            producto.cantidad += cantidad
            print(f"Producto {producto.nombre} actualizado. Stock: {producto.cantidad}")
            self.guardarProductos()
            self.cargarProductos()
        else:
            print("Producto no encontrado.")

    def consultarProducto(self, id):
        producto = self.buscarProducto(id)
        if producto:
            print(producto)
        else:
            print("Producto no encontrado.")

    def venderProducto(self, id, cantidad):
        producto = self.buscarProducto(id)
        if not producto:
            print("Producto no encontrado.")
            return
        
        if cantidad <= 0:
            print("Cantidad inválida.")
            return
        
        if producto.cantidad < cantidad:
            print("Stock insuficiente.")
            return
        
        subtotal = producto.precio * cantidad
        descuento = 0

        if cantidad >= 3:
            descuento += subtotal * 0.08
        if subtotal >= 500:
            descuento += subtotal * 0.05

        total = subtotal - descuento
        producto.cantidad -= cantidad
        print(f"Venta exitosa. Subtotal: ${subtotal:.2f} (Descuento: ${descuento:.2f}) \nTotal: ${total:.2f}")
        tipo = type(producto).__name__

        if tipo in self.ventasPorCategoria:
            self.ventasPorCategoria[tipo] += cantidad
        else:
            self.ventasPorCategoria[tipo] = cantidad

        self.guardarProductos()
        self.cargarProductos()

    def categoriaMasVendida(self):
        self.cargarProductos()

        if not self.ventasPorCategoria:
            print("No hay ventas registradas.")
            return

        categoria = max(self.ventasPorCategoria, key=self.ventasPorCategoria.get)
        cantidad = self.ventasPorCategoria[categoria]

        print(f"Categoría más vendida: {categoria} ({cantidad} unidades)")
