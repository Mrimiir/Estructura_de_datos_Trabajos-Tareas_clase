/*
Arrays en C++,Insercion en el primer elemento de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026
*/

#include <iostream>
#include <vector>

using namespace std;
int main(){
    int input_arr [] = {5, 15, 25, 35, 45, 55};
    int tamano = sizeof(input_arr)/sizeof(input_arr[0]);
    int elem {77};

    cout << "Antes de la insercion, el array es: ";
    for (int elemento : input_arr){     //for each
        cout << elemento << " ";
    }

    //Nuevo arreglo
    int new_input_arr [tamano + 1];

    //Insercion
    for (int i = 1; i <= tamano; i++ ){
        new_input_arr[i] = input_arr[i-1];
    }
    new_input_arr[0] = elem;

    cout << "\nDespues de la insercion, el array es: ";
    for (int elemento : new_input_arr){
        cout << elemento << " ";
    }
    
    //otra manera seria
    vector <int> array = {5, 15, 25, 35, 45, 55};

    array.insert(array.begin() + 0, elem);          //nombredelarreglo.insert("es el inicio del arreglo" + desplazamiento, elemento a agregar)

    cout << "\n\nDespues de la insercion, el array es: ";
    for (int elemento : array){
        cout << elemento << " ";
    }

    return 0;
}