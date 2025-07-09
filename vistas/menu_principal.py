from vistas.menu_usuarios import GestorUsuarios
from vistas.menu_pacientes import GestorPacientes
from vistas.menu_informes import GestorInformes
from vistas.menu_resultadojuegos import GestorResultadoJuegos
from vistas.menu_integrado import MenuIntegrado
from vistas.menu_gestion import MenuGestion

class MenuPrincipal:
    def __init__(self):
        self.menu_negocio = MenuIntegrado()
        self.menu_gestion = MenuGestion()
        self.entidades = {
            "1": GestorUsuarios(),
            "2": GestorPacientes(),
            "3": GestorInformes(),
            "4": GestorResultadoJuegos(),
        }

    def mostrar_menu(self):
        print("\n🌐 MENÚ PRINCIPAL - DetectaMentIA")
        print("=" * 60)
        print("1. 👥 Gestión de Usuarios")
        print("2. 🧠 Gestión de Pacientes")
        print("3. 📄 Gestión de Informes")
        print("4. 🎮 Gestión de Resultados de Juegos")
        print("5. 🧩 Flujos Clínicos (Alta completa y más)")
        print("6. 🧾 Gestión Clínica Resumida")
        print("7. 🚪 Salir")
        print("=" * 60)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ").strip()
            if opcion in self.entidades:
                self.entidades[opcion].ejecutar()
            elif opcion == "5":
                self.menu_negocio.ejecutar()
            elif opcion == "6":
                self.menu_gestion.ejecutar()
            elif opcion == "7":
                print("👋 Saliendo del sistema. ¡Hasta pronto!")
                break
            else:
                print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main = MenuPrincipal()
    main.ejecutar()
