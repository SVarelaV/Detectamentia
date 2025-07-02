from controlador.dominios.informe import Informe
from controlador.gestores.listagen import ListaGen
from typing import List, Optional


class Informes(ListaGen[Informe]):
    """
    Clase especializada para manejar la lista de informes clínicos.
    """

    def __init__(self):
        super().__init__()

    def agregar(self, informe: Informe) -> bool:
        if not self.existe(informe):
            self._elementos.append(informe)
            return True
        return False

    def eliminar(self, id_elemento: int) -> bool:
        informe = self.buscar(id_elemento)
        if informe:
            self._elementos.remove(informe)
            return True
        return False

    def buscar(self, id_elemento: int) -> Optional[Informe]:
        for informe in self._elementos:
            if hasattr(informe, 'id_informe') and informe.id_informe == id_elemento:
                return informe
        return None

    def mostrar_todos(self) -> List[Informe]:
        return self._elementos

    def existe(self, informe: Informe) -> bool:
        return informe in self._elementos
