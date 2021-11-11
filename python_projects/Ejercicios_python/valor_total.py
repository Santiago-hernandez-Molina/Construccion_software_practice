#2. Programa que recibe el valor de tres productos y calcula el iva
#en la impresion debe aparecer el total de los productos, el valor del iva y el total generado

producto1 =  int (input("Digite el valor del primer producto"))
producto2 =  int(input("Digite el valor del segundo producto "))
producto3 =  int(input("Digite el valor del tercer producto "))

valor_neto = producto1+producto2+producto3
iva = valor_neto * 0.19
total_generado = valor_neto + iva

print("valor Neto: ", valor_neto)
print("Iva: ", iva)
print("Total: ",total_generado)