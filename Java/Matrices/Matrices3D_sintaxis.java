/*
Matrices en Java, Sintaxis básica de Javas para escribir un arreglo de 3 dimensiones.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 08/09/2026
*/

public class Matrices3D_sintaxis{
    public static void main(String[] args){
        // Sintaxis de un arreglo tridimencional
        int[][][] Three_dimensional_array = new int[][][] {
            {
            {1,2,3},
            {4,5,6},
            {7,8,9}
            },
            {
            {10,11,12},
            {13,14,15},
            {16,17,18}
            }
        };

        System.out.println("Los elementos del array son: ");
        for (int[][] Two_dimensional_array : Three_dimensional_array){
            for (int[] row : Two_dimensional_array){
                for (int element : row){
                    System.out.print(element + " ");
                }        
            }
            System.out.println();
        }


    }
    
}