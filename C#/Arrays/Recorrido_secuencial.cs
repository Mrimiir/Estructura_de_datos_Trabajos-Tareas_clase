/*
Arrays en C#, Recorrido secuencial por un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026
*/

using System;

namespace Recorrido_secuencial
{
    class Program
    {
        static void Main(String[] args)
        {
            int [] input_arr = {1, 11, 21, 31, 41, 51};

            Console.WriteLine("Recorrido del arreglos secuancialmente: ");
            for (int i = 0; i < input_arr.Length; i++)
            {
                Console.WriteLine(input_arr[i] + " ");
            }
        }
    }
}