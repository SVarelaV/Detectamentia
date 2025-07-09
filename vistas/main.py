from vistas.menu_principal import MenuPrincipal
from vistas.login import login_basico

if __name__ == "__main__":
    if login_basico():
        sistema = MenuPrincipal()
        sistema.ejecutar()
    else:
        print("🚪 Acceso denegado. Programa finalizado.")

