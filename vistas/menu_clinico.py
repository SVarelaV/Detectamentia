from vistas.menu_usuarios import GestorUsuarios
from vistas.menu_pacientes import GestorPacientes
from vistas.menu_informes import GestorInformes
from vistas.menu_resultadojuegos import GestorResultadoJuegos
from vistas.menu_altas import GestorAltas
from controlador.gestores.usuarios import Usuarios
from controlador.gestores.pacientes import Pacientes
from controlador.gestores.informes import Informes
import vistas.validacion as v


class MenuClinico:
    """
    Menú Clínico principal de la aplicación DetectaMentIA.
    Gestiona flujos de trabajo combinados y permite acceso a funciones clínicas clave.
    """

    def __init__(self):
        self.menu_usuarios = GestorUsuarios()
        self.menu_pacientes = GestorPacientes()
        self.menu_informes = GestorInformes()
        self.menu_juegos = GestorResultadoJuegos()
        self.altas = GestorAltas()
        self.usuarios = Usuarios()
        self.pacientes = Pacientes()
        self.informes = Informes()

    def mostrar_menu(self):
        print("\n🌐 MENÚ CLÍNICO - DetectaMentIA")
        print("=" * 60)
        print("1. Alta completa de paciente")
        print("2. Consultar estado clínico de un paciente")
        print("3. Listar pacientes con datos clínicos")
        print("4. Evaluar riesgo y recomendaciones (en construcción)")
        print("5. Ver estadísticas generales del sistema (en construcción)")
        print("6. 🚪 Salir")
        print("=" * 60)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                self.altas.ejecutar()
            elif opcion == "2":
                self.consultar_estado()
            elif opcion == "3":
                self.listar_pacientes_con_estado()
            elif opcion == "4":
                print("🔧 Esta funcionalidad está en desarrollo. Próximamente disponible.")
            elif opcion == "5":
                print("📊 Esta sección aún no ha sido implementada.")
            elif opcion == "6":
                print("👋 Gracias por usar DetectaMentIA.")
                break
            else:
                print("❌ Opción inválida. Intenta de nuevo.")

    def consultar_estado(self):
        print("\n🔎 CONSULTA DE ESTADO CLÍNICO")
        email = input("📧 Introduce el email del usuario: ")
        if not v.validar_email(email):
            print("❌ Email inválido.")
            return

        usuario = self.usuarios.buscar_por_email(email)
        if not usuario:
            print("❌ No se encontró un usuario con ese email.")
            return

        print(f"✅ Usuario encontrado: {usuario.nombre} {usuario.apellido1} ({usuario.rol})")

        paciente = next((p for p in self.pacientes.mostrar_todos() if p.id_usuario == usuario.id_usuario), None)
        if not paciente:
            print("❌ No hay paciente asociado a este usuario.")
            return

        print(f"🧠 Paciente ID: {paciente.id_paciente} | {paciente.nombre} {paciente.apellido1} {paciente.apellido2} | Edad: {paciente.edad} | Género: {paciente.genero}")

        informe = self.informes.buscar(paciente.id_informe)
        if not informe:
            print("⚠️ Este paciente aún no tiene informe clínico registrado.")
            return

        print("\n📄 Informe Clínico:")
        print(f"📅 Fecha: {informe.fechaRegistro} | Alzheimer en familia: {informe.antecFamiliaresAlzheimer} | Sueño: {informe.horaSueno}h ({informe.calidadSueno})")
        print(f"🩺 Presión arterial: {informe.presionArterialSis}/{informe.presionArterialDia} | Nivel de estrés: {informe.nivelEstres}")

    def listar_pacientes_con_estado(self):
        print("\n📋 LISTADO DE PACIENTES CON INFORME CLÍNICO")
        pacientes = self.pacientes.mostrar_todos()
        if not pacientes:
            print("🕳️ No hay pacientes registrados.")
            return

        for paciente in pacientes:
            informe = self.informes.buscar(paciente.id_informe)
            if informe:
                alzheimer_fam = "Sí" if informe.antecFamiliaresAlzheimer else "No"
                print(f"🧠 {paciente.id_paciente} - {paciente.nombre} {paciente.apellido1} ({paciente.edad} años)")
                print(f"   📝 Informe ID: {informe.id_informe} | 📅 Fecha: {informe.fechaRegistro} | Sueño: {informe.horaSueno}h ({informe.calidadSueno})")
                print(f"   🩺 PA: {informe.presionArterialSis}/{informe.presionArterialDia} | Estrés: {informe.nivelEstres} | Alzheimer fam.: {alzheimer_fam}")
                print("-" * 60)


def main():
    menu = MenuClinico()
    try:
        menu.ejecutar()
    except KeyboardInterrupt:
        print("\n👋 Aplicación finalizada por el usuario.")

if __name__ == "__main__":
    main()
