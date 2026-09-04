/*
Eliminacion en Java, Eliminacion de un elemento elegido de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 04/09/2026
*/
import java.util.Arrays;

public class Eliminacion_elegida {
    public static void main(String[] args){
        int[] input_arr = {11, 21, 31, 41, 51, 61};     //array estatico
        int index_del = 3;      //indice a elminar
        
        //imprimimos arreglo sin cambios
        System.out.println("Antes de la eliminacion, el array es: ");
        for (int elemento : input_arr){
            System.out.println(elemento);
        }

        //Eliminacion del primer elemento
        int[] new_arr = new int[input_arr.length - 1];

        System.arraycopy(input_arr, 0, new_arr, 0, index_del);
        System.arraycopy(input_arr, index_del + 1, new_arr, index_del, input_arr.length - index_del - 1);
        
        System.out.println("Despue de la eliminacion, el array es: " + Arrays.toString(new_arr));       //otra forma de imprimir pero devuelve un string
    }
}
