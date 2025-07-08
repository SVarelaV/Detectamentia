from controlador.dominios.usuario import Usuario
from controlador.dominios.paciente import Paciente
from controlador.dominios.informe import Informe
from controlador.gestores.usuarios import Usuarios
from controlador.gestores.pacientes import Pacientes
from controlador.gestores.informes import Informes
import vistas.validacion as v

class GestorAltas:
    """
    Menú de alta combinada: usuario + paciente + informe.
    """

    def __init__(self):
        self.usuarios = Usuarios()
        self.pacientes = Pacientes()
        self.informes = Informes()

    def ejecutar(self):
        print("\n🧾 ALTA COMPLETA DE PACIENTE")
        print("=" * 60)

        # --- Alta de Usuario ---
        print("👤 Alta de Usuario")
        nombre = v.sanitize_input(input("Nombre: "))
        while not v.validar_texto(nombre):
            print("❌ Nombre inválido.")
            nombre = input("Nombre: ")

        apellido1 = input("Primer apellido: ")
        apellido2 = input("Segundo apellido: ")

        email = input("Email: ")
        while not v.validar_email(email):
            print("❌ Email inválido.")
            email = input("Email: ")

        usuario = Usuario(nombre, apellido1, apellido2, "paciente", email, True)
        if not self.usuarios.agregar(usuario):
            print("❌ Error al registrar el usuario.")
            return
        print(f"✅ Usuario creado con ID {usuario.id_usuario}")
        print(f"DEBUG ➤ ID del usuario insertado: {usuario.id_usuario}")

        # --- Alta de Paciente ---
        print("\n🩺 Alta de Paciente")
        genero = v.seleccionar_opcion(v.generos_validos, "Selecciona el género:")
        edad = input("Edad: ")
        while not v.validar_edad(edad):
            print("❌ Edad no válida.")
            edad = input("Edad: ")

        poblacion = input("Población: ")
        while not v.validar_poblacion(poblacion):
            print("❌ Población no válida.")
            poblacion = input("Población: ")

        ocupacion = v.seleccionar_opcion(v.ocupaciones_validas, "Selecciona la ocupación:")
        nivelEstudios = v.seleccionar_opcion(v.niveles_validos, "Selecciona nivel de estudios:")

        # --- Alta de Informe ---
        print("\n🧬 Registro de Informe Clínico")
        fecha = input("Fecha de registro (DD-MM-YYYY): ")
        while not v.validar_fecha(fecha):
            print("❌ Fecha inválida.")
            fecha = input("Fecha de registro (DD-MM-YYYY): ")

        def pedir_bin(m): return int(input(f"{m} (1=Sí, 0=No): "))
        def pedir_ent(m, mi, ma): return int(input(f"{m} ({mi}-{ma}): "))
        def pedir_float(m): return float(input(m))

        migrañas = v.seleccionar_opcion(v.frecuencias, "Frecuencia de migrañas:")
        calidad_sueno = v.seleccionar_opcion(v.calidades_sueno, "Calidad del sueño:")
        alcohol = v.seleccionar_opcion(v.frecuencias, "Frecuencia de consumo de alcohol:")
        actividad = v.seleccionar_opcion(v.niveles_actividad, "Nivel de actividad física:")

        informe = Informe(
            fecha,
            pedir_bin("Antecedentes Alzheimer"),
            pedir_bin("Diabetes"),
            pedir_bin("Colesterol"),
            v.frecuencias.index(migrañas),
            pedir_bin("Hipertensión"),
            pedir_bin("Cardiopatía"),
            pedir_bin("Depresión"),
            pedir_ent("Número de ACV", 0, 10),
            pedir_bin("Trastorno del sueño"),
            pedir_float("Horas de sueño (ej: 7.5): "),
            v.calidades_sueno.index(calidad_sueno),
            pedir_bin("Fumador"),
            v.frecuencias.index(alcohol),
            v.niveles_actividad.index(actividad),
            pedir_ent("Nivel de estrés", 1, 10),
            pedir_bin("Dieta saludable"),
            pedir_ent("Presión sistólica", 80, 250),
            pedir_ent("Presión diastólica", 40, 150)
        )

        if not self.informes.agregar(informe):
            print("❌ Error al registrar el informe.")
            return
        print(f"DEBUG ➤ ID del informe insertado: {informe.id_informe}")


        # Asociar claves foráneas
        paciente = Paciente(
            nombre, apellido1, apellido2, genero, int(edad), poblacion,
            ocupacion, nivelEstudios,
            id_usuario=usuario.id_usuario,
            id_informe=informe.id_informe
        )

        if not self.pacientes.agregar(paciente):
            print("❌ Error al registrar el paciente.")
            return

        print(f"✅ Informe ID {informe.id_informe} | Paciente ID {paciente.id_paciente}")
        print(f"🎉 Alta completa del paciente {nombre} realizada exitosamente.")

def main():
    gestor = GestorAltas()
    try:
        gestor.ejecutar()
    except KeyboardInterrupt:
        print("\n👋 Operación cancelada por el usuario.")

if __name__ == "__main__":
    main()

