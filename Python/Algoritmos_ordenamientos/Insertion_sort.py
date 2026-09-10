'''
Algoritmos de ordenamiento en Python, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 10/09/2026

Nota: Para algoritmos de busqueda  como la busqueda binaria es necesario tener ordenado el arreglo,
pero en alguno casos este no esta ordenado y estos algoritmos de ordenamiento resuelven ese problema
'''

def InsertionSort(a):
    for i in range(1, len(a)):
        temp = a[i]
        #Mueve los elementos mayores que temp
        # a una posicion mas adelante de su posicion actual
        j = i - 1
        while j >= 0 and temp < a[j]:
            a[j + 1] = a[j]
            j = j-1
        a[j + 1] = temp
def printArr(a):    # funcion para imprimir el array
    for i in range(len(a)):
        print(a[i], end = " ")
a = [70,15,2,51,60]
print("Antes de ordenar los elementos del arreglo: ")
printArr(a)
InsertionSort(a)
print("\nDespues de ordenarlos elementos del arreglo: ")
printArr(a)
