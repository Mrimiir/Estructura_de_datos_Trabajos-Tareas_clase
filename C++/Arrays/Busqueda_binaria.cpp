/*
Busqueda en C++, Programa para buscar un elemento en un array de manera binaria.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026

Nota: La busqueda binaria es un algoritmo de busqueda eficiente que requiere que el array este ordenado previamente.
*/

#include <iostream>
#include <cmath>        //para poder usar trunc()
#include <algorithm>    //para utilizar sort()

int find_elem(int arreglo[], int l, int h, int elemento){
    while (l <= h){
        int mid = trunc(l + (h - 1)/2);     //truncamos el resultamo para que de un numero entero
        if (arreglo[mid] == elemento){
            return mid;
        }
        else if (arreglo[mid] < elemento){
            l = mid + 1;
        }
        else {
            h = mid - 1;
        }
    }
    return -1;
}

using namespace std;
int main(){
    int input_arr[] = {45, 86, 23, 43, 11, 28, 109, 2};
    int s = sizeof(input_arr)/sizeof(input_arr[0]);
    int elem {11};

    //ordenamiento del arreglo con funcion sort(), en este caso porque el arreglo no esta ordenado
    sort(input_arr, input_arr + s);
    
    int index = find_elem(input_arr, 0, s - 1, elem);
    if (index != -1){
        cout << "El elemento " << elem << " fue encontrado en la posicion: " << index + 1 << endl;
    }
    else{
        cout << "El elemento " << elem << " no fue encontrado en el arreglo.";
    }


    return 0;
}