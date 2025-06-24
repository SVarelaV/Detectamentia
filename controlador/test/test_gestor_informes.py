from controlador.dominios.informe import Informe
from controlador.gestores.gestor_informes import GestorInformes

def test_agregar_informe():
    gestor = GestorInformes()
    informe = Informe(99, "01-01-2025", 1, 0, 1, 2, 0, 1, 0, 0, 1, 7.0, 2, 1, 2, 1, 5, 1, 120, 80)
    resultado = gestor.agregar_informe(informe)
    assert resultado, "No se pudo agregar el informe nuevo"
    assert gestor.informes.buscar(99) is not None, "No se encontró el informe agregado"
    print("✅ test_agregar_informe OK")

def test_agregar_informe_duplicado():
    gestor = GestorInformes()
    informe = Informe(1, "01-01-2025", 1, 0, 1, 2, 0, 1, 0, 0, 1, 7.0, 2, 1, 2, 1, 5, 1, 120, 80)
    try:
        gestor.agregar_informe(informe)
        assert False, "Se agregó un informe duplicado y no se lanzó excepción"
    except Exception as e:
        assert str(e) == "Informe duplicado", f"Excepción inesperada: {e}"
        print("✅ test_agregar_informe_duplicado OK")

def test_buscar_informe_existente():
    gestor = GestorInformes()
    informe = gestor.informes.buscar(1)
    assert informe is not None, "No se encontró el informe existente"
    assert informe.id == 1, "El ID del informe no coincide"
    print("✅ test_buscar_informe_existente OK")

def test_buscar_informe_inexistente():
    gestor = GestorInformes()
    informe = gestor.informes.buscar(999)
    assert informe is None, "Se encontró un informe que no existe"
    print("✅ test_buscar_informe_inexistente OK")

def test_eliminar_informe_existente():
    gestor = GestorInformes()
    resultado = gestor.informes.eliminar(1)
    assert resultado, "No se pudo eliminar el informe existente"
    assert gestor.informes.buscar(1) is None, "El informe no fue eliminado"
    print("✅ test_eliminar_informe_existente OK")

def test_eliminar_informe_inexistente():
    gestor = GestorInformes()
    resultado = gestor.informes.eliminar(999)
    assert not resultado, "Se eliminó un informe inexistente"
    print("✅ test_eliminar_informe_inexistente OK")

def test_agregar_varios_informes():
    gestor = GestorInformes()
    ids = [10, 20, 30]
    for i in ids:
        informe = Informe(i, "01-01-2025", 1, 0, 1, 2, 0, 1, 0, 0, 1, 7.0, 2, 1, 2, 1, 5, 1, 120, 80)
        assert gestor.agregar_informe(informe)
    for i in ids:
        assert gestor.informes.buscar(i) is not None
    print("✅ test_agregar_varios_informes OK")

def test_eliminar_todos_informes():
    gestor = GestorInformes()
    ids = [101, 102]
    for i in ids:
        informe = Informe(i, "01-01-2025", 1, 0, 1, 2, 0, 1, 0, 0, 1, 7.0, 2, 1, 2, 1, 5, 1, 120, 80)
        gestor.agregar_informe(informe)
    for i in ids:
        gestor.informes.eliminar(i)
        assert gestor.informes.buscar(i) is None
    print("✅ test_eliminar_todos_informes OK")

def test_buscar_despues_eliminar():
    gestor = GestorInformes()
    informe = Informe(200, "01-01-2025", 1, 0, 1, 2, 0, 1, 0, 0, 1, 7.0, 2, 1, 2, 1, 5, 1, 120, 80)
    gestor.agregar_informe(informe)
    gestor.informes.eliminar(200)
    assert gestor.informes.buscar(200) is None
    print("✅ test_buscar_despues_eliminar OK")

def test_agregar_informe_datos_invalidos():
    gestor = GestorInformes()
    try:
        informe = Informe(None, "", 1, 0, 1, 2, 0, 1, 0, 0, 1, 7.0, 2, 1, 2, 1, 5, 1, 120, 80)
        gestor.agregar_informe(informe)
        assert False, "Se agregó un informe con datos inválidos"
    except Exception:
        print("✅ test_agregar_informe_datos_invalidos OK")

if __name__ == "__main__":
    test_agregar_informe()
    test_agregar_informe_duplicado()
    test_buscar_informe_existente()
    test_buscar_informe_inexistente()
    test_eliminar_informe_existente()
    test_eliminar_informe_inexistente()
    test_agregar_varios_informes()
    test_eliminar_todos_informes()
    test_buscar_despues_eliminar()
    test_agregar_informe_datos_invalidos()
    print("🎉 Todas las pruebas simples pasaron correctamente.")