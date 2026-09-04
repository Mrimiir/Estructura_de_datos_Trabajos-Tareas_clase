/*
Eliminacion en Javascript, Eliminacion del ultimo elemento de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 03/09/2026
*/

//Declaramos al arreglo
const input_arr = [11, 21, 31, 41, 51, 61];

console.log("Antes de la eliminacion, el array es: ");
for (let i = 0; i < input_arr.length; i++){
    console.log(input_arr[i]);
}

input_arr.pop()     //remueve el ultimo elemento del arreglo

console.log("Despues de la eliminacion, el array es: ");
for (let i = 0; i < input_arr.length; i++){
    console.log(input_arr[i]);
}