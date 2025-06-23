from controlador.gestores.gestor_usuarios import GestorUsuarios
from controlador.dominios.usuario import Usuario


def test_agregar_usuario_valido():
    gestor = GestorUsuarios()
    usuario = Usuario(100, "Mario", "López", "García", "clave", "profesional", "mario@example.com", True)
    gestor.agregar(usuario)
    print("✅ Usuario válido agregado correctamente")

def test_agregar_usuario_duplicado():
    gestor = GestorUsuarios()
    usuario1 = Usuario(101, "Ana", "Ruiz", "Gómez", "clave", "paciente", "ana@example.com", True)
    usuario2 = Usuario(101, "Ana", "Ruiz", "Gómez", "clave", "paciente", "ana@example.com", True)
    gestor.agregar(usuario1)
    try:
        gestor.agregar(usuario2)
        print("❌ Error esperado: Se permitió agregar usuario duplicado")
    except Exception as e:
        print("✅ Error capturado al agregar duplicado:", str(e))

def test_buscar_usuario_existente():
    gestor = GestorUsuarios()
    usuario = Usuario(110, "Test", "Uno", "Apellido", "clave", "profesional", "test@example.com", True)
    gestor.usuarios.agregar(usuario)
    encontrado = gestor.usuarios.buscar(110)
    assert encontrado is not None
    print("✅ Buscar usuario existente funciona correctamente")

def test_buscar_usuario_inexistente():
    gestor = GestorUsuarios()
    encontrado = gestor.usuarios.buscar(999)
    assert encontrado is None
    print("✅ Buscar usuario inexistente funciona correctamente")

def test_eliminar_usuario_existente():
    gestor = GestorUsuarios()
    usuario = Usuario(120, "Eliminar", "Prueba", "Apellido", "clave", "paciente", "elim@example.com", True)
    gestor.usuarios.agregar(usuario)
    eliminado = gestor.usuarios.eliminar(120)
    assert eliminado is True
    print("✅ Eliminar usuario existente funciona correctamente")

def test_eliminar_usuario_inexistente():
    gestor = GestorUsuarios()
    eliminado = gestor.usuarios.eliminar(999)
    assert eliminado is False
    print("✅ Eliminar usuario inexistente funciona correctamente")

def test_mostrar_todos():
    gestor = GestorUsuarios()
    usuarios = gestor.usuarios.mostrar_todos()
    assert isinstance(usuarios, list)
    print("✅ Mostrar todos los usuarios funciona correctamente")

def test_agregar_usuario_email_duplicado():
    gestor = GestorUsuarios()
    usuario1 = Usuario(200, "Pepe", "García", "López", "clave", "paciente", "pepe@example.com", True)
    usuario2 = Usuario(201, "Pepa", "García", "López", "clave", "paciente", "pepe@example.com", True)
    gestor.agregar(usuario1)
    try:
        gestor.agregar(usuario2)
        print("❌ Error esperado: Se permitió agregar usuario con email duplicado")
    except Exception as e:
        print("✅ Error capturado al agregar email duplicado:", str(e))

def test_agregar_usuario_rol_invalido():
    gestor = GestorUsuarios()
    usuario = Usuario(202, "Luis", "Martín", "Soto", "clave", "admin", "luis@example.com", True)
    try:
        gestor.agregar(usuario)
        print("❌ Error esperado: Se permitió agregar usuario con rol inválido")
    except Exception as e:
        print("✅ Error capturado al agregar rol inválido:", str(e))

def test_agregar_usuario_contrasena_corta():
    gestor = GestorUsuarios()
    usuario = Usuario(203, "Ana", "Ruiz", "Gómez", "123", "paciente", "ana2@example.com", True)
    try:
        gestor.agregar(usuario)
        print("❌ Error esperado: Se permitió agregar usuario con contraseña corta")
    except Exception as e:
        print("✅ Error capturado al agregar contraseña corta:", str(e))

def test_buscar_usuario_por_email():
    gestor = GestorUsuarios()
    usuario = Usuario(204, "Eva", "López", "Martínez", "clave", "profesional", "eva@example.com", True)
    gestor.agregar(usuario)
    encontrado = gestor.usuarios.buscar_por_email("eva@example.com")
    assert encontrado is not None
    print("✅ Buscar usuario por email funciona correctamente")

def test_buscar_usuario_por_rol():
    gestor = GestorUsuarios()
    usuario = Usuario(205, "Raúl", "Soto", "Díaz", "clave", "paciente", "raul@example.com", True)
    gestor.agregar(usuario)
    lista = gestor.usuarios.buscar_por_rol("paciente")
    assert any(u.id == 205 for u in lista)
    print("✅ Buscar usuario por rol funciona correctamente")


if __name__ == "__main__":
    test_agregar_usuario_valido()
    test_agregar_usuario_duplicado()
    test_agregar_usuario_email_duplicado()
    test_agregar_usuario_rol_invalido()
    test_agregar_usuario_contrasena_corta()
    test_buscar_usuario_existente()
    test_buscar_usuario_inexistente()
    test_buscar_usuario_por_email()
    test_buscar_usuario_por_rol()
    test_eliminar_usuario_existente()
    test_eliminar_usuario_inexistente()
    test_mostrar_todos()