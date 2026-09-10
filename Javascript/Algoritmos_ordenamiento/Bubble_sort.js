/*
Algoritmos de ordenamiento en Javascript, algoritmos que nos ayudan a ordenar los arreglos para optimizar su busqueda.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 10/09/2026

Nota: Para algoritmos de busqueda  como la busqueda binaria es necesario tener ordenado el arreglo,
pero en alguno casos este no esta ordenado y estos algoritmos de ordenamiento resuelven ese problema

nota personal: Js no necesariamente necesia ";" pero yo se lo agrego aveces (cuando no se me olvida)
*/

function Bubble_sort(a){
    const s = a.length;
    for (let j = 0; j < s; j++){
        let isSwapped = false;                      //declara que no hubo ningun cambio
        for (let i = 0; i < (s - j - 1);i++){       //si en el indice j el elemento es mayor que lo del indice j+1 se intercambian estas posiciones
            if (a[i] > a[i + 1]){
                [a[i], a[i + 1]] = [a[i + 1], a[i]];        // todo debe estar entre "[]" para que funcione el intercambio
                isSwapped = true;                   //declara si el cambio se llevo a cabo
            }
        }
        if ( isSwapped == false){
            break;                      //sale de la funcion si no hubo algun cambio
        }
    }
}

function main(){
    let a = [46,7,7,18,38,7,39,48,32,26];
    let list = "";
    console.log("Antes de ordenar los elementos del array son: ");
    a.forEach(element => {
        list += element + " ";
    });
    console.log(list);


    Bubble_sort(a);
    let result = "";
    console.log("\nDespues de ordenar los elementos del array son: ");
    for (let j = 0; j < a.length; j++){
        result += a[j] + " ";
    }
    console.log(result);
}

if (import.meta.main){
    main()
}