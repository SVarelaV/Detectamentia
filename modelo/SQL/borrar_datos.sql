
-- Eliminar datos respetando las relaciones de claves foráneas

-- Primero eliminar de tablas hijas
DELETE FROM Seguridad;
DELETE FROM ResultadoJuegos;
DELETE FROM Pacientes;
DELETE FROM Informes;

-- Luego eliminar de tablas padre
DELETE FROM Usuarios;
