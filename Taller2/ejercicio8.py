from io import *
from datetime import datetime, timedelta

class Evento:
    titulo = ""
    fecha = ""
    hora = ""
    lugar = ""
    responsable = ""

    def save(self):
        file = open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller2\archivos\agenda.txt", "a")

        file.write(f"{self.titulo},{self.fecha},{self.hora},{self.lugar},{self.responsable}\n")

        file.close()

    def next_week_events(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller2\archivos\agenda.txt", "r") as file:
            today = datetime.now()
            limit = today + timedelta(days = 7)

            print("Eventos en la proxima semana: ")
            for line in file:
                event = line.strip().split(",")

                eventDate = datetime.strptime(event[1] + " " + event[2], "%Y-%m-%d %H:%M")

                if today <= eventDate <= limit:
                    print(f"{event[0]} - {event[1]} - {event[2]} - {event[3]} - {event[4]}\n")
                else:
                    pass
            print()
            
def main():
    tam = int(input("Ingrese la cantidad de eventos a guardar en el archivo: "))

    temp = Evento()
    for i in range(tam):
        print(f"\nEvento {i+1}")
        temp.titulo = input(f"Ingrese el titulo del evento {i+1}: ")
        temp.fecha = input(f"Ingrese la fecha del evento {i+1} (YYYY-MM-DD): ")
        temp.hora = input(f"Ingerse la hora del evento {i+1} (HH:MM): ")
        temp.lugar = input(f"Ingerse el lugar del evento {i+1}: ")
        temp.responsable = input(f"Ingrese el responsable del evento {i+1}: ")

        temp.save()

    temp.next_week_events()


main()