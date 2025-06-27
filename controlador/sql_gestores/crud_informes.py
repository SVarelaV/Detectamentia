from modelo.config import get_connection

def agregar_informe(
    id_informe, fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol,
    migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular,
    trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol,
    actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia
):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO Informes (
                id_informe, fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol,
                migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular,
                trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol,
                actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                id_informe, fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol,
                migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular,
                trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol,
                actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia
            )
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"❌ Error al agregar informe: {e}")
        return False
    finally:
        conn.close()

def buscar_informe_por_id(id_informe):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Informes WHERE id_informe = ?", (id_informe,))
        return cursor.fetchone()
    except Exception as e:
        print(f"❌ Error al buscar informe por ID: {e}")
        return None
    finally:
        conn.close()

def eliminar_informe(id_informe):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Informes WHERE id_informe = ?", (id_informe,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"❌ Error al eliminar informe: {e}")
        return False
    finally:
        conn.close()


def mostrar_informes():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Informes")
        return cursor.fetchall()
    except Exception as e:
        print(f"❌ Error al mostrar informes: {e}")
        return []
    finally:
        conn.close()


def existe_informe(id_informe):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM Informes WHERE id_informe = ?", (id_informe,))
        return cursor.fetchone() is not None
    except Exception as e:
        print(f"❌ Error al verificar existencia de informe: {e}")
        return False
    finally:
        conn.close()


def actualizar_informe(
    id_informe, fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol,
    migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular,
    trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol,
    actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia
):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            UPDATE Informes SET
                fechaRegistro = ?, antecFamiliaresAlzheimer = ?, diabetes = ?, colesterol = ?,
                migrainas = ?, hipertension = ?, cardiopatia = ?, depresionDiag = ?, accidenteCerebrovascular = ?,
                trastornoSueno = ?, horaSueno = ?, calidadSueno = ?, fumador = ?, consumoAlcohol = ?,
                actividadFisica = ?, nivelEstres = ?, dietaSaludable = ?, presionArterialSis = ?, presionArterialDia = ?
            WHERE id_informe = ?
            ''',
            (
                fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol,
                migrainas, hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular,
                trastornoSueno, horaSueno, calidadSueno, fumador, consumoAlcohol,
                actividadFisica, nivelEstres, dietaSaludable, presionArterialSis, presionArterialDia,
                id_informe
            )
        )
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"❌ Error al actualizar informe: {e}")
        return False
    finally:
        conn.close()
