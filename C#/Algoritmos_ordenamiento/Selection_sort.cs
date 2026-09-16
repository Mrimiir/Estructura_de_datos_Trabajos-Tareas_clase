/*
Algoritmos de ordenamiento en C#, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
Selection-sort
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 15/09/2026
*/

using System;
namespace Selection_sort
{
    class Program
    {
        public static void selection_sort(int[] a)
        {
            for(int i = 0; i < a.Length; i++)
            {
                int small = i;
                for (int j = i + 1; j < a.Length; j++)
                {
                    if (a[small] > a[j])
                    {
                        small = j;
                    }
                }
                int temp = a[i];
                a[i] = a[small];
                a[small] = temp;
            }
        }

        public static void printArr(int[] a)
        {
            foreach (int elemt in a)
            {
                Console.Write(elemt + " ");
            }
        }

        public static void Main(String[] args)
        {
            int[] a = {65,26,13,23,12};
            Console.WriteLine("Arreglo antes de ser ordenado: ");
            printArr(a);
            selection_sort(a);
            Console.WriteLine("\nArreglo despues de ser ordenado: ");
            selection_sort(a);
            printArr(a);
        }
    }
}