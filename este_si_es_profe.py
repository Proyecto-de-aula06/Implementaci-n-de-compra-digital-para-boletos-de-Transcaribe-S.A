import re 

# Lista de usuarios
usuarios = [
    ("elias", "123"),
    ("andres", "321"),
    ("juan", "000"),
    ("maria", "111")
]
opiniones= []

def login(username, password):
    for user in usuarios:
        if user[0] == username and user[1] == password:
            return True
    return False

def validar_letras(texto):
    patron_letras = r'^[a-zA-Z]+$'
    if re.match(patron_letras, texto):
        return True
    else:
        return False

def validar_numeros(texto):
    patron_numeros = r'^[0-9]+$'
    if re.match(patron_numeros, texto):
        return True
    else:
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
        if not validar_letras(username):
            print("El nombre de usuario solo puede contener letras.")
            continue
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
        while True:
            numero_cuenta = input("Ingrese su número de cuenta: ")
            if not validar_numeros(numero_cuenta):
                print("El número de cuenta solo puede contener números.")
                continue
            else:
                break
        contraseña = input("Ingrese su contraseña: ")
        print("Datos ingresados correctamente.")
    elif metodo_pago.lower() == 'tarjeta de debito':
        while True:
            numero_tarjeta = input("Ingrese el número de su tarjeta de débito: ")
            if not validar_numeros(numero_tarjeta):
                print("El número de tarjeta solo puede contener números.")
                continue
            else:
                break
        contraseña = input("Ingrese su contraseña: ")
        clave_dinamica = input("Ingrese su clave dinámica: ")
        print("Datos ingresados correctamente.")
    elif metodo_pago.lower() == 'pse':
        usuario_pse = input("Ingrese su usuario PSE: ")
        contraseña = input("Ingrese su contraseña: ")
        print("Datos ingresados correctamente.")

def dar_opinion():
    usuario = input("Ingrese su nombre de usuario: ")
    opinion = input("Por favor, escriba su opinión: ")
    opiniones[usuario] = opinion
    print("¡Gracias por compartir su opinión!")

def iniciar_recarga():
    Recargar_tarjeta = {}

    def Recargar_tarjeta_f(numero_de_tarjeta, monto):
        Recargar_tarjeta[numero_de_tarjeta] = monto
        print(f'Recarga {numero_de_tarjeta} realizada con éxito.')
        print(f'{monto} recargado con exito en su tarjeta.')

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
        print("4. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                numero_tarjeta = input("Ingrese el Numero de tarjeta de la Recarga: ")
                if not validar_numeros(numero_tarjeta):
                    print("El número de tarjeta solo puede contener números.")
                    continue
                else:
                    break
            monto = input("Ingrese el monto: $")
            if not validar_numeros(monto):
                print("El monto solo puede contener números.")
                continue
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
    while True:
        nombre = input("Ingresa tu nombre: ")
        if not validar_letras(nombre):
            print("El nombre solo puede contener letras.")
            continue
        apellidos = input("Ingresa tu apellido: ")
        if not validar_letras(apellidos):
            print("El apellido solo puede contener letras.")
            continue
        edad = input("Ingresa tu edad: ")
        if not validar_numeros(edad):
            print("La edad solo puede contener números.")
            continue
        edad = int(edad)
        if edad < 16 or edad > 100:
            print("solo se permiten a usuarios de 16 a 100 años de edad")
            continue
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
        print("Apellido:", apellidos)
        print("Edad:", edad)
        print("Correo:", correo)
        print("Contraseña:", contraseña)
        print("Confirma tu contraseña:", confirmar_contraseña)
        print("Su registro ha sido exitoso, ¡Bienvenido! :)")
        break


def main():
    while True:
        print("\n¡Menu de registro:")
        print("1. Registro")
        print("2. Iniciar sesión")
        print("3. Mi opinion")
        print("4. Salir")
        choice = input("Ingresa una opción: ")

        if choice == '1':
            register()
        elif choice == '2':
            if iniciar_sesion():
                iniciar_recarga()
        elif choice == '3':
            usuario = input("Ingrese su nombre de usuario: ")
            opinion = input("Por favor, escriba su opinión: ")
            print("¡Gracias por compartir su opinión!")
        elif choice == '4':
            print("Cerrando el programa... Hasta pronto :)")
            break
        else:
            print("Elección no válida. Por favor ingrese '1' para registrarse, '2' para iniciar sesión o '3' para salir.")

if __name__ == "__main__":
    main()
