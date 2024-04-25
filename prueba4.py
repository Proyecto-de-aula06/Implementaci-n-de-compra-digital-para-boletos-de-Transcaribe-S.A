# Lista de usuarios
usuarios = [
    ("elias", "123"),
    ("andres", "321"),
    ("juan", "000"),
    ("maria", "111")
]

def login(username, password):
    for user in usuarios:
        if user[0] == username and user[1] == password:
            return True
    return False

# Función principal
def main():
    intentos = 0 
    max_intentos = 5 

    while intentos < max_intentos:
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        if login(username, password):
            print("Inicio de sesión exitoso.")
            print("Bienvenido al portal de compra digital, ya puedes navegar en la web")
           
            break
        else:
            intentos += 1
            print("Nombre de usuario o contraseña incorrectos. Intente nuevamente.")
            print(f"Intentos restantes: {max_intentos - intentos}")

    if intentos == max_intentos:
        print("Número máximo de intentos alcanzado. Cerrando el programa.")
        return

    

    if True:
        Recargar_tarjeta = {}

        def Recargar_tarjeta_f(Numero_de_tarjeta, Monto):
            Recargar_tarjeta[Numero_de_tarjeta] = Monto
            print(f'Recarga {Numero_de_tarjeta} realizada con éxito.')

        # Función para mostrar todas las recargas
        def mostrar_Recargas():
            
            if Recargar_tarjeta:
                print("Lista de Recargas:")
                for Numero_de_tarjeta, Monto in Recargar_tarjeta.items():
                    print(f'Numero de tarjeta: {Numero_de_tarjeta}, Monto: {Monto}')
            else:
                print("El registro de recarga está vacío.")

        # Función para eliminar una recarga
        def eliminar_Recarga(Numero_de_tarjeta):
            if Numero_de_tarjeta in Recargar_tarjeta:
                del Recargar_tarjeta[Numero_de_tarjeta]
                print(f'Recarga {Numero_de_tarjeta} eliminada con éxito.')
            else:
                print(f'La Recarga {Numero_de_tarjeta} no se encuentra en la agenda.')

        # interactuar con el menú de recarga
        while True:
            print("\nMenú de Recarga ")
            print("1. Realizar Recarga")
            print("2. Registro de Recargas")
            print("3. Borrar Registro de Recarga")
            print("4. Cerrar Sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                Numero_de_tarjeta = input("Ingrese el Numero de tarjeta de la Recarga: ")
                Monto = input("Ingrese el monto: "+"$")
                Recargar_tarjeta_f(Numero_de_tarjeta, Monto)
                print("Tarjeta recargada con exito.")

            elif opcion == "2":
                mostrar_Recargas()
            elif opcion == "3":
                Numero_de_tarjeta = input("Ingrese el Numero de tarjeta de la Recarga a eliminar: ")
                eliminar_Recarga(Numero_de_tarjeta)
            elif opcion == "4":
                print("Sesión cerrada con éxito. ")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

# Ejecutar la función principal al ejecutar el script
if __name__ == "__main__":
    main()
