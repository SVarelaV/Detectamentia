from controlador.dominios.paciente import Paciente
from controlador.gestores.pacientes import Pacientes



class GestorPacientes:
    """Gestor que maneja las operaciones sobre pacientes."""

    def __init__(self, cargar_ejemplos=True):
        self.lista_pacientes = Pacientes()
        if cargar_ejemplos:
            self._cargar_ejemplos()

    def agregar(self, paciente):
        """
        Agrega un nuevo paciente a la lista con validaciones de datos y duplicados.
        Lanza una excepción si los datos no son válidos o el paciente ya existe.
        """
        # Validación de datos
        if not paciente._id or not paciente._nombre or paciente._edad is None or paciente._edad < 0:
            raise Exception("Datos inválidos para el paciente")
        # Validación de duplicados
        if any(p._id == paciente._id for p in self.lista_pacientes._elementos):
            raise Exception("Paciente duplicado")
        self.lista_pacientes.agregar(paciente)
        return True

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
        print("3. 🗑️ Eliminar paciente por ID")
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
            id_str = input("ID: ")
            if not id_str.isdigit():
                raise ValueError("El ID debe ser un número entero.")
            id = int(id_str)
            nombre = input("Nombre: ")
            apellido1 = input("Primer apellido: ")
            apellido2 = input("Segundo apellido: ")
            genero = input("Género: ")
            edad_str = input("Edad: ")
            if not edad_str.isdigit():
                raise ValueError("La edad debe ser un número entero.")
            edad = int(edad_str)
            poblacion = input("Población: ")
            ocupacion = input("Ocupación: ")
            nivelEstudios = input("Nivel de estudios: ")

            paciente = Paciente(id, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios)
            self.agregar(paciente)
            print("✅ Paciente agregado correctamente.")
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
