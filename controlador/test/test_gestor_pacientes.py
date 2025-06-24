from controlador.gestores.gestor_pacientes import GestorPacientes
from controlador.dominios.paciente import Paciente

def test_agregar_paciente_valido():
    gestor = GestorPacientes()
    paciente = Paciente(100, "Juan", "Pérez", "López", "Masculino", 70, "Madrid", "Jubilado", "Universidad completa")
    gestor.agregar(paciente)
    print("✅ Paciente válido agregado correctamente")

def test_agregar_paciente_duplicado():
    gestor = GestorPacientes()
    paciente1 = Paciente(101, "Ana", "Ruiz", "Gómez", "Femenino", 65, "Sevilla", "Ama de casa", "Primaria completa")
    paciente2 = Paciente(101, "Ana", "Ruiz", "Gómez", "Femenino", 65, "Sevilla", "Ama de casa", "Primaria completa")
    gestor.agregar(paciente1)
    try:
        gestor.agregar(paciente2)
        print("❌ Error esperado: Se permitió agregar paciente duplicado")
    except Exception as e:
        print("✅ Error capturado al agregar duplicado:", str(e))

def test_agregar_paciente_id_duplicado_datos_diferentes():
    gestor = GestorPacientes()
    paciente1 = Paciente(105, "Carlos", "Martín", "Soto", "Masculino", 80, "Madrid", "Jubilado", "Universidad")
    paciente2 = Paciente(105, "Carla", "Martínez", "Soto", "Femenino", 75, "Madrid", "Jubilada", "Universidad")
    gestor.agregar(paciente1)
    try:
        gestor.agregar(paciente2)
        print("❌ Error esperado: Se permitió agregar paciente con ID duplicado y datos diferentes")
    except Exception as e:
        print("✅ Error capturado al agregar duplicado con datos diferentes:", str(e))

def test_buscar_paciente_existente():
    gestor = GestorPacientes()
    paciente = Paciente(110, "Test", "Uno", "Apellido", "Otro", 50, "Ciudad", "Ocupación", "Estudios")
    gestor.agregar(paciente)
    encontrado = gestor.lista_pacientes.buscar(110)
    assert encontrado is not None
    print("✅ Buscar paciente existente funciona correctamente")

def test_buscar_paciente_inexistente():
    gestor = GestorPacientes()
    encontrado = gestor.lista_pacientes.buscar(999)
    assert encontrado is None
    print("✅ Buscar paciente inexistente funciona correctamente")

def test_eliminar_paciente_existente():
    gestor = GestorPacientes()
    paciente = Paciente(120, "Eliminar", "Prueba", "Apellido", "Otro", 60, "Ciudad", "Ocupación", "Estudios")
    gestor.agregar(paciente)
    eliminado = gestor.lista_pacientes.eliminar(120)
    assert eliminado is True
    print("✅ Eliminar paciente existente funciona correctamente")

def test_eliminar_paciente_inexistente():
    gestor = GestorPacientes()
    eliminado = gestor.lista_pacientes.eliminar(999)
    assert eliminado is False
    print("✅ Eliminar paciente inexistente funciona correctamente")

def test_mostrar_todos():
    gestor = GestorPacientes()
    pacientes = gestor.lista_pacientes.mostrar_todos()
    assert isinstance(pacientes, list)
    print("✅ Mostrar todos los pacientes funciona correctamente")

# Ejecutar todas las pruebas
if __name__ == "__main__":
    test_agregar_paciente_valido()
    test_agregar_paciente_duplicado()
    test_agregar_paciente_id_duplicado_datos_diferentes()
    test_buscar_paciente_existente()
    test_buscar_paciente_inexistente()
    test_eliminar_paciente_existente()
    test_eliminar_paciente_inexistente()
    test_mostrar_todos()
    print("🎉 Todas las pruebas pasaron correctamente.")