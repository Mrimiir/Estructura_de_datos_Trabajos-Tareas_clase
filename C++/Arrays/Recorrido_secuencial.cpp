/*
Arrays en C++, Recorrido secuencial por un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026

Nota: g++ archivo.cpp -o nombre_del_archivo.exe
        ./nombre_del_archivo.exe
*/

#include <iostream>
#include <stdlib.h>

using namespace std;
int main(){
    int input_arr [] = {5, 15, 25, 35, 45, 55};     //declaracion de arreglo
    int tamano = sizeof(input_arr)/sizeof(input_arr[0]);    //declaramos variable que contiene el tamaño del arreglo

    cout << "El recorrido del arreglo es el siguiente: " << endl;
    for ( int i = 0; i < tamano; i++){
        cout << input_arr[i] << " ";
    }

    system("pause");
    return 0;
}