from paciente import Paciente


class Pacientes():
    def __init__(self):
        self.lista_pacientes = []

    def agregar_paciente(self, paciente):
        self.lista_pacientes.append(paciente)

    def buscar_paciente(self, id_paciente):
        for paciente in self.lista_pacientes:
            if paciente.id_paciente == id_paciente:
                return paciente
        return None

    def eliminar_paciente(self, id_paciente):
        paciente = self.buscar_paciente(id_paciente)
        if paciente:
            self.lista_pacientes.remove(paciente)

    def mostrar_paciente(self):
        for paciente in self.lista_pacientes:
            return paciente
        return None

    def existe_paciente(self, id_paciente):
        for paciente in self.lista_pacientes:
            if paciente.id_paciente == id_paciente:
                return True
        return False
