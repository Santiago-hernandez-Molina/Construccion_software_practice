estudiantes = [
  'AMEZQUITA NUÑEZ JUAN DAVID',
  'CORREA RIVERA ANGEL MANUEL',
  'DIAZ SILVERA ANDRES FELIPE',
  'HERNANDEZ MOLINA SANTIAGO JUAN',
  'MORALES PEREZ ANDRES NICOLAS',
  'MORENO SANCHEZ SANTIAGO ANDRES JUAN',
  'NEIRA MARTINEZ JUAN DAVID',
  'PEREZ HERNANDEZ SEBASTIAN',
  'PEREZ MOLINA JAIDER NICOLAS',
]



cont = 0
for estudiante in estudiantes:
    if estudiante.find("JUAN") != -1:
        cont+=1

print(f"En la lista de estudiantes se encuentran {cont} Juanes")