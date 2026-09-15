/*
Algoritmos de ordenamiento en Javascript, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
Selection-sort
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 14/09/2026
*/

function selection_sort(arr){
    for (let i = 0; i < arr.length; i++){
        let small = i;
        for (let j = i+1; j < arr.length; j++){
            if (arr[small] > arr[j]){
                small = j;
            }
        }
        [arr[i], arr[small]] = [arr[small], arr[i]];
    }
}

function printArr(arr){
    let fila ="";
    for(let i = 0; i < arr.length; i++){
        fila += arr[i] + " ";
    }
    console.log(fila);
}

let arr = [65,26,13,23,12];
console.log("Arreglo antes de ser ordenado: ");
printArr(arr);
selection_sort(arr);
console.log("\nArreglo despues de ser ordenado: ");
selection_sort(arr);
printArr(arr);