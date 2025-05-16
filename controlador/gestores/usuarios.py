from dominios.usuario import Usuario

class Usuarios:
    def __init__(self, fichero="usuarios.txt"):
        self.fichero = fichero
        self.lista_usuarios = self.cargar_usuarios()

    def cargar_usuarios(self):
        try:
            with open(self.fichero, 'r') as file:
                lineas = file.readlines()
            lista_usuarios = []
            for linea in lineas:
                data = linea.strip().split(',')
                if len(data) == 4:
                    dni, nombre, apellido, passwd = data
                    lista_usuarios.append(Usuario(dni, nombre, apellido, passwd))
            return lista_usuarios
        except FileNotFoundError:
            return []

    def guardar_usuarios(self):
        with open(self.fichero, 'w') as file:
            for usuario in self.lista_usuarios:
                file.write(f"{usuario.dni},{usuario.nombre},{usuario.apellido},{usuario.passwd}\n")

    def agregar_usuario(self, usuario):
        if self.buscar_usuario(usuario.dni) is None:
            self.lista_usuarios.append(usuario)
            self.guardar_usuarios()
            return True
        return False

    def buscar_usuario(self, dni):
        for usuario in self.lista_usuarios:
            if usuario.dni == dni:
                return usuario
        return None

    def eliminar_usuario(self, dni):
        usuario = self.buscar_usuario(dni)
        if usuario:
            self.lista_usuarios.remove(usuario)
            self.guardar_usuarios()
            return True
        return False

    def mostrar_usuario(self):  
        return self.lista_usuarios

    def existe_usuario(self, dni):
        for usuario in self.lista_usuarios:
            if usuario.dni == dni:
                return True
        return False
