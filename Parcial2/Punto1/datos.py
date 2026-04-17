from .vehiculos import *

vehiculos = {
    "automovil": [
        Automovil("ABC123", "Toyota",    "Corolla",   80000,  4),
        Automovil("DEF456", "Chevrolet", "Spark",     60000,  4),
        Automovil("GHI789", "Mazda",     "CX-5",     120000,  4),
    ],
    "motocicleta": [
        Motocicleta("MOT001", "Honda",  "CB500F",  45000, 500),
        Motocicleta("MOT002", "Yamaha", "R3",      50000, 321),
        Motocicleta("MOT003", "Suzuki", "GSX-S750",55000, 750),
    ],
    "camion": [
        Camion("CAM001", "Kenworth",     "T680",      250000, 20.0),
        Camion("CAM002", "Freightliner", "Cascadia",  280000, 25.0),
        Camion("CAM003", "Volvo",        "FH16",      310000, 30.0),
    ],
}