from controlador.dominios.paciente import Paciente
from controlador.gestores.pacientes import Pacientes
import vistas.validacion as v

class GestorPacientes:
    """Gestor que maneja las operaciones sobre pacientes."""

    def __init__(self):
        self.lista_pacientes = Pacientes()

    def agregar(self, paciente):
        if self.lista_pacientes.buscar(paciente.id_paciente):
            raise Exception("Paciente duplicado")
        self.lista_pacientes.agregar(paciente)
        return True

    def mostrar_menu(self):
        print("\n" + "="*50)
        print("🧠 GESTOR DE PACIENTES - DetectaMentIA")
        print("="*50)
        print("1. ➕ Agregar paciente")
        print("2. 🔍 Buscar paciente por ID")
        print("3. 🗑️  Eliminar paciente por ID")
        print("4. 📋 Mostrar todos los pacientes")
        print("5. 🚪 Volver al menú principal")
        print("="*50)

    def mostrar_paciente(self, paciente: Paciente):
        print(f"{paciente.id_paciente}. {paciente.nombre} {paciente.apellido1} {paciente.apellido2} "
            f"({paciente.edad} años) - Género: {paciente.genero} | "
            f"Población: {paciente.poblacion} | Ocupación: {paciente.ocupacion} | Estudios: {paciente.nivelEstudios}")

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

            nombre = v.pedir_texto_validado("Nombre: ")
            apellido1 = v.pedir_texto_validado("Primer apellido: ")
            apellido2 = v.pedir_texto_validado("Segundo apellido: ")
            genero = v.seleccionar_opcion(v.generos_validos, "Selecciona el género")
            edad = v.pedir_entero_rango("Edad", 50, 120)
            poblacion = v.pedir_texto_validado("Población: ")
            ocupacion = v.seleccionar_opcion(v.ocupaciones_validas, "Selecciona la ocupación")
            nivelEstudios = v.seleccionar_opcion(v.niveles_validos, "Selecciona el nivel de estudios")

            paciente = Paciente(nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios)

            if self.lista_pacientes.agregar(paciente):
                print("✅ Paciente agregado correctamente.")
            else:
                print("❌ No se pudo agregar el paciente.")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

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
