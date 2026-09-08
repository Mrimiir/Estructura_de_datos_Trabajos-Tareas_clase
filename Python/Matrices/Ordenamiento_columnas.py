'''
Mapeo de una matriz 2D a una matriz 1D en Python, las matrices por defecto se ordenan por mediante sus columnas.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 07/09/2026
'''

#row  and  r = filas; c = columnas

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

'''
para que imprimas por columnas puedes modificar aqui arriva el for, pero mantener original abajo
Cambio:
for y in range(c):              
    for x in range(r):
        k = y * r + x
        arr[k] = TwoDArr[x][y]
        k = k + 1
'''

print("Los elementos del array bidimenicional son: ")
for row in TwoDArr:
    for ele in row:
        print(ele, end = " ")       # Mostrar los elementos de la fila separados por espacios
    print()
print("\nLos elementos del array unidimencional son: ")
# Imprimir los elementos del array unidimencional
for x in range(r):
    for y in range(c):
        print((arr[y * r + x]), end = " ")      #para que imprimas por columnas puedes modificar aqui y mantener el for original
        #original = print((arr[x * r + y]), end = " ")

print()

# Otra version
r = 3; c = 3
arr2 = [0] * r * c       #Matriz inicializada y luego se le asigna un valor
TwoDArr2 = [ [1,2,3],
        [4,5,6],
        [7,8,9]];
k = 0
for y in range(c):              
    for x in range(r):
        k = y * r + x
        arr[k] = TwoDArr[x][y]

print("Los elementos del array bidimenicional son: ")
for row in TwoDArr2:
    for ele in row:
        print(ele, end = " ")       # Mostrar los elementos de la fila separados por espacios
    print()
print("\nLos elementos del array unidimencional son: ")
# Imprimir los elementos del array unidimencional
for x in range(r):
    for y in range(c):
        print((arr[x * r + y]), end = " ")