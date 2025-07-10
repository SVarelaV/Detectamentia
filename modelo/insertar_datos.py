from config import get_connection

def insertar_datos():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        print("🚀 Insertando datos fijos...")

        # === Profesionales ===
        profesionales = [
            ("Ana", "Martínez", "López", "ana@hospital.org"),
            ("Carlos", "García", "Pérez", "carlos@hospital.org")
        ]
        for nombre, ap1, ap2, email in profesionales:
            cursor.execute("""
                INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
                VALUES (?, ?, ?, 'profesional', ?, 1)
            """, (nombre, ap1, ap2, email))
            cursor.execute("SELECT TOP 1 id_usuario FROM Usuarios ORDER BY id_usuario DESC")
            id_usuario = cursor.fetchone()[0]
            cursor.execute("INSERT INTO Seguridad (passwd, id_usuario) VALUES (?, ?)", ("123456", id_usuario))

        # === Pacientes ===
        pacientes = [
            ("Luis", "Ramírez", "Soto", "Masculino", 67, "Madrid", "Jubilado/a", "Primaria"),
            ("María", "Fernández", "Díaz", "Femenino", 72, "Barcelona", "Jubilado/a", "Secundaria"),
            ("Pedro", "López", "Muñoz", "Masculino", 65, "Sevilla", "Jubilado/a", "Primaria"),
            ("Lucía", "Gómez", "Ortega", "Femenino", 60, "Valencia", "Profesional universitario/a", "Universidad / Grado universitario"),
            ("José", "Ruiz", "Martín", "Masculino", 68, "Bilbao", "Jubilado/a", "Primaria"),
            ("Carmen", "Torres", "Vega", "Femenino", 69, "Granada", "Jubilado/a", "Secundaria"),
            ("Miguel", "Navarro", "Serrano", "Masculino", 66, "Zaragoza", "Técnico/a de nivel medio", "FP Superior / Universidad incompleta"),
            ("Elena", "Santos", "Campos", "Femenino", 74, "Málaga", "Ama/o de casa", "Primaria"),
            ("Raúl", "Castro", "Molina", "Masculino", 71, "Valladolid", "Jubilado/a", "Secundaria"),
            ("Laura", "Iglesias", "Romero", "Femenino", 70, "Santander", "Profesional universitario/a", "Máster / Posgrado"),
        ]

        informes = [
            (1, 0, 1, 1, 1, 0, 1, 0, 1, 6.5, 2, 1, 2, 1, 7, 1, 135, 85),
            (0, 1, 0, 2, 0, 1, 1, 1, 0, 7.5, 1, 0, 1, 2, 5, 1, 125, 80),
            (1, 1, 1, 0, 1, 1, 0, 2, 1, 5.5, 0, 1, 0, 0, 9, 0, 145, 95),
            (0, 0, 1, 1, 0, 0, 0, 0, 0, 8.0, 2, 0, 1, 1, 4, 1, 120, 78),
            (1, 0, 0, 2, 1, 1, 1, 1, 1, 6.0, 1, 1, 2, 2, 6, 0, 130, 88),
            (0, 1, 1, 0, 1, 0, 0, 1, 0, 7.0, 2, 0, 1, 1, 5, 1, 128, 82),
            (1, 1, 0, 1, 0, 1, 1, 2, 1, 4.5, 0, 1, 2, 0, 8, 0, 140, 90),
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 7.0, 2, 0, 0, 2, 3, 1, 115, 75),
            (1, 1, 1, 2, 1, 1, 1, 2, 1, 5.0, 1, 1, 2, 1, 7, 0, 138, 91),
            (0, 0, 1, 0, 0, 0, 0, 1, 0, 8.5, 2, 0, 0, 2, 2, 1, 118, 76)
        ]

        fechas = [
            "01-06-2025", "05-06-2025", "10-06-2025", "15-06-2025", "20-06-2025",
            "25-06-2025", "30-06-2025", "05-07-2025", "08-07-2025", "10-07-2025"
        ]

        for i, (nombre, ap1, ap2, genero, edad, pobla, ocupacion, estudios) in enumerate(pacientes, start=1):
            email = f"{nombre.lower()}.{ap1.lower()}@ejemplo.com"

            cursor.execute("""
                INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
                VALUES (?, ?, ?, 'paciente', ?, 1)
            """, (nombre, ap1, ap2, email))
            cursor.execute("SELECT TOP 1 id_usuario FROM Usuarios ORDER BY id_usuario DESC")
            id_usuario = cursor.fetchone()[0]

            cursor.execute("INSERT INTO Seguridad (passwd, id_usuario) VALUES (?, ?)", ("123456", id_usuario))

            cursor.execute("""
                INSERT INTO Informes (
                    fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol,
                    migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular,
                    trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol,
                    actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (fechas[i - 1], *informes[i - 1]))
            cursor.execute("SELECT TOP 1 id_informe FROM Informes ORDER BY id_informe DESC")
            id_informe = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO Pacientes (
                    nombre, apellido1, apellido2, genero, edad,
                    poblacion, ocupacion, nivelEstudios, id_usuario, id_informe
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                nombre, ap1, ap2, genero, edad, pobla, ocupacion, estudios, id_usuario, id_informe
            ))
            cursor.execute("SELECT TOP 1 id_paciente FROM Pacientes ORDER BY id_paciente DESC")
            id_paciente = cursor.fetchone()[0]

            juegos = [
                ("Stroop", "10-07-2025", 1.2, 18, 2, 0, 25.3),
                ("Nback", "10-07-2025", 1.8, 12, 4, 0, 30.0),
                ("Par", "10-07-2025", 1.0, 10, 1, 15, 45.6)
            ]
            for j in juegos:
                cursor.execute("""
                    INSERT INTO ResultadoJuegos (
                        id_paciente, nombreJuego, fecha,
                        tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (id_paciente, *j))

        conn.commit()
        print("✅ Datos fijos insertados con éxito.")
    except Exception as e:
        conn.rollback()
        print(f"❌ Error durante la inserción: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    insertar_datos()