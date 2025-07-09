from controlador.gestores.seguridad_gestor import SeguridadGestor

class LoginSistema:
    def __init__(self):
        self._seguridad = SeguridadGestor()

    def autenticar(self):
        print("\n🔐 INICIO DE SESIÓN - DetectaMentIA")
        print("=" * 50)
        email = input("📧 Email: ").strip()
        password = input("🔑 Contraseña: ").strip()

        usuario = self._seguridad.validar_credenciales(email, password)

        if not usuario:
            print("❌ Credenciales inválidas o usuario inactivo.")
            return None

        print(f"✅ Bienvenido, {usuario.nombre} {usuario.apellido1} ({usuario.rol})")
        return usuario

if __name__ == "__main__":
    login = LoginSistema()
    usuario = login.autenticar()
    if usuario:
        print("➡️ Acceso permitido al sistema.")
    else:
        print("🚪 Acceso denegado.")

