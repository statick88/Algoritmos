class MascotaVirtual:
    def __init__(self, nombre, dueno, sprite):
        self.nombre = nombre
        self.dueno = dueno
        self.sprite = sprite

    def __str__(self):
        return f"Mascota: {self.nombre}\nDueño: {self.dueno}\nSprite: {self.sprite}"


def mostrar_mascotas(mascotas):
    if mascotas:
        print("╔══════════════════════════╗")
        print("║         MASCOTAS         ║")
        print("╠══════════════════════════╣")
        for mascota in mascotas:
            print("║", mascota)
            print("╠══════════════════════════╣")
        print("║                          ║")
        print("╚══════════════════════════╝")
    else:
        print("No se han ingresado mascotas.")



def eliminar_mascota(mascotas):
    if mascotas:
        nombre = input("Ingrese el nombre de la mascota a eliminar: ")
        mascotas_filtradas = [mascota for mascota in mascotas if mascota.nombre != nombre]
        if len(mascotas_filtradas) < len(mascotas):
            mascotas[:] = mascotas_filtradas
            print("Mascota eliminada exitosamente.")
        else:
            print("No se encontró una mascota con ese nombre.")
    else:
        print("No se han ingresado mascotas.")


def modificar_mascota(mascotas):
    if mascotas:
        nombre = input("Ingrese el nombre de la mascota a modificar: ")
        for mascota in mascotas:
            if mascota.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre de la mascota: ")
                nuevo_dueno = input("Ingrese el nuevo nombre del dueño: ")
                nuevo_sprite = elegir_sprite()
                mascota.nombre = nuevo_nombre
                mascota.dueno = nuevo_dueno
                mascota.sprite = nuevo_sprite
                print("Mascota modificada exitosamente.")
                return
        print("No se encontró una mascota con ese nombre.")
    else:
        print("No se han ingresado mascotas.")


def elegir_sprite():
    opciones_sprite = [
        "😺",
        "🐶",
        "🐰",
        "🐠",
        "🐦",
        "🐸"
    ]

    print("Sprites disponibles:")
    for i, sprite in enumerate(opciones_sprite):
        print(f"{i + 1}. {sprite}")

    while True:
        opcion = input("Ingrese el número del sprite deseado: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(opciones_sprite):
            return opciones_sprite[int(opcion) - 1]
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")



def menu():
    mascotas = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar mascota")
        print("2. Mostrar mascotas")
        print("3. Eliminar mascota")
        print("4. Modificar mascota")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la mascota: ")
            dueno = input("Ingrese el nombre del dueño: ")
            sprite = elegir_sprite()
            mascota = MascotaVirtual(nombre, dueno, sprite)
            mascotas.append(mascota)
            print("Mascota ingresada exitosamente.")
        elif opcion == "2":
            mostrar_mascotas(mascotas)
        elif opcion == "3":
            eliminar_mascota(mascotas)
        elif opcion == "4":
            modificar_mascota(mascotas)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()
