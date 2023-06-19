class Persona:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


def mostrar_personas(personas):
    if personas:
        print("Personas ingresadas:")
        for persona in personas:
            print(persona)
    else:
        print("No se han ingresado las personas.")


def eliminar_persona(personas):
    if personas:
        nombre = input("Ingrese el nombre de la persona a eliminar: ")
        personas_filtradas = [persona for persona in personas if persona.nombre != nombre]
        if len(personas_filtradas) < len(personas):
            personas[:] = personas_filtradas
            print("Persona eliminada exitosamente.")
        else:
            print("No se encontró una persona con ese nombre.")
    else:
        print("No se han ingresado personas.")



def modificar_persona(personas):
    if personas:
        nombre = input("Ingrese el nombre de la persona a modificar: ")
        for persona in personas:
            if persona.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre de la persona: ")
                nuevo_anio = int(input("Ingrese el nuevo año de la persona: "))
                persona.nombre = nuevo_nombre
                persona.anio = nuevo_anio
                print("Persona modificada exitosamente.")
                return
        print("No se encontró una persona con ese nombre.")
    else:
        print("No se han ingresado las personas.")

def menu():
    personas = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar personas con su año de nacimiento")
        print("2. Mostrar personas con año de nacimiento")
        print("3. Eliminar personas")
        print("4. Modificar personas")
        print
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la persona: ")
            anio = int(input("Ingrese el año de la persona: "))
            persona = Persona(nombre, anio)
            personas.append(persona)
            print("Persona ingresada exitosamente.")
        elif opcion == "2":
            mostrar_personas(personas)
        elif opcion == "3":
            eliminar_persona(personas)
        elif opcion == "4":
            modificar_persona(personas)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()