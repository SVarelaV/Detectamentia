from vistas.menu_usuarios import GestorUsuarios
from vistas.menu_pacientes import GestorPacientes
from vistas.menu_informes import GestorInformes
from vistas.menu_resultadojuegos import GestorResultadoJuegos
from vistas.menu_altas import GestorAltas
from controlador.gestores.usuarios import Usuarios
from controlador.gestores.pacientes import Pacientes
from controlador.gestores.informes import Informes
import vistas.validacion as v


class MenuIntegrado:
    def __init__(self):
        self.menu_usuarios = GestorUsuarios()
        self.menu_pacientes = GestorPacientes()
        self.menu_informes = GestorInformes()
        self.menu_juegos = GestorResultadoJuegos()
        self.altas = GestorAltas()
        self.usuarios = Usuarios()
        self.pacientes = Pacientes()
        self.informes = Informes()

    def mostrar_menu(self):
        print("\n🌐 MENÚ INTEGRADO - DetectaMentIA")
        print("=" * 60)
        print("1. Alta completa (usuario + paciente + informe)")
        print("2. Completar alta con usuario existente")
        print("3. 👥 Gestión de Usuarios")
        print("4. 🧠 Gestión de Pacientes")
        print("5. 📄 Gestión de Informes")
        print("6. 🎮 Gestión de Resultados de Juegos")
        print("7. 🚪 Salir")
        print("=" * 60)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                self.altas.ejecutar()

            elif opcion == "2":
                self.completar_alta()

            elif opcion == "3":
                self.menu_usuarios.ejecutar()

            elif opcion == "4":
                self.menu_pacientes.ejecutar()

            elif opcion == "5":
                self.menu_informes.ejecutar()

            elif opcion == "6":
                self.menu_juegos.ejecutar()

            elif opcion == "7":
                print("👋 Gracias por usar DetectaMentIA.")
                break

            else:
                print("❌ Opción inválida. Intenta de nuevo.")

    def completar_alta(self):
        print("\n🔗 COMPLETAR ALTA A PARTIR DE USUARIO EXISTENTE")

        email = input("📧 Introduce el email del usuario: ")
        if not v.validar_email(email):
            print("❌ Email inválido.")
            return

        usuario = self.usuarios.buscar_por_email(email)
        if not usuario:
            print("❌ No se encontró un usuario con ese email.")
            return

        print(f"✅ Usuario encontrado: {usuario.nombre} {usuario.apellido1} ({usuario.rol})")

        # Buscar paciente vinculado
        paciente = next((p for p in self.pacientes.mostrar_todos() if p.id_usuario == usuario.id_usuario), None)

        if not paciente:
            print("\n🩺 No tiene paciente asociado. Procediendo con alta clínica...")
            self.menu_pacientes._agregar_paciente()
        else:
            print(f"👁️ Usuario ya tiene paciente registrado con ID {paciente.id_paciente}")

            # Buscar si tiene informe
            if paciente.id_informe is None or not self.informes.buscar(paciente.id_informe):
                print("\n🧬 No tiene informe clínico. Procediendo a registrar uno...")
                self.menu_informes._agregar_informe()
            else:
                print("ℹ️ Este usuario ya tiene informe clínico registrado.")

def main():
    menu = MenuIntegrado()
    try:
        menu.ejecutar()
    except KeyboardInterrupt:
        print("\n👋 Aplicación finalizada por el usuario.")

if __name__ == "__main__":
    main()