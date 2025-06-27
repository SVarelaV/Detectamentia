from modelo.config import get_connection

def agregar_usuario(id_usuario, nombre, apellido1, apellido2, rol, email, activo):
    """
    Agregar un nuevo usuario a la base de datos
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Usuarios (id_usuario, nombre, apellido1, apellido2, rol, email, activo) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (id_usuario, nombre, apellido1, apellido2, rol, email, activo)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"❌ Error al agregar usuario: {e}")
        return False
    finally:
        conn.close()

def existe_usuario(id_usuario):
    """
    Verificar si un usuario existe en la base de datos por su ID
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM Usuarios WHERE id_usuario = ?", (id_usuario,))
        return cursor.fetchone() is not None
    except Exception as e:
        print(f"❌ Error al verificar existencia de usuario: {e}")
        return False
    finally:
        conn.close()

def buscar_usuario_por_email(email):
    """"
    Buscar un usuario por su email en la base de datos
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE email = ?", (email,))
        return cursor.fetchone()
    except Exception as e:
        print(f"❌ Error al buscar usuario por email: {e}")
        return None
    finally:
        conn.close()

def buscar_usuarios_por_rol(rol):
    """
    Buscar usuarios por su rol en la base de datos
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE rol = ?", (rol,))
        return cursor.fetchall()
    except Exception as e:
        print(f"❌ Error al buscar usuarios por rol: {e}")
        return []
    finally:
        conn.close()

def eliminar_usuario(id_usuario):
    """
    Eliminar un usuario por su ID
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Usuarios WHERE id_usuario = ?", (id_usuario,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"❌ Error al eliminar usuario: {e}")
        return False
    finally:
        conn.close()

def mostrar_usuarios():
    """
    Mostrar todos los usuarios
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Usuarios")
        usuarios = cursor.fetchall()
        return usuarios
    except Exception as e:
        print(f"❌ Error al mostrar usuarios: {e}")
        return []
    finally:
        conn.close()
        
def actualizar_usuario(id_usuario, nombre, apellido1, apellido2, rol, email, activo):
    """
    Actualizar un usuario existente en la base de datos
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            UPDATE Usuarios 
            SET nombre = ?, apellido1 = ?, apellido2 = ?, rol = ?, email = ?, activo = ?
            WHERE id_usuario = ?
            ''',
            (nombre, apellido1, apellido2, rol, email, activo, id_usuario)
        )
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"❌ Error al actualizar usuario: {e}")
        return False
    finally:
        conn.close()




