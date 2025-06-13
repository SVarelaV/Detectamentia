
import pyodbc
from controlador.dominios.paciente import Paciente


class GestorPacientesSQL:
    def __init__(self):
        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'DATABASE=DetectaMentIA;'
            'Trusted_Connection=yes;'
        )
        self.cursor = self.conn.cursor()

    def mostrar_menu(self):
        print("\n🧠 GESTOR DE PACIENTES (SQL Server)")
        print("=" * 50)
        print("1. ➕ Agregar paciente")
        print("2. 🔍 Buscar paciente por ID")
        print("3. 🗑️  Eliminar paciente por ID")
        print("4. 📋 Mostrar todos los pacientes")
        print("5. 🚪 Salir")
        print("=" * 50)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                self.agregar_paciente()
            elif opcion == "2":
                self.buscar_paciente()
            elif opcion == "3":
                self.eliminar_paciente()
            elif opcion == "4":
                self.mostrar_todos()
            elif opcion == "5":
                print("👋 Cerrando el gestor de pacientes.")
                break
            else:
                print("❌ Opción no válida. Intenta de nuevo.")

    def agregar_paciente(self):
        try:
            print("\n➕ Agregar nuevo paciente")
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            apellido1 = input("Primer apellido: ")
            apellido2 = input("Segundo apellido: ")
            genero = input("Género: ")
            edad = int(input("Edad: "))
            poblacion = input("Población: ")
            ocupacion = input("Ocupación: ")
            nivelEstudios = input("Nivel de estudios: ")

            self.cursor.execute("""
                INSERT INTO Paciente (id, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, id, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios)
            self.conn.commit()
            print("✅ Paciente agregado correctamente.")
        except Exception as e:
            print(f"❌ Error al agregar: {e}")

    def buscar_paciente(self):
        try:
            id = int(input("\n🔍 ID del paciente a buscar: "))
            self.cursor.execute("SELECT * FROM Paciente WHERE id = ?", id)
            row = self.cursor.fetchone()
            if row:
                print(f"👤 ID: {row.id} | 🧑‍🦳 {row.nombre} {row.apellido1} {row.apellido2} | 🎂 {row.edad} años | 🏙️ {row.poblacion} | 💼 {row.ocupacion} | 🎓 {row.nivelEstudios}")
            else:
                print("❌ No se encontró un paciente con ese ID.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def eliminar_paciente(self):
        try:
            id = int(input("\n🗑️ ID del paciente a eliminar: "))
            self.cursor.execute("DELETE FROM Paciente WHERE id = ?", id)
            self.conn.commit()
            print("✅ Paciente eliminado si existía.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def mostrar_todos(self):
        print("\n📋 Lista de todos los pacientes:")
        self.cursor.execute("SELECT * FROM Paciente")
        rows = self.cursor.fetchall()
        if rows:
            for r in rows:
                print(f"👤 ID: {r.id} | 🧑‍🦳 {r.nombre} {r.apellido1} {r.apellido2} | 🎂 {r.edad} | 🏙️ {r.poblacion} | 💼 {r.ocupacion} | 🎓 {r.nivelEstudios}")
        else:
            print("🕳️ No hay pacientes registrados.")


def main():
    gestor = GestorPacientesSQL()
    try:
        gestor.ejecutar()
    except KeyboardInterrupt:
        print("\n👋 Aplicación terminada por el usuario.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


if __name__ == "__main__":
    main()
