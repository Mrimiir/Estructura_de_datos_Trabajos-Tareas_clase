'''
Eliminacion en Python, Programa para eliminar un elemento elegido de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 03/09/2026
'''

#definimos un array
input_arr = [11, 21, 31, 41, 51, 61]
elem = 31
index_elem = 4 #51

print("Antes de la eliminación, el array es: ")
for j in range(len(input_arr)):
    print(input_arr[j], end = " ")

#Eliminando el elemento elegido del array

input_arr.remove(elem)        #remove() = remueve la primera ocurrencia del elemento
#del input_arr[index_elem]    #del = delete

print("\nDespues de la eliminacion, el array es: ")
for j in range(len(input_arr)):
    print(input_arr[j], end = " ")

#ejemplo 2
input_arr2 = [11, 21, 31, 41, 51, 61]
print("\n\nAntes de la eliminacion, el array es: ")
for j in range(len(input_arr2)):
    print(input_arr2[j], end = " ")

#Eliminando el elemento elegido del array
for j in range(len(input_arr2)):
    if input_arr2[j] == elem:       #busca el elemento del index_elem y al ser igual al j este es eliminado en al arreglo
        del input_arr2[j]
        break

print("\nDespues de la eliminacion, el array es: ")
for j in range(len(input_arr2)):
    print(input_arr2[j], end = " ")