from controlador.dominios.paciente import Paciente
from controlador.gestores.listagen import ListaGen
from typing import List, Optional


class Pacientes(ListaGen[Paciente]):
    """
    Clase especializada para manejar la lista de pacientes.
    """

    def __init__(self):
        super().__init__()

    def agregar(self, paciente: Paciente) -> bool:
        if not self.existe(paciente):
            self._elementos.append(paciente)
            return True
        return False

    def eliminar(self, id_elemento: int) -> bool:
        paciente = self.buscar(id_elemento)
        if paciente:
            self._elementos.remove(paciente)
            return True
        return False

    def buscar(self, id_elemento: int) -> Optional[Paciente]:
        for paciente in self._elementos:
            if hasattr(paciente, 'id_paciente') and paciente.id_paciente == id_elemento:
                return paciente
        return None

    def mostrar_todos(self) -> List[Paciente]:
        return self._elementos

    def existe(self, paciente: Paciente) -> bool:
        return paciente in self._elementos
