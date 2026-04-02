from datetime import datetime

class PersonalUniversitario:
    def __init__(self, nombre, id, edad, fechaIngreso, correo, telefono):
        self.nombre = nombre
        self.id = id
        self.edad = edad
        self.fechaIngreso = fechaIngreso  #YYYY-MM-DD
        self.correo = correo
        self.telefono = telefono

    def calcular_antiguedad(self):
        fechaIngreso = datetime.strptime(self.fechaIngreso, "%Y-%m-%d")
        hoy = datetime.now()
        antiguedad = hoy.year - fechaIngreso.year
        return antiguedad
    
    def mostrarInfo(self):
        print(f"\n--- Info ---")
        print(f"Nombre: {self.nombre}")
        print(f"Antigüedad: {self.calcular_antiguedad()} años")


class Profesor(PersonalUniversitario):
    def __init__(self, nombre, id, edad, fecha_ingreso, correo, telefono, tipo, horas_trabajo, tarifa_hora):
        PersonalUniversitario.__init__(self, nombre, id, edad, fecha_ingreso, correo, telefono)

        self.tipo = tipo
        self.horas_trabajo = horas_trabajo
        self.tarifa_hora = tarifa_hora

        years = self.calcular_antiguedad()

        if years <= 2:
            self.nivel = "junior"
        elif years <= 5:
            self.nivel = "semi-senior"
        else:
            self.nivel = "senior"
        

    def calcular_sueldo(self):
        if self.tipo == "planta":
            return self.horas_trabajo * self.tarifa_hora * 1.5
        elif self.tipo == "catedra":
            return self.horas_trabajo * self.tarifa_hora * 1.2
        else:
            return self.horas_trabajo * self.tarifa_hora

    def mostrarMaterias(self):
        if self.nivel == "junior":
            materias = ["Intro Programación", "Lógica", "Matemáticas Básicas"]
        elif self.nivel == "semi-senior":
            materias = ["Estructuras de Datos", "POO", "Bases de Datos"]
        elif self.nivel == "senior":
            materias = ["IA", "Machine Learning", "Compiladores"]
        else:
            print("No tiene nivel registrado para dar materias.")
        print(f"Materias de {self.nombre}: {materias}")


class Alumno(PersonalUniversitario):
    def __init__(self, nombre, id, edad, fecha_ingreso, correo, telefono, carrera, semestre):
        PersonalUniversitario.__init__(self, nombre, id, edad, fecha_ingreso, correo, telefono)
        self.carrera = carrera
        self.semestre = semestre


class ProfesorAyudante(Profesor, Alumno):
    def __init__(self, nombre, id, edad, fecha_ingreso, correo, telefono, tipo, horas_trabajo, tarifa_hora, carrera, semestre):
        Profesor.__init__(self, nombre, id, edad, fecha_ingreso, correo, telefono, tipo, horas_trabajo, tarifa_hora)
        Alumno.__init__(self, nombre, id, edad, fecha_ingreso, correo, telefono, carrera, semestre)


def Save(persona):
    with open(r"C:\JuanJose\utp\Semestre5\Programacion4\Taller6\files\personal.txt", "a", encoding="utf8") as file:
        file.write(f"{persona.nombre},{persona.id},{persona.calcular_antiguedad()}\n")


def main():
    profesor = Profesor(
        "Luis Ramírez", 101, 45, "2015-08-10", "luis@uni.edu", "11111",
        "planta", 160, 50
    )

    alumno = Alumno(
        "María López", 202, 20, "2023-01-15", "maria@uni.edu", "22222",
        "Ingeniería de Sistemas", 3
    )

    ayudante = ProfesorAyudante(
        "Carlos Gómez", 101, 26, "2021-03-15", "carlos@uni.edu", "33333",
        "planta", 120, 50,
        "Ingeniería de Sistemas", 6)
    
    print(f"El sueldo de {profesor.nombre} es de: {profesor.calcular_sueldo()}")
    profesor.mostrarMaterias()

    profesor.mostrarInfo()
    alumno.mostrarInfo()
    ayudante.mostrarInfo()

    Save(profesor)
    Save(alumno)
    Save(ayudante)

main()