/*
Matrices en C#, Sintaxis básica de C# para escribir un arreglo de 3 dimensiones.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 10/09/2026
*/

using System;


namespace Matrices3D_sintaxis
{
    class Program
    {
        static void Main(String[] args)
        {
            int[, ,] Three_dimencional_array = new int[, ,]     // [z, x , y] = cubo
            {
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

            Console.WriteLine("Los elementos del array son: ");
            int capas = Three_dimencional_array.GetLength(0);    // número de capas, .Getlength(0) da el numero de capas = z
            int filas = Three_dimencional_array.GetLength(1); // número de filas, .Getlength(1) da el numero de filas    = x
            int columnas = Three_dimencional_array.GetLength(2); // número de columnas, .Getlength(2) da el numero de columnas = y

            for (int i = 0; i < capas; i++)
            {
                for (int j = 0; j < filas; j++)
                {
                    for (int k = 0; k < columnas; k++)
                    {
                        Console.Write(Three_dimencional_array[i, j, k] + " ");
                    }
                }
                Console.WriteLine();
            }
            Console.WriteLine();
        }
    }
}