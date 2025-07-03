
from controlador.dominios.usuario import Usuario
from controlador.gestores.listagen import ListaGen


class Usuarios(ListaGen[Usuario]):
    """
    Clase especializada para manejar la lista de usuarios del sistema.
    """

    def __init__(self):
        """
        Inicializa la lista de usuarios.
        """
        super().__init__()

    def buscar_por_email(self, email: str):
        """
        Busca un usuario por su correo electrónico.

        Args:
            email (str): Correo a buscar

        Returns:
            Usuario o None
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
