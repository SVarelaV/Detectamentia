from controlador.dominios.paciente import Paciente
from controlador.gestores.pacientes import Pacientes
from controlador.gestores.listagen import ListaGen

def crear_paciente():
    try:
        id = int(input("Ingrese ID del paciente: "))
        nombre = input("Ingrese nombre: ")
        apellido1 = input("Ingrese primer apellido: ")
        apellido2 = input("Ingrese segundo apellido: ")
        genero = input("Ingrese género: ")
        edad = int(input("Ingrese edad: "))
        poblacion = input("Ingrese población: ")
        ocupacion = input("Ingrese ocupación: ")
        nivelEstudios = input("Ingrese nivel de estudios: ")

        return Paciente(id, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios)
    except ValueError:
        print("Error en los datos introducidos.")
        return None

def menu():
    lista_pacientes = ListaGen()

    while True:
        print("\n--- MENÚ PACIENTES ---")
        print("1. Agregar paciente")
        print("2. Buscar paciente por ID")
        print("3. Eliminar paciente por ID")
        print("4. Mostrar todos los pacientes")
        print("5. Comprobar si existe paciente")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            paciente = crear_paciente()
            if paciente:
                if lista_pacientes.agregar(paciente):
                    print("Paciente agregado correctamente.")
                else:
                    print("El paciente ya existe.")

        elif opcion == "2":
            try:
                id_buscar = int(input("Ingrese ID a buscar: "))
                paciente = lista_pacientes.buscar(id_buscar)
                if paciente:
                    print(f"Paciente encontrado: {paciente.nombre} {paciente.apellido1} {paciente.apellido2}")
                else:
                    print("Paciente no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "3":
            try:
                id_eliminar = int(input("Ingrese ID a eliminar: "))
                if lista_pacientes.eliminar(id_eliminar):
                    print("Paciente eliminado.")
                else:
                    print("Paciente no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "4":
            pacientes = lista_pacientes.mostrar_todos()
            if pacientes:
                for p in pacientes:
                    print(f"{p.id} - {p.nombre} {p.apellido1} {p.apellido2}")
            else:
                print("No hay pacientes registrados.")

        elif opcion == "5":
            paciente = crear_paciente()
            if paciente:
                if lista_pacientes.existe(paciente):
                    print("El paciente ya existe en la lista.")
                else:
                    print("El paciente NO existe en la lista.")

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
