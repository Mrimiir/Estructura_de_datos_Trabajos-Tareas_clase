/*
Arrays en JavaScript, Sintaxis básica de JavaScript para escribir un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 02/09/2026
*/

//Formas de declarar un arreglo en JavaScript
const arreglo = new Array(5); // Crea un arreglo de tamaño 5
const otro_arreglo = [1, 2, 3, 4, 5]; // Crea un arreglo con valores iniciales
const arreglo_variado = [1, 3.67, "Hola", true]; // una arreglo en javascript puede contener diferentes tipos de datos

// Imprimir los elementos del arreglo
console.log(otro_arreglo[0]); // Imprime 1
console.log(otro_arreglo[4]); // Imprime 5

for (let i = 0; i < arreglo_variado.length; i++) {
    console.log(`El elemento en el indice ${i} es: ${arreglo_variado[i]}`);
}

//Insertamos valores al arreglo vacio
for (let i = 0; i < arreglo.length; i++) {
    arreglo[i] = i + 2;
}
console.log(arreglo);