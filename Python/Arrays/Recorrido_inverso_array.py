''' 
Arrays en Python, Recorrido inverso por un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 03/09/2026
'''

#Declaro mi arreglo
input_arr = [11, 21, 31, 41, 51]

#Recorrido inverso por el arreglo
for i in range(len(input_arr) - 1, -1, -1):         #para i en rango de longitud del arreglo - 1 hasta -1, con paso -1 / i en rango(5 - 1{4 indice maximo}, -1{hasta -1}, -1{decreciendo 1}) -> i en rango(4, -1, -1) -> i = 4, 3, 2, 1, 0
    print("Elemento en el índice", i, "es:", input_arr[i])

print(" ")

#Funcion reversed() para recorrer el arreglo en orden inverso
for elemento in reversed(input_arr):                 #para cada elemento en el arreglo invertido
    print("Elemento:", elemento)                      #imprime el elemento