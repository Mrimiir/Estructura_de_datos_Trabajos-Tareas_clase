''' 
Arrays en Python, Inserción de un elemento al inicio del array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 03/09/2026
'''

#Declaro mi arreglo
input_arr = [11, 21, 31, 41, 51]
input_arr2 = [11, 21, 31, 41, 51]
elem = 1

input_arr.insert(0, elem)  # Inserta el elemento 1 al inicio del arreglo
for i in range(len(input_arr)):
    print(input_arr[i], end = " ")  

#otra forma de insertar otro elemento al inicio sin modificar el tamaño original
for i in range(len(input_arr2) - 1, -1, -1):
    input_arr2[i] = input_arr2[i - 1]  # Desplaza los elementos hacia la derecha
input_arr2[0] = elem  # Inserta el elemento 1 al inicio del arreglo
print("\n")
for i in range(len(input_arr2)):
    print(input_arr2[i], end = " ")