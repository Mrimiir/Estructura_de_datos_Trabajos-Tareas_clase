/*
Arrays en C++, Recorrido inverso en un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026
*/

#include <iostream>

using namespace std;
int main(){
    int input_arr [] = {5, 15, 25, 35, 45, 55};     //declaracion de arreglo estatico
    int tamano = sizeof(input_arr)/sizeof(input_arr[0]);    //declaramos variable que contiene el tamaño del arreglo

    //arreglo inverso
    cout << "El arreglo en su version inversa es: ";
    for (int i = tamano -1; i > -1; i--){
        cout << input_arr[i] << " ";
    }

    return 0;
}