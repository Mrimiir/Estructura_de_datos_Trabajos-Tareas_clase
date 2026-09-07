/*
Eliminacion en Java, Eliminacion del ultimo elemento de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 04/09/2026
*/

using System;
using System.Linq;

namespace Eliminacion_final
{
    class Program
    {
        static void Main(String[] args)
        {
            int [] input_arr = {1, 11, 21, 31, 41, 51};
            int tam = input_arr.Length;

            Console.WriteLine("Antes de la eliminacion, el array es: ");
            foreach (int elemento in input_arr){
            Console.WriteLine(elemento);
            }

            input_arr = input_arr.Where((n,i) => i != tam -1).ToArray();        //arreglo = arreglo.where((n, i = indice), => indice != indice del elemento a borrar).toArray()
            //se modifica el arreglo 

            Console.WriteLine("Despues de la eliminacion, el array es: ");
            foreach (int elemento in input_arr){
            Console.WriteLine(elemento);
            }

        }
    }
}