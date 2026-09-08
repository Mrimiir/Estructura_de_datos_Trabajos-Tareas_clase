'''
Matrices en Python, Sintaxis básica de Python para escribir un arreglo de 3 dimensiones.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 07/09/2026
'''

Three_dimencional_array = [     #guarda 2 arreglos bidimencionales
[ [1,2,3],
[4,5,6],
[7,8,9]
],
[[10,11,12],
[13,14,15],
[16,17,18]
]
]

print("Los elementos del array son: ")
for Two_dimensional_array in Three_dimencional_array:
    for row in Two_dimensional_array:
        for element in row:
            print(element, end = " ")       #Muestra los elementos en fila separados por espacios
    print()         #ir a la siguiente linea despues de la fila
