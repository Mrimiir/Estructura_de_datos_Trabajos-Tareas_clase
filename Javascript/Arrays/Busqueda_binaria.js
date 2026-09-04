/*
Busqueda en Javascript, Programa para buscar un elemento en un array de manera binaria.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 03/09/2026

Nota: La busqueda binaria es un algoritmo de busqueda eficiente que requiere que el array este ordenado previamente.
*/

//declaracion de funcion de busqueda binaria
function find_elem(arreglo, l, h, elemento){
    while (l <= h){
        const mid = Math.trunc(l + (h - l) / 2);
        if (arreglo[mid] == elemento){      // Verifica si el elemento está presente en el medio
            return mid;                      // Elemento encontrado, devuelve el índice
        }
        else if (arreglo[mid] < elemento){     // Si el elemento es mayor que el medio, ignora la mitad izquierda
            l = mid + 1;
        }
        else{
            h = mid - 1;         //Si el elemento es menor que el medio, ignora la mitad derecha
        }
        //si el control llega hasta este punto significa que el elemento no se encuentra en el arreglo
    }
    return -1;
}


//bloque principal de codigo
function main() {
    //Declaracion del array y los elementos necesarios para la busqueda
    const input_arr = [11, 43, 13, 24, 45, 32, 51, 76, 67, 89, 1];
    const elem = 76;
    const s = input_arr.length;

    //ordena el arreglo porque en este caso es necesario
    input_arr.sort();
    console.log(input_arr)

    const index = find_elem(input_arr, 0, s - 1, elem);
    if (index != -1){
        console.log(`El elemento ${elem} fue encontrado en la posicion: ` + String(index + 1));
    }
    else{
        console.log(`El elemento ${elem} no fue encontrado en el arreglo.`);
    }


}

if (import.meta.main) {
    main();
}