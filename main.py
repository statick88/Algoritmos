class Pelicula:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


def mostrar_peliculas(peliculas):
    if peliculas:
        print("Películas ingresadas:")
        for pelicula in peliculas:
            print(pelicula)
    else:
        print("No se han ingresado películas.")


def eliminar_pelicula(peliculas):
    if peliculas:
        nombre = input("Ingrese el nombre de la película a eliminar: ")
        peliculas_filtradas = [pelicula for pelicula in peliculas if pelicula.nombre != nombre]
        if len(peliculas_filtradas) < len(peliculas):
            peliculas[:] = peliculas_filtradas
            print("Película eliminada exitosamente.")
        else:
            print("No se encontró una película con ese nombre.")
    else:
        print("No se han ingresado películas.")



def modificar_pelicula(peliculas):
    if peliculas:
        nombre = input("Ingrese el nombre de la película a modificar: ")
        for pelicula in peliculas:
            if pelicula.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre de la película: ")
                nuevo_anio = int(input("Ingrese el nuevo año de la película: "))
                pelicula.nombre = nuevo_nombre
                pelicula.anio = nuevo_anio
                print("Película modificada exitosamente.")
                return
        print("No se encontró una película con ese nombre.")
    else:
        print("No se han ingresado películas.")

def menu():
    peliculas = []

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
            anio = int(input("Ingrese el año de la película: "))
            pelicula = Pelicula(nombre, anio)
            peliculas.append(pelicula)
            print("Película ingresada exitosamente.")
        elif opcion == "2":
            mostrar_peliculas(peliculas)
        elif opcion == "3":
            eliminar_pelicula(peliculas)
        elif opcion == "4":
            modificar_pelicula(peliculas)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()