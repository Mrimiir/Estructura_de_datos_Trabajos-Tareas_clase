/*
Algoritmos de ordenamiento en Javascript, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
Quick-sort
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 16/09/2026
*/

//Funcion para hacer la particion del arreglo
function partition(a, l, h){
    let pvt = a[h];      //Pivote a utilizar puede ser el primer elemento, el del medio o el ultimo en este caso sera el ultimo
    let j = l - 1;      //j es indice de los elemento menores que el pivote
    for (let k = l; k < h; k++){
        if (a[k] < pvt){        //si el elemento en k es menor que el pivote
            j ++;               // j incrementa en 1
            swap(a, j, k);      // se realiza el intercambio entre j y k
        }
    }
    swap(a, j + 1, h);    // intercambia el pivote con el elemento siguiente al ultimo elemento mas pequeño
    return j + 1;
}

// Funcion para intercambiar dos elementos del arreglo
function swap(a, j, k){
    [a[j], a[k]] = [a[k], a[j]];        // intercambia los elementos
}

// Implementacion de la funcion QuickSort
function qck_sort(a, l, h){
    if (l < h){     // si el indice izquierdo es menor que el derecho
        let pi = partition(a, l, h);        // particiona el arreglo, pi es el indice del pivote
        qck_sort(a, l, pi - 1)  // llamada recursiva para los elementos menores que el pivote
        qck_sort(a, pi + 1, h)  // llamada recursiva para lso elementos mayores que el pivote
    }
}

// funcion para imprimir el arreglo
function printArr(a){
    let list = "";
    a.forEach(element => {
        list += element + " ";
    });
    console.log(list);
}

// codigo principal
function main(){
    let a = [10, 7, 8, 9, 1, 5];
    let size = a.length;
    console.log("El arreglo antes de ordenarlo: ");
    printArr(a);
    
    qck_sort(a, 0, size - 1);
    console.log("\nEl arreglo despues de ordenarlo: ");
    printArr(a);
}
if (import.meta.main){
    main();
}