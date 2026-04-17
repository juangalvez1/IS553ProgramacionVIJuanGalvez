from .productos import *

productos = {
    "computador": [
        Computador(1, "Laptop Dell", 3500000, 5, 16, "Intel i7"),
        Computador(2, "PC Gamer", 5200000, 3, 32, "AMD Ryzen 7"),
        Computador(3, "MacBook Air", 4800000, 4, 8, "M1"),
    ],
    
    "celular": [
        Celular(4, "iPhone 13", 4200000, 6, 128, 2),
        Celular(5, "Samsung S23", 3900000, 8, 256, 3),
        Celular(6, "Xiaomi Redmi Note 12", 1200000, 10, 128, 4),
    ],
    
    "accesorio": [
        Accesorio(7, "Mouse Logitech", 80000, 15, "Periférico"),
        Accesorio(8, "Teclado Mecánico", 250000, 7, "Periférico"),
        Accesorio(9, "Audífonos Sony", 300000, 12, "Audio"),
    ],
}