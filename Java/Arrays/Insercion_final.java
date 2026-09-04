/*
Arrays en Java,Insercion en el ultimo elemento de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 04/09/2026
*/

import java.util.Arrays;

public class Insercion_final {
    public static void main(String[] args){
        int[] input_arr = {11, 21, 31, 41, 51, 61};     //array estatico

        System.out.println("Antes de la insercion, el array es: ");

        for (int elemento : input_arr){
            System.out.println(elemento);
        }
        System.out.println("\nDespues de la insercion, el array es: ");

        int[] new_input_arr = Arrays.copyOf(input_arr, input_arr.length + 1);       //otra forma de copiar un arreglo estatico
        new_input_arr[input_arr.length] = 67;       //agregamos el elemento final en el ultimo indice

        for (int elemento : new_input_arr){
            System.out.println(elemento);
        }
    }
}   
