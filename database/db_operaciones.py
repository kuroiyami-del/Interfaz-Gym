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





