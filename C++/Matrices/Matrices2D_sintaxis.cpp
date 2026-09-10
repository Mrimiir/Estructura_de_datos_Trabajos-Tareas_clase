/*
Matrices en C++, Sintaxis básica de C++ para escribir un arreglo de 2 dimenciones.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 09/09/2026
*/

#include <iostream>

using namespace std;
int main(){
    // Sintaxis de un arreglo bidimencional matriz 3x3
    int Two_dimencional_array[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    cout << "Los elementos del array son: " << endl;
    for (auto &row : Two_dimencional_array){        //for-each en c++, para que la variable sea modificable se utiliza "auto" y se le agrega "&" a la variable para que funcione e inicialice
        for (auto element : row){
            cout << element << " ";
        }
        cout << "\n";
    }
}