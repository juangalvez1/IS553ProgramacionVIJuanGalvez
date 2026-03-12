class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f'"{self.titulo}" escrito por {self.autor}'


def main():
    libro1 = Libro("El principito", "Antoine de Saint-Exupéry")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")
    libro3 = Libro("1984", "George Orwell")
    libro4 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")
    libro5 = Libro("La Odisea", "Homero")

    books = [libro1, libro2, libro3, libro4, libro5]

    for book in books:
        print(book)

main()