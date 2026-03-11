import xml.etree.ElementTree as ET

class Producto:

    def __init__ (self, ID: int, name: str, price: float, quantityOnStock: int):
        self.ID = ID
        self.nombre = name
        self.precio = price
        self.cantidadEnInventario = quantityOnStock

    def disminuir_inventario(self, cantidad):
        if self.cantidadEnInventario >= cantidad:
            self.cantidadEnInventario -= cantidad
            return True
        else:
            return False

    def aumentar_inventario(self, cantidad):
        self.cantidadEnInventario += cantidad

    def mostrar_informacion(self):
        print(f"ID: {self.ID} - Nombre: {self.nombre} - Precio: {self.precio:.1f} - Cantidad en inventario: {self.cantidadEnInventario}")

class Cliente:
    def __init__(self, ID: int, name: str, balance: float):
        self.ID = ID
        self.nombre = name
        self.saldo = balance

    def realizar_compra(self, producto: Producto, cantidad: int):
        if producto.cantidadEnInventario >= cantidad:
            if self.saldo >= producto.precio * cantidad:
                self.saldo -= producto.precio * cantidad
                producto.disminuir_inventario(cantidad)
                return True
            else:
                return False
        else:
            return False

    def mostrar_informacion(self):
        print(f"ID: {self.ID} - Nombre: {self.nombre} - Saldo: {self.saldo:.1f}")

class Tienda:
    def __init__(self):
        self.productos = []
        self.clientes = []
    
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto) 

    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def realizar_venta(self, id_cliente: int, id_producto: int, cantidad: int): 
        for client in self.clientes:
            if client.ID == id_cliente:
                for producto in self.productos:
                    if producto.ID == id_producto:
                        if client.realizar_compra(producto, cantidad):
                            return True
                        else:
                            return False
                return False
        return False

    def mostrar_productos(self):
        print()
        for producto in self.productos:
            producto.mostrar_informacion()
        print()

    def mostrar_clientes(self):
        print()
        for cliente in self.clientes:
            cliente.mostrar_informacion()
        print()

    def guardar_datos(self, file: str):
        root = ET.Element("tienda")
        
        productos_elem = ET.SubElement(root, "productos")
        for p in self.productos:
            p_elem = ET.SubElement(productos_elem, "producto")
            ET.SubElement(p_elem, "ID").text = f"{p.ID}"
            ET.SubElement(p_elem, "nombre").text = p.nombre
            ET.SubElement(p_elem, "precio").text = f"{p.precio:.1f}"
            ET.SubElement(p_elem, "cantidadEnInventario").text = f"{p.cantidadEnInventario}"
            
        clientes_elem = ET.SubElement(root, "clientes")
        for c in self.clientes:
            c_elem = ET.SubElement(clientes_elem, "cliente")
            ET.SubElement(c_elem, "ID").text = f"{c.ID}"
            ET.SubElement(c_elem, "nombre").text = c.nombre
            ET.SubElement(c_elem, "saldo").text = f"{c.saldo:.1f}"
            
        tree = ET.ElementTree(root)
        ET.indent(tree, "    ", 0)

        try:
            tree.write(file, "utf-8", True)
            print(f"Datos guardados exitosamente.")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def cargar_datos(self, file: str):
        try:
            tree = ET.parse(file)
            root = tree.getroot()
            
            self.productos = []
            productos_elem = root.find("productos")
            if productos_elem != None:
                for p_elem in productos_elem.findall("producto"):
                    nombre = p_elem.find("nombre").text
                    id_val = int(p_elem.find("ID").text)
                    precio = float(p_elem.find("precio").text)
                    cantidad = int(p_elem.find("cantidadEnInventario").text)
                    self.productos.append(Producto(id_val, nombre, precio, cantidad))
                    
            self.clientes = []
            clientes_elem = root.find("clientes")
            if clientes_elem != None:
                for c_elem in clientes_elem.findall("cliente"):
                    nombre = c_elem.find("nombre").text
                    id_val = int(c_elem.find("ID").text)
                    saldo = float(c_elem.find("saldo").text)
                    self.clientes.append(Cliente(id_val, nombre, saldo))
            print(f"Datos cargados exitosamente.")
        except FileNotFoundError:
            print(f"El file {file} no existe. No se cargaron datos.")
        except ET.ParseError:
            print(f"El file {file} no tiene un formato XML válido.")
        except Exception as e:
            print(f"Ocurrió un error al cargar los datos: {e}")


def main():
    store = Tienda()

    product1 = Producto(1, "Papa", 1.3, 50)
    store.agregar_producto(product1)

    product2 = Producto(2, "Arroz", 2.7, 100)
    store.agregar_producto(product2)

    product3 = Producto(3, "Gaseosa", 4, 75)
    store.agregar_producto(product3)

    client1 = Cliente(111, "Mora", 10000)
    store.agregar_cliente(client1)

    client2 = Cliente(222, "Frijolito", 3000)
    store.agregar_cliente(client2)

    store.mostrar_productos()
    store.mostrar_clientes()

    store.realizar_venta(client1.ID, 1, 5)
    store.realizar_venta(client2.ID, 2, 3)
    store.realizar_venta(client1.ID, 3, 1)
    store.realizar_venta(client2.ID, 1, 4)
    
    store.mostrar_productos()
    store.mostrar_clientes()

    store.guardar_datos(r"C:\JuanJose\UTP\Semestre5\Programacion4\Parcial1\files\tienda.xml")
    store.cargar_datos(r"C:\JuanJose\UTP\Semestre5\Programacion4\Parcial1\files\tienda.xml")

    store.realizar_venta(client1.ID, 2, 6)
    store.realizar_venta(client2.ID, 3, 2)

    store.mostrar_productos()
    store.mostrar_clientes()

main()