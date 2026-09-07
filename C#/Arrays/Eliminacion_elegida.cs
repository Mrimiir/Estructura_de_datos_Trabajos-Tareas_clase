/*
Eliminacion en C#, Eliminacion de un elemento elegido de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026
*/

using System;
using System.Linq;

namespace Eliminacion_elegida
{
    class Program
    {
        static void Main(String[] args)
        {
            int [] input_arr = {1, 11, 21, 31, 41, 51};
            int elem = input_arr[3];

            Console.WriteLine("Antes de la eliminacion, el array es: ");
            foreach (int elemento in input_arr){
            Console.WriteLine(elemento);
            }

            input_arr = input_arr.Where(n => n != elem).ToArray();        //arreglo = arreglo.where(n(n= elemento) => elemento != elemento a borrar).toArray()
            //se modifica el arreglo 

            Console.WriteLine("Despues de la eliminacion, el array es: ");
            foreach (int elemento in input_arr){
            Console.WriteLine(elemento);
            }
        }
    }
}