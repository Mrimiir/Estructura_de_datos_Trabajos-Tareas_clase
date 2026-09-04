''' 
Arrays en Python, Inserción de un elemento al final del array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 03/09/2026
'''
#Declaro mi arreglo
input_arr = [11, 21, 31, 41, 51]
elem = 61

# Inserción de un elemento al final del arreglo
input_arr.append(elem)  # Inserta el elemento 61 al final del arreglo

for i in range(len(input_arr)):
    print(input_arr[i], end = " ")