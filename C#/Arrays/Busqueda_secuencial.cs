/*
Busqueda en C#, Programa para buscar un elemento en un array de manera secuencial.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026
*/

using System;

namespace Busqueda_secuencial
{
    class Program
    {
        public static int find_elem(int[] arreglo, int s, int elemento)
        {
            for (int i = 0; i < s; i++){
                if (arreglo[i] == elemento){
                    return i;
                }
            }
            return -1;
        }

        static void Main(String[] args)
        {
            int [] input_arr = {1, 11, 21, 31, 41, 51};
            int elem = 41;
            int tam = input_arr.Length;

            int index = find_elem(input_arr, tam, elem);
            if (index != -1)
            {
                Console.WriteLine($"El elemento {elem} fue encontrado en la posicion: {index + 1}.");
            }
            else
            {
                Console.WriteLine($"El elemento {elem} no fue encontrado en el arreglo.");
            }
        }
    }
}