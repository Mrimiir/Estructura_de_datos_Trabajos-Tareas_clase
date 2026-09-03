/*
Arrays en C++, Sintaxis básica de C++ para escribir un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 02/09/2026
*/
#include <iostream>

using namespace std;
int main()
{
    // Arreglos en C++
    int arreglo[5];
	
	cout << "El arreglo contiene los numeros: ";
	
    //rellenar el arreglo
    for (int i = 0; i < 5; i++)
    {
        arreglo[i] = i + 1;	//a cada bloque del arreglo le dal el valor del indice +1 ya que iniciamos desde 0 y 0+1 = 1 e iniciemos con una cuenta mas normal
        cout << arreglo[i] << " ";		//imprime lo que hay en el arreglo
    }

    return 0;
}