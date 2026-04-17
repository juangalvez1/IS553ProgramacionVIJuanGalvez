from .pacientes import *

pacientes = {
    "general": [
        PacienteGeneral(101, "Juan Pérez", 30, "Pendiente", "Sura"),
        PacienteGeneral(102, "Ana Gómez", 25, "Atendido", "Sanitas"),
        PacienteGeneral(103, "Carlos Ruiz", 40, "Pendiente", "Nueva EPS"),
    ],

    "prioritario": [
        PacientePrioritario(201, "María López", 65, "Atendido", "Adulto mayor"),
        PacientePrioritario(202, "Pedro Martínez", 50, "Pendiente", "Discapacidad"),
        PacientePrioritario(203, "Luisa Fernández", 70, "Atendido", "Embarazo"),
    ],

    "urgencia": [
        PacienteUrgencia(301, "Andrés Torres", 28, "Pendiente", 4),
        PacienteUrgencia(302, "Sofía Ramírez", 35, "Pendiente", 3),
        PacienteUrgencia(303, "Diego Castro", 22, "Pendiente", 2),
    ],
}