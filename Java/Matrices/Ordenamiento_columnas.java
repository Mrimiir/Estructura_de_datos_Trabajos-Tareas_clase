/*
Mapeo de una matriz 2D a una matriz 1D en Java, las matrices por defecto se ordenan por mediante sus columnas.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 09/09/2026
*/

import java.util.Arrays;

public class Ordenamiento_columnas {
    public static void main(String[] args){
        final int r = 3, c = 3;     // final hace que las variables sean constantes y no cambien el valor
        int[] arr = new int[r*c];
        Arrays.fill(arr, 0);    //inicializa el arreglo

        int[][] TwoDArr = {     //matriz con elementos
            {1,2,3},
            {4,5,6},
            {7,8,9}
        };

        int k = 0;
        for (int y = 0; y < c; y++){            //intercambias las "y" por las "x" a comparacion con el ordenamiento por filas, para asi al imprimir devuelva por columnas
            for (int x = 0; x < r; x++){
                k = y * r + x;
                arr[k] = TwoDArr[x][y];
            }
        }

        System.out.println("Los elementos del array bidimensional son: ");
        for (int[] row : TwoDArr) {
            StringBuilder linea = new StringBuilder();
            for (int ele : row) {
                linea.append(ele).append(" ");   // Mostrar los elementos de la fila separados por espacios / append() le agrega lo que esta dentro de los "()""
            }
            System.out.println(linea.toString());       //.toString() vuelve la variable en un string
        }

        System.out.println("\nLos elementos del array unidimensional son: ");
        // Imprimir los elementos del array unidimensional
        StringBuilder salida = new StringBuilder();
        for (int x = 0; x < r; x++) {
            for (int y = 0; y < c; y++) {
                salida.append(arr[x * r + y]).append(" ");
            }
        }
        System.out.println(salida.toString());
    }
}
