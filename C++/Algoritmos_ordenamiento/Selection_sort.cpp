/*
Algoritmos de ordenamiento en C++, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
Selection-sort
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 15/09/2026
*/

#include <iostream>

using namespace std;
void selection_sort(int arr[], int s){
    for (int i = 0; i < s; i++){
        int small = i;
        for (int j = i+1; j < s; j++){
            if (arr[small] > arr[j]){
                small = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[small];
        arr[small] = temp;
    }
}

void printArr(int arr[], int s){
    for (int i = 0; i < s; i++){
        cout << arr[i] << " ";
    }
}


int main(){
    int a[]= {65,26,13,23,12};
    int s = sizeof(a)/sizeof(a[0]);
    cout << "Arreglo antes de ser ordenado: " << endl;
    printArr(a, s);
    selection_sort(a, s);
    cout << "\nArreglo despues de ser ordenado: " << endl;
    selection_sort(a,s);
    printArr(a,s);


    return 0;
}