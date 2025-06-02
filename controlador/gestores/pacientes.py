from controlador.dominios.paciente import Paciente
from controlador.gestores.listagen import ListaGen


class Pacientes(ListaGen[Paciente]):
    """
    Clase especializada para manejar la lista de pacientes.
    (Por ahora hereda todo de ListaGen sin necesidad de modificar)
    """
    pass


