persona = {
    'nombres' : 'Monica',
    'Apellidos' : 'Reyes',
    'Telefono' : '3112345698'
}

print(persona['nombres'])
print(persona['Apellidos'])

for llave in persona:
    print(f"{llave}:{persona[llave]} ")

print(persona.keys())
print(persona.values())

#OPERACIONES

persona.update({'nombres':'Rocio'})
print(persona.values())