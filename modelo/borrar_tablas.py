from config import get_connection

def eliminar_tablas():
    conn = get_connection()
    cursor = conn.cursor()

    # Orden corregido: hijos → padres
    tablas = ["Seguridad", "ResultadoJuegos", "Informes", "Pacientes", "Usuarios"]

    for tabla in tablas:
        try:
            cursor.execute(f"DROP TABLE IF EXISTS {tabla}")
            print(f"✅ Tabla '{tabla}' eliminada (si existía).")
        except Exception as e:
            print(f"❌ Error eliminando la tabla {tabla}: {e}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    eliminar_tablas()

