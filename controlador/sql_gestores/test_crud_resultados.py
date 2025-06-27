from controlador.sql_gestores.crud_resultados import *

# Test manual para verificar el CRUD de resultados de juego
def test_crud_resultado_juego():
    id_test = '999'
    print("\n🔹 Agregando resultado de juego de prueba...")
    agregado = agregar_resultado_juego(
        id_resultado=id_test,
        id_paciente='001',
        nombreJuego='Stroop',
        fecha='27-06-2025',
        tiempoReaccion=1.85,
        aciertos=7,
        errores=1,
        tiempoTotal=40,
        numeroIntentos=8
    )
    print("✅ Resultado agregado:", agregado)

    print("\n🔍 Verificando si el resultado existe...")
    existe = existe_resultado(id_test)
    print("Existe:", existe)

    print("\n🔎 Buscando resultado por ID...")
    resultado = buscar_resultado_por_id(id_test)
    print("Resultado:", resultado)

    print("\n✏️ Actualizando resultado de juego...")
    actualizado = actualizar_resultado_juego(
        id_resultado=id_test,
        id_paciente='001',
        nombreJuego='N-back',
        fecha='2025-06-28',
        tiempoReaccion=1.4,
        aciertos=8,
        errores=0,
        tiempoTotal=38,
        numeroIntentos=6
    )
    print("Actualizado:", actualizado)

    print("\n📋 Mostrando todos los resultados de juego...")
    resultados = mostrar_resultados()
    for r in resultados:
        print(r)

    print("\n🗑️ Eliminando resultado de prueba...")
    eliminado = eliminar_resultado(id_test)
    print("Eliminado:", eliminado)

if __name__ == '__main__':
    test_crud_resultado_juego()
