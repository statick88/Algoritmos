class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def __str__(self):
        return f"{self.nombre} - {self.especie}"


def mostrar_mascotas(mascotas):
    if mascotas:
        print("Mascotas ingresadas:")
        for m in mascotas:
            print(m)
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
                nuevo_especie = int(input("Ingrese el nuevo año de la mascota: "))
                mascota.nombre = nuevo_nombre
                mascota.especie = nuevo_especie
                print("mascota modificada exitosamente.")
                return
        print("No se encontró una mascota con ese nombre.")
    else:
        print("No se han ingresado mascotas.")

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
            especie = input("Ingrese la especie de la mascota: ")
            mascota = Mascota(nombre, especie)
            mascotas.append(mascota)
            print("mascota ingresada exitosamente.")
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
system("pause")