class Estudiante:
    def __init__(self, nombre: str, codigo: str):
        self.nombre = nombre
        self.codigo = codigo

    def __eq__(self, otro):
        return self.codigo == otro.codigo

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Curso:
    def __init__(self, nombre_curso: str):
        self.nombre_curso = nombre_curso
        self.estudiantes = []

    def __len__(self):
        return len(self.estudiantes)

    def __str__(self):
        texto = f"Curso: {self.nombre_curso}\nEstudiantes:\n"
        for e in self.estudiantes:
            texto += f"- {e}\n"
        return texto

    def __eq__(self, otro):
        return len(self) == len(otro)


def main():
    student1 = Estudiante("Ana", "123")
    student2 = Estudiante("Carlos", "111")
    student3 = Estudiante("Laura", "100")
    student4 = Estudiante("Pedro", "222")

    class1 = Curso("Programación")
    class2 = Curso("Compu Gráfica")

    class1.estudiantes.append(student1)
    class1.estudiantes.append(student2)

    class2.estudiantes.append(student3)
    class2.estudiantes.append(student4)

    print(f"\n{len(class1)}\n")
    print(class1)
    print(class2)
    print(class1 == class2)

main()