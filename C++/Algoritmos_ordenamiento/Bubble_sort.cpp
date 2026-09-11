/*
Algoritmos de ordenamiento en C++, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 10/09/2026

Nota: Para algoritmos de busqueda  como la busqueda binaria es necesario tener ordenado el arreglo,
pero en alguno casos este no esta ordenado y estos algoritmos de ordenamiento resuelven ese problema
*/

#include <iostream>
using namespace std;
void bubble_sort(int arr[], int s){
    for (int j = 0; j < s; j++){
        bool isSwapped = false;
        for (int i = 0; i < s - j - 1; i++){
            if (arr[i] > arr[i + 1]){
                int temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                isSwapped = true;
            }
        }
        if (!isSwapped){        //isSwapped == false
            break;
        }
    }
}

void printArr(int arr[], int s)
{
    for (int i = 0; i < s; i++){
        cout << arr[i] << " ";
    }
}

int main(){
    int a[] = {46,7,7,18,38,7,39,48,32,26};
    int s = sizeof(a)/sizeof(a[0]);
    
    cout << "Antes de ordenar los elementos del array son: " << endl;
    printArr(a, s);

    bubble_sort(a,s);
    cout << "\nDespues de ordenar los elementos del array son: " << endl;
    printArr(a,s);

    return 0;
}