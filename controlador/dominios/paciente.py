class Paciente:
    def __init__(self, id_paciente, nombre, apellido1, apellido2, fecha_nacimiento, genero):
        self._id_paciente = id_paciente
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._fechaNac = fecha_nacimiento
        self._genero = genero

    @property
    def id_paciente(self):
        return self._id_paciente

    @id_paciente.setter
    def id_paciente(self, id_paciente):
        self._id_paciente = id_paciente

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
    def fecha_nacimiento(self):
        return self._fechaNac

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fechaNac = fecha_nacimiento

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero
