class Carro:
    def __init__(self, marca, anio):
        self.marca = marca
        self.anio = anio

    def __str__(self):
        return f"{self.marca} ({self.anio})"


def mostrar_carro(carros):
    if carros:
        print("Carros ingresados:")
        for carro in carros:
            print(carro)
    else:
        print("No se han ingresado carros.")


def eliminar_pelicula(carros):
    if carros:
        marca = input("Ingrese el la marca del carro a eliminar: ")
        carro_filtradas = [carro for carro in carros if carro.marca != marca]
        if len(carro_filtradas) < len(carros):
            carros[:] = carro_filtradas
            print("Carro eliminada exitosamente.")
        else:
            print("No se encontró una carro con ese nombre.")
    else:
        print("No se han ingresado carros.")



def modificar_pelicula(carros):
    if carros:
        marca = input("Ingrese la marca del carro a modificar: ")
        for carro in carros:
            if carro.marca == marca:
                nuevo_nombre = input("Ingrese la nueva marca del carro: ")
                nuevo_anio = int(input("Ingrese el nuevo año del carro: "))
                carro.marca = nuevo_nombre
                carro.anio = nuevo_anio
                print("Carro modificado exitosamente.")
                return
        print("No se encontró un carro con esa marca.")
    else:
        print("No se han ingresado carros.")

def menu():
    carro = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar carro")
        print("2. Mostrar carros")
        print("3. Eliminar carro")
        print("4. Modificar carro")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            marca = input("Ingrese la marca de la carro: ")
            anio = int(input("Ingrese el año del carro: "))
            pelicula = Carro(marca, anio)
            carro.append(pelicula)
            print("carro ingresada exitosamente.")
        elif opcion == "2":
            mostrar_carro(carro)
        elif opcion == "3":
            eliminar_pelicula(carro)
        elif opcion == "4":
            modificar_pelicula(carro)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()