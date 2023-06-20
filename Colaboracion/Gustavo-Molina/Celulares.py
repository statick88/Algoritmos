class Celular:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


def mostrar_celulares(celulares):
    if celulares:
        print("Celulares ingresadas:")
        for celular in celulares:
            print(celular)
    else:
        print("No se han ingresado el celular.")


def eliminar_celular(celulares):
    if celulares:
        nombre = input("Ingrese el nombre del celular a eliminar: ")
        celulares_filtradas = [celular for celular in celulares if celular.nombre != nombre]
        if len(celulares_filtradas) < len(celulares):
            celulares[:] = celulares_filtradas
            print("Celular eliminado exitosamente.")
        else:
            print("No se encontró un celular con ese nombre.")
    else:
        print("No se han ingresado el celular.")



def modificar_celular(celulares):
    if celulares:
        nombre = input("Ingrese el nombre del celular a modificar: ")
        for celular in celulares:
            if celular.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del celular: ")
                nuevo_anio = int(input("Ingrese el nuevo año del celular: "))
                celular.nombre = nuevo_nombre
                celular.anio = nuevo_anio
                print("Celular modificado exitosamente.")
                return
        print("No se encontró un celular con ese nombre.")
    else:
        print("No se han ingresado celulares.")

def menu():
    celulares = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar celular")
        print("2. Mostrar celulares")
        print("3. Eliminar celular")
        print("4. Modificar celular")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del celular: ")
            anio = int(input("Ingrese el año del celular: "))
            celular = Celular(nombre, anio)
            celulares.append(celular)
            print("Celular ingresado exitosamente.")
        elif opcion == "2":
            mostrar_celulares(celulares)
        elif opcion == "3":
            eliminar_celular(celulares)
        elif opcion == "4":
            modificar_celular(celulares)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()