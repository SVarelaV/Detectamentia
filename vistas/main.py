from vistas.menu_principal import MenuPrincipal
from vistas.login import LoginSistema

if __name__ == "__main__":
    login = LoginSistema()
    usuario = login.autenticar()

    if usuario:
        sistema = MenuPrincipal()
        sistema.ejecutar()
    else:
        print("🚪 Acceso denegado. Saliendo del sistema.")
