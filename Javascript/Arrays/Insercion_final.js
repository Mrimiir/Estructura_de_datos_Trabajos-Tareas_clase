/*
Arrays en Javascript,Insercion en el ultimo elemento de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 03/09/2026
*/

//declaracion de arreglos
const input_arr = [11, 21, 31, 41, 51, 61];
const elem = 34;

console.log("Antes de la insercion del arreglo:");
for (let i = 0; i < input_arr.length; i++){
    console.log(input_arr[i]);
}

input_arr.push(elem);       //inserta un elemento al final de arreglo modificando su longitud

console.log("\nDespues de la insercion del arreglo: ");
for (let i = 0; i < input_arr.length; i++){
    console.log(input_arr[i]);
}