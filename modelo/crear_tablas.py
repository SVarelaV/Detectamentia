from config import get_connection

def crear_tablas():
    conn = get_connection()
    cursor = conn.cursor()

    # Tabla Usuarios
    cursor.execute('''
        CREATE TABLE Usuarios (
            id_usuario INT IDENTITY(1,1) PRIMARY KEY,
            nombre NVARCHAR(100),
            apellido1 NVARCHAR(100),
            apellido2 NVARCHAR(100),
            rol NVARCHAR(50),
            email NVARCHAR(100),
            activo BIT
        )
    ''')

    # Tabla Informes (primero para permitir FK en Pacientes)
    cursor.execute('''
        CREATE TABLE Informes (
            id_informe INT IDENTITY(1,1) PRIMARY KEY,
            fechaRegistro VARCHAR(20),
            antecFamiliaresAlzheimer BIT,
            diabetes BIT,
            colesterol BIT,
            migrainas INT,
            hipertension BIT,
            cardiopatia BIT,
            depresionDiag BIT,
            accidenteCerebrovascular VARCHAR(10),
            trastornoSueno BIT,
            horaSueno FLOAT,
            calidadSueno INT,
            fumador BIT,
            consumoAlcohol INT,
            actividadFisica INT,
            nivelEstres INT,
            dietaSaludable BIT,
            presionArterialSis INT,
            presionArterialDia INT
        )
    ''')

    # Tabla Pacientes
    cursor.execute('''
        CREATE TABLE Pacientes (
            id_paciente INT IDENTITY(1,1) PRIMARY KEY,
            nombre NVARCHAR(100),
            apellido1 NVARCHAR(100),
            apellido2 NVARCHAR(100),
            genero NVARCHAR(20),
            edad INT,
            poblacion NVARCHAR(100),
            ocupacion NVARCHAR(100),
            nivelEstudios NVARCHAR(100),
            id_usuario INT,
            id_informe INT,
            FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
            FOREIGN KEY (id_informe) REFERENCES Informes(id_informe)
        )
    ''')

    # Tabla ResultadoJuegos
    cursor.execute('''
        CREATE TABLE ResultadoJuegos (
            id_resultado INT IDENTITY(1,1) PRIMARY KEY,
            id_paciente INT,
            nombreJuego NVARCHAR(100),
            fecha VARCHAR(20),
            tiempoReaccion FLOAT,
            aciertos INT,
            errores INT,
            numeroIntentos INT,
            tiempoTotal FLOAT,
            FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
        )
    ''')

    # Tabla Seguridad (login)
    cursor.execute('''
        CREATE TABLE Seguridad (
            id_login INT IDENTITY(1,1) PRIMARY KEY,
            passwd NVARCHAR(100),
            id_usuario INT,
            FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Tablas creadas correctamente con relaciones completas.")

if __name__ == "__main__":
    crear_tablas()
