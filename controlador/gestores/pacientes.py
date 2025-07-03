from controlador.dominios.paciente import Paciente
from controlador.gestores.listagen import ListaGen
from modelo.config import get_connection
from typing import List, Optional


class Pacientes(ListaGen[Paciente]):
    """
    Clase especializada para manejar la lista de pacientes desde SQL Server.
    """

    def __init__(self):
        super().__init__()
        self._elementos = self.mostrar_todos()

    def agregar(self, paciente: Paciente) -> bool:
        if self.existe(paciente):
            return False
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Pacientes (
                    id_paciente, nombre, apellido1, apellido2, genero, edad,
                    poblacion, ocupacion, nivelEstudios
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                paciente.id_paciente, paciente.nombre, paciente.apellido1, paciente.apellido2,
                paciente.genero, paciente.edad, paciente.poblacion,
                paciente.ocupacion, paciente.nivelEstudios
            ))
            conn.commit()
            self._elementos.append(paciente)
            return True
        except Exception as e:
            print(f"❌ Error al agregar paciente: {e}")
            return False
        finally:
            conn.close()

    def eliminar(self, id_elemento: int) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Pacientes WHERE id_paciente = ?", (id_elemento,))
            conn.commit()
            eliminado = cursor.rowcount > 0
            if eliminado:
                self._elementos = [p for p in self._elementos if p.id_paciente != id_elemento]
            return eliminado
        except Exception as e:
            print(f"❌ Error al eliminar paciente: {e}")
            return False
        finally:
            conn.close()

    def buscar(self, id_elemento: int) -> Optional[Paciente]:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            # cursor.execute("SELECT * FROM Pacientes WHERE id_paciente = ?", (id_elemento,))
            cursor.execute("""
            SELECT id_paciente, nombre, apellido1, apellido2, genero, edad,
                poblacion, ocupacion, nivelEstudios
            FROM Pacientes
            WHERE id_paciente = ?
        """, (id_elemento,))

            fila = cursor.fetchone()
            if fila:
                return Paciente(*fila)
            return None
        except Exception as e:
            print(f"❌ Error al buscar paciente: {e}")
            return None
        finally:
            conn.close()

    def mostrar_todos(self) -> List[Paciente]:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id_paciente, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios FROM Pacientes")
            # cursor.execute("SELECT * FROM Pacientes")
            filas = cursor.fetchall()
            return [Paciente(*fila) for fila in filas]
        except Exception as e:
            print(f"❌ Error al mostrar pacientes: {e}")
            return []
        finally:
            conn.close()

    def existe(self, paciente: Paciente) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM Pacientes WHERE id_paciente = ?", (paciente.id_paciente,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"❌ Error al verificar existencia de paciente: {e}")
            return False
        finally:
            conn.close()

    def actualizar(self, paciente: Paciente) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Pacientes 
                SET nombre = ?, apellido1 = ?, apellido2 = ?, genero = ?, edad = ?,
                    poblacion = ?, ocupacion = ?, nivelEstudios = ?
                WHERE id_paciente = ?
            ''', (
                paciente.nombre, paciente.apellido1, paciente.apellido2,
                paciente.genero, paciente.edad, paciente.poblacion,
                paciente.ocupacion, paciente.nivelEstudios, paciente.id_paciente
            ))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"❌ Error al actualizar paciente: {e}")
            return False
        finally:
            conn.close()
