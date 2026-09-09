/*
Matrices en javascript, Sintaxis básica de Javascript para escribir un arreglo de 3 dimensiones.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 07/09/2026
*/

const Three_dimencional_array = [     //guarda 2 arreglos bidimencionales
[ [1,2,3],
[4,5,6],
[7,8,9]
],
[[10,11,12],
[13,14,15],
[16,17,18]
]
]

let resultado = "";
console.log("Los elementos del array son: ")
for (let i = 0; i < Three_dimencional_array.length; i++){
    for ( let j = 0; j < Three_dimencional_array[i].length; j++){
        for (let k = 0; k < Three_dimencional_array[i][j].length; k++){
            resultado += Three_dimencional_array[i][j][k] + " ";
        }
    }
}
console.log(resultado);