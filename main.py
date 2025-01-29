from database.db_setup import crearDataBase
from database.db_operaciones import *


def main():
    crearDataBase()
    while True:
        print("1. Crear un nuevo usuario ")
        print("2. Ver todos los usuarios ")
        print("3. Eliminar usuario ")
        print("4. Buscar un usuario especifico ")
        print("5. Alterar usuario ")
        print("0. Salir")
        
        opcion = int(input("Inserta tu opcion: "))

        if opcion == 1:
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                telefono = input("Teléfono: ")
                foto = input("Ruta de la foto: ")
                cedula = input("Cédula: ")
                direccion = input("Direccion: ")
                plan = input("Ingrese el tipo de plan: ")

                insertarUsuario(nombre, edad, telefono, foto, cedula, direccion, plan)
                print("\nUsuario agregado con éxito.")

        if opcion == 2:
            usuarios = mostrarUsuarios()
            for usuario in usuarios:
                    print(f'\n{usuario}')
        
        if opcion == 3:
                cedula = input("Ingrese la cédula del usuario a eliminar: ")
                eliminarUsuario(cedula)
        
        if opcion == 4:
                cedula = input("Ingrese la cédula del usuario que desea buscar: ")
                usuarios = usuarioEspecifico(cedula)

                if usuarios:   
                    print("\nInformación del usuario:")
                for clave, valor in usuarios.items():
                        print(f'{clave.capitalize()}: {valor}')

        if opcion == 5:
            cedula = input("Ingrese la cédula del usuario a modificar: ")
            modificarUsuario(cedula)

        if opcion == 0:
            print("Saliendo del programa")
            break
        

if __name__ == "__main__":
    main()