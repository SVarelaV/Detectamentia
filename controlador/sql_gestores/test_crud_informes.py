from controlador.sql_gestores.crud_informes import *

# Test manual para verificar el CRUD de informes
def test_crud_informes():
    id_test = 999  # Debe ser int, no string
    print("\n🔹 Agregando informe de prueba...")
    agregado = agregar_informe(
        id_informe=id_test,
        fechaRegistro='27-06-2025',
        antecFamiliaresAlzheimer=1,
        diabetes=0,
        colesterol=1,
        migrainas=2,
        hipertension=1,
        cardiopatia=0,
        depresionDiag=1,
        accidenteCerebrovascular=0,
        trastornoSueno=1,
        horaSueno=7,
        calidadSueno='Buena',
        fumador=0,
        consumoAlcohol='Ocasional',
        actividadFisica='Activa',
        nivelEstres='4',
        dietaSaludable='Sí',
        presionArterialSis=125,
        presionArterialDia=80
    )
    print("✅ Informe agregado:", agregado)

    print("\n🔍 Verificando si el informe existe...")
    existe = existe_informe(id_test)
    print("Existe:", existe)

    print("\n🔎 Buscando informe por ID...")
    informe = buscar_informe_por_id(id_test)
    print("Resultado:", informe)

    print("\n✏️ Actualizando informe...")
    actualizado = actualizar_informe(
        id_informe=id_test,
        fechaRegistro='2025-06-28',
        antecFamiliaresAlzheimer=0,
        diabetes=1,
        colesterol=0,
        migrainas=1,
        hipertension=0,
        cardiopatia=1,
        depresionDiag=0,
        accidenteCerebrovascular=1,
        trastornoSueno=0,
        horaSueno=6,
        calidadSueno='Regular',
        fumador=1,
        consumoAlcohol='Frecuente',
        actividadFisica='Sedentaria',
        nivelEstres='6',
        dietaSaludable='No',
        presionArterialSis=140,
        presionArterialDia=90
    )
    print("Actualizado:", actualizado)

    print("\n📋 Mostrando todos los informes...")
    informes = mostrar_informes()
    for inf in informes:
        print(inf)

    print("\n🗑️ Eliminando informe de prueba...")
    eliminado = eliminar_informe(id_test)
    print("Eliminado:", eliminado)

if __name__ == '__main__':
    test_crud_informes()
