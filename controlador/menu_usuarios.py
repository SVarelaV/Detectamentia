import os
from gestores.usuarios import Usuarios
from dominios.usuario import Usuario

if os.path.exists("usuarios.txt"):
    print("El archivo usuarios.txt existe en:", os.path.abspath("usuarios.txt"))
else:
    print("El archivo usuarios.txt no existe.")

def login(usuarios):
    print("=== Sistema de Login ===")
    dni = input("Introduce tu DNI: ")
    passwd = input("Introduce tu contraseña: ")
    usuario = usuarios.buscar_usuario(dni)
    if usuario and usuario.passwd == passwd:
        print(f"Bienvenido, {usuario.nombre} {usuario.apellido}!")
        return True
    else:
        print("Usuario no encontrado. Pulse 2 para registrarse.")
        return False

def registro(usuarios):
    print("=== Registro de Usuario ===")
    dni = input("Introduce tu DNI: ")
    if usuarios.existe_usuario(dni):
        print("Error: El DNI ya está registrado.")
        return False
    nombre = input("Introduce tu nombre: ")
    apellido = input("Introduce tu apellido: ")
    passwd = input("Introduce tu contraseña: ")
    usuario = Usuario(dni, nombre, apellido, passwd)
    if usuarios.agregar_usuario(usuario):
        print("Usuario registrado correctamente.")
        return True
    else:
        print("Error al registrar el usuario.")
        return False

def mostrar_usuarios(usuarios):
    print("=== Mostrar Usuarios ===")
    lista_usuarios = usuarios.mostrar_usuario()
    if lista_usuarios:
        for usuario in lista_usuarios:
            print(f"DNI: {usuario.dni}, Nombre: {usuario.nombre}, Apellido: {usuario.apellido}, Passwd: {usuario.passwd}")
    else:
        print("No hay usuarios registrados.")

def eliminar_usuario(usuarios):
    print("=== Eliminar Usuario ===")
    dni = input("Introduce el DNI del usuario a eliminar: ")
    if usuarios.eliminar_usuario(dni):
        print("Usuario eliminado correctamente.")
    else:
        print("Error: Usuario no encontrado.")

def buscar_usuario(usuarios):
    print("=== Buscar Usuario ===")
    dni = input("Introduce el DNI del usuario a buscar: ")
    usuario = usuarios.buscar_usuario(dni)
    if usuario:
        print(f"DNI: {usuario.dni}, Nombre: {usuario.nombre}, Apellido: {usuario.apellido}, Passwd: {usuario.passwd}")
    else:
        print("Error: Usuario no encontrado.")

def main():
    usuarios = Usuarios()
    while True:
        print("\n=== Menú Principal ===")
        print("1. Iniciar sesión")
        print("2. Registro")
        print("3. Mostrar Usuarios")
        print("4. Eliminar Usuario")
        print("5. Buscar Usuario")
        print("6. Salir")
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == '1':
            login(usuarios)
        elif opcion == '2':
            registro(usuarios)
        elif opcion == '3':
            mostrar_usuarios(usuarios)
        elif opcion == '4':
            eliminar_usuario(usuarios)
        elif opcion == '5':
            buscar_usuario(usuarios)
        elif opcion == '6':
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida, intenta de nuevo")

if __name__ == "__main__":
    main()