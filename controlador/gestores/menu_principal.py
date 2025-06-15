from controlador.gestores.gestor_pacientes import GestorPacientes
from controlador.gestores.gestor_informes import GestorInformes
from controlador.gestores.gestor_resultadojuegos import GestorResultadoJuegos
from controlador.gestores.gestor_usuarios import GestorUsuarios


class MenuPrincipal:
    """
    Menú principal para navegar entre los diferentes módulos del sistema.
    """

    def mostrar_menu(self):
        print("\n🌐 MENÚ PRINCIPAL - DetectaMentIA")
        print("=" * 60)
        print("1. 👤 Gestión de Pacientes")
        print("2. 📄 Gestión de Informes")
        print("3. 🎮 Gestión de Resultados de Juegos")
        print("4. 👥 Gestión de Usuarios")
        print("5. 🚪 Salir")
        print("=" * 60)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                GestorPacientes().ejecutar()
            elif opcion == "2":
                GestorInformes().ejecutar()
            elif opcion == "3":
                GestorResultadoJuegos().ejecutar()
            elif opcion == "4":
                GestorUsuarios().ejecutar()
            elif opcion == "5":
                print("👋 Gracias por usar DetectaMentIA.")
                break
            else:
                print("❌ Opción inválida. Intenta de nuevo.")


def main():
    menu = MenuPrincipal()
    try:
        menu.ejecutar()
    except KeyboardInterrupt:
        print("\n👋 Aplicación finalizada por el usuario.")

if __name__ == "__main__":
    main()

