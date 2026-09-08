/*
Mapeo de una matriz 2D a una matriz 1D en Python, las matrices por defecto se ordenan por mediante sus columnas.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 07/09/2026
*/

const r = 3, c = 3;
let arr = new Array(r * c).fill(0);   // Matriz inicializada y luego se le asigna un valor
let TwoDArr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];   // Almacenar elementos en un array unidimensional ordenados por filas

let k = 0;
for (let y = 0; y < c; y++) {
    for (let x = 0; x < r; x++) {
        k = y * r + x;
        arr[k] = TwoDArr[x][y];
    }
}

console.log("Los elementos del array bidimensional son: ");
for (let row of TwoDArr) {
    let linea = "";
    for (let ele of row) {
        linea += ele + " ";   // Mostrar los elementos de la fila separados por espacios
    }
    console.log(linea);
}

console.log("\nLos elementos del array unidimensional son: ");
// Imprimir los elementos del array unidimensional
let salida = "";
for (let x = 0; x < r; x++) {
    for (let y = 0; y < c; y++) {
        salida += arr[x * r + y] + " ";
    }
}
console.log(salida);