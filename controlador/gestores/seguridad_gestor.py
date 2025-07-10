from modelo.config import get_connection
from controlador.dominios.seguridad import Seguridad
from controlador.gestores.usuarios import Usuarios

class SeguridadGestor:
    def __init__(self):
        self.usuarios = Usuarios()

    def buscar_por_id_usuario(self, id_usuario):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id_login, passwd, id_usuario FROM Seguridad WHERE id_usuario = ?", (id_usuario,))
            fila = cursor.fetchone()
            if fila:
                return Seguridad(fila[1], fila[2], fila[0])
            return None
        except Exception as e:
            print(f"❌ Error al buscar credenciales: {e}")
            return None
        finally:
            conn.close()

    def validar_credenciales(self, email, password):
        usuario = self.usuarios.buscar_por_email(email)
        if not usuario or not usuario.activo:
            return None

        credenciales = self.buscar_por_id_usuario(usuario.id_usuario)
        if credenciales and credenciales.passwd == password:
            return usuario
        return None
