from controlador.dominios.informe import Informe
from controlador.gestores.listagen import ListaGen
from modelo.config import get_connection
from typing import List, Optional


class Informes(ListaGen[Informe]):
    """
    Clase especializada para manejar la lista de informes clínicos desde SQL Server.
    """

    def __init__(self):
        super().__init__()
        self._elementos = self.mostrar_todos()

    def agregar(self, informe: Informe) -> bool:
        if self.existe(informe):
            return False
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Informes (
                    id_informe, fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol,
                    migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular,
                    trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol,
                    actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                informe.id_informe, informe.fechaRegistro, informe.antecFamiliaresAlzheimer, informe.diabetes,
                informe.colesterol, informe.migrainas, informe.hipertension, informe.cardiopatia,
                informe.depresionDiag, informe.accidenteCerebrovascular, informe.trastornoSueno,
                informe.horaSueno, informe.calidadSueno, informe.fumador, informe.consumoAlcohol,
                informe.actividadFisica, informe.nivelEstres, informe.dietaSaludable,
                informe.presionArterialSis, informe.presionArterialDia
            ))
            conn.commit()
            self._elementos.append(informe)
            return True
        except Exception as e:
            print(f"❌ Error al agregar informe: {e}")
            return False
        finally:
            conn.close()

    def eliminar(self, id_elemento: int) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Informes WHERE id_informe = ?", (id_elemento,))
            conn.commit()
            eliminado = cursor.rowcount > 0
            if eliminado:
                self._elementos = [i for i in self._elementos if i.id_informe != id_elemento]
            return eliminado
        except Exception as e:
            print(f"❌ Error al eliminar informe: {e}")
            return False
        finally:
            conn.close()

    def buscar(self, id_elemento: int) -> Optional[Informe]:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Informes WHERE id_informe = ?", (id_elemento,))
            fila = cursor.fetchone()
            if fila:
                return Informe(*fila)
            return None
        except Exception as e:
            print(f"❌ Error al buscar informe: {e}")
            return None
        finally:
            conn.close()

    def mostrar_todos(self) -> List[Informe]:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Informes")
            filas = cursor.fetchall()
            return [Informe(*fila) for fila in filas]
        except Exception as e:
            print(f"❌ Error al mostrar informes: {e}")
            return []
        finally:
            conn.close()

    def existe(self, informe: Informe) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM Informes WHERE id_informe = ?", (informe.id_informe,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"❌ Error al verificar existencia de informe: {e}")
            return False
        finally:
            conn.close()

    def actualizar(self, informe: Informe) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                '''
                UPDATE Informes SET
                    fechaRegistro = ?, antecFamiliaresAlzheimer = ?, diabetes = ?, colesterol = ?,
                    migrainas = ?, hipertension = ?, cardiopatia = ?, depresionDiag = ?, accidenteCerebrovascular = ?,
                    trastornoSueno = ?, horaSueno = ?, calidadSueno = ?, fumador = ?, consumoAlcohol = ?,
                    actividadFisica = ?, nivelEstres = ?, dietaSaludable = ?, presionArterialSis = ?, presionArterialDia = ?
                WHERE id_informe = ?
                ''',
                (
                    informe.fechaRegistro, informe.antecFamiliaresAlzheimer, informe.diabetes, informe.colesterol,
                    informe.migrainas, informe.hipertension, informe.cardiopatia, informe.depresionDiag,
                    informe.accidenteCerebrovascular, informe.trastornoSueno, informe.horaSueno, informe.calidadSueno,
                    informe.fumador, informe.consumoAlcohol, informe.actividadFisica, informe.nivelEstres,
                    informe.dietaSaludable, informe.presionArterialSis, informe.presionArterialDia,
                    informe.id_informe
                )
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"❌ Error al actualizar informe: {e}")
            return False
        finally:
            conn.close()
