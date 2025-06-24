-- Insertar un nuevo usuario en la base de datos
INSERT INTO Usuarios (id, nombre, apellido1, apellido2, email, fechaNacimiento, genero)
VALUES (1, 'Carlos', 'García', 'López', 'carlos.garcia@example.com', '1980-01-15', 'Masculino');

-- Buscar un usuario por su ID
SELECT * FROM Usuarios WHERE id = 1;

-- Eliminar un usuario por su ID
DELETE FROM Usuarios WHERE id = 1;

-- Mostrar todos los usuarios
SELECT * FROM Usuarios;

-- Verificar si un usuario existe por su ID
SELECT CASE 
        WHEN EXISTS (SELECT 1 FROM Usuarios WHERE id = 1) THEN 1
        ELSE 0
    END AS Existe;

-- Buscar por email
SELECT * FROM Usuarios WHERE email = 'carlos.garcia@example.com';

-- Buscar por rol
SELECT * FROM Usuarios WHERE rol = 'paciente';