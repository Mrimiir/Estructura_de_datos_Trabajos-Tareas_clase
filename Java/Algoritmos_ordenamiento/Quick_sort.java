/*
Algoritmos de ordenamiento en Java, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
Quick-sort
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 16/09/2026
*/

public class Quick_sort{
    //funcion para hacer la particion del arreglo
    public static int partition(int[] a, int l, int h){
        int pvt = a[h];     //Pivote a utilizar puede ser el primer elemento, el del medio o el ultimo en este caso sera el ultimo
        int j = l - 1;      //j es indice de los elemento menores que el pivote
        for (int k = l; k < h; k++){
            if ( a[k] < pvt){       //si el elemento en k es menor que el pivote
                j++;                // j incrementa en 1 / compara el elemento actual con el pivote
                swap(a, j, k);      // se realiza el intercambio entre j y k
            }
        }
        swap(a, j + 1, h);      // intercambia el pivote con el elemento siguiente al ultimo elemento mas pequeño
        return j + 1;       // devuelve el indice del pivote
    }

    // funcion de intercambio
    public static void swap(int[] a, int j, int k){
        int temp = a[j];
        a[j] = a[k];
        a[k] = temp;
    }

    // implementacion de la funcion quick-sort
    public static void qck_sort(int[] a,int l,int h){
        if ( l < h){        // si el indice izquierdo es menor que el derecho
            int pi = partition(a, l, h);        // particiona el arreglo, pi es el indice del pivote
            qck_sort(a, l, pi - 1);     // llamada recursiva para los elementos menores que el pivote
            qck_sort(a, pi + 1, h);     // llamada recursiva para lso elementos mayores que el pivote
        }
    }

    //funcion de impresion de arreglo
    public static void printArr(int[] a){
        for (int elem : a){
            System.out.print(elem + " ");
        }
    }

    // Bloque principal de codigo
    public static void main(String[] args){
        int[] a = {10, 7, 8, 9, 1, 5};
        int size = a.length;
        System.out.println("El arreglo antes de ordenarlo: ");
        printArr(a);

        qck_sort(a, 0, size - 1);
        System.out.println("\nEl elemento despues de ordenalo: ");
        printArr(a);
    }
}