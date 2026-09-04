/*
Busqueda en Java, Programa para buscar un elemento en un array de manera binaria.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 04/09/2026

Nota: La busqueda binaria es un algoritmo de busqueda eficiente que requiere que el array este ordenado previamente.
*/

import java.util.Arrays;    //funcion que nos dejara usar el sort()

public class Busqueda_binaria {
    //Funcion de busqueda
    public static int find_elem(int[] arreglo, int l, int h, int elemento){
        while (l <= h){
            int mid = (int) l + (h - 1) /2;
            if (arreglo[mid] == elemento){      // Verifica si el elemento está presente en el medio
            return mid;                      // Elemento encontrado, devuelve el índice
        }
        else if (arreglo[mid] < elemento){     // Si el elemento es mayor que el medio, ignora la mitad izquierda
            l = mid + 1;
        }
        else{
            h = mid - 1;         //Si el elemento es menor que el medio, ignora la mitad derecha
        }
        //si el control llega hasta este punto significa que el elemento no se encuentra en el arreglo
        }
        return -1;
    }

    public static void main(){
        //declaramos elementos a usar
        int[] input_arr = {11, 43, 13, 24, 45, 32, 51, 76, 67, 89, 1}; 
        int elem = 13;
        int s = input_arr.length;

        //ordena el arreglo porque en este caso es necesario
        Arrays.sort(input_arr);

        int index = find_elem(input_arr, 0, s - 1, elem);
            if (index != -1){
                System.out.printf("El elemento %d fue encontrado en la posicion: %d.%n", elem, index + 1 );
            }
            else{
            System.out.printf("El elemento %d no fue encontrado en el arreglo %n", elem);
            }
    }
}
