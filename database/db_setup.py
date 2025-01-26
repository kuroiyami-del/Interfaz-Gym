import sqlite3

def crearDataBase():
    conn = sqlite3.connect("database/gym.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            telefono TEXT NOT NULL,
            foto TEXT NOT NULL,
            cedula TEXT NOT NULL UNIQUE,
            direccion TEXT NOT NULL,
            plan TEXT NOT NULL
        )
    """)

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS planes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER NOT NULL,
            tipo_plan TEXT NOT NULL,
            fecha_inicio DATE NOT NULL,
            fecha_fin DATE NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id) ON DELETE CASCADE ON UPDATE CASCADE
        )
    ''')

    conn.commit()
    conn.close()

    print("Base de datos creada exitosamente.")

if __name__ == "__main__":
    crearDataBase()
