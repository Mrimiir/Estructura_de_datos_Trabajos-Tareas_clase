'''
Algoritmos de ordenamiento en Python, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 02/09/2026

Nota: Para algoritmos de busqueda  como la busqueda binaria es necesario tener ordenado el arreglo,
pero en alguno casos este no esta ordenado y estos algoritmos de ordenamiento resuelven ese problema
'''

def bubble_sort (a):
    # Iterando por todos los elementos del array
    s = len(a)
    for j in range(s):
        isSwapped = False
        # Los ultimos j  elementos ya estan en su lugar correspondiente.
        for j in range(0, s - j -1):
            # Recorriendo el array de 0 a s - j - 1
            # Intercambiando si el elemento encontrando es mayor
            #que el siguiente elemento
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                isSwapped = True
        if (isSwapped == False):
            break

# Codigo del coontrolador para la prueba anterior
if __name__ == "__main__":
    a = [15 ,16 ,11 ,13 , 14]
    print("Antes de ordenar los elementos del array son: ")
    for j in a:
        print(j, end = " ")

bubble_sort(a)
print("\nDespues de ordenar los elementos del array son: ")
for j in range(len(a)):
    print("%d" % a[j], end = " ")
