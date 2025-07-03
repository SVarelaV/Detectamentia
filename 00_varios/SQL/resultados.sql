-- Insertar un nuevo resultado de juego en la base de datos
INSERT INTO ResultadosJuegos (id_resultado, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
VALUES (99, 'Par', '10-06-2025', 1.5, 8, 1, 0, 20.0);

-- Buscar un resultado por su ID
SELECT * FROM ResultadosJuegos WHERE id_resultado = 99;

-- Eliminar un resultado por su ID
DELETE FROM ResultadosJuegos WHERE id_resultado = 99;

-- Mostrar todos los resultados de juegos
SELECT * FROM ResultadosJuegos;

-- Verificar si un resultado existe por su ID
SELECT CASE 
        WHEN EXISTS (SELECT 1 FROM ResultadosJuegos WHERE id_resultado = 99) THEN 1
        ELSE 0
    END AS Existe;
