
from controlador.dominios.usuario import Usuario
from controlador.gestores.usuarios import Usuarios

class GestorUsuarios:
    """
    Gestor para manejar operaciones sobre usuarios del sistema.
    """

    def __init__(self):
        self.usuarios = Usuarios()

    def agregar(self, usuario):
        if self.usuarios.buscar(usuario.id_usuario):
            raise Exception("Usuario duplicado")
        self.usuarios.agregar(usuario)
        return True

    def mostrar_menu(self):
        print("\n👥 GESTOR DE USUARIOS")
        print("=" * 50)
        print("1. ➕ Agregar usuario")
        print("2. 🔍 Buscar usuario por ID")
        print("3. 🗑️  Eliminar usuario por ID")
        print("4. 📧 Buscar por email")
        print("5. 🎭 Buscar por rol")
        print("6. 📋 Mostrar todos los usuarios")
        print("7. 🚪 Salir")
        print("=" * 50)

    def mostrar_usuario(self, u):
        estado = "✅ Activo" if u.activo else "⛔ Inactivo"
        print(f"🆔 {u.id_usuario} | 👤 {u.nombre} {u.apellido1} {u.apellido2} | 📧 {u.email} | 🎭 {u.rol} | {estado}")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                self._agregar_usuario()
            elif opcion == "2":
                self._buscar_usuario()
            elif opcion == "3":
                self._eliminar_usuario()
            elif opcion == "4":
                self._buscar_por_email()
            elif opcion == "5":
                self._buscar_por_rol()
            elif opcion == "6":
                self._mostrar_todos()
            elif opcion == "7":
                print("👋 Finalizando gestión de usuarios.")
                break
            else:
                print("❌ Opción inválida.")

    def _agregar_usuario(self):
        try:
            print("\n➕ Nuevo usuario")
            nombre = input("Nombre: ")
            apellido1 = input("Primer apellido: ")
            apellido2 = input("Segundo apellido: ")
            rol = input("Rol (paciente/profesional): ")
            email = input("Email: ")
            activo = input("¿Activo? (s/n): ").lower() == "s"

            nuevo = Usuario(nombre, apellido1, apellido2, rol, email, activo)
            self.usuarios.agregar(nuevo)
            print(f"✅ Usuario agregado con ID: {nuevo.id_usuario}")
        except Exception as e:
            print(f"❌ Error al agregar: {e}")

    def _buscar_usuario(self):
        try:
            id = int(input("🔍 ID del usuario: "))
            u = self.usuarios.buscar(id)
            if u:
                self.mostrar_usuario(u)
            else:
                print("❌ Usuario no encontrado.")
        except Exception:
            print("❌ Entrada inválida.")

    def _eliminar_usuario(self):
        try:
            id = int(input("🗑️ ID del usuario a eliminar: "))
            if self.usuarios.eliminar(id):
                print("✅ Usuario eliminado.")
            else:
                print("❌ No se encontró usuario con ese ID.")
        except Exception:
            print("❌ Entrada inválida.")

    def _buscar_por_email(self):
        try:
            email = input("📧 Email del usuario: ")
            u = self.usuarios.buscar_por_email(email)
            if u:
                self.mostrar_usuario(u)
            else:
                print("❌ No se encontró usuario con ese email.")
        except Exception:
            print("❌ Entrada inválida.")

    def _buscar_por_rol(self):
        try:
            rol = input("🎭 Rol a buscar (paciente/profesional): ")
            lista = self.usuarios.buscar_por_rol(rol)
            if lista:
                for u in lista:
                    self.mostrar_usuario(u)
            else:
                print("❌ No se encontraron usuarios con ese rol.")
        except Exception:
            print("❌ Entrada inválida.")

    def _mostrar_todos(self):
        print("\n📋 Lista de todos los usuarios:")
        lista = self.usuarios.mostrar_todos()
        if lista:
            for u in lista:
                self.mostrar_usuario(u)
        else:
            print("🕳️ No hay usuarios registrados.")

def main():
    gestor = GestorUsuarios()
    try:
        gestor.ejecutar()
    except KeyboardInterrupt:
        print("\n👋 Aplicación interrumpida por el usuario.")

if __name__ == "__main__":
    main()
