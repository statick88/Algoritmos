class VideoJuego:
    def __init__(self, nombre, plataforma):
        self.nombre = nombre
        self.plataforma = plataforma

    def __str__(self):
        return f"{self.nombre} ({self.plataforma})"

def mostrar_videojuegos(videojuegos):
    if videojuegos:
        print("Videojuegos ingresados:")
        for videojuego in videojuegos:
            print(videojuego)
    else:
        print("No se han ingresado videojuegos.")

def eliminar_videojuego(videojuegos):
    if videojuegos:
        nombre = input("Ingrese el nombre del videojuego a eliminar: ")
        videojuegos_filtrados = [videojuego for videojuego in videojuegos if videojuego.nombre != nombre]
        if len(videojuegos_filtrados) < len(videojuegos):
            videojuegos[:] = videojuegos_filtrados
            print("Videojuego eliminado exitosamente.")
        else:
            print("No se encontró un videojuego con ese nombre.")
    else:
        print("No se han ingresado videojuegos.")

def modificar_videojuego(videojuegos):
    if videojuegos:
        nombre = input("Ingrese el nombre del videojuego a modificar: ")
        for videojuego in videojuegos:
            if videojuego.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del videojuego: ")
                nueva_plataforma = input("Ingrese la nueva plataforma del videojuego: ")
                videojuego.nombre = nuevo_nombre
                videojuego.plataforma = nueva_plataforma
                print("Videojuego modificado exitosamente.")
                return
        print("No se encontró un videojuego con ese nombre.")
    else:
        print("No se han ingresado videojuegos.")

def menu():
    videojuegos = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar videojuego")
        print("2. Mostrar videojuegos")
        print("3. Eliminar videojuego")
        print("4. Modificar videojuego")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del videojuego: ")
            plataforma = input("Ingrese la plataforma del videojuego: ")
            videojuego = VideoJuego(nombre, plataforma)
            videojuegos.append(videojuego)
            print("Videojuego ingresado exitosamente.")
        elif opcion == "2":
            mostrar_videojuegos(videojuegos)
        elif opcion == "3":
            eliminar_videojuego(videojuegos)
        elif opcion == "4":
            modificar_videojuego(videojuegos)
        elif opcion == "0":
            print("¡Chao Chao!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

menu()
