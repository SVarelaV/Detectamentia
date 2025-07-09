from vistas.menu_altas import GestorAltas
from controlador.gestores.usuarios import Usuarios
from controlador.gestores.pacientes import Pacientes
from controlador.gestores.informes import Informes

class MenuGestion:
    def __init__(self):
        self.altas = GestorAltas()
        self.usuarios = Usuarios()
        self.pacientes = Pacientes()
        self.informes = Informes()

    def mostrar_menu(self):
        print("\n📋 MENÚ DE GESTIÓN CLÍNICA")
        print("=" * 50)
        print("1. ➕ Alta completa de paciente")
        print("2. 📋 Ver pacientes registrados")
        print("3. 📄 Ver informes clínicos")
        print("4. 👥 Ver usuarios registrados")
        print("5. 🔙 Volver")
        print("=" * 50)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ").strip()
            if opcion == "1":
                self.altas.ejecutar()
            elif opcion == "2":
                self.mostrar_pacientes()
            elif opcion == "3":
                self.mostrar_informes()
            elif opcion == "4":
                self.mostrar_usuarios()
            elif opcion == "5":
                break
            else:
                print("❌ Opción no válida. Intenta de nuevo.")

    def mostrar_pacientes(self):
        print("\n👥 PACIENTES REGISTRADOS")
        for p in self.pacientes.mostrar_todos():
            print(f"🆔 {p.id_paciente} | {p.nombre} {p.apellido1} {p.apellido2}")

    def mostrar_informes(self):
        print("\n📄 INFORMES CLÍNICOS")
        for i in self.informes.mostrar_todos():
            print(f"📝 ID: {i.id_informe} | Fecha: {i.fechaRegistro}")

    def mostrar_usuarios(self):
        print("\n🙍 USUARIOS REGISTRADOS")
        for u in self.usuarios.mostrar_todos():
            print(f"🆔 {u.id_usuario} | {u.nombre} {u.apellido1} ({u.rol})")

if __name__ == "__main__":
    menu = MenuGestion()
    menu.ejecutar()
