from controlador.dominios.paciente import Paciente
from controlador.gestores.pacientes import Pacientes


class GestorPacientes:
    """Gestor que maneja las operaciones sobre pacientes."""

    def __init__(self, cargar_ejemplos=True):
        self.lista_pacientes = Pacientes()
        if cargar_ejemplos:
            self._cargar_ejemplos()

    def agregar(self, paciente):
        if self.lista_pacientes.buscar(paciente.id_paciente):
            raise Exception("Paciente duplicado")
        self.lista_pacientes.agregar(paciente)
        return True

    def _cargar_ejemplos(self):
        """Carga algunos pacientes de ejemplo."""
        self.lista_pacientes.agregar(Paciente(1, "Juan", "Pérez", "Gómez", "Masculino", 72, "Madrid", "Jubilado", "Secundaria completa"))
        self.lista_pacientes.agregar(Paciente(2, "Ana", "López", "Martínez", "Femenino", 68, "Barcelona", "Ama de casa", "Primaria completa"))
        self.lista_pacientes.agregar(Paciente(3, "Luis", "Martín", "Soto", "Masculino", 80, "Valencia", "Jubilado", "Universidad"))
        self.lista_pacientes.agregar(Paciente(4, "Carmen", "Ruiz", "Díaz", "Femenino", 75, "Sevilla", "Jubilada", "Secundaria"))
        self.lista_pacientes.agregar(Paciente(5, "Pedro", "García", "Fernández", "Masculino", 65, "Bilbao", "Comerciante", "Primaria"))
        self.lista_pacientes.agregar(Paciente(6, "Lucía", "Sánchez", "Moreno", "Femenino", 70, "Granada", "Profesora", "Universidad"))
        self.lista_pacientes.agregar(Paciente(7, "Miguel", "Torres", "Navarro", "Masculino", 60, "Zaragoza", "Ingeniero", "Universidad"))
        self.lista_pacientes.agregar(Paciente(8, "Isabel", "Jiménez", "Romero", "Femenino", 73, "Valladolid", "Jubilada", "Secundaria"))
        self.lista_pacientes.agregar(Paciente(9, "Antonio", "Hernández", "Molina", "Masculino", 69, "Alicante", "Agricultor", "Primaria"))
        self.lista_pacientes.agregar(Paciente(10, "María", "Castro", "Ortega", "Femenino", 67, "Córdoba", "Ama de casa", "Primaria completa"))

    def mostrar_menu(self):
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
        print(f"👤 ID: {paciente.id_paciente} | {paciente.nombre} {paciente.apellido1} {paciente.apellido2} | "
            f"{paciente.edad} años | {paciente.poblacion} | {paciente.ocupacion} | {paciente.nivelEstudios}")

    def ejecutar(self):
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
            id_paciente = int(input("ID: "))
            nombre = input("Nombre: ")
            apellido1 = input("Primer apellido: ")
            apellido2 = input("Segundo apellido: ")
            genero = input("Género: ")
            edad = int(input("Edad: "))
            poblacion = input("Población: ")
            ocupacion = input("Ocupación: ")
            nivelEstudios = input("Nivel de estudios: ")

            paciente = Paciente(id_paciente, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios)
            self.agregar(paciente)
            print("✅ Paciente agregado correctamente.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def _buscar_paciente(self):
        try:
            id_paciente = int(input("\n🔍 ID del paciente a buscar: "))
            paciente = self.lista_pacientes.buscar(id_paciente)
            if paciente:
                print("\n👁️ Paciente encontrado:")
                self.mostrar_paciente(paciente)
            else:
                print("❌ No se encontró un paciente con ese ID.")
        except Exception:
            print("❌ Entrada inválida.")

    def _eliminar_paciente(self):
        try:
            id_paciente = int(input("\n🗑️ ID del paciente a eliminar: "))
            if self.lista_pacientes.eliminar(id_paciente):
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
