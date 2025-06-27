-- Insertar un nuevo usuario en la base de datos
-INSERT INTO Usuarios (id_usuario, nombre, apellido1, apellido2, rol, email, activo)
-VALUES (99, 'Carlos', 'García', 'López', 'paciente', 'carlos.garcia@example.com', 1);

-- Buscar un usuario por su ID
SELECT * FROM Usuarios WHERE id_usuario = 99;

-- Verificar si un usuario existe por su ID
SELECT CASE 
        WHEN EXISTS (SELECT 1 FROM Usuarios WHERE id_usuario = 99) THEN 1
        ELSE 0
    END AS Existe;

-- Buscar por email
SELECT * FROM Usuarios WHERE email = 'carlos.garcia@example.com';

-- Buscar por rol
SELECT * FROM Usuarios WHERE rol = 'paciente';

-- Eliminar un usuario por su ID
DELETE FROM Usuarios WHERE id_usuario = 99;

-- Mostrar todos los usuarios
SELECT * FROM Usuarios;
