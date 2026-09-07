/*
Eliminacion en C++, Eliminacion del ultimo elemento de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026
*/

#include <iostream>
#include <vector>

using namespace std;
int main(){
    int input_arr[] = {1, 11, 21, 31, 41, 51};
    int tamano = sizeof(input_arr)/sizeof(input_arr[0]);
    int index_del {tamano - 1};

    cout << "Antes de la Eliminacion, el array es: ";
    for (int elemento : input_arr){
        cout << elemento << " ";
    }
	

    //Eliminacion
    int new_input_arr [index_del];
    for (int i = 0; i < tamano; i++){
        new_input_arr[i] = input_arr[i];
    }

    cout << "\nDespues de la eliminacion, el array es: ";
    for (int elemento : new_input_arr){
        cout << elemento << " ";
    }

    //otras formas
    vector <int> arr = {1, 11, 21, 31, 41, 51};

    arr.erase(arr.begin() + index_del);     //elimina en el indice 5

    cout << "\n\nDespues de la eliminacion, el array es: ";
    for (int elemento : arr){
        cout << elemento << " ";
    }

    return 0;
}