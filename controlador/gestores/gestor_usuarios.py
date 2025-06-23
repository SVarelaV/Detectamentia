from controlador.dominios.usuario import Usuario
from controlador.gestores.usuarios import Usuarios


class GestorUsuarios:
    """
    Gestor para manejar operaciones sobre usuarios del sistema.
    """

    def __init__(self):
        self.usuarios = Usuarios()
        self._cargar_ejemplos()

    def agregar(self, usuario):
        # Validación de campos obligatorios
        if not usuario.nombre or not usuario.apellido1 or not usuario.email or not usuario.passwd:
            raise Exception("Faltan datos obligatorios")
        # Validación de email único
        if any(u.email == usuario.email for u in self.usuarios._elementos):
            raise Exception("Email duplicado")
        # Validación de rol
        if usuario.rol not in ("paciente", "profesional"):
            raise Exception("Rol no válido")
        # Validación de contraseña
        if len(usuario.passwd) < 4:
            raise Exception("Contraseña demasiado corta")
        # Validación de duplicados por ID
        if any(u.id == usuario.id for u in self.usuarios._elementos):
            raise Exception("Usuario duplicado")
        self.usuarios._elementos.append(usuario)
        return True

    def _cargar_ejemplos(self):
        """Carga usuarios de ejemplo."""
        self.usuarios.agregar(Usuario(1, "Laura", "Sánchez", "Gómez", "clave123", "profesional", "laura@example.com", True))
        self.usuarios.agregar(Usuario(2, "Carlos", "Ruiz", "Díaz", "pass456", "paciente", "carlos@example.com", True))

    def mostrar_menu(self):
        print("\n👥 GESTOR DE USUARIOS")
        print("=" * 50)
        print("1. ➕ Agregar usuario")
        print("2. 🔍 Buscar usuario por ID")
        print("3. 🗑️ Eliminar usuario por ID")
        print("4. 📧 Buscar por email")
        print("5. 🎭 Buscar por rol")
        print("6. 📋 Mostrar todos los usuarios")
        print("7. 🚪 Salir")
        print("=" * 50)

    def mostrar_usuario(self, u):
        estado = "✅ Activo" if u.activo else "⛔ Inactivo"
        print(f"🆔 {u.id} | 👤 {u.nombre} {u.apellido1} {u.apellido2} | 📧 {u.email} | 🎭 {u.rol} | {estado}")

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
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            apellido1 = input("Primer apellido: ")
            apellido2 = input("Segundo apellido: ")
            passwd = input("Contraseña: ")
            rol = input("Rol (paciente/profesional): ")
            email = input("Email: ")
            activo = input("¿Activo? (s/n): ").lower() == "s"

            nuevo = Usuario(id, nombre, apellido1, apellido2, passwd, rol, email, activo)
            if self.usuarios.agregar(nuevo):
                print("✅ Usuario agregado.")
            else:
                print("⚠️ Ya existe un usuario con ese ID.")
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
        email = input("📧 Email del usuario: ")
        u = self.usuarios.buscar_por_email(email)
        if u:
            self.mostrar_usuario(u)
        else:
            print("❌ No se encontró usuario con ese email.")

    def _buscar_por_rol(self):
        rol = input("🎭 Rol a buscar (paciente/profesional): ")
        lista = self.usuarios.buscar_por_rol(rol)
        if lista:
            for u in lista:
                self.mostrar_usuario(u)
        else:
            print("❌ No se encontraron usuarios con ese rol.")

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
