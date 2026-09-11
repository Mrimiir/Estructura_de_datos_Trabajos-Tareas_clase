/*
Algoritmos de ordenamiento en C#, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 10/09/2026
*/

using System;

namespace Insertion_sort
{
    class Program
    {
        // Funcion de ordenamiento por insercion
        public static void Insertion_sort(int[] a)
        {
            for(int i = 1; i < a.Length; i++)
            {
                int temp = a[i];
                int j = i - 1;
                while (j >= 0 && temp < a[j]){
                    a[j + 1] = a[j];
                    j --;               // lo hice 4 veces y no se me ocurrio poner j-- enves de j = j - 1
                }
                a[j + 1] = temp;
            }
        }

    //funcion de impresion de arreglo
    public static void PrintArr(int[] a){
        foreach (int elem in a){
            Console.Write(elem + " ");
        }
    }

        // Bloque principal
        public static void Main(String[] args)
        {
            int[] a = {50,38,11,28,44,19,9,36,26,12};

            Console.WriteLine("Antes de ordenar los elementos del array son: ");
            PrintArr(a);

            Insertion_sort(a);
            Console.WriteLine("\nDespues de ordenar los elementos del array son: ");
            PrintArr(a);
        }
    }
}