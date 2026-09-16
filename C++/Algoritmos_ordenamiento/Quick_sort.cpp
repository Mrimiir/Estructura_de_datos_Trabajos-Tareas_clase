/*
Algoritmos de ordenamiento en C++, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
Quick-sort
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 16/09/2026
*/

#include <iostream>

using namespace std;
// funcion de intercambio de elementos / en este caso el compilador lee de arriba hasta abajo por eso es necesario que swap este arriba a comparacion de los otros lenguajes
void swap(int a[], int j, int k){
    int temp = a[j];
        a[j] = a[k];
        a[k] = temp;
}

// funcion de particion del arreglo
int partition(int a[], int l, int h){
    int pvt = a[h];     
        int j = l - 1;      //j es indice de los elemento menores que el pivote
        for (int k = l; k < h; k++){
            if ( a[k] < pvt){       //si el elemento en k es menor que el pivote
                j++;                // j incrementa en 1 / compara el elemento actual con el pivote
                swap(a, j, k);      // se realiza el intercambio entre j y k
            }
        }
        swap(a, j + 1, h);      // intercambia el pivote con el elemento siguiente al ultimo elemento mas pequeño
        return j + 1;       // devuelve el indice del pivote
}



// implementacion de la funcion de quick-sort
void qck_sort(int a[], int l, int h){
    if ( l < h){        // si el indice izquierdo es menor que el derecho
        int pi = partition(a, l, h);        // particiona el arreglo, pi es el indice del pivote
        qck_sort(a, l, pi - 1);     // llamada recursiva para los elementos menores que el pivote
        qck_sort(a, pi + 1, h);     // llamada recursiva para lso elementos mayores que el pivote
    }
}

// funcion para imprimir el arreglo
void printArr(int arr[], int s){
    for (int i = 0; i < s; i++){
        cout << arr[i] << " ";
    }
}

// Bloque principal de codigo
int main(){
    int a[] = {10, 7, 8, 9, 1, 5};
    int size = sizeof(a)/sizeof(a[0]);
    cout << "El arreglo antes de ordenarlo: " << endl;
    printArr(a, size);

    qck_sort(a, 0, size - 1);
    cout << "\nEl arreglo despues de ordenarlo: " << endl;
    printArr(a, size);


    return 0;
} 