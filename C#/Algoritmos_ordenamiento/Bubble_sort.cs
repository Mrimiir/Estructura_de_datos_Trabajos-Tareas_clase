/*Algoritmos de ordenamiento en C#, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 10/09/2026
*/

using System;

namespace Bubble_sort{
    class Program{
        // Funcion de ordenamiento
        public static void Bubble_sort(int[] a){
            int s = a.Length;
            for (int i = 0; i < s; i++)
            {
                bool isSwapped = false;
                for (int j = 0; j < s - i - 1 ; j++)
                {
                    if (a[j] > a[j + 1])
                    {
                        int temp = a[j];
                        a[j] = a[j + 1];
                        a[j + 1] = temp;
                        isSwapped = true;
                    }
                }
                if (isSwapped == false)
                {
                    break;
                }
            }
        }

        //funcion de impresion de arreglo
    public static void PrintArr(int[] a){
        foreach (int elem in a){
            Console.Write(elem + " ");
        }
    }

        //bloque principal
        public static void Main(String[] args){
            int[] a = {46,7,7,18,38,7,39,48,32,26};

            Console.WriteLine("Antes de ordenar los elementos del array son: ");
            PrintArr(a);

            Bubble_sort(a);
            Console.WriteLine("\nDespues de ordenar los elementos del array son: ");
            PrintArr(a);

        }
    }
}