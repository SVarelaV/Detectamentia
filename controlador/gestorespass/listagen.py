from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar('T')

class ListaGen(ABC, Generic[T]):
    """
    Clase base abstracta para gestionar listas de elementos genéricos.
    """

    def __init__(self):
        self._elementos: List[T] = []
        self._atributos_id = ['id_paciente', 'id_usuario', 'id_informe', 'id_resultado']

    @abstractmethod
    def agregar(self, elemento: T) -> bool:
        pass

    @abstractmethod
    def eliminar(self, id_elemento: int) -> bool:
        pass

    @abstractmethod
    def buscar(self, id_elemento: int) -> T:
        pass

    @abstractmethod
    def mostrar_todos(self) -> List[T]:
        pass

    @abstractmethod
    def existe(self, elemento: T) -> bool:
        pass
