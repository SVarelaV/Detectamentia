from controlador.dominios.paciente import Paciente
from controlador.gestores.pacientes import Pacientes


class GestorPacientes:
    """Gestor que maneja las operaciones sobre pacientes."""

    def __init__(self):
        self.lista_pacientes = Pacientes()
        self._cargar_ejemplos()

    def _cargar_ejemplos(self):
        """Carga algunos pacientes de ejemplo."""
        self.lista_pacientes.agregar(Paciente(1, "Juan", "Pérez", "Gómez", "Masculino", 72, "Madrid", "Jubilado", "Secundaria completa"))
        self.lista_pacientes.agregar(Paciente(2, "Ana", "López", "Martínez", "Femenino", 68, "Barcelona", "Ama de casa", "Primaria completa"))

    def mostrar_menu(self):
        """Muestra el menú de opciones."""
        print("\n" + "="*50)
        print("🧠 GESTOR DE PACIENTES - DetectaMentIA")
        print("="*50)
        print("1. ➕ Agregar paciente")
        print("2. 🔍 Buscar paciente por ID")
        print("3. 🗑️  Eliminar paciente por ID")
        print("4. 📋 Mostrar todos los pacientes")
        print("5. 🚪 Salir")
        print("="*50)

    def mostrar_paciente(self, paciente: Paciente):
        """Imprime los datos de un paciente con íconos."""
        print(f"👤 ID: {paciente.id} | {paciente.nombre} {paciente.apellido1} {paciente.apellido2} | {paciente.edad} años | "
              f" {paciente.poblacion} | {paciente.ocupacion} | {paciente.nivelEstudios}")

    def ejecutar(self):
        """Ejecuta el ciclo principal de interacción."""
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                self._agregar_paciente()
            elif opcion == "2":
                self._buscar_paciente()
            elif opcion == "3":
                self._eliminar_paciente()
            elif opcion == "4":
                self._mostrar_todos()
            elif opcion == "5":
                print("\n👋 ¡Gracias por usar el Gestor de Pacientes!")
                break
            else:
                print("❌ Opción inválida. Intenta de nuevo.")

    def _agregar_paciente(self):
        try:
            print("\n➕ Agregar nuevo paciente")
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            apellido1 = input("Primer apellido: ")
            apellido2 = input("Segundo apellido: ")
            genero = input("Género: ")
            edad = int(input("Edad: "))
            poblacion = input("Población: ")
            ocupacion = input("Ocupación: ")
            nivelEstudios = input("Nivel de estudios: ")

            paciente = Paciente(id, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios)
            if self.lista_pacientes.agregar(paciente):
                print("✅ Paciente agregado correctamente.")
            else:
                print("⚠️ Ya existe un paciente con ese ID.")
        except Exception as e:
            print(f"❌ Error al agregar paciente: {e}")

    def _buscar_paciente(self):
        try:
            id = int(input("\n🔍 ID del paciente a buscar: "))
            paciente = self.lista_pacientes.buscar(id)
            if paciente:
                print("\n👁️ Paciente encontrado:")
                self.mostrar_paciente(paciente)
            else:
                print("❌ No se encontró un paciente con ese ID.")
        except Exception:
            print("❌ Entrada inválida.")

    def _eliminar_paciente(self):
        try:
            id = int(input("\n🗑️ ID del paciente a eliminar: "))
            if self.lista_pacientes.eliminar(id):
                print("✅ Paciente eliminado correctamente.")
            else:
                print("❌ No se encontró un paciente con ese ID.")
        except Exception:
            print("❌ Entrada inválida.")

    def _mostrar_todos(self):
        print("\n📋 Lista de todos los pacientes:")
        pacientes = self.lista_pacientes.mostrar_todos()
        if pacientes:
            for paciente in pacientes:
                self.mostrar_paciente(paciente)
        else:
            print("🕳️ No hay pacientes registrados.")


def main():
    gestor = GestorPacientes()
    try:
        gestor.ejecutar()
    except KeyboardInterrupt:
        print("\n\n👋 Aplicación cerrada por el usuario.")


if __name__ == "__main__":
    main()
