/*
Algoritmos de ordenamiento en Javascript, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 10/09/2026

Nota: Para algoritmos de busqueda  como la busqueda binaria es necesario tener ordenado el arreglo,
pero en alguno casos este no esta ordenado y estos algoritmos de ordenamiento resuelven ese problema
*/
//funcion de ordenamiento por insercion
function Insertion_sort(a){
    for (let i = 1; i < a.length; i++){
        let temp = a[i];
        let j = i - 1;
        while (j >= 0 && temp < a[j]){
            a[j + 1] = a[j];
            j = j-1;
        }
        a[j + 1] = temp;
    }
}
//funcion de imprecion del arreglo
function printArr(a){
    let list = "";
    a.forEach(element => {
        list += element + " ";
    });
    console.log(list);
}

function main(){
    const a = [50,38,11,28,44,19,9,36,26,12];
    console.log("Antes de ordenar los elementos del arreglo: ");
    printArr(a);
    Insertion_sort(a);
    console.log("\nDespues de ordenar los elementos del arreglo: ");
    printArr(a);
}
if(import.meta.main){
    main()
}