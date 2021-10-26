# 6. Solicitar al usuario el ingreso de una frase y de una letra 
# (que puede o no estar en la frase). Recorrer la frase, carácter a
#  carácter, comparando con la letra buscada. Si el carácter no coincide,
#  indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar.
#  Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

frase = input("Ingrese una frase de su agrado")
letra = input("ingrese una letra de su agrado")
i = 0

for letra_frase in frase:
    if letra_frase == letra:
        print(f"la letra {letra} coincide en la posición{i} ")
    else:
        print(f"la letra no coincide en la posición {i}")
    i+=1