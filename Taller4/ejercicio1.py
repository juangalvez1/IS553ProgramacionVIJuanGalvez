class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad}"

def main():
    persona1 = Persona("Carlos", 25)
    persona2 = Persona("Ana", 30)
    persona3 = Persona("Luis", 19)

    print(persona1)
    print(persona2)
    print(persona3)

main()