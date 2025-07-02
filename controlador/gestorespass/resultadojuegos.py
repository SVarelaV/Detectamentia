from controlador.dominios.resultadojuego import ResultadoJuego
from controlador.gestores.listagen import ListaGen
from typing import List, Optional


class ResultadoJuegos(ListaGen[ResultadoJuego]):
    """
    Clase especializada para manejar la lista de resultados de juegos cognitivos.
    """

    def __init__(self):
        super().__init__()

    def agregar(self, resultado: ResultadoJuego) -> bool:
        if not self.existe(resultado):
            self._elementos.append(resultado)
            return True
        return False

    def eliminar(self, id_elemento: int) -> bool:
        resultado = self.buscar(id_elemento)
        if resultado:
            self._elementos.remove(resultado)
            return True
        return False

    def buscar(self, id_elemento: int) -> Optional[ResultadoJuego]:
        for resultado in self._elementos:
            if hasattr(resultado, 'id_resultado') and resultado.id_resultado == id_elemento:
                return resultado
        return None

    def mostrar_todos(self) -> List[ResultadoJuego]:
        return self._elementos

    def existe(self, resultado: ResultadoJuego) -> bool:
        return resultado in self._elementos
