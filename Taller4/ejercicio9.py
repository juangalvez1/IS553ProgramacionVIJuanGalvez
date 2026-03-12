class Biblioteca:
    def __init__(self):
        self.libros = []

    def __len__(self):
        return len(self.libros)

    def __add__(self, otra):
        new = Biblioteca()
        new.libros = self.libros + otra.libros
        return new


def main():
    library1 = Biblioteca()
    library2 = Biblioteca()

    library1.libros.append("El principito")
    library1.libros.append("1984")

    library2.libros.append("Don Quijote")
    library2.libros.append("La Odisea")
    library2.libros.append("Cien años de soledad")

    library3 = library1 + library2

    print(f"Biblioteca 1 tiene {len(library1)} libros")
    print(f"Biblioteca 2 tiene {len(library2)} libros")
    print(f"Biblioteca 3 (unida) tiene {len(library3)} libros")

main()