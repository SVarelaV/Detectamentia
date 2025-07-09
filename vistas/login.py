# login_simple.py
from modelo.config import get_connection

def login_basico():
    print("\n🔐 LOGIN BÁSICO - DetectaMentIA")
    email = input("📧 Email: ").strip()
    password = input("🔑 Contraseña: ").strip()

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT u.nombre, u.apellido1, u.rol, u.activo
            FROM Usuarios u
            JOIN Seguridad s ON u.id_usuario = s.id_usuario
            WHERE u.email = ? AND s.passwd = ?
        ''', (email, password))

        fila = cursor.fetchone()
        if fila is None:
            print("❌ Usuario o contraseña incorrectos.")
            return None

        nombre, apellido1, rol, activo = fila

        if not activo:
            print("⛔ Usuario inactivo. Contacte al administrador.")
            return None

        print(f"✅ Bienvenido, {nombre} {apellido1} ({rol})")
        return True

    except Exception as e:
        print(f"❌ Error de autenticación: {e}")
        return None
    finally:
        conn.close()

if __name__ == "__main__":
    acceso = login_basico()
    if acceso:
        print("➡️ Acceso permitido al sistema")
    else:
        print("🚪 Cerrando aplicación.")


