from vistas.menu_usuarios import GestorUsuarios
from vistas.menu_pacientes import GestorPacientes
from vistas.menu_informes import GestorInformes
from vistas.menu_resultadojuegos import GestorResultadoJuegos
from vistas.menu_altas import GestorAltas
from vistas.menu_integrado import MenuIntegrado


class MenuPrincipal:
    def __init__(self):
        self.gestor_usuarios = GestorUsuarios()
        self.gestor_pacientes = GestorPacientes()
        self.gestor_informes = GestorInformes()
        self.gestor_juegos = GestorResultadoJuegos()
        self.menu_negocio = MenuIntegrado()  # contiene las opciones de flujo clínico

    def mostrar_menu(self):
        print("\n🌐 MENÚ PRINCIPAL - DetectaMentIA")
        print("=" * 60)
        print("1. Gestión por entidad")
        print("2. Lógica del negocio (flujos clínicos)")
        print("3. Salir")
        print("=" * 60)

    def menu_entidades(self):
        while True:
            print("\n📂 GESTIÓN POR ENTIDAD")
            print("1. 👥 Usuarios")
            print("2. 🧠 Pacientes")
            print("3. 📄 Informes")
            print("4. 🎮 Resultados de Juegos")
            print("5. 🔙 Volver")
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                self.gestor_usuarios.ejecutar()
            elif opcion == "2":
                self.gestor_pacientes.ejecutar()
            elif opcion == "3":
                self.gestor_informes.ejecutar()
            elif opcion == "4":
                self.gestor_juegos.ejecutar()
            elif opcion == "5":
                break
            else:
                print("❌ Opción inválida.")

    def menu_logica_negocio(self):
        self.menu_negocio.ejecutar()

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ").strip()
            if opcion == "1":
                self.menu_entidades()
            elif opcion == "2":
                self.menu_logica_negocio()
            elif opcion == "3":
                print("👋 Saliendo del sistema. ¡Hasta pronto!")
                break
            else:
                print("❌ Opción no válida.")

def main():
    menu = MenuPrincipal()
    try:
        menu.ejecutar()
    except KeyboardInterrupt:
        print("\n👋 Aplicación cerrada por el usuario.")

if __name__ == "__main__":
    main()