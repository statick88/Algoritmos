class Pelicula:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


def mostrar_peliculas(peliculas):
    if peliculas:
        print("aviones ingresadas:")
        for pelicula in peliculas:
            print(pelicula)
    else:
        print("No se han ingresado aviones.")


def eliminar_pelicula(peliculas):
    if peliculas:
        nombre = input("Ingrese el nombre de la avión a eliminar: ")
        peliculas_filtradas = [pelicula for pelicula in peliculas if pelicula.nombre != nombre]
        if len(peliculas_filtradas) < len(peliculas):
            peliculas[:] = peliculas_filtradas
            print("avión eliminada exitosamente.")
        else:
            print("No se encontró una avión con ese nombre.")
    else:
        print("No se han ingresado aviones.")



def modificar_pelicula(peliculas):
    if peliculas:
        nombre = input("Ingrese el nombre de la avión a modificar: ")
        for pelicula in peliculas:
            if pelicula.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre de la avión: ")
                nuevo_anio = int(input("Ingrese el nuevo año de la avión: "))
                pelicula.nombre = nuevo_nombre
                pelicula.anio = nuevo_anio
                print("avión modificada exitosamente.")
                return
        print("No se encontró una avión con ese nombre.")
    else:
        print("No se han ingresado aviones.")

def dibujar_avion():
    print ("                   [ - .")
    print ("                    [ ....\ -")
    print ("         [ .\ __ ....[......\ ..... .._")
    print ("       -- { __ ...............( ) ( ) _ >;")
    print ("         [ ./ .......[......./ ' ' ")
    print ("                    [._. /-")
    print ("                   [ _./")

def menu():
    peliculas = []

    while True:
        print("------ MENÚ ------")
        dibujar_avion()
        print("1. Ingresar avión")
        print("2. Mostrar aviones")
        print("3. Eliminar avión")
        print("4. Modificar avión")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la avión: ")
            anio = int(input("Ingrese el año de la avión: "))
            pelicula = Pelicula(nombre, anio)
            peliculas.append(pelicula)
            print("avión ingresada exitosamente.")
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