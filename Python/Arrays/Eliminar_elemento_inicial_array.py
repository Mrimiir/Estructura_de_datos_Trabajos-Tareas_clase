''' 
# TRABAJO EN CLASE #
Eliminacion en Python, Programa para eliminar el primer elemento de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 02/09/2026
'''

#ejemplo NO.1 / "del"

inputArr = [11, 21, 31, 41, 51, 61]
print("Antes de la eliminación, el array es: ")
for j in range(len(inputArr)):
    print(inputArr[j], end = " ")

#Elimiando el primer elemento del array
del inputArr[0]     #del = delete

print("\nDespués de la eliminación, el array es: ")
for j in range(len(inputArr)):
    print(inputArr[j], end = " ")

print("\n")

#ejemplo NO.2 / "pop()"

inputArr2 = [11, 21, 31, 41, 51, 61]
print("\nAntes de la eliminación, el array es: ")
for j in range(len(inputArr2)):
    print(inputArr2[j], end = " ")

#Eliminando el primer elemento del array
inputArr2.pop(0)        #pop() = remueve y retorna el item del indice

print("\nDespués de la eliminación, el array es: ")
for j in range(len(inputArr2)):
    print(inputArr2[j], end = " ")