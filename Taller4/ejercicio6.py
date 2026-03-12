class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector2D(self.x + otro.x, self.y + otro.y)

    def __str__(self):
        return f"({self.x},{self.y})"


def main():
    v1 = Vector2D(2, 3)
    v2 = Vector2D(4, 1)

    print(f"{v1} + {v2} = {v1 + v2}")


main()