from paciente import Paciente
from pacientes import Pacientes

class GestionPacientes:
    def __init__(self):
        self.lista_pacientes = Pacientes()

    def mostrar_menu(self):
        print("\n--- Gestión de Pacientes ---")
        print("1. Agregar paciente")
        print("2. Buscar paciente")
        print("3. Eliminar paciente")
        print("4. Mostrar pacientes")
        print("5. Salir")

    def agregar_paciente(self):
        print("\n--- Agregar Paciente ---")
        id_paciente = input("ID del paciente: ")
        nombre = input("Nombre: ")
        apellido1 = input("Primer apellido: ")
        apellido2 = input("Segundo apellido: ")
        fecha_nacimiento = input("Fecha de nacimiento (DD-MM-YYYY): ")
        genero = input("Género: ")

        if self.lista_pacientes.existe_paciente(id_paciente):
            print("Error: El ID del paciente ya existe.")
            return

        paciente = Paciente(id_paciente, nombre, apellido1, apellido2, fecha_nacimiento, genero)
        self.lista_pacientes.agregar_paciente(paciente)
        print("Paciente agregado correctamente.")

    def buscar_paciente(self):
        print("\n--- Buscar Paciente ---")
        id_paciente = input("ID del paciente: ")
        paciente = self.lista_pacientes.buscar_paciente(id_paciente)
        if paciente:
            print(f"Paciente encontrado:\n{paciente}")
            print(f"ID: {paciente.id_paciente}, Nombre: {paciente.nombre}, "
                  f"Primer Apellido: {paciente.apellido1}, Segundo Apellido: {paciente.apellido2}, "
                  f"Fecha de Nacimiento: {paciente.fecha_nacimiento}, Género: {paciente.genero}")
        else:
            print("Paciente no encontrado.")

    def eliminar_paciente(self):
        print("\n--- Eliminar Paciente ---")
        id_paciente = input("ID del paciente: ")
        if self.lista_pacientes.eliminar_paciente(id_paciente):
            print("Paciente eliminado correctamente.")
        else:
            print("Paciente no encontrado.")

    def mostrar_pacientes(self):
        print("\n--- Lista de Pacientes ---")
        pacientes = self.lista_pacientes.lista_pacientes
        if not pacientes:
            print("No hay pacientes registrados.")
        else:
            for paciente in pacientes:
                print(f"ID: {paciente.id_paciente}, Nombre: {paciente.nombre}, "
                      f"Primer Apellido: {paciente.apellido1}, Segundo Apellido: {paciente.apellido2}, "
                      f"Fecha de Nacimiento: {paciente.fecha_nacimiento}, Género: {paciente.genero}")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_paciente()
            elif opcion == "2":
                self.buscar_paciente()
            elif opcion == "3":
                self.eliminar_paciente()
            elif opcion == "4":
                self.mostrar_pacientes()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    gestion = GestionPacientes()
    gestion.ejecutar()