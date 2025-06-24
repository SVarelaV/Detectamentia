-- Insertar un informe en la base de datos
INSERT INTO Informes (
    id, fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas,
    hipertension, cardiopatia, depresionDiagnosticada, accidenteCerebrovascular,
    trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol,
    actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia
)
VALUES (
    1, '2024-05-12', 1, 1, 0, 2, 1, 0, 1, 1,
    1, 6.5, 2, 0, 1, 2, 5, 1, 130, 85
);

-- Buscar un informe por su ID
SELECT * FROM Informes WHERE id = 1;

--Eliminar un informe por su ID
DELETE FROM Informes WHERE id = 1;

--Mostrar todos los informes
SELECT * FROM Informes ORDER BY id;

SELECT CASE 
        WHEN EXISTS (SELECT 1 FROM Informes WHERE id = 1) THEN 1
        ELSE 0
    END AS Existe;
