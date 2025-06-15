
from controlador.dominios.informe import Informe
from controlador.gestores.listagen import ListaGen


class Informes(ListaGen[Informe]):
    """
    Clase especializada para manejar la lista de informes clínicos.
    """

    def __init__(self):
        """
        Inicializa la lista de informes.
        """
        super().__init__()
