from controlador.dominios.resultadojuego import ResultadoJuego
from controlador.gestores.gestor_resultadojuegos import GestorResultadoJuegos

def test_agregar_resultado():
    gestor = GestorResultadoJuegos()
    resultado = ResultadoJuego(99, "Simon", "10-07-2025", 1.5, 8, 1, 0, 20.0)
    res = gestor.resultados.agregar(resultado)
    assert res, "No se pudo agregar el resultado nuevo"
    assert gestor.resultados.buscar(99) is not None, "No se encontró el resultado agregado"
    print("✅ test_agregar_resultado OK")

def test_agregar_resultado_duplicado():
    gestor = GestorResultadoJuegos()
    resultado = ResultadoJuego(1, "Stroop Test", "01-06-2025", 1.2, 10, 2, 0, 30.5)
    try:
        gestor.agregar_resultado(resultado)
        assert False, "Se agregó un resultado duplicado y no se lanzó excepción"
    except Exception as e:
        assert str(e) == "Resultado duplicado", f"Excepción inesperada: {e}"
        print("✅ test_agregar_resultado_duplicado OK")

def test_agregar_resultado_datos_invalidos():
    gestor = GestorResultadoJuegos()
    try:
        resultado = ResultadoJuego(None, "", "", -1, -1, -1, -1, -1)
        gestor.agregar_resultado(resultado)
        assert False, "Se agregó un resultado con datos inválidos"
    except Exception:
        print("✅ test_agregar_resultado_datos_invalidos OK")

def test_buscar_resultado_existente():
    gestor = GestorResultadoJuegos()
    resultado = gestor.resultados.buscar(1)
    assert resultado is not None, "No se encontró el resultado existente"
    assert resultado.id == 1, "El ID del resultado no coincide"
    print("✅ test_buscar_resultado_existente OK")

def test_buscar_resultado_inexistente():
    gestor = GestorResultadoJuegos()
    resultado = gestor.resultados.buscar(999)
    assert resultado is None, "Se encontró un resultado que no existe"
    print("✅ test_buscar_resultado_inexistente OK")

def test_eliminar_resultado_existente():
    gestor = GestorResultadoJuegos()
    gestor.resultados.agregar(ResultadoJuego(50, "Simon", "10-07-2025", 1.5, 8, 1, 0, 20.0))
    res = gestor.resultados.eliminar(50)
    assert res, "No se pudo eliminar el resultado existente"
    assert gestor.resultados.buscar(50) is None, "El resultado no fue eliminado"
    print("✅ test_eliminar_resultado_existente OK")

def test_eliminar_resultado_inexistente():
    gestor = GestorResultadoJuegos()
    res = gestor.resultados.eliminar(999)
    assert not res, "Se eliminó un resultado inexistente"
    print("✅ test_eliminar_resultado_inexistente OK")

def test_buscar_despues_eliminar():
    gestor = GestorResultadoJuegos()
    resultado = ResultadoJuego(200, "Juego", "10-07-2025", 1.0, 5, 0, 0, 10.0)
    gestor.agregar_resultado(resultado)
    gestor.resultados.eliminar(200)
    assert gestor.resultados.buscar(200) is None, "El resultado no fue eliminado correctamente"
    print("✅ test_buscar_despues_eliminar OK")

def test_agregar_varios_resultados():
    gestor = GestorResultadoJuegos()
    ids = [10, 20, 30]
    for i in ids:
        resultado = ResultadoJuego(i, "Juego", "10-07-2025", 1.0, 5, 0, 0, 10.0)
        gestor.agregar_resultado(resultado)
    for i in ids:
        assert gestor.resultados.buscar(i) is not None, f"No se encontró el resultado con ID {i}"
    print("✅ test_agregar_varios_resultados OK")

if __name__ == "__main__":
    test_agregar_resultado()
    test_agregar_resultado_duplicado()
    test_agregar_resultado_datos_invalidos()
    test_buscar_resultado_existente()
    test_buscar_resultado_inexistente()
    test_eliminar_resultado_existente()
    test_eliminar_resultado_inexistente()
    test_buscar_despues_eliminar()
    test_agregar_varios_resultados()
    print("🎉 Todas las pruebas de GestorResultadoJuegos pasaron correctamente.")