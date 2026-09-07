/*
Arrays en C#,Insercion en el ultimo elemento de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026
*/

using System;

namespace Isercion_final
{
    class Program
    {
        static void Main(String[] args)
        {
            int [] input_arr = {1, 11, 21, 31, 41, 51};
            int elem = 27;
            int tam = input_arr.Length;     //tamaño del arreglo

            Console.WriteLine("Antes de la insercion, el array es: ");
            foreach (int elemento in input_arr){
            Console.WriteLine(elemento);
            }
            
            Array.Resize(ref input_arr, tam);       //redimenciono el arreglo ya existente
            input_arr[tam - 1 ] = elem;

            Console.WriteLine("Despues de la insercion, el array es: ");
            foreach (int elemento in input_arr){
            Console.WriteLine(elemento);
            }

        }
    }
}