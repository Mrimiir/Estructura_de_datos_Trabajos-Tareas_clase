'''
Algoritmos de ordenamiento en Python, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
Quick-sort
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 15/09/2026
'''
# funcion para hacer la particion del arreglo
def partition(a, l, h):
    # Selecciona el elemento pivote
    pvt = a[h];
    # j es el indice de los elementos que son menores que
    # pivot y tambien indica la posicion correcta del pivot encontrado hasta este momento
    j = l - 1
    # Recorre  a[l...h-1] y mueve todos los elementos menores
    # al lado izqierdo del pivote.
    # elements to te left side.
    # Los elementos de l a j son mas pequeños despes de cada iteracion
    for k in range(l, h):
        # Si el elemento actual es menor que el pivote
        if a[k] < pvt:  # recorre el arreglo
            j += 1  # compara el elemento actual con el pivote
            swap(a,j,k) # intercambia los elementos 
    # Mover el pivote despues de elementos mas pequeños y
    # devolverlo a su posicion
    swap(a, j + 1, h)    # intercambia el pivote con el elemento siguiente al ultimo elemento mas pequeño
    return j + 1 # devuelve el indice del pivote

# funcion para intercambiar dos elementos en el arreglo
def swap(a, j, k):    # intercambia los elementos
    a[j], a[k] = a[k], a[j] # intercambia los elementos

# implementacion de la funcion Quick-Sort
def qck_sort(a, l, h):    # funcion principal de Quick-sort
    if l < h:   # si el indice izquierdo es menor que el derecho
        # pi es el indice de particion, regresa el indice del pivote
        pi = partition(a, l, h)   # particiona el arreglo
        # llamadas recurisvas para los elemento menores
        # y mayores o iguales a los elementos 
        qck_sort(a, l, pi - 1)  # llamada recursiva para los elementos menores que el pivote
        qck_sort(a, pi + 1, h)  # llamada recursiva para lso elementos mayores que el pivote

# Codigo para probar la implementacion de Quick-sort
if __name__ == "__main__":  # punto de entrada del programa
    a = [10, 7, 8, 9, 1, 5]  # arreglo desordenado
    size = len(a)   # tamaño del arreglo
    print("El arreglo antes de ordenarlo: ")
    for v in a: # imprime el arreglo
        print(v, end = " ")
    print() # salto de linea
    qck_sort(a, 0, size - 1)
    print("El arreglo despues de ordenarlo: ")
    for v in a: # inprime el arreglo ordenado
        print(v, end = " ")