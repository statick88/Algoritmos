class Equipo:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


def mostrar_equipos(equipos):
    if equipos:
        print("equipos de futbol ingresados:")
        for equipo in equipos:
            print(equipo)
    else:
        print("No se han ingresado equipos de futbol.")


def eliminar_equipo(equipos):
    if equipos:
        nombre = input("Ingrese el nombre de la equipos de futbol a eliminar: ")
        equipos_filtradas = [equipo for equipo in equipos if equipo.nombre != nombre]
        if len(equipos_filtradas) < len(equipos):
            equipos[:] = equipos_filtradas
            print("equipo de futbol eliminado exitosamente.")
        else:
            print("No se encontró un equipo de futbol con ese nombre.")
    else:
        print("No se han ingresado equipos de futbol.")



def modificar_equipo(equipos):
    if equipos:
        nombre = input("Ingrese el nombre del equipo de futbol a modificar: ")
        for equipo in equipos:
            if equipo.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del equipo de futbol: ")
                nuevo_anio = int(input("Ingrese el año de creacion del equipo de futbol: "))
                equipo.nombre = nuevo_nombre
                equipo.anio = nuevo_anio
                print("equipo de futbol modificado exitosamente.")
                return
        print("No se encontró un equipo de futbol con ese nombre.")
    else:
        print("No se han ingresado equipos de futbol.")

def menu():
    equipos = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar equipos de futbol")
        print("2. Mostrar equipos de futbol")
        print("3. Eliminar equipos de futbol")
        print("4. Modificar equipos de futbol")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del equipo de futbol: ")
            anio = int(input("Ingrese el año de creacion del equipo de futbol: "))
            equipo = Equipo(nombre, anio)
            equipos.append(equipo)
            print("equipo de futbol ingresado exitosamente.")
        elif opcion == "2":
            mostrar_equipos(equipos)
        elif opcion == "3":
            eliminar_equipo(equipos)
        elif opcion == "4":
            modificar_equipo(equipos)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()