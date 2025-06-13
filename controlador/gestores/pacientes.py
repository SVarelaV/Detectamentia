from controlador.dominios.paciente import Paciente
from controlador.gestores.listagen import ListaGen


class Pacientes(ListaGen[Paciente]):
    """
    Clase especializada para manejar la lista de pacientes.
    """
    
    def __init__(self):
        """
        Inicializa la lista de pacientes.
        """
        super().__init__()



