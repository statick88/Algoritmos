class Gato:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def __str__(self):
        return f"{self.nombre} ({self.raza})"


def mostrar_gatos(gatos):
    if gatos:
        print("Gatos ingresados:")
        for gato in gatos:
            print(gato)
    else:
        print("No se han ingresado gatos.")


def eliminar_gato(gatos):
    if gatos:
        nombre = input("Ingrese el nombre del gato a eliminar: ")
        gatos_filtrados = [gato for gato in gatos if gato.nombre != nombre]
        if len(gatos_filtrados) < len(gatos):
            gatos[:] = gatos_filtrados
            print("Gato eliminado exitosamente.")
        else:
            print("No se encontró un gato con ese nombre.")
    else:
        print("No se han ingresado gatos.")


def modificar_gato(gatos):
    if gatos:
        nombre = input("Ingrese el nombre del gato a modificar: ")
        for gato in gatos:
            if gato.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del gato: ")
                nueva_raza = input("Ingrese la nueva raza del gato: ")
                gato.nombre = nuevo_nombre
                gato.raza = nueva_raza
                print("Gato modificado exitosamente.")
                return
        print("No se encontró un gato con ese nombre.")
    else:
        print("No se han ingresado gatos.")


def menu():
    gatos = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar gato")
        print("2. Mostrar gatos")
        print("3. Eliminar gato")
        print("4. Modificar gato")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del gato: ")
            raza = input("Ingrese la raza del gato: ")
            gato = Gato(nombre, raza)
            gatos.append(gato)
            print("Gato ingresado exitosamente.")
        elif opcion == "2":
            mostrar_gatos(gatos)
        elif opcion == "3":
            eliminar_gato(gatos)
        elif opcion == "4":
            modificar_gato(gatos)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()
