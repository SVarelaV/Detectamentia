from modelo.config import get_connection

def agregar_paciente(id_paciente, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO Pacientes 
            (id_paciente, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (id_paciente, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"❌ Error al agregar paciente: {e}")
        return False
    finally:
        conn.close()

def buscar_paciente_por_id(id_paciente):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Pacientes WHERE id_paciente = ?", (id_paciente,))
        return cursor.fetchone()
    except Exception as e:
        print(f"❌ Error al buscar paciente por ID: {e}")
        return None
    finally:
        conn.close()

def eliminar_paciente(id_paciente):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Pacientes WHERE id_paciente = ?", (id_paciente,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"❌ Error al eliminar paciente: {e}")
        return False
    finally:
        conn.close()

def mostrar_pacientes():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Pacientes")
        return cursor.fetchall()
    except Exception as e:
        print(f"❌ Error al mostrar pacientes: {e}")
        return []
    finally:
        conn.close()

def existe_paciente(id_paciente):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM Pacientes WHERE id_paciente = ?", (id_paciente,))
        return cursor.fetchone() is not None
    except Exception as e:
        print(f"❌ Error al verificar existencia de paciente: {e}")
        return False
    finally:
        conn.close()

def actualizar_paciente(id_paciente, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            UPDATE Pacientes 
            SET nombre = ?, apellido1 = ?, apellido2 = ?, genero = ?, edad = ?, 
                poblacion = ?, ocupacion = ?, nivelEstudios = ?
            WHERE id_paciente = ?
            ''',
            (nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios, id_paciente)
        )
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"❌ Error al actualizar paciente: {e}")
        return False
    finally:
        conn.close()

