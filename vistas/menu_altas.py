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
        nombre = v.pedir_texto_validado("Nombre: ")
        apellido1 = v.pedir_texto_validado("Primer apellido: ")
        apellido2 = v.pedir_texto_validado("Segundo apellido: ")
        email = v.pedir_email()

        usuario = Usuario(nombre, apellido1, apellido2, "paciente", email, True)
        if not self.usuarios.agregar(usuario):
            print("❌ Error al registrar el usuario.")
            return
        print(f"✅ Usuario creado con ID {usuario.id_usuario}")
        print(f"DEBUG ➤ ID del usuario insertado: {usuario.id_usuario}")

        # --- Alta de Paciente ---
        print("\n🩺 Alta de Paciente")
        genero = v.seleccionar_opcion(v.generos_validos, "Selecciona el género:")
        edad = v.pedir_entero_rango("Edad", 50, 120)
        poblacion = v.pedir_texto_validado("Población: ")
        ocupacion = v.seleccionar_opcion(v.ocupaciones_validas, "Selecciona la ocupación:")
        nivelEstudios = v.seleccionar_opcion(v.niveles_validos, "Selecciona nivel de estudios:")

        # --- Alta de Informe ---
        print("\n🧬 Registro de Informe Clínico")
        fecha = v.pedir_fecha()

        migrañas = v.seleccionar_opcion(v.frecuencias, "Frecuencia de migrañas:")
        calidad_sueno = v.seleccionar_opcion(v.calidades_sueno, "Calidad del sueño:")
        alcohol = v.seleccionar_opcion(v.frecuencias, "Frecuencia de consumo de alcohol:")
        actividad = v.seleccionar_opcion(v.niveles_actividad, "Nivel de actividad física:")

        informe = Informe(
            fecha,
            v.pedir_binario("Antecedentes Alzheimer"),
            v.pedir_binario("Diabetes"),
            v.pedir_binario("Colesterol"),
            v.frecuencias.index(migrañas),
            v.pedir_binario("Hipertensión"),
            v.pedir_binario("Cardiopatía"),
            v.pedir_binario("Depresión"),
            v.pedir_entero_rango("Número de ACV", 0, 10),
            v.pedir_binario("Trastorno del sueño"),
            v.pedir_float_rango("Horas de sueño", 0, 24),
            v.calidades_sueno.index(calidad_sueno),
            v.pedir_binario("Fumador"),
            v.frecuencias.index(alcohol),
            v.niveles_actividad.index(actividad),
            v.pedir_entero_rango("Nivel de estrés", 1, 10),
            v.pedir_binario("Dieta saludable"),
            v.pedir_entero_rango("Presión sistólica", 80, 250),
            v.pedir_entero_rango("Presión diastólica", 40, 150)
        )

        if not self.informes.agregar(informe):
            print("❌ Error al registrar el informe.")
            return
        print(f"DEBUG ➤ ID del informe insertado: {informe.id_informe}")

        # Asociar claves foráneas
        paciente = Paciente(
            nombre, apellido1, apellido2, genero, edad, poblacion,
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
