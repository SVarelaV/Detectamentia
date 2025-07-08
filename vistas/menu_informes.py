from controlador.dominios.informe import Informe
from controlador.gestores.informes import Informes
from vistas import validacion as v

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

            fechaRegistro = input("Fecha de registro (DD-MM-YYYY): ")
            while not v.validar_fecha(fechaRegistro):
                print("❌ Formato inválido. Usa DD-MM-YYYY.")
                fechaRegistro = input("Fecha de registro (DD-MM-YYYY): ")

            def pedir_binario(mensaje):
                valor = input(mensaje)
                while not v.validar_binario(valor):
                    print("❌ Valor inválido. Usa 1 (Sí) o 0 (No).")
                    valor = input(mensaje)
                return int(valor)

            def pedir_entero_positivo(mensaje):
                valor = input(mensaje)
                while not valor.isdigit() or int(valor) < 0:
                    print("❌ Debe ser un número entero mayor o igual a 0.")
                    valor = input(mensaje)
                return int(valor)

            def pedir_float_rango(mensaje, min_val, max_val):
                valor = input(mensaje)
                while not v.validar_float_rango(valor, min_val, max_val):
                    print(f"❌ Valor fuera de rango ({min_val}-{max_val}).")
                    valor = input(mensaje)
                return float(valor)

            def pedir_entero_rango(mensaje, min_val, max_val):
                valor = input(mensaje)
                while not v.validar_entero_rango(valor, min_val, max_val):
                    print(f"❌ Valor fuera de rango ({min_val}-{max_val}).")
                    valor = input(mensaje)
                return int(valor)

            antecFamiliaresAlzheimer = pedir_binario("Antecedentes familiares Alzheimer (1: Sí, 0: No): ")
            diabetes = pedir_binario("Diabetes (1: Sí, 0: No): ")
            colesterol = pedir_binario("Colesterol (1: Sí, 0: No): ")

            migrañas_str = v.seleccionar_opcion(v.frecuencias, "Selecciona el nivel de migrañas")
            migrainas = v.frecuencias.index(migrañas_str)

            hipertension = pedir_binario("Hipertensión (1: Sí, 0: No): ")
            cardiopatia = pedir_binario("Cardiopatía (1: Sí, 0: No): ")
            depresionDiag = pedir_binario("Depresión diagnosticada (1: Sí, 0: No): ")
            accidenteCerebrovascular = pedir_entero_positivo("ACV (0 si no, o número de episodios): ")
            trastornoSueno = pedir_binario("Trastorno del sueño (1: Sí, 0: No): ")
            horaSueno = pedir_float_rango("Horas de sueño: ", 0, 24)

            calidadSueno_str = v.seleccionar_opcion(v.calidades_sueno, "Selecciona la calidad del sueño")
            calidadSueno = v.calidades_sueno.index(calidadSueno_str)

            fumador = pedir_binario("Fumador (1: Sí, 0: No): ")

            consumoAlcohol_str = v.seleccionar_opcion(v.frecuencias, "Frecuencia de consumo de alcohol")
            consumoAlcohol = v.frecuencias.index(consumoAlcohol_str)

            actividadFisica_str = v.seleccionar_opcion(v.niveles_actividad, "Nivel de actividad física")
            actividadFisica = v.niveles_actividad.index(actividadFisica_str)

            nivelEstres = pedir_entero_rango("Nivel de estrés (1-10): ", 1, 10)
            dietaSaludable = pedir_binario("Dieta saludable (1: Sí, 0: No): ")
            presionArterialSis = pedir_entero_rango("Presión sistólica: ", 80, 250)
            presionArterialDia = pedir_entero_rango("Presión diastólica: ", 40, 150)

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