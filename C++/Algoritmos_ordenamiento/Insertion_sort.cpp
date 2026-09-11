/*
Algoritmos de ordenamiento en C++, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 10/09/2026
*/

#include <iostream>
using namespace std;

void insert_sort(int a[],int s){
    for (int i = 1; i < s; i++){            // inicia desde el indice 1, y lo guarda en una variable temporal
        int temp = a[i];
        int j = i - 1;                  // j sera el indice anterior a i
        while (j >= 0 && temp < a[j]){  //si j es mayor o igual a 0 y temp es menor que elemento en indice j
            a[j + 1] = a[j];                //elemento en el indice j + 1 sera igual al del indice j
            j = j-1;                        // j se reduce en 1
        }
        a[j + 1] = temp;        // Ahora el elemento en j + 1 se almacenara en temp
    }
}
//imprime el arreglo
void printArr(int a[], int s){
    for (int i = 0; i < s; i++){
        cout << a[i] << " ";
    }
}

int main(){
    int a[] = {50,38,11,28,44,19,9,36,26,12};
    int s = sizeof(a)/sizeof(a[0]);
    
    cout << "Antes de ordenar los elementos del array son: " << endl;
    printArr(a, s);

    insert_sort(a,s);
    cout << "\nDespues de ordenar los elementos del array son: " << endl;
    printArr(a,s);

    return 0;
}