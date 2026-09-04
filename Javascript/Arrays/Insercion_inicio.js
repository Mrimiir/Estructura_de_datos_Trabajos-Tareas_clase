/*
Arrays en Javascript,Insercion en el primer elemento de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 03/09/2026
*/

//declaracion de arreglo
const input_arr = [11, 21, 31, 41, 51, 61];
const elem = 16;

console.log("Antes de la insercion del arreglo:");
for (let i = 0; i < input_arr.length; i++){
    console.log(input_arr[i]);
}

input_arr.unshift(elem)     //inserta un nuevo elemento en el indice 0 y empuja a los demas

console.log("Despues de la insercion del arreglo:");
for (let i = 0; i < input_arr.length; i++){
    console.log(input_arr[i]);
}
