from controlador.dominios.informe import Informe
from controlador.gestores.informes import Informes

class GestorInformes:
    """
    Gestor interactivo para operar con informes clínicos.
    """

    def __init__(self):
        self.informes = Informes()  # Carga directa desde la base de datos

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
        if self.informes.buscar(informe.id_informe) is not None:
            raise Exception("Informe duplicado")
        self.informes.agregar(informe)
        return True

    def _agregar_informe(self):
        try:
            print("➕ Agregar nuevo informe")
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
                fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas,
                hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno,
                horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica,
                nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia
            )

            self.informes.agregar(nuevo)
            print(f"✅ Informe agregado con ID: {nuevo.id_informe}")

        except Exception as e:
            print(f"❌ Error al agregar informe: {e}")

    def _buscar_informe(self):
        try:
            id_informe = int(input("🔍 ID del informe: "))
            informe = self.informes.buscar(id_informe)
            if informe:
                self.mostrar_informe(informe)
            else:
                print("❌ Informe no encontrado.")
        except Exception:
            print("❌ Entrada inválida.")

    def _eliminar_informe(self):
        try:
            id_informe = int(input("🗑️ ID del informe a eliminar: "))
            if self.informes.eliminar(id_informe):
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

