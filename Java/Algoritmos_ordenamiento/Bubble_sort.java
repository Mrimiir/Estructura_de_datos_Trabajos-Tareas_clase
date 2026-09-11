/*
Algoritmos de ordenamiento en Java, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 10/09/2026

Nota: Para algoritmos de busqueda  como la busqueda binaria es necesario tener ordenado el arreglo,
pero en alguno casos este no esta ordenado y estos algoritmos de ordenamiento resuelven ese problema
*/

public class Bubble_sort{
    //funcion de ordenamiento 
    public static void bubble_sort(int[] a){
        int s = a.length;
        for (int i = 0; i < s; i++){
        boolean isSwapped = false;                      //declara que no hubo ningun cambio
        for (int j = 0; j < (s - i - 1);j++){       //si en el indice j el elemento es mayor que lo del indice j+1 se intercambian estas posiciones
            if (a[j] > a[j + 1]){
                int temp = a[j];                    //utilizamos una variable temporal para almacenar los elementos
                a[j] = a[j + 1];
                a[j + 1] = temp;
                isSwapped = true;                   //declara si el cambio se llevo a cabo
            }
        }
        if ( isSwapped == false){
            break;                      //sale de la funcion si no hubo algun cambio
        }
        }
    }
    //funcion de impresion de arreglo
    public static void printArr(int[] a){
        for (int elem : a){
            System.out.print(elem + " ");
        }
    }

    public static void main(String[] args) {
        int[] a = {46,7,7,18,38,7,39,48,32,26};
        System.out.println("Antes de ordenar los elementos del array son: ");
        printArr(a);

        bubble_sort(a);
        System.out.println("\nDespues de ordenar los elementos del array son: ");
        printArr(a);
    }
}