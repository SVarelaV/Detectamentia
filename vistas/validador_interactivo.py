
# Listas válidas (puedes importarlas desde validador_paciente si ya están allí)
ocupaciones_validas = [
    "Sin ocupación / Nunca trabajó", "Desempleado/a", "Jubilado/a", "Ama/o de casa",
    "Estudiante", "Trabajador/a no cualificado/a", "Trabajador/a cualificado/a",
    "Empleado/a administrativo/a o de oficina", "Técnico/a o profesional de nivel medio",
    "Profesional universitario/a", "Directivo/a o Ejecutivo/a", "Empresario/a o autónomo/a",
    "Agricultor/a o trabajador/a del campo", "Otro (especificar)"
]

niveles_validos = [
    "Sin escolarización", "Educación primaria incompleta", "Educación primaria completa",
    "Educación secundaria incompleta", "Educación secundaria completa",
    "Bachillerato o equivalente incompleto", "Bachillerato o equivalente completo",
    "Estudios universitarios incompletos", "Estudios universitarios completos",
    "Estudios de posgrado / máster", "Doctorado o equivalente"
]

generos_validos = ["masculino", "femenino", "otro"]

def mostrar_opciones(lista):
    for i, opcion in enumerate(lista, 1):
        print(f"{i}. {opcion}")

def seleccionar_opcion(lista, mensaje):
    while True:
        print(f"\n{mensaje}")
        mostrar_opciones(lista)
        entrada = input("Selecciona una opción (número): ").strip()
        if entrada.isdigit():
            idx = int(entrada) - 1
            if 0 <= idx < len(lista):
                return lista[idx]
        print("❌ Opción no válida. Intenta de nuevo.")
