/*
Arrays en C++,Insercion en el ultimo elemento de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026
*/

#include <iostream>
#include <vector>

using namespace std;
int main()
{
    int input_arr[] = {1, 11, 21, 31, 41, 51};
    int tamano = sizeof(input_arr)/sizeof(input_arr[0]);
    int elem {61};

    cout << "Antes de la insercion, el array es: ";
    for (int elemento : input_arr){
        cout << elemento << " ";
    }

        //Nuevo arreglo
    int new_input_arr [tamano + 1];

    //Insercion
    for (int i = 0; i <= tamano; i++ ){
        new_input_arr[i] = input_arr[i];
    }
    new_input_arr[tamano] = elem;

    cout << "\nDespues de la insercion, el array es: ";
    for (int elemento : new_input_arr){
        cout << elemento << " ";
    }


    //Otra forma
    vector <int> other_arr = {1, 11, 21, 31, 41, 51};

    other_arr.insert(other_arr.begin() + tamano, elem);
    cout << "\n\nDespues de la insercion, el array es: ";
    for (int elemento : other_arr){
        cout << elemento << " ";
    }
    return 0;
}