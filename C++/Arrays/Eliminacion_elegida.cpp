/*
Eliminacion en C++, Eliminacion de un elemento elegido de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026
*/

#include <iostream>
#include <vector>

using namespace std;
int main(){
    vector <int> input_arr = {1, 11, 21, 31, 41, 51};
    int tamano = sizeof(input_arr)/sizeof(input_arr[0]);
    int index_del {4};

    cout << "Antes de la Eliminacion, el array es: ";
    for (int elemento : input_arr){
        cout << elemento << " ";
    }

    //Eliminacion
    input_arr.erase(input_arr.begin() + index_del);     //elimina en el indice elegido

    cout << "\n\nDespues de la eliminacion, el array es: ";
    for (int elemento : input_arr){
        cout << elemento << " ";
    }

    return 0;
}