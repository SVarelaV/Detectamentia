import pyodbc

def get_connection():
    DRIVER = '{ODBC Driver 17 for SQL Server}'
    SERVER = 'localhost\\SQLEXPRESS'
    DATABASE = 'Detectamentia'
    TRUSTED_CONNECTION = 'yes'
    try:
        conn = pyodbc.connect(
            f'DRIVER={DRIVER};'
            f'SERVER={SERVER};'
            f'DATABASE={DATABASE};'
            f'Trusted_Connection={TRUSTED_CONNECTION};'
        )
        print("✅ Conexión exitosa a la base de datos SQL Server.")
        return conn
    except Exception as e:
        print("Ocurrió un error al conectar a SQL Server: ", e)
        return None

# if __name__ == "__main__":
#     conn = get_connection()
#     if conn:
#         print("La conexión se realizó correctamente.")
#         conn.close()
#     else:
#         print("No se pudo conectar a la base de datos.")
