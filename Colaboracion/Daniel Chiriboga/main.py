class Menu:
    def __init__(self, platillo, precio):
        self.platillo = platillo
        self.precio = precio

    def __str__(self):
        return f"{self.platillo} ({self.precio})"


def mostrar_platillos(platillos):
    if platillos:
        print("Películas ingresadas:")
        for platillo in platillos:
            print(platillo)
    else:
        print("No se han ingresado películas.")


def eliminar_pelicula(platillos):
    if platillos:
        nombre = input("Ingrese el nombre de la película a eliminar: ")
        peliculas_filtradas = [platillo for platillo in platillos if platillo.nombre != nombre]
        if len(peliculas_filtradas) < len(platillos):
            platillos[:] = peliculas_filtradas
            print("Película eliminada exitosamente.")
        else:
            print("No se encontró una película con ese nombre.")
    else:
        print("No se han ingresado películas.")



def modificar_pelicula(platillos):
    if platillos:
        nombre = input("Ingrese el nombre de la película a modificar: ")
        for platillo in platillos:
            if platillo.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre de la película: ")
                nuevo_precio = int(input("Ingrese el nuevo año de la película: "))
                platillo.nombre = nuevo_nombre
                platillo.precio = nuevo_precio
                print("Película modificada exitosamente.")
                return
        print("No se encontró una película con ese nombre.")
    else:
        print("No se han ingresado películas.")

def menu():
    platillos = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar película")
        print("2. Mostrar películas")
        print("3. Eliminar película")
        print("4. Modificar película")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la película: ")
            precio = int(input("Ingrese el año de la película: "))
            platillo = Menu(nombre, precio)
            platillos.append(platillo)
            print("Película ingresada exitosamente.")
        elif opcion == "2":
            mostrar_platillo(platillos)
        elif opcion == "3":
            eliminar_pelicula(platillos)
        elif opcion == "4":
            modificar_pelicula(platillos)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()