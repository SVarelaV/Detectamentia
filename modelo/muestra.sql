
-- Paso 1: Insertar 10 usuarios con ID explícito
INSERT INTO Usuarios (id_usuario, nombre, apellido1, apellido2, rol, email, activo) VALUES
(1, 'Ana', 'García', 'López', 'profesional', 'ana@example.com', 1),
(2, 'Carlos', 'Martínez', 'Sánchez', 'profesional', 'carlos@example.com', 1),
(3, 'Lucía', 'Fernández', 'Ruiz', 'paciente', 'lucia@example.com', 1),
(4, 'Miguel', 'Gómez', 'Díaz', 'paciente', 'miguel@example.com', 1),
(5, 'Laura', 'Torres', 'Ramírez', 'paciente', 'laura@example.com', 1),
(6, 'Pedro', 'Vargas', 'Romero', 'paciente', 'pedro@example.com', 1),
(7, 'Sofía', 'Jiménez', 'Navarro', 'paciente', 'sofia@example.com', 1),
(8, 'Javier', 'Molina', 'Ortega', 'paciente', 'javier@example.com', 1),
(9, 'Elena', 'Ramos', 'Castillo', 'paciente', 'elena@example.com', 1),
(10, 'David', 'Cano', 'Reyes', 'paciente', 'david@example.com', 1);

-- Paso 2: Insertar 10 informes con ID explícito
INSERT INTO Informes (
  id_informe, fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas,
  hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno,
  horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica, nivelEstres,
  dietaSaludable, presionArterialSis, presionArterialDia
) VALUES
(1, '2024-01-10', 1, 0, 1, 1, 1, 0, 0, 0, 0, 7, 'Buena', 0, 'Ocasional', 'Activo', '5', 'Sí', 120, 80),
(2, '2024-01-12', 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 'Buena', 0, 'Nunca', 'Moderado', '3', 'Sí', 118, 76),
(3, '2024-01-14', 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 'Mala', 1, 'Frecuente', 'Sedentario', '7', 'No', 140, 90),
(4, '2024-01-15', 0, 0, 1, 0, 1, 0, 0, 0, 0, 9, 'Regular', 0, 'Nunca', 'Moderado', '4', 'Sí', 125, 80),
(5, '2024-01-17', 1, 0, 0, 1, 0, 0, 1, 0, 1, 6, 'Regular', 1, 'Ocasional', 'Moderado', '6', 'No', 130, 85),
(6, '2024-01-18', 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 'Buena', 0, 'Nunca', 'Activo', '3', 'Sí', 115, 75),
(7, '2024-01-20', 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 'Mala', 1, 'Frecuente', 'Sedentario', '8', 'No', 145, 95),
(8, '2024-01-21', 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 'Buena', 0, 'Nunca', 'Moderado', '2', 'Sí', 112, 70),
(9, '2024-01-22', 1, 0, 1, 1, 1, 1, 1, 0, 1, 6, 'Regular', 1, 'Ocasional', 'Moderado', '7', 'No', 135, 88),
(10, '2024-01-25', 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 'Buena', 0, 'Nunca', 'Activo', '1', 'Sí', 110, 72);

-- Paso 3: Insertar 10 pacientes con ID explícito
INSERT INTO Pacientes (
  id_paciente, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion,
  nivelEstudios, id_usuario, id_informe
) VALUES
(1, 'Lucía', 'Fernández', 'Ruiz', 'Femenino', 65, 'Madrid', 'Jubilado/a', 'Universitarios completos', 3, 1),
(2, 'Miguel', 'Gómez', 'Díaz', 'Masculino', 70, 'Barcelona', 'Jubilado/a', 'Secundaria completa', 4, 2),
(3, 'Laura', 'Torres', 'Ramírez', 'Femenino', 60, 'Sevilla', 'Ama/o de casa', 'Bachillerato completo', 5, 3),
(4, 'Pedro', 'Vargas', 'Romero', 'Masculino', 72, 'Valencia', 'Jubilado/a', 'Primaria completa', 6, 4),
(5, 'Sofía', 'Jiménez', 'Navarro', 'Femenino', 68, 'Bilbao', 'Universitario/a', 'Posgrado', 7, 5),
(6, 'Javier', 'Molina', 'Ortega', 'Masculino', 64, 'Granada', 'Jubilado/a', 'Doctorado', 8, 6),
(7, 'Elena', 'Ramos', 'Castillo', 'Femenino', 67, 'Zaragoza', 'Administrativo/a', 'Bachillerato completo', 9, 7),
(8, 'David', 'Cano', 'Reyes', 'Masculino', 71, 'Alicante', 'Jubilado/a', 'Secundaria completa', 10, 8),
(9, 'María', 'Nieto', 'Pérez', 'Femenino', 62, 'Murcia', 'Sin ocupación', 'Primaria completa', 3, 9),
(10, 'Luis', 'Herrera', 'Luna', 'Masculino', 66, 'Vigo', 'Jubilado/a', 'Universitarios incompletos', 4, 10);

-- Paso 4: Insertar resultados de juegos con ID explícito
INSERT INTO ResultadoJuegos (
  id_resultado, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal, id_paciente
) VALUES
(1, 'stroop', '2024-02-01', 0.75, 18, 2, NULL, 30.5, 1),
(2, 'nback', '2024-02-01', 1.20, 15, 5, NULL, 45.0, 1),
(3, 'par', '2024-02-01', NULL, 8, 4, 12, 60.0, 1),
(4, 'stroop', '2024-02-02', 0.95, 14, 6, NULL, 40.0, 2),
(5, 'nback', '2024-02-02', 1.10, 12, 8, NULL, 50.0, 2),
(6, 'par', '2024-02-02', NULL, 7, 5, 14, 70.0, 2),
(7, 'stroop', '2024-02-03', 0.80, 17, 3, NULL, 33.0, 3),
(8, 'nback', '2024-02-03', 1.00, 16, 4, NULL, 48.0, 3),
(9, 'par', '2024-02-03', NULL, 9, 3, 10, 58.0, 3),
(10, 'stroop', '2024-02-04', 0.70, 19, 1, NULL, 29.0, 4);
