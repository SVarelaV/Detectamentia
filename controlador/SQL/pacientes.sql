-- Insertar un nuevo paciente en la base de datos

INSERT INTO Pacientes (id, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios)
VALUES (1, 'Juan', 'Pérez', 'Gómez', 'Masculino', 72, 'Madrid', 'Jubilado', 'Secundaria completa');

-- Buscar un paciente por su ID
SELECT * FROM Pacientes WHERE id = 1;

-- Eliminar un paciente por su ID
DELETE FROM Pacientes WHERE id = 1;

-- Mostrar todos los pacientes
SELECT * FROM Pacientes;

-- Verificar si un paciente existe por su ID
IF EXISTS (SELECT 1 FROM Pacientes WHERE id = 1)
    PRINT 'Existe';
ELSE
    PRINT 'No existe';

