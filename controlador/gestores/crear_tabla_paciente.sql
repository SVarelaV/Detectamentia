
-- Script de creación de tabla Paciente para DetectaMentIA
CREATE TABLE Paciente (
    id INT PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    apellido1 NVARCHAR(100) NOT NULL,
    apellido2 NVARCHAR(100),
    genero NVARCHAR(20),
    edad INT,
    poblacion NVARCHAR(100),
    ocupacion NVARCHAR(100),
    nivelEstudios NVARCHAR(100)
);
