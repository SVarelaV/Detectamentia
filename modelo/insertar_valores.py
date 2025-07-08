from config import get_connection

def insertar_datos():
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Insertar profesionales
    profesionales = [
        ('Laura', 'Martínez', 'Gómez', 'profesional', 'laura@hospital.com', 1),
        ('José', 'Ramírez', 'Santos', 'profesional', 'jose@hospital.com', 1)
    ]

    for nombre, apellido1, apellido2, rol, email, activo in profesionales:
        cursor.execute("""
            INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre, apellido1, apellido2, rol, email, activo))

    # 2. Insertar pacientes (usuarios + informes + pacientes + juegos)
    nombres_pacientes = [
        ('Carlos', 'Pérez', 'Ruiz', 'Masculino', 67, 'Madrid'),
        ('Ana', 'López', 'Martín', 'Femenino', 72, 'Barcelona'),
        ('Luis', 'Gómez', 'Fernández', 'Masculino', 65, 'Valencia'),
        ('María', 'Rodríguez', 'Serrano', 'Femenino', 70, 'Sevilla'),
        ('Javier', 'Torres', 'Morales', 'Masculino', 68, 'Bilbao')
    ]

    for i, (nombre, apellido1, apellido2, genero, edad, poblacion) in enumerate(nombres_pacientes):
        email = f"{nombre.lower()}.{apellido1.lower()}@mail.com"

        # 2.1 Insertar usuario paciente
        cursor.execute("""
            INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
            VALUES (?, ?, ?, 'paciente', ?, 1)
        """, (nombre, apellido1, apellido2, email))

        cursor.execute("SELECT TOP 1 id_usuario FROM Usuarios ORDER BY id_usuario DESC")
        id_usuario = cursor.fetchone()[0]

        # 2.2 Insertar informe
        cursor.execute("""
            INSERT INTO Informes (
                fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol,
                migrainas, hipertension, cardiopatia, depresionDiag,
                accidenteCerebrovascular, trastornoSueno, horaSueno,
                calidadSueno, fumador, consumoAlcohol, actividadFisica,
                nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia
            )
            VALUES (
                '01/07/2025', 1, 0, 1, 2, 0, 0, 0, '0', 1, 7.0,
                2, 0, 1, 2, 6, 1, 125, 82
            )
        """)
        cursor.execute("SELECT TOP 1 id_informe FROM Informes ORDER BY id_informe DESC")
        id_informe = cursor.fetchone()[0]

        # 2.3 Insertar paciente
        cursor.execute("""
            INSERT INTO Pacientes (
                nombre, apellido1, apellido2, genero, edad,
                poblacion, ocupacion, nivelEstudios, id_usuario, id_informe
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            nombre, apellido1, apellido2, genero, edad,
            poblacion, 'Jubilado/a', 'Estudios universitarios completos',
            id_usuario, id_informe
        ))

        cursor.execute("SELECT TOP 1 id_paciente FROM Pacientes ORDER BY id_paciente DESC")
        id_paciente = cursor.fetchone()[0]

        # 2.4 Insertar resultados de juegos
        juegos = [
            ('Stroop', '01/07/2025', 1.2, 12, 3, 0, 45.0),
            ('Nback', '01/07/2025', 1.1, 10, 2, 0, 50.0),
            ('Par', '01/07/2025', 1.5, 9, 1, 6, 60.0)
        ]

        for nombreJuego, fecha, tiempoReaccion, aciertos, errores, intentos, tiempoTotal in juegos:
            cursor.execute("""
                INSERT INTO ResultadoJuegos (
                    id_paciente, nombreJuego, fecha,
                    tiempoReaccion, aciertos, errores,
                    numeroIntentos, tiempoTotal
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                id_paciente, nombreJuego, fecha,
                tiempoReaccion, aciertos, errores,
                intentos, tiempoTotal
            ))

    conn.commit()
    conn.close()
    print("✅ Datos insertados correctamente.")

if __name__ == "__main__":
    insertar_datos()
