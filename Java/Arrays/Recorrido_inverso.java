/*
Arrays en Java, Recorrido inverso en un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 04/09/2026
*/

public class Recorrido_inverso {
    public static void main(String[] args){
        int[] input_arr = {11, 21, 31, 41, 51, 61};

        System.out.println("Los elementos del ultimo al primero son los siguientes: ");

        for(int i = input_arr.length - 1; i > -1; i--){
            System.out.println(input_arr[i]);
        }
    }
}
