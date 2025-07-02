from controlador.dominios.usuario import Usuario
from controlador.gestores.listagen import ListaGen
from typing import List, Optional


class Usuarios(ListaGen[Usuario]):
    """
    Clase especializada para manejar la lista de usuarios del sistema.
    """

    def __init__(self):
        super().__init__()

    def agregar(self, usuario: Usuario) -> bool:
        if not self.existe(usuario):
            self._elementos.append(usuario)
            return True
        return False

    def eliminar(self, id_elemento: int) -> bool:
        usuario = self.buscar(id_elemento)
        if usuario:
            self._elementos.remove(usuario)
            return True
        return False

    def buscar(self, id_elemento: int) -> Optional[Usuario]:
        for usuario in self._elementos:
            if hasattr(usuario, 'id_usuario') and usuario.id_usuario == id_elemento:
                return usuario
        return None

    def mostrar_todos(self) -> List[Usuario]:
        return self._elementos

    def existe(self, usuario: Usuario) -> bool:
        return usuario in self._elementos

    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        """
        Busca un usuario por su correo electrónico.
        """
        for usuario in self._elementos:
            if usuario.email == email:
                return usuario
        return None

    def buscar_por_rol(self, rol: str):
        """
        Busca usuarios por rol.

        Args:
            rol (str): Rol a buscar

        Returns:
            Lista de usuarios con el rol especificado
        """
        usuarios_filtrados = []
        for usuario in self._elementos:
            if usuario.rol == rol:
                usuarios_filtrados.append(usuario)
        return usuarios_filtrados