#login de usuarios

class user:
    def __init__(self, nom, pwd):
        self.nom = nom
        self.pwd = pwd

u1 = user("elias", "123")
u2 = user("andres", "321")
u3 = user("juan", "000")
u4 = user("maria", "111")

usuarios = [u1, u2, u3, u4]

n= input("Ingrese su usuario: ")
p= input("Ingrese la contraseña: ")

k=0

for i in range(len(usuarios)):
    if usuarios[i].nom == n and usuarios[i].pwd == p:
       print( usuarios[i].nom, "- Bienvenido al portal de compra digital")
       k=1
       break 
        
 
 


if k==0:
    print("Datos incorrectos, intente nuevamente!")  
    
   
break


#menu de compra
Recargar_tarjeta = {}


def Recargar_tarjeta_f(Numero_de_tarjeta, Monto):
    Recargar_tarjeta[Numero_de_tarjeta] = Monto
    print(f'Recarga {Numero_de_tarjeta} realizda con éxito.')



# Función para mostrar todos los Recargas
def mostrar_Recargas():
    if Recargar_tarjeta:
        print("Lista de Recargas:")
        for Numero_de_tarjeta, Monto in Recargar_tarjeta.items():
            print(f'Numero de tarjeta: {Numero_de_tarjeta}, Monto: {Monto}')
    else:
        print("El registro de recarga está vacía.")

# Función para eliminar un Recarga
def eliminar_Recarga(Numero_de_tarjeta):
    if Numero_de_tarjeta in Recargar_tarjeta:
        del Recargar_tarjeta[Numero_de_tarjeta]
        print(f'Recarga {Numero_de_tarjeta} eliminada con éxito.')
    else:
        print(f'El Recarga {Numero_de_tarjeta} no se encuentra en la agenda.')

# Loop principal para interactuar con la agenda
while True:
    print("\nMenu De Recarga")
    print("1. Realizar Recarga")
    
    print("2. Registro de Recargas")
    print("3. Borrar Registro de  Recarga")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        Numero_de_tarjeta = input("Ingrese el Numero de tarjeta de la Recarga: ")
        Monto = input("Ingrese el número del monto: ")
        Recargar_tarjeta_f(Numero_de_tarjeta, Monto)
    
    elif opcion == "2":
        mostrar_Recargas()
    elif opcion == "3":
        Numero_de_tarjeta = input("Ingrese el Numero de tarjeta del Recarga a eliminar: ")
        eliminar_Recarga(Numero_de_tarjeta)
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")