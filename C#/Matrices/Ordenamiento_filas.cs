/*
Mapeo de una matriz 2D a una matriz 1D en C#, las matrices por defecto se ordenan por mediante sus filas.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 10/09/2026
*/

using System;

namespace Ordenamiento_filas
{
    class Program
    {
        static void Main(String[] args)
        {
            int r = 3, c = 3;
            int[] arr = new int[r*c];   //tamaño r*c y por defecto int inicializa todo en 0

            int[,] TwoDArr = new int[,]
            {
                {1,2,3},
                {4,5,6},
                {7,8,9}
            };

            int k = 0;
            for (int x = 0; x < r; x++)
            {
                for (int y = 0; y < c; y++)
                {
                    k = x * r + y;
                    arr[k] = TwoDArr[x,y];
                }
            }

            Console.WriteLine("Los elementos del array bidimensional son: ");
            for (int x = 0; x < r; x++)
            {
                for (int y = 0; y < c; y++)
                {
                    Console.Write(TwoDArr[x, y] + " ");
                }
                Console.WriteLine();
            }

            Console.WriteLine("Los elementos del array unidimensional son: ");
            for (int x = 0; x < r; x++){
                for (int y = 0; y < c; y++)
                {
                    Console.Write(arr[x * r + y] + " ");
                }
            }
        }
    }
}