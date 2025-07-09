import pyodbc


_conectado = False

def get_connection():
    global _conectado
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
        if not _conectado:
            print("✅ Conexión exitosa a la base de datos SQL Server.")
            _conectado = True
        return conn
    except Exception as e:
        print("❌ Error de conexión a SQL Server: ", e)
        return None




# if __name__ == "__main__":
#     conn = get_connection()
#     if conn:
#         print("La conexión se realizó correctamente.")
#         conn.close()
#     else:
#         print("No se pudo conectar a la base de datos.")
