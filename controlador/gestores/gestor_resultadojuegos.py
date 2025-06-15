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
        """Carga datos de prueba."""
        self.resultados.agregar(ResultadoJuego(1, "Stroop Test", "01-06-2025", 1.2, 10, 2, 0, 30.5))
        self.resultados.agregar(ResultadoJuego(2, "N-back", "04-06-2025", 1.8, 12, 1, 0, 45.2))

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
            if self.resultados.agregar(nuevo):
                print("✅ Resultado agregado.")
            else:
                print("⚠️ Ya existe un resultado con ese ID.")
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