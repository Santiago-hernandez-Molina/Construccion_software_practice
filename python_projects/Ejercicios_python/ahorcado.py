#Juego del ahocardo
#Dato: El juego cuenta los espacios como letra

palabra="hola mundo"
palabra_usuario=[]
estado = 0
IMAGENES = ['''
     +---+
     |   |
         |
         |
         |
         |
  =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
 ========= PERDIO''']

def ingresar_letra():
    while True:

        letra = input("Ingrese la letra a añadir")

        if len(letra)>1:

            print("solo se puede una letra")

        else:

            return letra

def verificar_letra(letra):
    contador = 0
    adivino=False
    for i in palabra:
        if(letra==i and palabra_usuario[contador]=='0'):
            palabra_usuario[contador]=i
            adivino=True
        contador +=1
    print(palabra_usuario)
    
    return adivino
        
def llenar_palabra():
    for i in palabra:
        palabra_usuario.append('0')

llenar_palabra()
while estado!=6:
    if(verificar_letra(ingresar_letra())==False):
        print("perdio")
        estado += 1
        print(IMAGENES[estado])
    if('0' not in palabra_usuario):
        print("gano")
        break
    

    


