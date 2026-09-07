/*
Arrays en C#,Insercion en el primer elemento de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026
*/

using System;

namespace Insercion_inicio
{
    class Program
    {
        static void Main(String[] args)
        {
            int [] input_arr = {1, 11, 21, 31, 41, 51};
            int elem = 27;

            Console.WriteLine("Antes de la insercion, el array es: ");
            foreach (int elemento in input_arr){
            Console.WriteLine(elemento);
            }

            int[] new_array = new int[input_arr.Length + 1];        //se creo un nuevo arreglo
            new_array[0] = elem;

            input_arr.CopyTo(new_array, 1);

            Console.WriteLine("Despues de la insercion, el array es: ");
            foreach (int elemento in new_array){
            Console.WriteLine(elemento);
            }


        }
    }
}