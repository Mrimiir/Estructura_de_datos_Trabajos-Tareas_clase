'''
Matrices en Python, Sintaxis básica de Python para escribir un arreglo de 2 dimenciones.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 07/09/2026
'''

#sintaxis de un arreglo bidimencional 
Two_dimensional_array = [
[1,2,3],
[4,5,6],
[7,8,9]
]

print("Los elementos del array son: ")
for row in Two_dimensional_array:
    for element in row:
        print(element, end = " ")       #Muestra los elementos en fila separados por espacios
    print()     #ir a la siguiente linea despues de la fila