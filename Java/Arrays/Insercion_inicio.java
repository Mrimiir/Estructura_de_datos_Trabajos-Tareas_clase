/*
Arrays en Java,Insercion en el primer elemento de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 04/09/2026
*/

public class Insercion_inicio {
    public static void main(String[] args){
        int[] input_arr = {11, 21, 31, 41, 51, 61};     //array estatico

        System.out.println("Antes de la insercion, el array es: ");

        for (int elemento : input_arr){
            System.out.println(elemento);
        }

        System.out.println("Despues de la insercion, el array es: ");

        int[] input_arr2 = new int[input_arr.length +1];        //crea un nuevo array con el tamaño del original +1 
        input_arr2[0] = 1;      //en el indice 0 se le da el valor de 1
        System.arraycopy(input_arr, 0, input_arr2, 1, input_arr.length);        //se copia el primer array al segundo, (array1_origen, indice donde empieza a copiar, array2_destino, indice desde donde se empieza a copiar, numero de elementos del array1 

        for (int elemento : input_arr2){
            System.out.println(elemento);
        }
        
    }
}
