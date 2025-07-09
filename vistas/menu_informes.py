from controlador.dominios.informe import Informe
from controlador.gestores.informes import Informes
import vistas.validacion as v

class GestorInformes:
    """
    Gestor interactivo para operar con informes clínicos.
    """

    def __init__(self):
        self.informes = Informes()

    def mostrar_menu(self):
        print("\n📄 GESTOR DE INFORMES - DetectaMentIA")
        print("=" * 60)
        print("1. ➕ Agregar informe")
        print("2. 🔍 Buscar informe por ID")
        print("3. 🗑️  Eliminar informe por ID")
        print("4. 📋 Mostrar todos los informes")
        print("5. 🚪 Volver al menú principal")
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

            fechaRegistro = v.pedir_fecha()

            antecFamiliaresAlzheimer = v.pedir_binario("Antecedentes familiares Alzheimer")
            diabetes = v.pedir_binario("Diabetes")
            colesterol = v.pedir_binario("Colesterol")

            migrañas_str = v.seleccionar_opcion(v.frecuencias, "Selecciona el nivel de migrañas")
            migrainas = v.frecuencias.index(migrañas_str)

            hipertension = v.pedir_binario("Hipertensión")
            cardiopatia = v.pedir_binario("Cardiopatía")
            depresionDiag = v.pedir_binario("Depresión diagnosticada")
            accidenteCerebrovascular = v.pedir_entero_rango("ACV", 0, 20)
            trastornoSueno = v.pedir_binario("Trastorno del sueño")
            horaSueno = v.pedir_float_rango("Horas de sueño", 0, 24)

            calidadSueno_str = v.seleccionar_opcion(v.calidades_sueno, "Selecciona la calidad del sueño")
            calidadSueno = v.calidades_sueno.index(calidadSueno_str)

            fumador = v.pedir_binario("Fumador")
            consumoAlcohol_str = v.seleccionar_opcion(v.frecuencias, "Frecuencia de consumo de alcohol")
            consumoAlcohol = v.frecuencias.index(consumoAlcohol_str)
            actividadFisica_str = v.seleccionar_opcion(v.niveles_actividad, "Nivel de actividad física")
            actividadFisica = v.niveles_actividad.index(actividadFisica_str)

            nivelEstres = v.pedir_entero_rango("Nivel de estrés", 1, 10)
            dietaSaludable = v.pedir_binario("Dieta saludable")
            presionArterialSis = v.pedir_entero_rango("Presión sistólica", 80, 250)
            presionArterialDia = v.pedir_entero_rango("Presión diastólica", 40, 150)

            nuevo = Informe(
                fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas,
                hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno,
                horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica,
                nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia
            )

            self.informes.agregar(nuevo)
            print(f"✅ Informe agregado")

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