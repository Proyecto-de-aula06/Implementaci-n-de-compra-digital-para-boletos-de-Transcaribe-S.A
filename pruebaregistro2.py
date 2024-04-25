def register():
    print("¡Bienvenido al registro de usuario!")
    nombre = input("Ingresa tu nombre: ")
    apellidos = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    correo = input("Ingresa tu correo: ")
    
    # You can add more fields like address, phone number, etc.
    print("\n¡Gracias por registrarte :)!")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Correo:", correo)
    print("Apellido:", apellidos)



def main():
    while True:
        print("\n¡Menu de registro:")
        print("1. Registro")
        print("2. Salir")
        choice = input("Ingresa una opción: ")

        if choice == '1':
            register()
        elif choice == '2':
            print("Cerrando el programa... Hasta pronto :(")
            break
        else:
            print("Elección no válida. Por favor ingrese '1' para registrarse o '2' para salir.")


if __name__ == "__main__":
    main()