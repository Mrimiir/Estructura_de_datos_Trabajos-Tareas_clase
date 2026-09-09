/*
Matrices en Java, Sintaxis básica de Java para escribir un arreglo de 2 dimenciones.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 08/09/2026
*/

public class Matrices2D_sintaxis{
    public static void main(String[] args){
        // Sintaxis de un arreglo bidimencional
        int[][] Two_dimensional_array = new int[][] {
            {1,2,3},
            {4,5,6},
            {7,8,9}
        };

        /*int tam = Two_dimensional_array.length;
        String end = " ";*/

        System.out.println("Los elementos del array son: ");
        for (int[] row : Two_dimensional_array){        //For-each para java
            for (int element : row){
                System.out.print(element + " ");        //println da un salto de linea, print no
            }
            System.out.println();
        }

    }
}