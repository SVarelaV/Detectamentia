class Paciente:
    def __init__(self, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios, id_paciente=None):
        self._id_paciente = id_paciente
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._genero = genero
        self._edad = edad
        self._poblacion = poblacion
        self._ocupacion = ocupacion
        self._nivelEstudios = nivelEstudios

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
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def poblacion(self):
        return self._poblacion

    @poblacion.setter
    def poblacion(self, poblacion):
        self._poblacion = poblacion 

    @property
    def ocupacion(self):
        return self._ocupacion

    @ocupacion.setter
    def ocupacion(self, ocupacion):
        self._ocupacion = ocupacion

    @property
    def nivelEstudios(self):
        return self._nivelEstudios

    @nivelEstudios.setter
    def nivelEstudios(self, nivelEstudios):
        self._nivelEstudios = nivelEstudios
