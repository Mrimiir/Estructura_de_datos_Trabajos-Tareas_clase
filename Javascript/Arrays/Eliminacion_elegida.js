/*
Eliminacion en Javascript, Eliminacion de un elemento elegible de un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 03/09/2026
*/

//Declramos el array
const input_arr = [11, 21, 31, 41, 51, 61];
const elem = 41;
const index = 4;
const elem_borrar = 1;

console.log("Antes de la eliminacion, el array es: ");
for (let i = 0; i < input_arr.length; i++){
    console.log(input_arr[i]);
}

input_arr.splice(index, elem_borrar);       //.splice(indice del objetivo, cuantos elementos borrar desde ese indice)
/*
for (let i = 0; i < input_arr.length; i++){
    if (input_arr[i] == elem){
        input_arr.splice(i, 1);
    }
}
*/
console.log("Despues de la eliminacion, el array es: ");
for (let i = 0; i < input_arr.length; i++){
    console.log(input_arr[i]);
}