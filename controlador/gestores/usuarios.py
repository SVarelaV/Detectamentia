from controlador.dominios.usuario import Usuario
from controlador.gestores.listagen import ListaGen
from modelo.config import get_connection
from typing import List, Optional


class Usuarios(ListaGen[Usuario]):
    """
    Clase especializada para manejar la lista de usuarios desde SQL Server.
    """

    def __init__(self):
        super().__init__()
        self._elementos = self.mostrar_todos()


    def agregar(self, usuario: Usuario) -> bool:
        if self.existe(usuario):
            return False
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
                OUTPUT INSERTED.id_usuario
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    usuario.nombre, usuario.apellido1,
                    usuario.apellido2, usuario.rol, usuario.email, usuario.activo
                )
            )
            usuario.id_usuario = cursor.fetchone()[0]
            conn.commit()

            if not usuario.id_usuario:
                print("❌ No se pudo obtener el ID del usuario insertado.")
                return False

            self._elementos.append(usuario)
            return True
        except Exception as e:
            print(f"❌ Error al agregar usuario: {e}")
            return False
        finally:
            conn.close()



    def eliminar(self, id_elemento: int) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Usuarios WHERE id_usuario = ?", (id_elemento,))
            conn.commit()
            eliminado = cursor.rowcount > 0
            if eliminado:
                self._elementos = [u for u in self._elementos if u.id_usuario != id_elemento]
            return eliminado
        except Exception as e:
            print(f"❌ Error al eliminar usuario: {e}")
            return False
        finally:
            conn.close()


    def buscar(self, id_elemento: int) -> Optional[Usuario]:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, apellido1, apellido2, rol, email, activo, id_usuario FROM Usuarios FROM Usuarios WHERE id_usuario = ?", (id_elemento,))
            fila = cursor.fetchone()
            if fila:
                return Usuario(*fila)
            return None
        except Exception as e:
            print(f"❌ Error al buscar usuario: {e}")
            return None
        finally:
            conn.close()


    def mostrar_todos(self) -> List[Usuario]:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, apellido1, apellido2, rol, email, activo, id_usuario FROM Usuarios")
            filas = cursor.fetchall()
            return [Usuario(*fila) for fila in filas]
        except Exception as e:
            print(f"❌ Error al mostrar usuarios: {e}")
            return []
        finally:
            conn.close()


    def existe(self, usuario: Usuario) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM Usuarios WHERE id_usuario = ?", (usuario.id_usuario,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"❌ Error al verificar existencia de usuario: {e}")
            return False
        finally:
            conn.close()


    def actualizar(self, usuario: Usuario) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Usuarios 
                SET nombre = ?, apellido1 = ?, apellido2 = ?, rol = ?, email = ?, activo = ?
                WHERE id_usuario = ?
            ''', (
                usuario.nombre, usuario.apellido1, usuario.apellido2,
                usuario.rol, usuario.email, usuario.activo, usuario.id_usuario
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"❌ Error al actualizar usuario: {e}")
            return False
        finally:
            conn.close()


    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, apellido1, apellido2, rol, email, activo, id_usuario FROM Usuarios FROM Usuarios WHERE email = ?", (email,))
            fila = cursor.fetchone()
            if fila:
                return Usuario(*fila)
            return None
        except Exception as e:
            print(f"❌ Error al buscar por email: {e}")
            return None
        finally:
            conn.close()


    def buscar_por_rol(self, rol: str) -> List[Usuario]:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, apellido1, apellido2, rol, email, activo, id_usuario FROM Usuarios FROM Usuarios WHERE rol = ?", (rol,))
            filas = cursor.fetchall()
            return [Usuario(*fila) for fila in filas]
        except Exception as e:
            print(f"❌ Error al buscar por rol: {e}")
            return []
        finally:
            conn.close()
