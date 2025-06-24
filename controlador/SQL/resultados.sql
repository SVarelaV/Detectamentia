-- Insertar un nuevo resultado en la base de datos
INSERT INTO Resultados (id, idUsuario, idJuego, fecha, tiempoReaccion, aciertos, errores, intentos, tiempoTotal)
VALUES (1, 1, 1, '2024-05-12', 1.5, 8, 1, 0, 20.0);

-- Buscar un resultado por su ID
SELECT * FROM Resultados WHERE id = 1;

-- Eliminar un resultado por su ID
DELETE FROM Resultados WHERE id = 1;

-- Mostrar todos los resultados
SELECT * FROM Resultados;

-- Verificar si un resultado existe por su ID
SELECT CASE 
        WHEN EXISTS (SELECT 1 FROM ResultadoJuego WHERE id = 1) THEN 1
        ELSE 0
    END AS Existe;

