/*
Matrices en C++, Sintaxis básica de C++ para escribir un arreglo de 3 dimensiones.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 09/09/2026
*/

#include <iostream>

using namespace std;
int main(){
    // Sintaxis de un arreglo tridimencional
    int Three_dimensional_array[2][3][3] = {        //matriz [z][x][y]
            {
            {1,2,3},
            {4,5,6},
            {7,8,9}
            },
            {
            {10,11,12},
            {13,14,15},
            {16,17,18}
            }
        };

        cout << "Los elementos del array son: " << endl;
        for (auto &Two_dimensional_array : Three_dimensional_array){
            for (auto &row : Two_dimensional_array){
                for (auto element : row){
                    cout << element << " ";
                }
            }
            cout << "\n";
        }

}