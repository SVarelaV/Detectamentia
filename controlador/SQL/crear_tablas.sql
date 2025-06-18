
-- Script de creación de tabla Paciente para DetectaMentIA
CREATE TABLE Paciente (
    id INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido1 VARCHAR(100),
    apellido2 VARCHAR(100),
    genero VARCHAR(20),
    edad INT,
    poblacion VARCHAR(100),
    ocupacion VARCHAR(100),
    nivelEstudios VARCHAR(100)
);
