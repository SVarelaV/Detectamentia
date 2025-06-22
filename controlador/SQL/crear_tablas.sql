
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
    id_informe INT,
    id_usuario INT,
    FOREIGN KEY (id_informe) REFERENCES Informes(id_informe)
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id)id_usuario
);

-- Script de creación de tabla Informes
CREATE TABLE Informes (
    id_informe INT NOT NULL PRIMARY KEY,
    fechaRegistro VARCHAR(10),
    antecFamiliaresAlzheimer BOOLEAN,
    diabetes BOOLEAN,
    colesterol BOOLEAN,
    migrainas BOOLEAN,
    hipertension BOOLEAN,
    cardiopatia BOOLEAN,
    depresionDiag BOOLEAN,
    accidenteCerebrovascular BOOLEAN,
    trastornoSueno BOOLEAN,
    horaSueno INT,
    calidadSueno VARCHAR(50),
    fumador BOOLEAN,
    consumoAlcohol VARCHAR(50),
    actividadFisica VARCHAR(50),
    nivelEstres VARCHAR(50),
    dietaSaludable VARCHAR(50),
    presionArterialSis INT,
    presionArterialDia INT,
    FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente)
);

-- Script de creación de tabla ResltadosJuegos
CREATE TABLE ResultadosJuegos (
    id_resultado INT NOT NULL PRIMARY KEY,
    nombreJuego VARCHAR(100),
    fecha VARCHAR(10),
    tiempoReaccion FLOAT,
    aciertos INT,
    errores INT,
    numeroIntentos INT,
    tiempoTotal FLOAT,,
    id_paciente INT,
    FOREIGN KEY (id_paciente) REFERENCES Pacientes(id)
);

-- Script de creación de tabla Usuarios
CREATE TABLE Usuarios (
    id_usuario INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido1 VARCHAR(100),
    apellido2 VARCHAR(100),
    passwd VARCHAR(255),
    rol VARCHAR(50),
    email VARCHAR(100),
    activo BOOLEAN
);

-- Script de creación de tabla Seguridad
CREATE TABLE Seguridad (
    id_login INT NOT NULL PRIMARY KEY,
    passwd VARCHAR(255),
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);