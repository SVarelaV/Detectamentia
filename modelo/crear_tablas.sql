-- Script de creación de tabla Informes
CREATE TABLE Informes (
    id_informe INT NOT NULL PRIMARY KEY,
    fechaRegistro VARCHAR(9),
    antecFamiliaresAlzheimer BIT,
    diabetes BIT,
    colesterol BIT,
    migrainas BIT,
    hipertension BIT,
    cardiopatia BIT,
    depresionDiag BIT,
    accidenteCerebrovascular BIT,
    trastornoSueno BIT,
    horaSueno INT,
    calidadSueno VARCHAR(49),
    fumador BIT,
    consumoAlcohol VARCHAR(49),
    actividadFisica VARCHAR(49),
    nivelEstres VARCHAR(49),
    dietaSaludable VARCHAR(49),
    presionArterialSis INT,
    presionArterialDia INT
);

-- Script de creación de tabla Usuarios
CREATE TABLE Usuarios (
    id_usuario INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido1 VARCHAR(100),
    apellido2 VARCHAR(100),
    rol VARCHAR(50),
    email VARCHAR(100),
    activo BIT
);

-- Script de creación de tabla Seguridad
CREATE TABLE Seguridad (
    id_login INT NOT NULL PRIMARY KEY,
    passwd VARCHAR(255),
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Script de creación de tabla Pacientes
CREATE TABLE Pacientes (
    id_paciente INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido1 VARCHAR(100),
    apellido2 VARCHAR(100),
    genero VARCHAR(20),
    edad INT,
    poblacion VARCHAR(100),
    ocupacion VARCHAR(100),
    nivelEstudios VARCHAR(100),
    id_usuario INT,
    id_informe INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_informe) REFERENCES Informes(id_informe)
);

-- Script de creación de tabla ResultadosJuegosJuegos
CREATE TABLE ResultadoJuegos (
    id_resultado INT NOT NULL PRIMARY KEY,
    nombreJuego VARCHAR(100),
    fecha VARCHAR(10),
    tiempoReaccion FLOAT,
    aciertos INT,
    errores INT,
    numeroIntentos INT,
    tiempoTotal FLOAT,
    id_paciente INT,
    FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);
