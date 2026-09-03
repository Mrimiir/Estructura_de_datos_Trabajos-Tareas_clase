/*
Arrays en Java, Sintaxis básica de Java para escribir un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 02/09/2026
*/
class Arreglos_sintaxis {
    public static void main(String[] args) {
        //Sintaxis básica de Java para escribir un array.
        int[] miArray = new int[5]; // Declaración de un array de enteros con tamaño 5
        // Establecer elementos
		miArray[0] = 23;
		miArray[1] = 50;
		miArray[2] = 80;
		miArray[3] = 18;
		miArray[4] = 20;

        //Definir arreglo y sus elementos en una sola línea
        int[] otro_array = new int[] {1, 2, 3, 4, 5};

        //Imprimir elementos del arreglo
        System.out.println("Elementos del arreglo: ");
        for (int x = 0; x < otro_array.length; x++) {
			System.out.printf("Numeros[%d] = %d\n", x, otro_array[x]);
		}
    }
}