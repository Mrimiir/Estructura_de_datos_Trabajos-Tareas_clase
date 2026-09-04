'''
Eliminacion en Python, Programa para eliminar el ultimo elemento de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 03/09/2026
'''
#definimos array
input_arr = [11, 21, 31, 41, 51, 61]
print("Antes de la eliminación, el array es: ")
for j in range(len(input_arr)):
    print(input_arr[j], end = " ")

#Eliminando el ultimo elemento del array
input_arr.pop()        #pop() = remueve y retorna el item del indice

print("\nDespues de la eliminacion, el array es: ")
for j in range(len(input_arr)):
    print(input_arr[j], end = " ")

#Ejemplo 2
input_arr2 = [11, 21, 31, 41, 51, 61]
print("\n\nAntes de la ultima eliminacion, el array es: ")
for j in range(len(input_arr2)):
    print(input_arr2[j], end = " ")

#Eliminando el ultimo elemento del array
del input_arr2[len(input_arr2) - 1]        #del = delete
#del input_arr2[-1]  #otra forma de eliminar el ultimo elemento

print("\nDespues de la ultima eliminacion, el array es: ")
for j in range(len(input_arr2)):
    print(input_arr2[j], end = " ")