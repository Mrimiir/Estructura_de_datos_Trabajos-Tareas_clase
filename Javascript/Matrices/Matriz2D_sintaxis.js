/*
Matrices en Javascript, Sintaxis básica de Python para escribir un arreglo de 2 dimenciones.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 07/09/2026
*/

const Two_dimensional_array = [
[1,2,3],
[4,5,6],
[7,8,9]
];
const tam = Two_dimensional_array.length

console.log("Los elementos del array son: ");
for (let i = 0; i < tam; i++){
    for (let j = 0; j < tam; j++){
        console.log(Two_dimensional_array[i][j]);
    }
}