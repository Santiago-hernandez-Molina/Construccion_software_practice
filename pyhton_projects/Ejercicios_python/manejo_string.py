nombre = 'jeniffer Margarita Guerrero'
nombre2 = 'Jeniffer margarita guerrero'
print(nombre.capitalize())
print(nombre.upper())
print(nombre.lower())
print(nombre.isdecimal())
print(len(nombre))
print(nombre.replace('jeniffer', "Anita"))
print(nombre)
print(nombre.find('M'))
print(nombre.isalpha())

#Manejo de sub_strings
print(nombre[0])
print(nombre[0:3])
print(nombre[8:-1])
print(nombre[nombre.find("M"):-1])
print(3*nombre)
print(nombre.find('m'))
#ciclos repetitivos

for character1 in nombre:
    print(character1)