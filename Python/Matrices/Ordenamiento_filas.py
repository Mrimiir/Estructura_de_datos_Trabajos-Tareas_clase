'''
Mapeo de una matriz 2D a una matriz 1D en Python, las matrices por defecto se ordenan por mediante sus filas.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 07/09/2026
'''

#row = filas

r = 3; c = 3
arr = [0] * r * c       #Matriz inicializada y luego se le asigna un valor
TwoDArr = [ [1,2,3],
        [4,5,6],
        [7,8,9]];   #Almacenar elementos en un array unidimencional ordenados por filas
k = 0
for x in range(r):
    for y in range(c):
        k = x * r + y
        arr[k] = TwoDArr[x][y]

print("Los elementos del array bidimenicional son: ")
for row in TwoDArr:
    for ele in row:
        print(ele, end = " ")       # Mostrar los elementos de la fila separados por espacios
    print()
print("\nLos elementos del array unidimencional son: ")
# Imprimir los elementos del array unidimencional
for x in range(r):
    for y in range(c):
        print((arr[x * r + y]), end = " ")