-- Insertar un nuevo paciente en la base de datos
INSERT INTO Pacientes (id_paciente, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios)
VALUES (99, 'Juan', 'Pérez', 'Gómez', 'Masculino', 72, 'Madrid', 'Jubilado', 'Secundaria completa');

-- Buscar un paciente por su ID
SELECT * FROM Pacientes WHERE id_paciente = 99;

-- Eliminar un paciente por su ID
DELETE FROM Pacientes WHERE id_paciente = 99;

-- Mostrar todos los pacientes
SELECT * FROM Pacientes;

-- Verificar si un paciente existe por su ID
SELECT CASE 
        WHEN EXISTS (SELECT 1 FROM Pacientes WHERE id_paciente = 99) THEN 1
        ELSE 0
    END AS Existe;