''' 
Arrays en Python, Sintaxis básica de Python para escribir un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 02/09/2026

*Nota: En Python, los arrays se implementan como listas, que son estructuras de datos dinámicas y flexibles. 
A diferencia de los arrays en otros lenguajes de programación, las listas en Python pueden contener elementos de diferentes tipos
y su tamaño puede cambiar durante la ejecución del programa.
'''

# LISTAS / ARREGLOS
my_array = [1,2,3,4,5]  #sintaxis para una lista

#Accediendo a elementos de la lista
print("El primer elemento de la lista es:", my_array[0])  #Accediendo al elemento de manera directa

print("La lista completa es: ", my_array) #imprime la lista completa

#Metodos que tiene python para manipular listas
# Agregar
my_array.append(9)          # -> [1, 2, 3, 4, 5, 9]
my_array.insert(0, 0)       # -> [0, 1, 2, 3, 4, 5, 9]
my_array.extend([2, 7])     # -> [0, 1, 2, 3, 4, 5, 9, 2, 7]

# Buscar
my_array.index(4)           # -> 3 (índice del primer 4)
my_array.count(1)           # -> 2 (aparece dos veces)

# Eliminar
my_array.remove(1)          # elimina la primera ocurrencia de 1
my_array.pop()              # elimina y devuelve el último
my_array.pop(0)             # elimina y devuelve el del índice 0
my_array.clear()            # vacía toda la lista

# Ordenar / Reordenar
my_array.sort()             # ordena in-place (ascendente)
my_array.sort(reverse=True) # ordena descendente
my_array.reverse()          # invierte el orden


#Funciones
len(my_array)    # -> 5  (longitud)
sum(my_array)    # -> 15 (suma)
sorted(my_array) # -> [1, 2, 3, 4, 5] (devuelve lista nueva ordenada) / Ya estaba ordenada
#hay mas pero esta son las mas comunes
