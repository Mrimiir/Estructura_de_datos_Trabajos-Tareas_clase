/*
Arrays en C#, Recorrido inverso en un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026
*/

using System;

namespace Recorrido_inverso
{
    class Program
    {
        static void Main(String[] args)
        {
            int [] input_arr = {1, 11, 21, 31, 41, 51};

            Console.WriteLine("El recorrido del arreglo pero de manera inversa es: ");
            for (int i = input_arr.Length - 1; i > -1; i--)
            {
                Console.WriteLine(input_arr[i]);
            }
        }
    }
}