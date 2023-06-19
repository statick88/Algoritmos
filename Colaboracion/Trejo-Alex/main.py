"""
Modelos discretos para Ingenieria en Software
Nombre: Alex Trejo
NRC:9714
Fecha: 19/6/2023


"""

class Computadora:
    def __init__(self, nombre, anioFabricacion, procesador):
        self.nombre = nombre
        self.anioFabricacion = anioFabricacion
        self.procesador = procesador

    def __str__(self):
        return f"{self.nombre} ({self.anioFabricacion}) ({self.procesador})"


def mostrar_computadora(computadoras):
    if computadoras:
        print("Equipos ingresados:")
        for computadora in computadoras:
            print(computadora)
    else:
        print("No se han ingresados equipos.")


def eliminar_computadora(computadora):
    if computadora:
        nombre = input("Ingrese el modelo del equipo a eliminar: ")
        computadoraas_filtradas = [computadora for computadora in computadora if computadora.nombre != nombre]
        if len(computadoraas_filtradas) < len(computadora):
            computadora[:] = computadoraas_filtradas
            print("Equipo eliminado correctamente.")
        else:
            print("No se encontró el equipo ingresado.")
    else:
        print("No se han ingresado equipos.")



def modificar_computadora(computadoras):
    if computadoras:
        nombre = input("Ingrese el modelo del equipo a modificar: ")
        for computadora in computadoras:
            if computadora.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo modelo del equipo: ")
                nuevo_anio = int(input("Ingrese el nuevo año de fabricacion: "))
                nuevo_procesador= input("Ingrese el nuevo procesador: ")
                computadora.nombre = nuevo_nombre
                computadora.anioFabricacion = nuevo_anio
                computadora.procesador= nuevo_procesador
                print("Equipo modificado.")
                return
        print("No se encontró una equipo con ese modelo.")
    else:
        print("No se han ingresado equipos.")

def menu():
    computadoras = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar computadora")
        print("2. Mostrar computadora")
        print("3. Eliminar computadora")
        print("4. Modificar computadora")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el modelo de la computadora: ")
            anio = int(input("Ingrese el año fabricacion: "))
            procesador=input("Ingrese el procesador: ")
            computadora = Computadora(nombre, anio,procesador)
            computadoras.append(computadora)
            print("Equipo ingresado correctamente.")
        elif opcion == "2":
            mostrar_computadora(computadoras)
        elif opcion == "3":
            eliminar_computadora(computadoras)
        elif opcion == "4":
            modificar_computadora(computadoras)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()