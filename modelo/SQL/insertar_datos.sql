-- Script SQL corregido con BEGIN...END y GO para evitar conflictos de variables
SET NOCOUNT ON;

-- Insertar profesionales
INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo) VALUES
('Ana', 'Martínez', 'López', 'profesional', 'ana@hospital.org', 1),
('Carlos', 'García', 'Pérez', 'profesional', 'carlos@hospital.org', 1);

BEGIN
    PRINT '➕ Insertando paciente: Luis Ramírez';
    DECLARE @id_usuario INT, @id_informe INT, @id_paciente INT;
    INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
    VALUES ('Luis', 'Ramírez', 'Soto', 'paciente', 'luis.ramírez@ejemplo.com', 1);
    SET @id_usuario = SCOPE_IDENTITY();
    INSERT INTO Seguridad (passwd, id_usuario) VALUES ('123456', @id_usuario);
    INSERT INTO Informes (fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia)
    VALUES ('01-06-2025', 1, 0, 1, 1, 1, 0, 1, 0, 1, 6.5, 2, 1, 2, 1, 7, 1, 135, 85);
    SET @id_informe = SCOPE_IDENTITY();
    INSERT INTO Pacientes (nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios, id_usuario, id_informe)
    VALUES ('Luis', 'Ramírez', 'Soto', 'Masculino', 67, 'Madrid', 'Jubilado/a', 'Primaria', @id_usuario, @id_informe);
    SET @id_paciente = SCOPE_IDENTITY();
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Stroop', '10-07-2025', 1.2, 18, 2, 0, 25.3);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Nback', '10-07-2025', 1.8, 12, 4, 0, 30.0);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Par', '10-07-2025', 1.0, 10, 1, 15, 45.6);
END
GO

BEGIN
    PRINT '➕ Insertando paciente: María Fernández';
    DECLARE @id_usuario INT, @id_informe INT, @id_paciente INT;
    INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
    VALUES ('María', 'Fernández', 'Díaz', 'paciente', 'maría.fernández@ejemplo.com', 1);
    SET @id_usuario = SCOPE_IDENTITY();
    INSERT INTO Seguridad (passwd, id_usuario) VALUES ('123456', @id_usuario);
    INSERT INTO Informes (fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia)
    VALUES ('05-06-2025', 0, 1, 0, 2, 0, 1, 1, 1, 0, 7.5, 1, 0, 1, 2, 5, 1, 125, 80);
    SET @id_informe = SCOPE_IDENTITY();
    INSERT INTO Pacientes (nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios, id_usuario, id_informe)
    VALUES ('María', 'Fernández', 'Díaz', 'Femenino', 72, 'Barcelona', 'Jubilado/a', 'Secundaria', @id_usuario, @id_informe);
    SET @id_paciente = SCOPE_IDENTITY();
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Stroop', '10-07-2025', 1.2, 18, 2, 0, 25.3);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Nback', '10-07-2025', 1.8, 12, 4, 0, 30.0);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Par', '10-07-2025', 1.0, 10, 1, 15, 45.6);
END
GO

BEGIN
    PRINT '➕ Insertando paciente: Pedro López';
    DECLARE @id_usuario INT, @id_informe INT, @id_paciente INT;
    INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
    VALUES ('Pedro', 'López', 'Muñoz', 'paciente', 'pedro.lópez@ejemplo.com', 1);
    SET @id_usuario = SCOPE_IDENTITY();
    INSERT INTO Seguridad (passwd, id_usuario) VALUES ('123456', @id_usuario);
    INSERT INTO Informes (fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia)
    VALUES ('10-06-2025', 1, 1, 1, 0, 1, 1, 0, 2, 1, 5.5, 0, 1, 0, 0, 9, 0, 145, 95);
    SET @id_informe = SCOPE_IDENTITY();
    INSERT INTO Pacientes (nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios, id_usuario, id_informe)
    VALUES ('Pedro', 'López', 'Muñoz', 'Masculino', 65, 'Sevilla', 'Jubilado/a', 'Primaria', @id_usuario, @id_informe);
    SET @id_paciente = SCOPE_IDENTITY();
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Stroop', '10-07-2025', 1.2, 18, 2, 0, 25.3);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Nback', '10-07-2025', 1.8, 12, 4, 0, 30.0);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Par', '10-07-2025', 1.0, 10, 1, 15, 45.6);
END
GO

BEGIN
    PRINT '➕ Insertando paciente: Lucía Gómez';
    DECLARE @id_usuario INT, @id_informe INT, @id_paciente INT;
    INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
    VALUES ('Lucía', 'Gómez', 'Ortega', 'paciente', 'lucía.gómez@ejemplo.com', 1);
    SET @id_usuario = SCOPE_IDENTITY();
    INSERT INTO Seguridad (passwd, id_usuario) VALUES ('123456', @id_usuario);
    INSERT INTO Informes (fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia)
    VALUES ('15-06-2025', 0, 0, 1, 1, 0, 0, 0, 0, 0, 8.0, 2, 0, 1, 1, 4, 1, 120, 78);
    SET @id_informe = SCOPE_IDENTITY();
    INSERT INTO Pacientes (nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios, id_usuario, id_informe)
    VALUES ('Lucía', 'Gómez', 'Ortega', 'Femenino', 60, 'Valencia', 'Profesional universitario/a', 'Universidad / Grado universitario', @id_usuario, @id_informe);
    SET @id_paciente = SCOPE_IDENTITY();
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Stroop', '10-07-2025', 1.2, 18, 2, 0, 25.3);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Nback', '10-07-2025', 1.8, 12, 4, 0, 30.0);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Par', '10-07-2025', 1.0, 10, 1, 15, 45.6);
END
GO

BEGIN
    PRINT '➕ Insertando paciente: José Ruiz';
    DECLARE @id_usuario INT, @id_informe INT, @id_paciente INT;
    INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
    VALUES ('José', 'Ruiz', 'Martín', 'paciente', 'josé.ruiz@ejemplo.com', 1);
    SET @id_usuario = SCOPE_IDENTITY();
    INSERT INTO Seguridad (passwd, id_usuario) VALUES ('123456', @id_usuario);
    INSERT INTO Informes (fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia)
    VALUES ('20-06-2025', 1, 0, 0, 2, 1, 1, 1, 1, 1, 6.0, 1, 1, 2, 2, 6, 0, 130, 88);
    SET @id_informe = SCOPE_IDENTITY();
    INSERT INTO Pacientes (nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios, id_usuario, id_informe)
    VALUES ('José', 'Ruiz', 'Martín', 'Masculino', 68, 'Bilbao', 'Jubilado/a', 'Primaria', @id_usuario, @id_informe);
    SET @id_paciente = SCOPE_IDENTITY();
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Stroop', '10-07-2025', 1.2, 18, 2, 0, 25.3);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Nback', '10-07-2025', 1.8, 12, 4, 0, 30.0);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Par', '10-07-2025', 1.0, 10, 1, 15, 45.6);
END
GO

BEGIN
    PRINT '➕ Insertando paciente: Carmen Torres';
    DECLARE @id_usuario INT, @id_informe INT, @id_paciente INT;
    INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
    VALUES ('Carmen', 'Torres', 'Vega', 'paciente', 'carmen.torres@ejemplo.com', 1);
    SET @id_usuario = SCOPE_IDENTITY();
    INSERT INTO Seguridad (passwd, id_usuario) VALUES ('123456', @id_usuario);
    INSERT INTO Informes (fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia)
    VALUES ('25-06-2025', 0, 1, 1, 0, 1, 0, 0, 1, 0, 7.0, 2, 0, 1, 1, 5, 1, 128, 82);
    SET @id_informe = SCOPE_IDENTITY();
    INSERT INTO Pacientes (nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios, id_usuario, id_informe)
    VALUES ('Carmen', 'Torres', 'Vega', 'Femenino', 69, 'Granada', 'Jubilado/a', 'Secundaria', @id_usuario, @id_informe);
    SET @id_paciente = SCOPE_IDENTITY();
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Stroop', '10-07-2025', 1.2, 18, 2, 0, 25.3);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Nback', '10-07-2025', 1.8, 12, 4, 0, 30.0);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Par', '10-07-2025', 1.0, 10, 1, 15, 45.6);
END
GO

BEGIN
    PRINT '➕ Insertando paciente: Miguel Navarro';
    DECLARE @id_usuario INT, @id_informe INT, @id_paciente INT;
    INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
    VALUES ('Miguel', 'Navarro', 'Serrano', 'paciente', 'miguel.navarro@ejemplo.com', 1);
    SET @id_usuario = SCOPE_IDENTITY();
    INSERT INTO Seguridad (passwd, id_usuario) VALUES ('123456', @id_usuario);
    INSERT INTO Informes (fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia)
    VALUES ('30-06-2025', 1, 1, 0, 1, 0, 1, 1, 2, 1, 4.5, 0, 1, 2, 0, 8, 0, 140, 90);
    SET @id_informe = SCOPE_IDENTITY();
    INSERT INTO Pacientes (nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios, id_usuario, id_informe)
    VALUES ('Miguel', 'Navarro', 'Serrano', 'Masculino', 66, 'Zaragoza', 'Técnico/a de nivel medio', 'FP Superior / Universidad incompleta', @id_usuario, @id_informe);
    SET @id_paciente = SCOPE_IDENTITY();
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Stroop', '10-07-2025', 1.2, 18, 2, 0, 25.3);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Nback', '10-07-2025', 1.8, 12, 4, 0, 30.0);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Par', '10-07-2025', 1.0, 10, 1, 15, 45.6);
END
GO

BEGIN
    PRINT '➕ Insertando paciente: Elena Santos';
    DECLARE @id_usuario INT, @id_informe INT, @id_paciente INT;
    INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
    VALUES ('Elena', 'Santos', 'Campos', 'paciente', 'elena.santos@ejemplo.com', 1);
    SET @id_usuario = SCOPE_IDENTITY();
    INSERT INTO Seguridad (passwd, id_usuario) VALUES ('123456', @id_usuario);
    INSERT INTO Informes (fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia)
    VALUES ('05-07-2025', 0, 0, 0, 0, 0, 0, 0, 0, 0, 7.0, 2, 0, 0, 2, 3, 1, 115, 75);
    SET @id_informe = SCOPE_IDENTITY();
    INSERT INTO Pacientes (nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios, id_usuario, id_informe)
    VALUES ('Elena', 'Santos', 'Campos', 'Femenino', 74, 'Málaga', 'Ama/o de casa', 'Primaria', @id_usuario, @id_informe);
    SET @id_paciente = SCOPE_IDENTITY();
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Stroop', '10-07-2025', 1.2, 18, 2, 0, 25.3);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Nback', '10-07-2025', 1.8, 12, 4, 0, 30.0);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Par', '10-07-2025', 1.0, 10, 1, 15, 45.6);
END
GO

BEGIN
    PRINT '➕ Insertando paciente: Raúl Castro';
    DECLARE @id_usuario INT, @id_informe INT, @id_paciente INT;
    INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
    VALUES ('Raúl', 'Castro', 'Molina', 'paciente', 'raúl.castro@ejemplo.com', 1);
    SET @id_usuario = SCOPE_IDENTITY();
    INSERT INTO Seguridad (passwd, id_usuario) VALUES ('123456', @id_usuario);
    INSERT INTO Informes (fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia)
    VALUES ('08-07-2025', 1, 1, 1, 2, 1, 1, 1, 2, 1, 5.0, 1, 1, 2, 1, 7, 0, 138, 91);
    SET @id_informe = SCOPE_IDENTITY();
    INSERT INTO Pacientes (nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios, id_usuario, id_informe)
    VALUES ('Raúl', 'Castro', 'Molina', 'Masculino', 71, 'Valladolid', 'Jubilado/a', 'Secundaria', @id_usuario, @id_informe);
    SET @id_paciente = SCOPE_IDENTITY();
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Stroop', '10-07-2025', 1.2, 18, 2, 0, 25.3);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Nback', '10-07-2025', 1.8, 12, 4, 0, 30.0);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Par', '10-07-2025', 1.0, 10, 1, 15, 45.6);
END
GO

BEGIN
    PRINT '➕ Insertando paciente: Laura Iglesias';
    DECLARE @id_usuario INT, @id_informe INT, @id_paciente INT;
    INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
    VALUES ('Laura', 'Iglesias', 'Romero', 'paciente', 'laura.iglesias@ejemplo.com', 1);
    SET @id_usuario = SCOPE_IDENTITY();
    INSERT INTO Seguridad (passwd, id_usuario) VALUES ('123456', @id_usuario);
    INSERT INTO Informes (fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia)
    VALUES ('10-07-2025', 0, 0, 1, 0, 0, 0, 0, 1, 0, 8.5, 2, 0, 0, 2, 2, 1, 118, 76);
    SET @id_informe = SCOPE_IDENTITY();
    INSERT INTO Pacientes (nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivelEstudios, id_usuario, id_informe)
    VALUES ('Laura', 'Iglesias', 'Romero', 'Femenino', 70, 'Santander', 'Profesional universitario/a', 'Máster / Posgrado', @id_usuario, @id_informe);
    SET @id_paciente = SCOPE_IDENTITY();
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Stroop', '10-07-2025', 1.2, 18, 2, 0, 25.3);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Nback', '10-07-2025', 1.8, 12, 4, 0, 30.0);
    INSERT INTO ResultadoJuegos (id_paciente, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal)
    VALUES (@id_paciente, 'Par', '10-07-2025', 1.0, 10, 1, 15, 45.6);
END
GO
