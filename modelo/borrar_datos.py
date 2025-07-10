# borrar_datos.py

from config import get_connection

def borrar_datos():
    conn = get_connection()
    cursor = conn.cursor()

    # Orden correcto: primero tablas hijas, luego las padres
    tablas = ["Seguridad", "ResultadoJuegos", "Pacientes", "Informes", "Usuarios"]

    for tabla in tablas:
        try:
            cursor.execute(f"DELETE FROM {tabla}")
            print(f"🗑️ Datos borrados de la tabla '{tabla}'.")
        except Exception as e:
            print(f"❌ Error al borrar datos de {tabla}: {e}")

    conn.commit()
    conn.close()
    print("✅ Borrado de datos completado.")

if __name__ == "__main__":
    borrar_datos()
