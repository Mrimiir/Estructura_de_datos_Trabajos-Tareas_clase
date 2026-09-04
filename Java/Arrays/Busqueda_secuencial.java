/*
Busqueda en Java, Programa para buscar un elemento en un array de manera secuencial.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 04/09/2026
*/

//Declaramos una funcion de busqueda
public  class Busqueda_secuencial {
    public static int find_elem(int[] arreglo, int s, int elemento){
        for (int i = 0; i < s; i++){
            if (arreglo[i] == elemento){
                return i;
            }
        }
        return -1;
    }
    public static void main(){
        //declaramos elementos a usar
        int[] input_arr = {11, 21, 31, 41, 51, 61}; 
        int elem = 81;
        int s = input_arr.length;

        int index = find_elem(input_arr, s, elem);
        if (index != -1){
            System.out.printf("El elemento %d fue encontrado en la posicion: %d.%n", elem, index + 1 ); //%n es un salto de linea o algo asi
        }
        else{
            System.out.printf("El elemento %d no fue encontrado en el arreglo %n", elem);
        }
    }
}