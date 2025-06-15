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
        print(f"📝 ID: {inf.id} | 📅 Fecha: {inf.fechaRegistro} | 🧬 Alzheimer: {inf.antecFamiliaresAlzheimer} | 😴 Sueño: {inf.horaSueno}h ({inf.calidadSueno}) | 🩺 Presión: {inf.presionArterialSis}/{inf.presionArterialDia}")

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

    def _agregar_informe(self):
        try:
            print("\n➕ Agregar nuevo informe")
            id = int(input("ID: "))
            fecha = input("Fecha de registro (DD-MM-YYYY): ")
            antec = int(input("Antecedentes familiares Alzheimer (1/0): "))
            diabetes = int(input("Diabetes (1/0): "))
            colesterol = int(input("Colesterol (1/0): "))
            migrainas = int(input("Migrainas (0: Nunca, 1: Ocasional, 2: Frecuente): "))
            hipertension = int(input("Hipertensión (1/0): "))
            cardiopatia = int(input("Cardiopatía (1/0): "))
            depresion = int(input("Depresión diagnosticada (1/0): "))
            acv = int(input("ACV (0 si no, o número de episodios): "))
            trastorno_sueno = int(input("Trastorno del sueño (1/0): "))
            horas_sueno = float(input("Horas de sueño: "))
            calidad_sueno = int(input("Calidad del sueño (0: Mala, 1: Regular, 2: Buena): "))
            fumador = int(input("Fumador (1/0): "))
            alcohol = int(input("Consumo de alcohol (0: Nunca, 1: Ocasional, 2: Frecuente): "))
            actividad = int(input("Actividad física (0: Sedentario, 1: Moderado, 2: Activo): "))
            estres = int(input("Nivel de estrés (1-10): "))
            dieta = int(input("Dieta saludable (1/0): "))
            presion_sis = int(input("Presión sistólica: "))
            presion_dia = int(input("Presión diastólica: "))

            nuevo = Informe(id, fecha, antec, diabetes, colesterol, migrainas, hipertension,
                            cardiopatia, depresion, acv, trastorno_sueno, horas_sueno,
                            calidad_sueno, fumador, alcohol, actividad, estres,
                            dieta, presion_sis, presion_dia)

            if self.informes.agregar(nuevo):
                print("✅ Informe agregado correctamente.")
            else:
                print("⚠️ Ya existe un informe con ese ID.")
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
