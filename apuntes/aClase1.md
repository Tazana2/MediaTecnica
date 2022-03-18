### Nodo:
Es el elemento que me permite formar cualquier estructura de datos (Pila, Cola).

Un nodo es uno de los elementos de una *lista enlazada*, de una arbol o de un grafo. Cada nodo será
una estructura o registo que dispondra de varios campos, al menos de esos campos será un puntero o 
referencia a otro nodo; de forma que, conocido un nodo, a partir de esa referencia, será posible en 
teoría tener acceso a otros nodos de la estructura.

- Si uno de los nodos tiene más de un puntero, todos los demás nodos deberan tener el mismo número de
punteros.

- Cuando un puntero no está apuntando a nada, se refiere a que apunta a null o none. Es decir, termina
la lista.

- En las listas enlazadas no se puede trabajar con indices, sino mediante nodos.

- Tiene un dato y un puntero.

--------------------------------------------------------------------------------


### Git y github: 
Manejo y control de versiones.

--------------------------------------------------------------------------------

### POO:
El objeto tiene propiedades y metodos.

--------------------------------------------------------------------------------

### Estructuras de datos:

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