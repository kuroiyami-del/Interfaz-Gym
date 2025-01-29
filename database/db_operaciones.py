import sqlite3

def connect():
    return sqlite3.connect("database/gym.db")

def insertarUsuario(nombre,edad,telefono,foto,cedula,direccion,plan):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(""" 
                   INSERT INTO usuarios (nombre,edad,telefono,foto,cedula,direccion,plan)
                   VALUES (?,?,?,?,?,?,?)
                    """, (nombre,edad,telefono,foto,cedula,direccion,plan))
    
    conn.commit()
    conn.close()

def mostrarUsuarios():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def eliminarUsuario(cedula):
    conn = connect()
    cursor = conn.cursor()

    try:
        # Eliminar usuario
        cursor.execute("DELETE FROM usuarios WHERE cedula = ?", (cedula,))
        conn.commit()

        # Verificar si el usuario aún existe
        cursor.execute("SELECT * FROM usuarios WHERE cedula = ?", (cedula,))
        resultado = cursor.fetchone()

        if resultado is None:
            print(f"Usuario con cédula {cedula} eliminado exitosamente.")
        else:
            print("El usuario todavía existe en la base de datos.")

    except sqlite3.Error as e:
        print(f"Error al eliminar el usuario: {e}")
    finally:
        conn.close()

def usuarioEspecifico(cedula):
    conn = connect()
    cursor = conn.cursor()

    try:

        cursor.execute("SELECT * FROM usuarios WHERE cedula = ? ",(cedula,))
        resultado = cursor.fetchone()
        

        if resultado is None:
                print(f"Usuario con cédula {cedula} no existe.")
                return None

          # Obtener nombres de las columnas
        columnas = [desc[0] for desc in cursor.description]
        
        # Crear un diccionario con los nombres de las columnas y los valores
        usuario_dict = dict(zip(columnas, resultado))
        
        return usuario_dict  

    except sqlite3.Error as e:
        print(f"Error al elcontrar el usuario: {e}")
    finally:
        conn.close()


def modificarUsuario(cedula):
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM usuarios WHERE cedula = ? ", (cedula,))
        usuario = cursor.fetchone()

        if usuario is None:
            print(f'⚠️ Usuario con cédula {cedula} no existe.')
            return 

          # Obtener nombres de las columnas
        columnas = [desc[0] for desc in cursor.description]

        #Mostrar datos actuales del usuario

        print(f"\nInformacion actual del usuario:")
        for clave,valor in zip(columnas,usuario):
            print(f"{clave.capitalize()}: {valor}")

        # Lista de opciones disponibles para modificar
        opciones = {
            "1": "nombre",
            "2": "edad",
            "3": "telefono",
            "4": "foto",
            "5": "direccion",
            "6": "plan"
        }

        print("\nQue dato deseas cambiar?: ")
        for key, value in opciones.items():
            print(f'{key}. {value}')

        opcion = input("Ingrese la opcion: ")

        if opcion not in opciones:
            print("⚠️ Opción inválida.")
            return
        
        nuevo_valor = input(f"Ingrese el nuevo valor para {opciones[opcion]}: ")

        cursor.execute(f'UPDATE usuarios SET {opciones[opcion]} = ? WHERE cedula = ?', (nuevo_valor,cedula))
        conn.commit()

        print("\n✅ Datos actualizados con éxito.")

    except sqlite3.Error as e:
        print(f"❌ Error al modificar el usuario: {e}")
        
    finally:
        conn.close()

        






