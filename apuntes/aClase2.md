### Estructuras de datos: (Se vio en la clase 1)

*Listas enlazadas*: Son estructuras de datos semejantes a los arrays, salvo que el
acceso a un elemento no se hace mediante indicies sino por punteros.

*L.E simple*: Basicamente tiene un solo puntero el cual apunta hacia otro nodo
hasta que acabe la lista.

    Metodos para listas enlazadas:

    Insertar un elemento a la lista: 
    - Este metodo involucra 4 posibilidades:
    
        1. Insertar elemento en una lista vacia (Se inserta como elemento unico).
        2. Insertar elemento al inicio de una lista.
        3. Insertar elemento al final de la listas.
        4. Insertar elemento en otra parte de la lista.


---------------------------------------------------------------------------------------------------------------


*Metodos para listas enlazadas*:


Insertar un elemento en una lista vacia:
- Pasos para lograr esta tarea:

    1. Declarar el elemento a insertar.
    2. Asignar la memoria para el nuevo elemento.
    3. El puntero siguiente del nuevo elemtento apunara hacia NULL.
    4. Los punteros (Nodos) "inicio" y "fin" apuntaran hacia el nuevo elemento.



Insertar un elemento al inicio de una lista:
- Pasos para lograr esta tarea:

    1. Declarar el elemento a insertar.
    2. Asignar la memoria para el nuevo elemento.
    3. El puntero siguiente del nuevo elemento apunta hacia el primer elemento.
    4. El puntero (Nodo) inicio apunta hacia el nuevo elemento.
    5. El putero "fin" no cambia.
    6. EL tamaño incrementa (en algunos lenguajes).



Insertar un elemento en una lista en otra parte de la lista: (Se vio en la clase 3)
- Pasos para lograr esta tarea:
    
    1. Asignar la memoria al nuevo elemento.
    2. Rellenar el campo de datos del nuevo elemento
    3. Elegir una posicion en la lista (la insercion se hara despues de haber elegido la posición).
    4. El puntero siguiente del nuevo elemento apunta hacia la dirección a la que apunta el puntero siguiente del elemento actual.
    5. El puntero siguiente del elemento actual apunta al nuevo elemento.
    6. Los punteros inicio y fin no cambian (a menos de que se inserte el elemento al final de la lista, aunque esto es dependiendo de como se haga su funcionamiento).
    7. El tamaño se incrementa en una unidad (en algunos leguajes).