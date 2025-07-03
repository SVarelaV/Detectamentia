from controlador.dominios.informe import Informe
from controlador.gestores.informes import Informes


class GestorInformes:
    """
    Gestor interactivo para operar con informes clínicos.
    """

    def __init__(self):
        self.informes = Informes()
        self._cargar_ejemplos()

    def _cargar_ejemplos(self):
        """Carga informes de ejemplo para pruebas rápidas."""
        self.informes.agregar(Informe(
            1, "12-05-2024", 1, 1, 0, 2, 1, 0, 1, 1, 1, 6.5, 2, 0, 1, 2, 5, 1, 130, 85))
        self.informes.agregar(Informe(
            2, "13-05-2024", 0, 0, 1, 1, 0, 0, 0, 0, 0, 7.0, 1, 1, 2, 1, 3, 0, 120, 70))
        self.informes.agregar(Informe(
            3, "15-05-2024", 1, 0, 1, 0, 1, 1, 0, 0, 1, 8.0, 2, 0, 1, 2, 7, 1, 125, 80))
        self.informes.agregar(Informe(
            4, "20-05-2024", 0, 1, 0, 1, 0, 0, 1, 1, 0, 5.5, 0, 1, 2, 0, 4, 1, 140, 90))
        self.informes.agregar(Informe(
            5, "25-05-2024", 1, 1, 1, 2, 1, 1, 1, 0, 1, 7.2, 2, 1, 2, 2, 8, 1, 135, 88))
        self.informes.agregar(Informe(
            6, "28-05-2024", 0, 0, 0, 0, 0, 0, 0, 0, 0, 6.0, 1, 0, 0, 1, 2, 0, 118, 72))
        self.informes.agregar(Informe(
            7, "01-06-2024", 1, 1, 1, 1, 1, 1, 1, 1, 1, 8.5, 2, 1, 2, 2, 9, 1, 145, 95))
        self.informes.agregar(Informe(
            8, "05-06-2024", 0, 1, 0, 2, 0, 0, 1, 0, 1, 5.8, 0, 0, 1, 0, 3, 0, 122, 76))
        self.informes.agregar(Informe(
            9, "10-06-2024", 1, 0, 1, 0, 1, 1, 0, 1, 0, 7.7, 2, 1, 2, 1, 6, 1, 132, 84))
        self.informes.agregar(Informe(
            10, "15-06-2024", 0, 0, 0, 1, 0, 0, 0, 0, 1, 6.3, 1, 0, 0, 0, 4, 0, 125, 78))

    def mostrar_menu(self):
        print("\n📄 GESTOR DE INFORMES - DetectaMentIA")
        print("=" * 60)
        print("1. ➕ Agregar informe")
        print("2. 🔍 Buscar informe por ID")
        print("3. 🗑️  Eliminar informe por ID")
        print("4. 📋 Mostrar todos los informes")
        print("5. 🚪 Salir")
        print("=" * 60)

    def mostrar_informe(self, inf):
        print(f"📝 ID: {inf.id_informe} | 📅 Fecha: {inf.fechaRegistro} | 🧬 Alzheimer: {inf.antecFamiliaresAlzheimer} | 😴 Sueño: {inf.horaSueno}h ({inf.calidadSueno}) | 🩺 Presión: {inf.presionArterialSis}/{inf.presionArterialDia}")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                self._agregar_informe()
            elif opcion == "2":
                self._buscar_informe()
            elif opcion == "3":
                self._eliminar_informe()
            elif opcion == "4":
                self._mostrar_todos()
            elif opcion == "5":
                print("👋 Cerrando el gestor de informes.")
                break
            else:
                print("❌ Opción no válida. Intenta de nuevo.")

    def agregar_informe(self, informe):
        """Agrega un informe solo si no existe otro con el mismo ID."""
        if self.informes.buscar(informe.id_informe) is not None:
            raise Exception("Informe duplicado")
        self.informes.agregar(informe)
        return True

    
    def _agregar_informe(self):
        try:
            print("➕ Agregar nuevo informe")
            id_informe = int(input("ID del informe: "))
            fechaRegistro = input("Fecha de registro (DD-MM-YYYY): ")
            antecFamiliaresAlzheimer = int(input("Antecedentes familiares Alzheimer (1: Sí, 0: No): "))
            diabetes = int(input("Diabetes (1: Sí, 0: No): "))
            colesterol = int(input("Colesterol (1: Sí, 0: No): "))
            migrainas = int(input("Migrañas (0: Nunca, 1: Ocasional, 2: Frecuente): "))
            hipertension = int(input("Hipertensión (1: Sí, 0: No): "))
            cardiopatia = int(input("Cardiopatía (1: Sí, 0: No): "))
            depresionDiag = int(input("Depresión diagnosticada (1: Sí, 0: No): "))
            accidenteCerebrovascular = int(input("ACV (0 si no, o número de episodios): "))
            trastornoSueno = int(input("Trastorno del sueño (1: Sí, 0: No): "))
            horaSueno = float(input("Horas de sueño: "))
            calidadSueno = int(input("Calidad del sueño (0: Mala, 1: Regular, 2: Buena): "))
            fumador = int(input("Fumador (1: Sí, 0: No): "))
            consumoAlcohol = int(input("Consumo de alcohol (0: Nunca, 1: Ocasional, 2: Frecuente): "))
            actividadFisica = int(input("Actividad física (0: Sedentario, 1: Moderado, 2: Activo): "))
            nivelEstres = int(input("Nivel de estrés (1-10): "))
            dietaSaludable = int(input("Dieta saludable (1: Sí, 0: No): "))
            presionArterialSis = int(input("Presión sistólica: "))
            presionArterialDia = int(input("Presión diastólica: "))

            nuevo = Informe(
                id_informe, fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas,
                hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno,
                horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica,
                nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia
            )

            self.agregar_informe(nuevo)
            print("✅ Informe agregado correctamente.")
        except Exception as e:
            print(f"❌ Error al agregar informe: {e}")


    def _buscar_informe(self):
        try:
            id = int(input("🔍 ID del informe: "))
            informe = self.informes.buscar(id)
            if informe:
                self.mostrar_informe(informe)
            else:
                print("❌ Informe no encontrado.")
        except Exception:
            print("❌ Entrada inválida.")

    def _eliminar_informe(self):
        try:
            id = int(input("🗑️ ID del informe a eliminar: "))
            if self.informes.eliminar(id):
                print("✅ Informe eliminado.")
            else:
                print("❌ No se encontró un informe con ese ID.")
        except Exception:
            print("❌ Entrada inválida.")

    def _mostrar_todos(self):
        print("\n📋 Lista de todos los informes:")
        todos = self.informes.mostrar_todos()
        if todos:
            for inf in todos:
                self.mostrar_informe(inf)
        else:
            print("🕳️ No hay informes registrados.")


def main():
    gestor = GestorInformes()
    try:
        gestor.ejecutar()
    except KeyboardInterrupt:
        print("\n👋 Aplicación interrumpida por el usuario.")

if __name__ == "__main__":
    main()