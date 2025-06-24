import io
from unittest.mock import patch
from controlador.gestores.gestor_resultadojuegos import GestorResultadoJuegos

def test_interaccion_agregar_resultado():
    gestor = GestorResultadoJuegos()
    # Simula las respuestas del usuario para cada input
    entradas = [
        "123",           # ID
        "Simon",         # Nombre del juego
        "10-07-2025",    # Fecha
        "1.5",           # Tiempo de reacción
        "8",             # Aciertos
        "1",             # Errores
        "0",             # Intentos
        "20.0"           # Tiempo total
    ]
    with patch('builtins.input', side_effect=entradas), \
        patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        gestor._agregar_resultado()
        salida = mock_stdout.getvalue()
        assert "✅ Resultado agregado." in salida
    print("✅ test_interaccion_agregar_resultado OK")

if __name__ == "__main__":
    print("INICIO TEST")
    test_interaccion_agregar_resultado()
    print("FIN TEST")