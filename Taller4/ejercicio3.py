class Playlist:

    def __init__(self, nombre_playlist: str):
        self.nombre_playlist = nombre_playlist
        self.canciones = []

    def __len__(self):
        return len(self.canciones)
    
    def addSong(self, song: str):
        self.canciones.append(song)


def main():
    playlist = Playlist("Favoritas")

    playlist.addSong("Gil")
    playlist.addSong("Love me Not")
    playlist.addSong("Smells Like Teen Spirit")
    playlist.addSong("Kilometros")
    playlist.addSong("Judas")
    playlist.addSong("Afraid")

    print(f"Número de canciones en la playlist: {len(playlist)}")

main()