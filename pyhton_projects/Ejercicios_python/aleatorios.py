import random

estuadiantes = [
    'AMEZQUITA NUÑEZ JUAN DAVID',
  'CORREA RIVERA ANGEL MANUEL',
  'DIAZ SILVERA ANDRES FELIPE',
  'HERNANDEZ MOLINA SANTIAGO ',
  'MORALES PEREZ ANDRES NICOLAS',
  'MORENO SANCHEZ SANTIAGO ANDRES ',
  'NEIRA MARTINEZ JUAN DAVID',
  'PEREZ HERNANDEZ SEBASTIAN',
  'PEREZ MOLINA JAIDER NICOLAS',
]

print (random.randrange(1,15))
print(random.choices(estuadiantes))

contador=0
numeros = []
while contador !=10:
  numeros.append(random.randrange(0,20))
  contador += 1

numeros_set= set(numeros)

print (numeros_set)