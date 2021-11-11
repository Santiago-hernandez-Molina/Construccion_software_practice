def pedirNombre():
    while True:

        nombre = input("Ingrese el nombre del estudiante a añadir: ")

        if nombre=="":

            print("el nombre no puede estar vacio")

        else:

            return nombre

def pedirTelefono():
    while True:
            telefono = input("Ingrese el telefono del estudiante:")
            return telefono


def pedirCodigo():
    while True:
            codigo = input("Ingrese el codigo del estudiante:")
            return codigo




def retornar_Estudiante():

    nombre=pedirTelefono()

    for estudiante in estudiantes:

        if estudiante[0] == nombre:

            print("el telefono del estudiante '{}' es {}".format(nombre, estudiante[1]))

            return True

    print("No se encuentró el estudiante")
    return False


def retornar_telefono_estuadiante():
    telefono=pedirTelefono()

    for estudiante in estudiantes:

        if estudiante[1] == telefono:

            print("el nombre del estudiante '{}' es {}".format(telefono, estudiante[0]))

            return True

    print("No se encuentra el telefono")
    return False


def listar_estudiantes():

    print("\n".join(i[0]+" - "+str(i[1])+" - "+str(i[2]) for i in estudiantes))

def listar_nombres():
    estudiantes.sort()
    nombres_estudiantes=[]
    nombres_estudiantes.append(" ".join(i[0] for i in estudiantes))
    print(nombres_estudiantes)

def borrarEstudiante():

    codigo=pedirCodigo()

    indice=buscarEstudiante(codigo)

    if indice==-1:

        print("No se ha encontrado el estudiante '{}'".format(codigo))

        return False

 

    print("Se ha eliminado el estudiante '{}' con el código {}".format(estudiantes[indice][0], estudiantes[indice][2]))

    del estudiantes[indice]

    return True




def buscarEstudiante(codigo):

    for i,e in enumerate(estudiantes):

        if e[2]==codigo:

            return i

    return -1

def Menú():

    print("|_________________________________________________________________|")
    print("|_____________________Bienvenido__________________________________|")
    print("|______________________Opciones:__________________________________|")

    print ("\t1 - Listar estudiantes")

    print ("\t2 - Buscar estudiante por nombre")

    print ("\t3 - Buscar estudiante por telefono")

    print ("\t4 - Añadir estudiante")

    print ("\t5 - Borrar un estudiante")

    print ("\t6 - Listar nombres en nueva lista")

    print ("\n\t0 - Salir")

#Lista
estudiantes=[]

while True:
    Menú ()

    try:

        opcion = int(input("Ingrese el número de la opción escogida: "))

    except:

        opcion=-1

 

    if opcion == 1:

       listar_estudiantes()

    elif opcion == 2:

        retornar_Estudiante()

    elif opcion == 3:

        retornar_telefono_estuadiante()

    elif opcion == 4:
        estudiantes.append((pedirNombre(), pedirTelefono(),pedirCodigo()))

    elif opcion == 5:

        borrarEstudiante()

    elif opcion == 6:

        listar_nombres()

    elif opcion == 0:

        break

    else:

        print("Ingrese solo las opciones que aparecen en el menú")