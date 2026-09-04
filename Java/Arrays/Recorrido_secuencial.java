/*
Arrays en Java, Recorrido secuencial por un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 04/09/2026
*/

public class Recorrido_secuencial {
    public static void main (String [] args){
        int[] input_arr = {11, 21, 31, 41, 51, 61};

        System.out.println("Los elementos del arreglo son los siguientes: ");

        //Ciclo for each, es el bucle for mejorado
        for(int elemento : input_arr){
            System.out.println(elemento);
        }
    }
}
