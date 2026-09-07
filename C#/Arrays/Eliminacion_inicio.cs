/*
Eliminacion en C#, Eliminacion del primer elemento de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026
*/

using System;

namespace Eliminacion_inicio
{
    class Program
    {
        static void Main(String[] args)
        {
            int [] input_arr = {1, 11, 21, 31, 41, 51};
            int tam = input_arr.Length;
            int [] new_array = new int[tam - 1];        //nuevo arreglo que contendra lo elementos del otro arreglo exeptuando a uno

            Console.WriteLine("Antes de la eliminacion, el array es: ");
            foreach (int elemento in input_arr){
            Console.WriteLine(elemento);
            }

            for( int j = 0; j < tam - 1; j++)
            {
                new_array[j] = input_arr[j + 1]; 
            }

            Console.WriteLine("Despues de la eliminacion, el array es: ");
            foreach (int elemento in new_array){
            Console.WriteLine(elemento);
            }

        }
    }
}