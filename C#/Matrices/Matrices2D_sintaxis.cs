/*
Matrices en C#, Sintaxis básica de C# para escribir un arreglo de 2 dimenciones.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 10/09/2026
*/

using System;

namespace Matrices2D_sintaxis
{
    class Program
    {
        static void Main(String[] args)
        {
            // Sintaxis de un arreglo bidimencional
            int[,] Two_dimensional_array = new int[,] {     // [,] = matriz rectangular
                {1,2,3},                                    // [][] = matriz de matrices
                {4,5,6},
                {7,8,9}
            };

            Console.WriteLine("Los elementos del array son: ");
            int filas = Two_dimensional_array.GetLength(0);    // número de filas, .Getlength(0) da el numero de filas
            int columnas = Two_dimensional_array.GetLength(1); // número de columnas, .Getlength(1) da el numero de columnas

            for (int i = 0; i < filas; i++)
            {
                for (int j = 0; j < columnas; j++)
                {
                    Console.Write(Two_dimensional_array[i, j] + " ");
                }
                Console.WriteLine();
            }
        }
    }
}