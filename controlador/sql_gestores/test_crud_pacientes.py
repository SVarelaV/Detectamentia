from controlador.sql_gestores.crud_pacientes import *

# Test manual para verificar el CRUD de pacientes
def test_crud_pacientes():
    id_test = 999
    print("\n🔹 Agregando paciente de prueba...")
    agregado = agregar_paciente(
        id_paciente=id_test,
        nombre='Juan',
        apellido1='Pérez',
        apellido2='Gómez',
        genero='Masculino',
        edad=72,
        poblacion='Madrid',
        ocupacion='Jubilado',
        nivelEstudios='Secundaria completa'
    )
    print("✅ Paciente agregado:", agregado)

    print("\n🔍 Verificando si el paciente existe...")
    existe = existe_paciente(id_test)
    print("Existe:", existe)

    print("\n🔎 Buscando paciente por ID...")
    paciente = buscar_paciente_por_id(id_test)
    print("Resultado:", paciente)

    print("\n✏️ Actualizando paciente...")
    actualizado = actualizar_paciente(
        id_paciente=id_test,
        nombre='Juan Modificado',
        apellido1='Pérez',
        apellido2='Gómez',
        genero='Masculino',
        edad=73,
        poblacion='Madrid',
        ocupacion='Jubilado',
        nivelEstudios='Universidad completa'
    )
    print("Actualizado:", actualizado)

    print("\n📋 Mostrando todos los pacientes...")
    pacientes = mostrar_pacientes()
    for p in pacientes:
        print(p)

    print("\n🗑️ Eliminando paciente de prueba...")
    eliminado = eliminar_paciente(id_test)
    print("Eliminado:", eliminado)

if __name__ == '__main__':
    test_crud_pacientes()
