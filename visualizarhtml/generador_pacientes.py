import pandas as pd
from datetime import datetime

def crear_pacientes_dataframe():
    """Simular pacientes para pruebas iniciales"""
    datos = [
        {"ID": 1, "Nombre": "Ana", "Apellido": "Gómez", "Edad": 70, "Género": "Femenino", "Ocupación": "Jubilada"},
        {"ID": 2, "Nombre": "Luis", "Apellido": "Martínez", "Edad": 68, "Género": "Masculino", "Ocupación": "Ama/o de casa"},
        {"ID": 3, "Nombre": "Carmen", "Apellido": "Sánchez", "Edad": 75, "Género": "Femenino", "Ocupación": "Desempleada"},
    ]
    return pd.DataFrame(datos)

def generar_tabla_html(df):
    """Convertir DataFrame a tabla HTML"""
    return df.to_html(
        index=False,
        classes='table table-productos',
        table_id='tabla-pacientes',
        border=0
    )

def actualizar_html_plantilla():
    df = crear_pacientes_dataframe()
    tabla_html = generar_tabla_html(df)
    total_pacientes = len(df)

    with open("plantilla_pacientes.html", "r", encoding="utf-8") as f:
        plantilla = f.read()

    html_final = plantilla.replace("{{TABLA_PACIENTES}}", tabla_html)
    html_final = html_final.replace("{{TOTAL_PACIENTES}}", str(total_pacientes))
    html_final = html_final.replace("{{FECHA_ACTUALIZACION}}", datetime.now().strftime("%d/%m/%Y %H:%M"))

    with open("pacientes_final.html", "w", encoding="utf-8") as f:
        f.write(html_final)

    print("✅ HTML generado: pacientes_final.html")

if __name__ == "__main__":
    actualizar_html_plantilla()
