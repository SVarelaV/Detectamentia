import unittest
from unittest.mock import patch
import io
from controlador.gestores.gestor_pacientes import GestorPacientes

class TestMenuInteractivo(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        # 1. Agregar paciente válido
        '1', '999', 'Test', 'Uno', 'Apellido', 'Otro', '50', 'Ciudad', 'Ocupación', 'Estudios',
        # 2. Mostrar todos los pacientes
        '4',
        # 3. Buscar paciente existente
        '2', '999',
        # 4. Eliminar paciente existente
        '3', '999',
        # 5. Mostrar todos los pacientes (debe estar vacío)
        '4',
        # 6. Salir
        '5'
    ])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_completo(self, mock_stdout, mock_input):
        gestor = GestorPacientes(cargar_ejemplos=False)
        gestor.ejecutar()
        salida = mock_stdout.getvalue()
        self.assertIn("✅ Paciente agregado correctamente.", salida)
        self.assertIn("Test Uno Apellido", salida)
        self.assertIn("👁️ Paciente encontrado:", salida)
        self.assertIn("✅ Paciente eliminado correctamente.", salida)
        self.assertIn("🕳️ No hay pacientes registrados.", salida)
        self.assertIn("¡Gracias por usar el Gestor de Pacientes!", salida)

class TestMenuErrores(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        # 1. Agregar paciente válido
        '1', '100', 'Ana', 'Ruiz', 'Gómez', 'Femenino', '65', 'Sevilla', 'Ama de casa', 'Primaria completa',
        # 2. Intentar agregar duplicado
        '1', '100', 'Ana', 'Ruiz', 'Gómez', 'Femenino', '65', 'Sevilla', 'Ama de casa', 'Primaria completa',
        # 3. Opción inválida
        '9',
        # 4. Salir
        '5'
    ])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_errores(self, mock_stdout, mock_input):
        gestor = GestorPacientes()
        gestor.ejecutar()
        salida = mock_stdout.getvalue()
        self.assertIn("✅ Paciente agregado correctamente.", salida)
        self.assertIn("Paciente duplicado", salida)
        self.assertIn("❌ Opción inválida. Intenta de nuevo.", salida)
        self.assertIn("¡Gracias por usar el Gestor de Pacientes!", salida)

if __name__ == "__main__":
    unittest.main()