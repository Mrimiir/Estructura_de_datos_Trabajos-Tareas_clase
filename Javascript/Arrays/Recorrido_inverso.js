/*
Arrays en Javascript, Recorrido inverso en un array.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 03/09/2026
*/

//definimos el array
const input_arr = [11, 21, 31, 41, 51, 61];

console.log(`El arreglo desde su primer elemento: ${input_arr}`);   //imprime el arreglo en su estado original

console.log('Ahora el arreglo invertido: ');
for (let i = input_arr.length -1; i > -1 ; i--){        //imprime el arreglo de manera inversa sin cambiar al original
    console.log(input_arr[i]);
}

//Funcion
input_arr.reverse();        //invierte el orden del arreglo, pero modificandolo
console.log(`El arreglo desde su ultimo elemento: ${input_arr}`); 