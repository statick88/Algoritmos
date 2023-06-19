class VideoJuego:
    def __init__(self, nombre, desarrolladora, anio):
        self.nombre = nombre
        self.desarrolladora = desarrolladora
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} {self.desarrolladora} ({self.anio})"


def mostrar_videojuegos(videoJuegos):
    if videoJuegos:
        print("Video juegos ingresadas:")
        for videoJuego in videoJuegos:
            print(videoJuego)
    else:
        print("No se han ingresado Video juegos.")


def eliminar_videojuego(videoJuegos):
    if videoJuegos:
        nombre = input("Ingrese el nombre del video juego a eliminar: ")
        VideoJuego_filtradas = [videoJuego for videoJuego in videoJuegos if videoJuego.nombre != nombre]
        if len(VideoJuego_filtradas) < len(videoJuegos):
            videoJuegos[:] = VideoJuego_filtradas
            print("Videojuego eliminado exitosamente.")
        else:
            print("No se encontró una video juego con ese nombre.")
    else:
        print("No se han ingresado Video juegos.")



def modificar_videjojuego(videoJuegos):
    if videoJuegos:
        nombre = input("Ingrese el nombre del Vide jouego a modificar: ")
        for videoJuego in videoJuegos:
            if videoJuego.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del Video juego: ")
                nuevo_desarrollador = input("Ingrese el nuevo Desarrollador del videojuego: ")
                nuevo_anio = int(input("Ingrese el nuevo año del videojuego: "))

                videoJuego.nombre = nuevo_nombre
                videoJuego.desarrollador = nuevo_desarrollador
                videoJuego.anio = nuevo_anio
                print("videojuego modificada exitosamente.")
                return
        print("No se encontró un videojuego con ese nombre.")
    else:
        print("No se han ingresado videojuegos.")

def menu():
    videoJuegos = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar video juego")
        print("2. Mostrar video juegos")
        print("3. Eliminar video juego")
        print("4. Modificar video juego")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del videojuego: ")
            desarrolladora = input("Ingrese el nombre de la desarrrolladora: ")
            anio = int(input("Ingrese el año del videojuego: "))
            videoJuego = VideoJuego(nombre,desarrolladora, anio)
            videoJuegos.append(videoJuego)
            print("Video juego ingresada exitosamente.")
        elif opcion == "2":
            mostrar_videojuegos(videoJuegos)
        elif opcion == "3":
            eliminar_videojuego(videoJuegos)
        elif opcion == "4":
            modificar_videjojuego(videoJuegos)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()