/*
Mapeo de una matriz 2D a una matriz 1D en C++, las matrices por defecto se ordenan por mediante sus filas.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 09/09/2026
*/

#include <iostream>
#include <vector>

using namespace std;
int main(){
    int r {3}, c {3};
    vector<int> arr (r * c, 0);     //crea un arreglo unidimencional con r*c elemento, todos inicializados en 0
    int TwoDArr[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    int k {0};
    for (int x = 0; x < r; x++){
        for (int y = 0; y < c; y++){
            k = x * r + y;
            arr[k] = TwoDArr[x][y];
        }
    }

    cout << "Los elementos del array bidimensional son: " << endl;
    for (auto &row : TwoDArr){
        for (auto elem : row){
            cout << elem << " ";
        }
        cout << "\n";
    }
    cout << "\nLos elementos del array unidimensional son: " << endl;
    for (int x = 0; x < r; x++){
        for (int y = 0; y < c; y++){
            cout << arr[x * r + y] << " ";
        }
    }
}