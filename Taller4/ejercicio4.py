class EquipoFutbol:
    def __init__(self, nombre_equipo: str):
        self.nombre_equipo = nombre_equipo
        self.jugadores = []

    def __len__(self):
        return len(self.jugadores)


def main():
    equipo1 = EquipoFutbol("Barcelona")
    equipo2 = EquipoFutbol("Real Madrid")

    equipo1.jugadores.append("Lamine")
    equipo1.jugadores.append("Pedri")
    equipo1.jugadores.append("Raphina")
    equipo1.jugadores.append("Lewandowski")
    equipo1.jugadores.append("Cubarsi")
    equipo1.jugadores.append("Bernal")

    equipo2.jugadores.append("Vini")
    equipo2.jugadores.append("Mbappe")
    equipo2.jugadores.append("Valverde")
    equipo2.jugadores.append("Camavinga")
    equipo2.jugadores.append("Courtois")

    print(f"{equipo1.nombre_equipo} tiene {len(equipo1)} jugadores")
    print(f"{equipo2.nombre_equipo} tiene {len(equipo2)} jugadores")

main()