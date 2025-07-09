from MODELO.config import get_connection

def validar_usuario():
    usuario=input("Introduce tu usuario: ")
    clave=input("Introduce tu contraseña: ")  
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        consulta_calve = "SELECT * FROM  calves WHERE dni = ? AND calve = ?;"
        cursor.execute(consulta_calve, (usuario, clave))
        resultado = cursor.fetchone()   
        if resultado is None:
            raise ValueError("Usuario o contraseña incorrectos")    
        # Si llegamos aquí, el usuario ha sido validado correctamente
        return True
    except (Exception, ValueError) as e:    
        return f"Error al validar el usuario: {e}"  
    finally:
            conn.close()
    
