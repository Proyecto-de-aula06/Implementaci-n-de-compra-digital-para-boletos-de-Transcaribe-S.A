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
        
 
 
 
 
if k== 0:
    print("Datos incorrectos, intente nuevamente!")       


