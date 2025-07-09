from config import get_connection

def insertar_datos():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Insertar 2 profesionales
        profesionales = [
            ("Laura", "Martínez", "Gómez", "profesional", "laura@hospital.com", 1),
            ("José", "Ramírez", "Santos", "profesional", "jose@hospital.com", 1)
        ]
        for nombre, ap1, ap2, rol, email, activo in profesionales:
            cursor.execute("""
                INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (nombre, ap1, ap2, rol, email, activo))
            cursor.execute("SELECT TOP 1 id_usuario FROM Usuarios ORDER BY id_usuario DESC")
            id_usuario = cursor.fetchone()[0]

            # Insertar contraseña genérica
            cursor.execute("""
                INSERT INTO Seguridad (passwd, id_usuario)
                VALUES (?, ?)
            """, ("123456", id_usuario))

        # Insertar 10 pacientes
        pacientes = [
            ("Carlos", "Pérez", "Ruiz", "Masculino", 67, "Madrid"),
            ("Ana", "López", "Martín", "Femenino", 72, "Barcelona"),
            ("Luis", "Gómez", "Fernández", "Masculino", 65, "Valencia"),
            ("María", "Rodríguez", "Serrano", "Femenino", 70, "Sevilla"),
            ("Javier", "Torres", "Morales", "Masculino", 68, "Bilbao"),
            ("Lucía", "García", "Muñoz", "Femenino", 66, "Zaragoza"),
            ("Andrés", "Navarro", "Iglesias", "Masculino", 71, "Granada"),
            ("Sofía", "Domínguez", "Vega", "Femenino", 74, "Málaga"),
            ("Miguel", "Sanz", "Ortega", "Masculino", 69, "Alicante"),
            ("Elena", "Herrera", "Delgado", "Femenino", 73, "Valladolid")
        ]

        for nombre, ap1, ap2, genero, edad, poblacion in pacientes:
            email = f"{nombre.lower()}.{ap1.lower()}@mail.com"

            # Insertar usuario
            cursor.execute("""
                INSERT INTO Usuarios (nombre, apellido1, apellido2, rol, email, activo)
                VALUES (?, ?, ?, 'paciente', ?, 1)
            """, (nombre, ap1, ap2, email))
            cursor.execute("SELECT TOP 1 id_usuario FROM Usuarios ORDER BY id_usuario DESC")
            id_usuario = cursor.fetchone()[0]

            # Insertar contraseña genérica
            cursor.execute("""
                INSERT INTO Seguridad (passwd, id_usuario)
                VALUES (?, ?)
            """, ("123456", id_usuario))

            # Insertar informe clínico básico
            cursor.execute("""
                INSERT INTO Informes (
                    fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol,
                    migrainas, hipertension, cardiopatia, depresionDiag,
                    accidenteCerebrovascular, trastornoSueno, horaSueno,
                    calidadSueno, fumador, consumoAlcohol, actividadFisica,
                    nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia
                ) VALUES (
                    '09/07/2025', 1, 0, 1, 2, 0, 0, 0,
                    '0', 1, 7.5, 2, 0, 1, 2, 5, 1, 130, 85
                )
            """)
            cursor.execute("SELECT TOP 1 id_informe FROM Informes ORDER BY id_informe DESC")
            id_informe = cursor.fetchone()[0]

            # Insertar paciente
            cursor.execute("""
                INSERT INTO Pacientes (
                    nombre, apellido1, apellido2, genero, edad,
                    poblacion, ocupacion, nivelEstudios, id_usuario, id_informe
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                nombre, ap1, ap2, genero, edad, poblacion,
                "Jubilado/a", "Universidad / Grado universitario", id_usuario, id_informe
            ))
            cursor.execute("SELECT TOP 1 id_paciente FROM Pacientes ORDER BY id_paciente DESC")
            id_paciente = cursor.fetchone()[0]

            # Insertar 3 juegos cognitivos
            juegos = [
                ("Stroop", 1.2, 12, 3, 0, 45.0),
                ("Nback", 1.1, 10, 2, 0, 50.0),
                ("Par", 1.4, 9, 1, 6, 55.0)
            ]

            for nombreJuego, reaccion, aciertos, errores, intentos, total in juegos:
                cursor.execute("""
                    INSERT INTO ResultadoJuegos (
                        id_paciente, nombreJuego, fecha,
                        tiempoReaccion, aciertos, errores,
                        numeroIntentos, tiempoTotal
                    ) VALUES (?, ?, '09/07/2025', ?, ?, ?, ?, ?)
                """, (
                    id_paciente, nombreJuego, reaccion, aciertos, errores, intentos, total
                ))

        conn.commit()
        print("✅ Datos de prueba insertados correctamente.")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Error al insertar datos: {e}")
        raise
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    insertar_datos()