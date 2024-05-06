import re 

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

def validar_correo(correo):
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(patron_correo, correo):
        return True
    else:
        return False

def iniciar_sesion():
    intentos = 0
    max_intentos = 5
    while intentos < max_intentos:
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        if login(username, password):
            print("Inicio de sesión exitoso.")
            print("¡Bienvenido al portal de compra digital de Transcaribe!")
            return True
        else:
            intentos += 1
            print("Nombre de usuario o contraseña incorrectos. Intente nuevamente.")
            print(f"Intentos restantes: {max_intentos - intentos}")

    if intentos == max_intentos:
        print("Número máximo de intentos alcanzado. Cerrando el programa.")
        return False

def validar_metodo_pago(metodo_pago):
    metodos_validos = ['nequi', 'daviplata', 'tarjeta de debito', 'pse']
    if metodo_pago.lower() in metodos_validos:
        return True
    else:
        return False

def ingresar_datos_pago(metodo_pago):
    print(f"Ingresando datos para el método de pago: {metodo_pago}")
    if metodo_pago.lower() == 'nequi' or metodo_pago.lower() == 'daviplata':
        numero_cuenta = input("Ingrese su número de cuenta: ")
        contraseña = input("Ingrese su contraseña: ")
        print("Datos ingresados correctamente.")
    elif metodo_pago.lower() == 'tarjeta de debito':
        numero_tarjeta = input("Ingrese el número de su tarjeta de débito: ")
        contraseña = input("Ingrese su contraseña: ")
        clave_dinamica = input("Ingrese su clave dinámica: ")
        print("Datos ingresados correctamente.")
    elif metodo_pago.lower() == 'pse':
        usuario_pse = input("Ingrese su usuario PSE: ")
        contraseña = input("Ingrese su contraseña: ")
        print("Datos ingresados correctamente.")

def iniciar_recarga():
    Recargar_tarjeta = {}

    def Recargar_tarjeta_f(numero_de_tarjeta, monto):
        Recargar_tarjeta[numero_de_tarjeta] = monto
        print(f'Recarga {numero_de_tarjeta} realizada con éxito.')

    # Función para mostrar todas las recargas
    def mostrar_Recargas():
        if Recargar_tarjeta:
            print("Lista de Recargas:")
            for numero_de_tarjeta, monto in Recargar_tarjeta.items():
                print(f'Numero de tarjeta: {numero_de_tarjeta}, Monto: {monto}')
        else:
            print("El registro de recarga está vacío.")

    # Función para eliminar una recarga
    def eliminar_Recarga(numero_de_tarjeta):
        if numero_de_tarjeta in Recargar_tarjeta:
            del Recargar_tarjeta[numero_de_tarjeta]
            print(f'Recarga {numero_de_tarjeta} eliminada con éxito.')
        else:
            print(f'La Recarga {numero_de_tarjeta} no se encuentra en la agenda.')

    while True:
        print("\nMenú de Recarga ")
        print("1. Realizar Recarga")
        print("2. Registro de Recargas")
        print("3. Borrar Registro de Recarga")
        print("4. Cerrar Sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero_tarjeta = input("Ingrese el Numero de tarjeta de la Recarga: ")
            monto = input("Ingrese el monto: $")
            metodo_pago = input("Ingrese el método de pago (nequi, daviplata, tarjeta de debito, pse): ")
            if validar_metodo_pago(metodo_pago):
                ingresar_datos_pago(metodo_pago)
                Recargar_tarjeta_f(numero_tarjeta, monto)
                print("Tarjeta recargada con éxito.")
            else:
                print("Método de pago no válido.")
        elif opcion == "2":
            mostrar_Recargas()
        elif opcion == "3":
            numero_tarjeta = input("Ingrese el Numero de tarjeta de la Recarga a eliminar: ")
            eliminar_Recarga(numero_tarjeta)
        elif opcion == "4":
            print("Sesión cerrada con éxito. ")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def register():
    print("¡Bienvenido al registro de usuario!")
    nombre = input("Ingresa tu nombre: ")
    apellidos = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
  
    while True:
        correo = input("Ingresa tu correo electrónico: ")
        if validar_correo(correo):
            break
        else:
            print("El correo electrónico ingresado no es válido. Por favor, inténtelo nuevamente.")

    contraseña = input("Ingresa tu contraseña: ")
    confirmar_contraseña = input("Confirma tu contraseña: ")

    usuarios.append((nombre.lower(), contraseña))


    print("\n¡Gracias por registrarte :)!")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Correo:", correo)
    print("Apellido:", apellidos)
    print("Contraseña:", contraseña)
    print("Confirma tu contraseña:", confirmar_contraseña)
    print("Su registro ha sido exitoso, ¡Bienvenido! :)")

def main():
    while True:
        print("\n¡Menu de registro:")
        print("1. Registro")
        print("2. Iniciar sesión")
        print("3. Salir")
        choice = input("Ingresa una opción: ")

        if choice == '1':
            register()
        elif choice == '2':
            if iniciar_sesion():
                iniciar_recarga()
        elif choice == '3':
            print("Cerrando el programa... Hasta pronto :)")
            break
        else:
            print("Elección no válida. Por favor ingrese '1' para registrarse, '2' para iniciar sesión o '3' para salir.")

if __name__ == "__main__":
    main()
