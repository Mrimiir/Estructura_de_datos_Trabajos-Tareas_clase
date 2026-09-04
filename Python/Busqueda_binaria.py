'''
Busqueda en Python, Programa para buscar un elemento en un array de manera binaria.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 03/09/2026

Nota: La busqueda binaria es un algoritmo de busqueda eficiente que requiere que el array este ordenado previamente.
'''

def find_elem(arreglo, l, h, elemento):
    while l <= h:       #mientras el limite inferior sea menor o igual al limite superior
        mid = l + (h - l) // 2  # Calcula el índice del elemento medio
        if arreglo[mid] == elemento:        # Verifica si el elemento está presente en el medio
            return mid                      # Elemento encontrado, devuelve el índice
        elif arreglo[mid] < elemento:       # Si el elemento es mayor que el medio, ignora la mitad izquierda
            l = mid + 1
        else:
            h = mid - 1         # Si el elemento es menor que el medio, ignora la mitad derecha
        #si el control llega hasta este punto significa que el elemento no se encuentra en el arreglo
    return -1

if __name__ == '__main__':
    #definimos un arreglo
    input_arr = [11, 21, 31, 41, 51, 61, 45, 63, 44, 89]
    elem = 63
    s = len(input_arr)  #obtenemos el tamaño del arreglo

    #si el arreglo no esta ordenado, se ordena como en este caso
    input_arr.sort()  # Ordena el arreglo de manera ascendente

    print()

    #operacion de busqueda
    index = find_elem(input_arr, 0, s - 1, elem)  #llamamos a la funcion de busqueda
    if (index != -1):
        print("El elemento", elem, "fue encontrado en la posicion: " + str(index + 1))        #imprime la posicion del elemento, 1 hasta n para un conteo normal(1,2,3,4...)
    else:
        print("El elemento", elem, "no fue encontrado en el arreglo.")