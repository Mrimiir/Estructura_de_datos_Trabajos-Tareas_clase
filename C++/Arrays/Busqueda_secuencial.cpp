/*
Busqueda en C++, Programa para buscar un elemento en un array de manera secuencial.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026
*/

#include <iostream>
//declaramos funcion de busqueda
int find_elem(int arreglo[],int s, int elemento){
    for (int i = 0; i < s; i++){
        if (arreglo[i] == elemento){
            return i;
        }
    }
    return -1;
}

using namespace std;
int main(){
    int input_arr[] = {1, 11, 21, 31, 41, 51};
    int s = sizeof(input_arr)/sizeof(input_arr[0]);
    int elem {21};

    int index = find_elem(input_arr, s, elem);
    if (index != -1){
        cout << "El elemento " << elem << " fue encontrado en la posicion: " << index + 1 << endl;
    }
    else{
        cout << "El elemento " << elem << " no fue encontrado en el arreglo.";
    }
    return 0;
}