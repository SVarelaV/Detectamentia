from controlador.gestores.usuarios import Usuarios
from controlador.gestores.pacientes import Pacientes
from controlador.gestores.informes import Informes
from vistas.menu_altas import GestorAltas


class MenuGestion:
    def __init__(self):
        self.usuarios = Usuarios()
        self.pacientes = Pacientes()
        self.informes = Informes()
        self.menu_altas = GestorAltas()

    def mostrar_menu(self):
        while True:
            print("\n📋 MENÚ DE GESTIÓN DETECTAMENTIA")
            print("=" * 40)
            print("1. Alta completa de paciente")
            print("2. Ver pacientes registrados")
            print("3. Ver informes clínicos")
            print("4. Ver usuarios")
            print("5. Salir")

            opcion = input("Selecciona una opción (1-5): ")

            if opcion == "1":
                self.menu_altas.ejecutar()
            elif opcion == "2":
                self.ver_pacientes()
            elif opcion == "3":
                self.ver_informes()
            elif opcion == "4":
                self.ver_usuarios()
            elif opcion == "5":
                print("👋 Saliendo del sistema. ¡Hasta pronto!")
                break
            else:
                print("❌ Opción no válida. Intenta de nuevo.")

    def ver_pacientes(self):
        print("\n👥 PACIENTES REGISTRADOS")
        print("-" * 30)
        for paciente in self.pacientes.mostrar_todos():
            print(f"🆔 {paciente.id_paciente} | {paciente.nombre} {paciente.apellido1} {paciente.apellido2}")

    def ver_informes(self):
        print("\n📄 INFORMES CLÍNICOS")
        print("-" * 30)
        for informe in self.informes.mostrar_todos():
            print(f"🆔 Informe ID: {informe.id_informe} | Fecha: {informe.fechaRegistro}")

    def ver_usuarios(self):
        print("\n🙍 USUARIOS REGISTRADOS")
        print("-" * 30)
        for usuario in self.usuarios.mostrar_todos():
            print(f"🆔 {usuario.id_usuario} | {usuario.nombre} {usuario.apellido1} ({usuario.rol})")


def main():
    menu = MenuGestion()
    menu.mostrar_menu()


if __name__ == "__main__":
    main()