/*
Algoritmos de ordenamiento en Java, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 10/09/2026

Nota: Para algoritmos de busqueda  como la busqueda binaria es necesario tener ordenado el arreglo,
pero en alguno casos este no esta ordenado y estos algoritmos de ordenamiento resuelven ese problema
*/

public class Insertion_sort {
    //funcion de ordenamiento 
    public static void insertion_sort(int[] a){
        for (int i = 1; i < a.length; i++){
            int temp = a[i];
            int j = i - 1;
            while (j >= 0 && temp < a[j]){
            a[j + 1] = a[j];
            j = j-1;
        }
        a[j + 1] = temp;
        }
    }
    //funcion de impresion de arreglo
    public static void printArr(int[] a){
        for (int elem : a){
            System.out.print(elem + " ");
        }
    }

    public static void main(String[] args){
        int[] a = {50,38,11,28,44,19,9,36,26,12};
        System.out.println("Antes de ordenar los elementos del array son: ");
        printArr(a);

        insertion_sort(a);
        System.out.println("\nDespues de ordenar los elementos del array son: ");
        printArr(a);
    }
}
