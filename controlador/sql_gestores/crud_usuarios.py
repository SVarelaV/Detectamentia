def agregar_usuario(id_usuario, nombre, apellido1, apellido2, rol, email, activo):
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

