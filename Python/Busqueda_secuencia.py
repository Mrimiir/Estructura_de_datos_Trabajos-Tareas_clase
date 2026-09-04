'''
Busqueda en Python, Programa para buscar un elemento en un array de manera secuencial.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 03/09/2026
'''
#definimos funcion de busqueda lineal/secuencial
def find_elem(arreglo, s, elemento):
    for j in range(s):
        if (arreglo[j] == elemento):
            return j
    return -1


if __name__ == '__main__':      #iniciamos bloque de codigo principal
    #definimos un array
    input_arr = [11, 21, 31, 41, 51, 61, 45, 63, 44, 89]
    #definimos el elemento a buscar
    elem = 45
    s = len(input_arr)  #obtenemos el tamaño del array

    index = find_elem(input_arr, s, elem)  #llamamos a la funcion de busqueda
    if (index != -1):
        print(f"El elemento {elem} fue encontrado en la posicion: " + str(index + 1))        #imprime la posicion del elemento, 1 hasta n para un conteo normal(1,2,3,4...)
    else:
        print("El elemento", elem, "no fue encontrado en el arreglo.")

