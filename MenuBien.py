class User:
    def __init__(self, nom, pwd):
        self.nom = nom
        self.pwd = pwd

u1 = User("elias", "123")
u2 = User("andres", "321")
u3 = User("juan", "000")
u4 = User("maria", "111")

usuarios = [u1, u2, u3, u4]

n = input("Ingrese su usuario: ")
p = input("Ingrese la contraseña: ")

autenticado = False

for usuario in usuarios:
    if usuario.nom == n and usuario.pwd == p:
        print(usuario.nom, "- Bienvenido al portal de compra digital")
        autenticado = True
        break

if autenticado:
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

    # Loop principal para interactuar con el menú de recarga
    while True:
       
        print( "  \nMenú de Recarga "  )
        print("1. Realizar Recarga")
        print("2. Registro de Recargas")
        print("3. Borrar Registro de Recarga")
        print("4. Cerrar Sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Numero_de_tarjeta = input("Ingrese el Numero de tarjeta de la Recarga: ")
            Monto = input("Ingrese el monto: ")
            Recargar_tarjeta_f(Numero_de_tarjeta, Monto)

        elif opcion == "2":
            mostrar_Recargas()
        elif opcion == "3":
            Numero_de_tarjeta = input("Ingrese el Numero de tarjeta de la Recarga a eliminar: ")
            eliminar_Recarga(Numero_de_tarjeta)
        elif opcion == "4":
            print ("Sesión cerrada con exito. ")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
else:
    print("Usuario o contraseña incorrectos.")
