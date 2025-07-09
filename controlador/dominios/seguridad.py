class Seguridad:
    def __init__(self, passwd, id_usuario=None, id_login=None):
        self._id_login = id_login
        self._passwd = passwd
        self._id_usuario = id_usuario

    @property
    def id_login(self):
        return self._id_login

    @id_login.setter
    def id_login(self, id_login):
        self._id_login = id_login

    @property
    def passwd(self):
        return self._passwd

    @passwd.setter
    def passwd(self, passwd):
        self._passwd = passwd

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario
