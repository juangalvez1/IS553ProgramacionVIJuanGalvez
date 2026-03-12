class Estudiante:
    def __init__(self, nombre: str, codigo: float):
        self.nombre = nombre
        self.codigo = codigo

    def __eq__(self, otro):
        return self.codigo == otro.codigo


def main():
    e1 = Estudiante("Ana", 123)
    e2 = Estudiante("Carlos", 111)
    e3 = Estudiante("Ana Maria", 123)

    print(e1 == e2)
    print(e1 == e3)
    print(e2 == e3)

main()