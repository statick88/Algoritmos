class Videojuego:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.nombre} ({self.descripcion})"


def mostrar_videojuegos(videojuegos):
    if videojuegos:
        print("Videojuegos ingresados:")
        for videojuego in videojuegos:
            print(videojuego)
    else:
        print("No se han ingresado nada.")


def eliminar_videojuego(videojuegos):
    if videojuegos:
        nombre = input("Ingrese el nombre del videojuego a eliminar: ")
        vj_filtr = [videojuego for videojuego in videojuegos if videojuego.nombre != nombre]
        if len(vj_filtr) < len(videojuegos):
            videojuegos[:] = vj_filtr
            print("Videojuego eliminado exitosamente.")
        else:
            print("No se encontró nada con ese nombre.")
    else:
        print("No se ha ingresado nada.")



def modificar_videojuego(videojuegos):
    if videojuegos:
        nombre = input("Ingrese el nombre del videojuego a modificar: ")
        for videojuego in videojuegos:
            if videojuego.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del videojuego: ")
                nuevo_descripcion = input("Ingrese la nueva descripcion del videojuego: ")
                videojuego.nombre = nuevo_nombre
                videojuego.descripcion = nuevo_descripcion
                print("Modificacion exitosa.")
                return
        print("No se encontró nada con ese nombre.")
    else:
        print("No se ha ingresado nada.")

def menu():
    videojuegos = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar videojuego")
        print("2. Mostrar videojuego/s")
        print("3. Eliminar videojuego/s")
        print("4. Modificar videojuego/s")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del videojuego: ")
            descripcion = input("Ingrese una descripcion del videojuego: ")
            videojuego = Videojuego(nombre, descripcion)
            videojuegos.append(videojuego)
            print("Registro del videojuego exitoso.")
        elif opcion == "2":
            mostrar_videojuegos(videojuegos)
        elif opcion == "3":
            eliminar_videojuego(videojuegos)
        elif opcion == "4":
            modificar_videojuego(videojuegos)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()