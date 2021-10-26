abecedario = ['a',' b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letras_eliminar = []

for letra in abecedario:
     if abecedario.index(letra) % 3 == 0 or abecedario.index(letra) % 5 == 0:
        letras_eliminar.extend(letra)

print(letras_eliminar)

for letra in letras_eliminar:
    abecedario.remove(letra)
    
    
print(abecedario)