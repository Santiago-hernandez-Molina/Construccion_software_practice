
def suma(a=0,b=0):
    return a+b

print(suma(b=5))

def saludar(nombres, apellidos):
    print("hola desde construccion de software '{}', {}".format(nombres,apellidos))

saludar('santiago','Hernandez')

def acceso(año_nacimiento):
    edad = 2021-año_nacimiento
    if edad >=18:
        print("Bienvenido al establecimiento")
    else:
        print("no se le permite el acceso")

acceso(2005)