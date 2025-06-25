class Usuario:
    def __init__(self, id, nombre, apellido1, apellido2, rol, email, activo):
        self._id = id
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._rol = rol
        self._email = email
        self._activo = activo

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido1(self):
        return self._apellido1

    @apellido1.setter
    def apellido1(self, apellido1):
        self._apellido1 = apellido1

    @property
    def apellido2(self):
        return self._apellido2

    @apellido2.setter
    def apellido2(self, apellido2):
        self._apellido2 = apellido2

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, activo):
        self._activo = activo
