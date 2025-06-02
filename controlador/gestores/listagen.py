from typing import TypeVar, Generic, List, Optional

T = TypeVar('T')

class ListaGen(Generic[T]):
    """
    Clase genérica para gestionar listas de elementos.
    """

    def __init__(self):
        self._elementos: List[T] = []

    def agregar(self, elemento: T) -> bool:
        """
        Agrega un elemento a la lista.
        
        Args:
            elemento: El elemento a agregar
            
        Returns:
            bool: True si se agregó correctamente, False si ya existe
        """
        if not self.existe(elemento):
            self._elementos.append(elemento)
            return True
        return False
    
    def eliminar(self, id_elemento: int) -> bool:
        """
        Elimina un elemento de la lista por su ID.
        
        Args:
            id_elemento: ID del elemento a eliminar
            
        Returns:
            bool: True si se eliminó, False si no se encontró
        """
        elemento = self.buscar(id_elemento)
        if elemento:
            self._elementos.remove(elemento)
            return True
        return False
    
    def buscar(self, id_elemento: int) -> Optional[T]:
        """
        Busca un elemento por su ID.
        
        Args:
            id_elemento: ID del elemento a buscar
            
        Returns:
            Optional[T]: El elemento si se encuentra, None en caso contrario
        """
        for elemento in self._elementos:
            if hasattr(elemento, 'id') and elemento.id == id_elemento:
                return elemento
        return None
    
    def mostrar_todos(self) -> List[T]:
        """
        Muestra todos los elementos de la lista.
        
        Returns:
            List[T]: Lista de todos los elementos
        """
        return self._elementos
    
    def existe(self, elemento: T) -> bool:
        """
        Verifica si un elemento ya existe en la lista.
        
        Args:
            elemento: El elemento a verificar
            
        Returns:
            bool: True si el elemento ya existe, False en caso contrario
        """
        if elemento in self._elementos:
            return True
        else:
            return False
