
from controlador.dominios.resultadojuego import ResultadoJuego
from controlador.gestores.listagen import ListaGen
from modelo.config import get_connection
from typing import List, Optional

class ResultadoJuegos(ListaGen[ResultadoJuego]):
    """Clase especializada para manejar la lista de resultados de juegos cognitivos desde SQL Server."""

    def __init__(self):
        super().__init__()
        self._elementos = self.mostrar_todos()

    def agregar(self, resultado: ResultadoJuego) -> bool:
        if self.existe(resultado):
            return False
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO ResultadoJuegos (
                    id_resultado, nombreJuego, fecha,
                    tiempoReaccion, aciertos, errores, tiempoTotal, numeroIntentos
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    resultado.id_resultado, resultado.nombreJuego, resultado.fecha,
                    resultado.tiempoReaccion, resultado.aciertos, resultado.errores,
                    resultado.tiempoTotal, resultado.numeroIntentos
                )
            )
            conn.commit()
            self._elementos.append(resultado)
            return True
        except Exception as e:
            print(f"❌ Error al agregar resultado de juego: {e}")
            return False
        finally:
            conn.close()

    def eliminar(self, id_elemento: int) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM ResultadoJuegos WHERE id_resultado = ?", (id_elemento,))
            conn.commit()
            eliminado = cursor.rowcount > 0
            if eliminado:
                self._elementos = [r for r in self._elementos if r.id_resultado != id_elemento]
            return eliminado
        except Exception as e:
            print(f"❌ Error al eliminar resultado de juego: {e}")
            return False
        finally:
            conn.close()

    def buscar(self, id_elemento: int) -> Optional[ResultadoJuego]:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id_resultado, nombreJuego, fecha,
                    tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal
                    FROM ResultadoJuegos
                WHERE id_resultado = ?
                """, (id_elemento,)
            )
            fila = cursor.fetchone()
            if fila:
                return ResultadoJuego(*fila)
            return None
        except Exception as e:
            print(f"❌ Error al buscar resultado de juego: {e}")
            return None
        finally:
            conn.close()

    def mostrar_todos(self) -> List[ResultadoJuego]:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id_resultado, nombreJuego, fecha,
                    tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal
                FROM ResultadoJuegos
                """
            )
            filas = cursor.fetchall()
            return [ResultadoJuego(*fila) for fila in filas]
        except Exception as e:
            print(f"❌ Error al mostrar resultados de juego: {e}")
            return []
        finally:
            conn.close()

    def existe(self, resultado: ResultadoJuego) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM ResultadoJuegos WHERE id_resultado = ?", (resultado.id_resultado,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"❌ Error al verificar existencia del resultado: {e}")
            return False
        finally:
            conn.close()

    def actualizar(self, resultado: ResultadoJuego) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE ResultadoJuegos
                SET nombreJuego = ?, fecha = ?, tiempoReaccion = ?, 
                    aciertos = ?, errores = ?, tiempoTotal = ?, numeroIntentos = ?
                WHERE id_resultado = ?
                """,
                (
                    resultado.nombreJuego, resultado.fecha, resultado.tiempoReaccion,
                    resultado.aciertos, resultado.errores, resultado.tiempoTotal,
                    resultado.numeroIntentos, resultado.id_resultado
                )
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"❌ Error al actualizar resultado de juego: {e}")
            return False
        finally:
            conn.close()
