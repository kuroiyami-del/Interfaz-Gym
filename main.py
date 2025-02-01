from database.db_setup import crearDataBase
from database.db_operaciones import *
from datetime import datetime, timedelta


def main():
    crearDataBase()
    while True:
        print("\n🏋️  GESTIÓN DE GIMNASIO  🏋️")
        print("1. Crear un nuevo usuario ")
        print("2. Ver todos los usuarios ")
        print("3. Eliminar usuario ")
        print("4. Buscar un usuario especifico ")
        print("5. Alterar usuario ")
        print("6. Asigna un plan a usuario")
        print("7. Ver plan de usuario")
        print("0. Salir")
        
        opcion = int(input("Inserta tu opcion: "))

        if opcion == 1:
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                telefono = input("Teléfono: ")
                foto = input("Ruta de la foto: ")
                cedula = input("Cédula: ")
                direccion = input("Direccion: ")
                

                insertarUsuario(nombre, edad, telefono, foto, cedula, direccion)
                print("\n✅Usuario agregado con éxito.")

        if opcion == 2:
            usuarios = mostrarUsuarios()
            for usuario in usuarios:
                    print(f'\n{usuario}\n')
                    print(f'-'*30)
        
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
        
        if opcion == 6:
            cedula = input("Ingrese la cédula del usuario para asignar un plan: ")
            
            opciones_plan = {
                "1": ("Diario", 1),
                "2": ("Semanal", 7),
                "3": ("Mensual", 30),
                "4": ("Trimestral", 90),
                "5": ("Anual", 365)
            }

            # Mostrar opciones de planes
            print("\n🏋️  PLANES DISPONIBLES")
            for key, (nombre, _) in opciones_plan.items():
                print(f"{key}. {nombre}")

            tipo_plan = input("\nSeleccione el numero de plan: ").strip()

            if tipo_plan not in opciones_plan:
                print("⚠️ Opción de plan inválida.")
                continue

            plan_nombre, dias_duracion = opciones_plan[tipo_plan]

            fecha_inicio = datetime.now().strftime("%Y-%m-%d")
            fecha_fin = (datetime.now() + timedelta(days=dias_duracion)).strftime("%Y-%m-%d")

            # Pasar todos los valores correctamente
            asignarPlan(cedula, plan_nombre, fecha_inicio, fecha_fin)


        if opcion == 7:
            cedula = input("Ingrese la cédula del usuario: ")
            mostrarPlanUsuario(cedula)

        if opcion == 0:
            print("Saliendo del programa")
            break
        

if __name__ == "__main__":
    main()