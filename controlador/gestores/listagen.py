from typing import TypeVar, Generic, List, Optional

T = TypeVar('T')

class ListaGen(Generic[T]):
    """
    Clase genérica para gestionar listas de elementos.
    """

    def __init__(self):
        self._elementos: List[T] = []
        self._atributos_id = ['id_paciente', 'id_usuario', 'id_informe', 'id_resultado']

    def agregar(self, elemento: T) -> bool:
        """
        Agrega un elemento a la lista si no existe.
        """
        if not self.existe(elemento):
            self._elementos.append(elemento)
            return True
        return False

    def eliminar(self, id_elemento: int) -> bool:
        """
        Elimina un elemento de la lista por su ID específico.
        """
        elemento = self.buscar(id_elemento)
        if elemento:
            self._elementos.remove(elemento)
            return True
        return False

    def buscar(self, id_elemento: int) -> Optional[T]:
        """
        Busca un elemento por su identificador único específico.
        """
        for elemento in self._elementos:
            for atributo in self._atributos_id:
                if hasattr(elemento, atributo) and getattr(elemento, atributo) == id_elemento:
                    return elemento
        return None

    def mostrar_todos(self) -> List[T]:
        """
        Devuelve todos los elementos de la lista.
        """
        return self._elementos

    def existe(self, elemento: T) -> bool:
        """
        Verifica si el elemento ya existe en la lista (por igualdad de objetos).
        """
        return elemento in self._elementos

