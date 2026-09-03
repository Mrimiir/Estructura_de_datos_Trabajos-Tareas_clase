/*
Arrays en C#, Sintaxis básica de C# para escribir un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 02/09/2026
*/

using System;

namespace Arreglos_sintaxis
{
    class Program
    {
        static void Main(string[] args)
        {
            // Sintaxis de un array en C#
            int[] numeros = new int[5];
            int[] arreglo = { 1, 2, 3};
            int[] otro_arreglo = new int[2] { 1, 2 };

            // Asignación de valores al array
            numeros[0] = 10;
            numeros[1] = 20;
            numeros[2] = 30;
            numeros[3] = 40;
            numeros[4] = 50;

            // Impresión de los valores del array en consola
            Console.WriteLine("Valores del array:");
            for (int i = 0; i < numeros.Length; i++)
            {
                Console.WriteLine(numeros[i]);
            }


        }
    }
}