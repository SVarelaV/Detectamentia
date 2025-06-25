-- Insertar datos de ejemplo en la tabla informes
INSERT INTO Informes (
    id_informe, fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas,
    hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular,
    trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol,
    actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia
) VALUES
(1, '2024-05-12', 1, 1, 0, 2, 1, 0, 1, 1, 1, 6.5, 2, 0, 1, 2, 5, 1, 130, 85),
(2, '2024-05-13', 0, 0, 1, 1, 0, 0, 0, 0, 0, 7.0, 1, 1, 2, 1, 3, 0, 120, 70),
(3, '2024-05-15', 1, 0, 1, 0, 1, 1, 0, 0, 1, 8.0, 2, 0, 1, 2, 7, 1, 125, 80),
(4, '2024-05-20', 0, 1, 0, 1, 0, 0, 1, 1, 0, 5.5, 0, 1, 2, 0, 4, 1, 140, 90),
(5, '2024-05-25', 1, 1, 1, 2, 1, 1, 1, 0, 1, 7.2, 2, 1, 2, 2, 8, 1, 135, 88),
(6, '2024-05-28', 0, 0, 0, 0, 0, 0, 0, 0, 0, 6.0, 1, 0, 0, 1, 2, 0, 118, 72),
(7, '2024-06-01', 1, 1, 1, 1, 1, 1, 1, 1, 1, 8.5, 2, 1, 2, 2, 9, 1, 145, 95),
(8, '2024-06-05', 0, 1, 0, 2, 0, 0, 1, 0, 1, 5.8, 0, 0, 1, 0, 3, 0, 122, 76),
(9, '2024-06-10', 1, 0, 1, 0, 1, 1, 0, 1, 0, 7.7, 2, 1, 2, 1, 6, 1, 132, 84),
(10, '2024-06-15', 0, 0, 0, 1, 0, 0, 0, 0, 1, 6.3, 1, 0, 0, 0, 4, 0, 125, 78);



-- Insertar datos de ejemplo en la tabla pacientes
INSERT INTO Pacientes (
    id_paciente, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios
) VALUES
(1, 'Juan', 'Pérez', 'Gómez', 'Masculino', 72, 'Madrid', 'Jubilado', 'Secundaria completa'),
(2, 'Ana', 'López', 'Martínez', 'Femenino', 68, 'Barcelona', 'Ama de casa', 'Primaria completa'),
(3, 'Luis', 'Martín', 'Soto', 'Masculino', 80, 'Valencia', 'Jubilado', 'Universidad'),
(4, 'Carmen', 'Ruiz', 'Díaz', 'Femenino', 75, 'Sevilla', 'Jubilada', 'Secundaria'),
(5, 'Pedro', 'García', 'Fernández', 'Masculino', 65, 'Bilbao', 'Comerciante', 'Primaria'),
(6, 'Lucía', 'Sánchez', 'Moreno', 'Femenino', 70, 'Granada', 'Profesora', 'Universidad'),
(7, 'Miguel', 'Torres', 'Navarro', 'Masculino', 60, 'Zaragoza', 'Ingeniero', 'Universidad'),
(8, 'Isabel', 'Jiménez', 'Romero', 'Femenino', 73, 'Valladolid', 'Jubilada', 'Secundaria'),
(9, 'Antonio', 'Hernández', 'Molina', 'Masculino', 69, 'Alicante', 'Agricultor', 'Primaria'),
(10, 'María', 'Castro', 'Ortega', 'Femenino', 67, 'Córdoba', 'Ama de casa', 'Primaria completa');

-- Insertar datos de ejemplo en la tabla usuarios
INSERT INTO Usuarios (
    id_usuario, nombre, apellido1, apellido2, rol, email, activo
) VALUES
(1, 'Laura', 'Sánchez', 'Gómez', 'profesional', 'laura@example.com', 1),
(2, 'Carlos', 'Ruiz', 'Díaz', 'paciente', 'carlos@example.com', 1),
(3, 'Marta', 'López', 'Fernández', 'profesional', 'marta.lopez@example.com', 1),
(4, 'Pedro', 'Martínez', 'Santos', 'paciente', 'pedro.martinez@example.com', 0),
(5, 'Ana', 'García', 'Moreno', 'profesional', 'ana.garcia@example.com', 1),
(6, 'Luis', 'Torres', 'Navarro', 'paciente', 'luis.torres@example.com', 1),
(7, 'Elena', 'Jiménez', 'Romero', 'profesional', 'elena.jimenez@example.com', 0),
(8, 'Javier', 'Hernández', 'Molina', 'paciente', 'javier.hernandez@example.com', 1),
(9, 'Sofía', 'Castro', 'Ortega', 'profesional', 'sofia.castro@example.com', 1),
(10, 'Miguel', 'Serrano', 'Vega', 'paciente', 'miguel.serrano@example.com', 0);

-- Inserción de resultados de juegos
INSERT INTO ResultadosJuegos (
    id_resultado, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal
) VALUES
(1, 'Stroop Test', '01-06-2025', 1.2, 10, 2, 0, 30.5),
(2, 'N-back', '04-06-2025', 1.8, 12, 1, 0, 45.2),
(3, 'Par', '07-06-2025', 2.5, 8, 3, 1, 50.0),
(4, 'Stroop Test', '10-06-2025', 1.1, 11, 1, 0, 29.8),
(5, 'N-back', '12-06-2025', 2.2, 7, 5, 1, 60.0),
(6, 'Par', '15-06-2025', 1.9, 13, 2, 0, 48.7),
(7, 'Stroop Test', '18-06-2025', 1.3, 9, 4, 2, 55.3),
(8, 'N-back', '20-06-2025', 1.7, 15, 0, 0, 40.0),
(9, 'Par', '22-06-2025', 2.0, 10, 3, 1, 52.1);