from informe import Informe


class Informes():
    def __init__(self):
        self.lista_informes = []

    def agregar_informe(self, informe):
        self.lista_informes.append(informe)

    def buscar_informe(self, id_informe):
        for informe in self.lista_informes:
            if informe.id_informe == id_informe:
                return informe
        return None

    def eliminar_informe(self, id_informe):
        informe = self.buscar_informe(id_informe)
        if informe:
            self.lista_informes.remove(informe)

    def mostrar_informe(self):
        for informe in self.lista_informes:
            return informe
        return None

    def existe_informe(self, id_informe):
        for informe in self.lista_informes:
            if informe.id_informe == id_informe:
                return True
        return False
