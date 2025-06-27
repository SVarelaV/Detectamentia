from modelo.config import get_connection

def agregar_resultado_juego(id_resultado, id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, tiempoTotal, numeroIntentos):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO ResultadoJuegos (
                id_resultado, id_paciente, nombreJuego, fecha, tiempoReaccion,
                aciertos, errores, tiempoTotal, numeroIntentos
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (id_resultado, id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, tiempoTotal, numeroIntentos)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"❌ Error al agregar resultado de juego: {e}")
        return False
    finally:
        conn.close()

def buscar_resultado_por_id(id_resultado):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ResultadoJuegos WHERE id_resultado = ?", (id_resultado,))
        return cursor.fetchone()
    except Exception as e:
        print(f"❌ Error al buscar resultado de juego: {e}")
        return None
    finally:
        conn.close()

def eliminar_resultado(id_resultado):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ResultadoJuegos WHERE id_resultado = ?", (id_resultado,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"❌ Error al eliminar resultado de juego: {e}")
        return False
    finally:
        conn.close()

def mostrar_resultados():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ResultadoJuegos")
        return cursor.fetchall()
    except Exception as e:
        print(f"❌ Error al mostrar resultados de juego: {e}")
        return []
    finally:
        conn.close()

def existe_resultado(id_resultado):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM ResultadoJuegos WHERE id_resultado = ?", (id_resultado,))
        return cursor.fetchone() is not None
    except Exception as e:
        print(f"❌ Error al verificar existencia del resultado: {e}")
        return False
    finally:
        conn.close()

def actualizar_resultado_juego(id_resultado, id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, tiempoTotal, numeroIntentos):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            UPDATE ResultadoJuegos
            SET id_paciente = ?, nombreJuego = ?, fecha = ?, tiempoReaccion = ?, 
                aciertos = ?, errores = ?, tiempoTotal = ?, numeroIntentos = ?
            WHERE id_resultado = ?
            ''',
            (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, tiempoTotal, numeroIntentos, id_resultado)
        )
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"❌ Error al actualizar resultado de juego: {e}")
        return False
    finally:
        conn.close()
