### Continuacion de metodos para listas enlazadas (Visto en la clase 2)

Insertar un elemento en una lista en otra parte de la lista:
- Pasos para lograr esta tarea:
    
    1. Asignar la memoria al nuevo elemento.
    2. rellenar el campo de datos del nuevo elemento
    3. Elegir una posicion en la lista (la insercion se hara despues de haber elegido la posición).
    4. El puntero siguiente del nuevo elemento apunta hacia la dirección a la que apunta el puntero siguiente del elemento actual.
    5. El puntero siguiente del elemento actual apunta al nuevo elemento.
    6. Los punteros inicio y fin no cambian (a menos de que se inserte el elemento al final de la lista, aunque esto es dependiendo de como se haga su funcionamiento).
    7. El tamaño se incrementa en una unidad (en algunos leguajes).



*Eliminar elementos*

Eliminar elemento al inicio de una lista
- Pasos para lograr esta tarea:
    1. El puntero auxiliar contendra la direccion del primer elemento.
    2. El puntero inicio apuntara hacia el segundo elemento.
    3. El tamaño de la lista tendra que disminuir un elemento (en algunos lenguajes).