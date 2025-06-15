
from controlador.dominios.resultadojuego import ResultadoJuego
from controlador.gestores.listagen import ListaGen


class ResultadoJuegos(ListaGen[ResultadoJuego]):
    """
    Clase especializada para manejar la lista de resultados de juegos cognitivos.
    """

    def __init__(self):
        """
        Inicializa la lista de resultados de juegos.
        """
        super().__init__()
