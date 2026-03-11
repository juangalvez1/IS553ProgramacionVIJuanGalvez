from io import *

class Empleado:
    def __init__(self, ID: int, nombre: str, salario: float, años_experiencia: int):
        self.ID = ID
        self.nombre = nombre
        self.salario = salario
        self.años_experiencia = años_experiencia

    def __str__(self):
        return f"ID: {self.ID}, Nombre: {self.nombre}, Salario: {self.salario}, Años de experiencia: {self.años_experiencia}"  

    def calcular_salario(self):
        if 0 <= self.años_experiencia <= 2:
            return self.salario * 1.05
        elif 3 <= self.años_experiencia <= 5:
            return self.salario * 1.10
        elif self.años_experiencia > 5:
            return self.salario * 1.15

class GestorEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado: Empleado):
        self.empleados.append(empleado)
        
    def eliminar_empleado(self, ID: int):
        for empleado in self.empleados:
            if empleado.ID == ID:
                self.empleados.remove(empleado)
                return True
        return False

    def buscar_empleado(self, ID: int):
        for empleado in self.empleados:
            if empleado.ID == ID:
                return empleado
        return None
    
    def editar_empleado(self, ID: int, nombre = None, salario = None, años_experiencia = None):
        empleado = self.buscar_empleado(ID)
        if empleado:
            if nombre:
                empleado.nombre = nombre
            if salario:
                empleado.salario = salario
            if años_experiencia:
                empleado.años_experiencia = años_experiencia
            return True
        return False
    
    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(empleado)
            print(f"Salario total: {empleado.calcular_salario()}")

    def guardar_empleados(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Parcial1\files\empleados.txt", "w") as file:
            for empleado in self.empleados:
                file.write(f"{empleado.ID},{empleado.nombre},{empleado.salario},{empleado.años_experiencia}\n")
    
    def cargar_empleados(self):
        try:
            with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Parcial1\files\empleados.txt", "r") as file:
                for line in file:
                    ID, nombre, salario, años_experiencia = line.strip().split(",")
                    empleado = Empleado(int(ID), nombre, float(salario), int(años_experiencia))
                    self.agregar_empleado(empleado)
        except FileNotFoundError:
            print("No se encontró el archivo. 123")

def main():
    gestor = GestorEmpleados()
    gestor.cargar_empleados()

    while 1:
        print("\nSistema de Gestión de Empleados")
        print("1. Agregar empleado")
        print("2. Eliminar empleado")
        print("3. Buscar empleado por ID")
        print("4. Mostrar empleados")
        print("5. Guardar empleados")
        print("6. Salir\n")

        opcion = int(input("Seleccione una opción: "))
        print()

        if opcion == 1:
            ID = int(input("Ingrese la ID: "))
            nombre = input("Ingrese el nombre: ")
            salario = float(input("Ingrese el salario: "))
            años = int(input("Ingrese los años de experiencia: "))

            empleado = Empleado(ID, nombre, salario, años)
            gestor.agregar_empleado(empleado)
            print("\nEmpleado agregado correctamente.")
        elif opcion == 2:
            ID = int(input("Ingrese el ID del empleado a eliminar: "))
            if gestor.eliminar_empleado(ID):
                print(f"\nEmpleado con Id '{ID}' eliminado.")
            else:
                print(f"\nEmpleado con ID '{ID}' no encontrado.")
        elif opcion == 3:
            ID = int(input("Ingrese el ID a buscar: "))
            empleado = gestor.buscar_empleado(ID)

            if empleado:
                print("\nEmpleado encontrado:")
                print(empleado)
                print(f"Salario con total: {empleado.calcular_salario()}")
            else:
                print(f"\nEmpleado con ID '{ID}' no encontrado.")
        elif opcion == 4:
            print("Lista de empleados:")
            gestor.mostrar_empleados()
        elif opcion == 5:
            gestor.guardar_empleados()
            print("Empleados guardados en archivo.")
        elif opcion == 6:
            gestor.guardar_empleados()
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de Nuevo.\n")
    
main()