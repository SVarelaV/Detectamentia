from controlador.dominios.resultadojuego import ResultadoJuego
from controlador.gestores.resultadojuegos import ResultadoJuegos

class GestorResultadoJuegos:
    """
    Gestor para manejar operaciones sobre resultados de juegos cognitivos.
    """

    def __init__(self):
        self.resultados = ResultadoJuegos()
        self._cargar_ejemplos()

    def _cargar_ejemplos(self):
        """Carga datos de prueba solo con los juegos permitidos."""
        self.resultados.agregar(ResultadoJuego(1, "Stroop Test", "01-06-2025", 1.2, 10, 2, 0, 30.5))
        self.resultados.agregar(ResultadoJuego(2, "N-back", "04-06-2025", 1.8, 12, 1, 0, 45.2))
        self.resultados.agregar(ResultadoJuego(3, "Par", "07-06-2025", 2.5, 8, 3, 1, 50.0))
        self.resultados.agregar(ResultadoJuego(4, "Stroop Test", "10-06-2025", 1.1, 11, 1, 0, 29.8))
        self.resultados.agregar(ResultadoJuego(5, "N-back", "12-06-2025", 2.2, 7, 5, 1, 60.0))
        self.resultados.agregar(ResultadoJuego(6, "Par", "15-06-2025", 1.9, 13, 2, 0, 48.7))
        self.resultados.agregar(ResultadoJuego(7, "Stroop Test", "18-06-2025", 1.3, 9, 4, 2, 55.3))
        self.resultados.agregar(ResultadoJuego(8, "N-back", "20-06-2025", 1.7, 15, 0, 0, 40.0))
        self.resultados.agregar(ResultadoJuego(9, "Par", "22-06-2025", 2.0, 10, 3, 1, 52.1))

    def agregar_resultado(self, resultado):
        """Agrega un resultado solo si no existe otro con el mismo ID."""
        if self.resultados.buscar(resultado.id) is not None:
            raise Exception("Resultado duplicado")
        self.resultados.agregar(resultado)
        return True

    def mostrar_menu(self):
        print("\n🎮 GESTOR DE RESULTADOS DE JUEGOS")
        print("=" * 50)
        print("1. ➕ Agregar resultado de juego")
        print("2. 🔍 Buscar resultado por ID")
        print("3. 🗑️  Eliminar resultado por ID")
        print("4. 📋 Mostrar todos los resultados")
        print("5. 🚪 Salir")
        print("=" * 50)

    def mostrar_resultado(self, rj):
        print(f"🎯 ID: {rj.id} | 🕹️ Juego: {rj.nombreJuego} | 📅 Fecha: {rj.fecha} | ⚡ Reacción: {rj.tiempoReaccion}s | ✅ Aciertos: {rj.aciertos} | ❌ Errores: {rj.errores} | ⏱️ Total: {rj.tiempoTotal}s")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                self._agregar_resultado()
            elif opcion == "2":
                self._buscar_resultado()
            elif opcion == "3":
                self._eliminar_resultado()
            elif opcion == "4":
                self._mostrar_todos()
            elif opcion == "5":
                print("👋 Finalizando gestión de resultados de juegos.")
                break
            else:
                print("❌ Opción inválida.")

    def _agregar_resultado(self):
        try:
            print("\n➕ Nuevo resultado de juego")
            id = int(input("ID: "))
            juego = input("Nombre del juego: ")
            fecha = input("Fecha (DD-MM-YYYY): ")
            reaccion = float(input("Tiempo de reacción (s): "))
            aciertos = int(input("Número de aciertos: "))
            errores = int(input("Número de errores: "))
            intentos = int(input("Número de intentos (si aplica): "))
            total = float(input("Tiempo total (s): "))

            nuevo = ResultadoJuego(id, juego, fecha, reaccion, aciertos, errores, intentos, total)
            self.agregar_resultado(nuevo)
            print("✅ Resultado agregado.")
        except Exception as e:
            print(f"❌ Error al agregar: {e}")



    def _buscar_resultado(self):
        try:
            id = int(input("🔍 ID del resultado: "))
            r = self.resultados.buscar(id)
            if r:
                self.mostrar_resultado(r)
            else:
                print("❌ No se encontró resultado con ese ID.")
        except Exception:
            print("❌ Entrada inválida.")

    def _eliminar_resultado(self):
        try:
            id = int(input("🗑️ ID del resultado a eliminar: "))
            if self.resultados.eliminar(id):
                print("✅ Resultado eliminado.")
            else:
                print("❌ No se encontró resultado con ese ID.")
        except Exception:
            print("❌ Entrada inválida.")

    def _mostrar_todos(self):
        print("\n📋 Todos los resultados registrados:")
        lista = self.resultados.mostrar_todos()
        if lista:
            for r in lista:
                self.mostrar_resultado(r)
        else:
            print("🕳️ No hay resultados registrados.")


def main():
    gestor = GestorResultadoJuegos()
    try:
        gestor.ejecutar()
    except KeyboardInterrupt:
        print("\n👋 Aplicación interrumpida por el usuario.")


if __name__ == "__main__":
    main()