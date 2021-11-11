#diccionario

meses = {
    1: 'enero',
    2: 'febrero',
    3: 'marzo'
}
def get_mes(x):
    mes = meses.get(x)
    if mes == None:
        return "No existe el mes"
    return mes


mes = int(input("Digite el numero del mes"))
print(get_mes(mes))

