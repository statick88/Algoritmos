class Contactos:
    def __init__(self, nombre, apellido, numero, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Numero: {self.numero}, Edad: {self.edad}"


def mostrar_contactos(contactos):
    if contactos:
        print("Contactos ingresados ingresadas:")
        for contacto in contactos:
            print(contacto)
    else:
        print("No se han ingresado contactos.")


def eliminar_contacto(contactos):
    if contactos:
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        contactos_filtrados = [contacto for contacto in contactos if contacto.nombre != nombre]
        if len(contactos_filtrados) < len(contactos):
            contactos[:] = contactos_filtrados
            print("Contacto eliminada exitosamente.")
        else:
            print("No se encontró a un contacto con ese nombre.")
    else:
        print("No se han ingresado contactos.")


def modificar_contacto(contactos):
    if contactos:
        nombre = input("Ingrese el nombre del contacto a modificar: ")
        for contacto in contactos:
            if contacto.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del contacto: ")
                nuevo_apellido = input("Ingrese el nuevo apellido del contacto: ")
                nuevo_numero = int(input("Ingrese el nuevo numero del contacto: "))
                nuevo_edad = int(input("Ingrese la nueva edad del contacto: "))
                contacto.nombre = nuevo_nombre
                contacto.apellido = nuevo_apellido
                contacto.numero = nuevo_numero
                contacto.edad = nuevo_edad
                print("Contacto modificada exitosamente.")
                return
        print("No se encontró a un contacto con ese nombre.")
    else:
        print("No se han ingresado contactos.")

def menu():
    contactos = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar contacto")
        print("2. Mostrar contactos")
        print("3. Eliminar contacto")
        print("4. Modificar contacto")
        print("0. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 2:
            nombre = input("Ingrese el nombre de la persona: ")
            apellido = input("Ingrese el apellido de la persona: ")
            numero = int(input("Ingrese el numero de la persona: "))
            edad = int(input("Ingrese la edad de la persona: "))
            
            contacto = Contactos(nombre, apellido, numero, edad)
            contactos.append(contacto)
            print("Contacto ingresada exitosamente.")
        elif opcion == 2:
            mostrar_contactos(contactos)
        elif opcion == 3:
            eliminar_contacto(contactos)
        elif opcion == 4:
            modificar_contacto(contactos)
        elif opcion == 0:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()