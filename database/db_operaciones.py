import sqlite3
from datetime import datetime,timedelta

def connect():
    return sqlite3.connect("database/gym.db")


conn= connect()
cursor = conn.cursor()

# OPERACIONES PARA LA TABLA usuarios

def insertarUsuario(nombre,edad,telefono,foto,cedula,direccion):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(""" 
                   INSERT INTO usuarios (nombre,edad,telefono,foto,cedula,direccion)
                   VALUES (?,?,?,?,?,?)
                    """, (nombre,edad,telefono,foto,cedula,direccion))
    
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
            print(f"Usuario con cédula {cedula} eliminado exitosamente.\n")
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

        



# OPERACIONES PARA LA TABLA planes


def asignarPlan(cedula, tipo_plan, fecha_inicio, fecha_fin):
    conn = sqlite3.connect("database/gym.db")
    cursor = conn.cursor()

    try:
        # Buscar el ID del usuario con la cédula proporcionada
        cursor.execute("SELECT id FROM usuarios WHERE cedula = ?", (cedula,))
        usuario = cursor.fetchone()

        if usuario is None:
            print(f"⚠️ No se encontró un usuario con la cédula {cedula}. No se puede asignar el plan.")
            return

        usuario_id = usuario[0]

        # Insertar el nuevo plan en la base de datos
        cursor.execute("""
            INSERT INTO planes (id_usuario, tipo_plan, fecha_inicio, fecha_fin)
            VALUES (?, ?, ?, ?)
        """, (usuario_id, tipo_plan, fecha_inicio, fecha_fin))

        conn.commit()
        print(f"✅ Plan '{tipo_plan}' asignado correctamente a {cedula}.")

    except sqlite3.Error as e:
        print(f"❌ Error al asignar el plan: {e}")

    finally:
        conn.close()

def mostrarPlanUsuario(cedula):
    conn = None  # Inicializar la conexión fuera del try-except para cerrarla correctamente
    try:
        conn = sqlite3.connect("database/gym.db")  # Conectar a la base de datos
        cursor = conn.cursor()

        # Buscar al usuario por cédula
        cursor.execute("SELECT id, nombre FROM usuarios WHERE cedula = ?", (cedula,))
        usuario = cursor.fetchone()

        if usuario is None:
            print(f"⚠️ No se encontró un usuario con la cédula {cedula}.")
            return
        
        usuario_id, nombre = usuario
        print(f"📌 Usuario encontrado: {nombre} (ID: {usuario_id})")  # 🔍 Depuración

        # Verificar si el usuario tiene un plan activo
        cursor.execute("""
            SELECT tipo_plan, fecha_inicio, fecha_fin 
            FROM planes WHERE id_usuario = ?
        """, (usuario_id,))
        
        plan = cursor.fetchone()

        if plan is None:
            print(f"⚠️ {nombre} está registrado, pero no tiene un plan activo.")
            return
        
        tipo_plan, fecha_inicio, fecha_fin = plan

        # Mostrar información del plan
        print("\n📋 Información del plan:")
        print("-" * 50)
        print(f"👤 Usuario: {nombre}")
        print(f"📅 Tipo de Plan: {tipo_plan}")
        print(f"📆 Fecha de Inicio: {fecha_inicio}")
        print(f"⏳ Fecha de Vencimiento: {fecha_fin}")
        print("-" * 50)

    except sqlite3.Error as e:
        print(f"❌ Error al obtener el plan: {e}")

    finally:
        if conn:
            conn.close()  # Asegurar que la conexión siempre se cierra





