/*
Busqueda en Javascript, Programa para buscar un elemento en un array de manera secuencial.
@Autor: Daniel Alejandro Alvarado Velázquez
@grupo: #2-02
@Fecha: 03/09/2026
*/

function find_elem(arreglo, s, elemento){
    for (let i = 0; i < s; i++){
        if (arreglo[i] == elemento){
            return i;
        }
    }
    return -1;
}

//bloque principal de codigo
function main() {
    //Declaracion del array y los elementos necesarios para la busqueda
    const input_arr = [11, 21, 31, 41, 51, 61];
    const elem = 51;
    const s = input_arr.length;

    const index = find_elem(input_arr, s, elem);
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