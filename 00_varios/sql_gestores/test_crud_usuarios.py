from controlador.sql_gestores.crud_usuarios import *

# Test manual para verificar el CRUD de usuarios
def test_crud_usuarios():
    id_test = 999  # Ahora es un entero, no string
    print("\n🔹 Agregando usuario de prueba...")
    agregado = agregar_usuario(
        id_usuario=id_test,
        nombre='Carlos',
        apellido1='García',
        apellido2='López',
        rol='paciente',
        email='carlos.prueba@example.com',
        activo=1
    )
    print("✅ Usuario agregado:", agregado)

    print("\n🔍 Verificando si el usuario existe...")
    existe = existe_usuario(id_test)
    print("Existe:", existe)

    print("\n📧 Buscando por email...")
    usuario = buscar_usuario_por_email('carlos.prueba@example.com')
    print("Resultado:", usuario)

    print("\n👥 Buscando usuarios por rol 'paciente'...")
    pacientes = buscar_usuarios_por_rol('paciente')
    print(f"Se encontraron {len(pacientes)} usuario(s) con rol paciente")

    print("\n✏️ Actualizando usuario...")
    actualizado = actualizar_usuario(
        id_usuario=id_test,
        nombre='Carlos Modificado',
        apellido1='García',
        apellido2='López',
        rol='paciente',
        email='carlos.prueba@example.com',
        activo=0
    )
    print("Actualizado:", actualizado)

    print("\n📋 Mostrando todos los usuarios...")
    usuarios = mostrar_usuarios()
    for u in usuarios:
        print(u)

    print("\n🗑️ Eliminando usuario de prueba...")
    eliminado = eliminar_usuario(id_test)
    print("Eliminado:", eliminado)

if __name__ == "__main__":
    test_crud_usuarios()
