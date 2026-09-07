/*
Busqueda en C#, Programa para buscar un elemento en un array de manera binaria.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 06/09/2026

Nota: La busqueda binaria es un algoritmo de busqueda eficiente que requiere que el array este ordenado previamente.
*/

using System;

namespace Busqueda_binaria
{
    class Program
    {
        public static int find_elem(int[] arreglo,int l,int h,int elemento)
        {
            while (l <= h)
            {
                int mid = l + (h - l) / 2;
                if (arreglo[mid] == elemento)
                {
                    return mid;
                }
                else if (arreglo[mid] < elemento)
                {
                    l = mid + 1;
                }
                else
                {
                    h = mid - 1;
                }
            }
            return -1;
        }

        static void Main(String[] args)
        {
            int [] input_arr = {65,21,34,2,1,35,54,52,67,89};
            int elem = 54;
            int tam = input_arr.Length;

            //ordenar arreglo para la busqueda binaria
            Array.Sort(input_arr);

            int index = find_elem(input_arr, 0, tam - 1, elem);
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