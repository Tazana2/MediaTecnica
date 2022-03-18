# importar la clase "Nodo" de la biblioteca Nodo
from listasE.nodes import Node

class SimplyLinkedList():

    # Definir el constructor
    def __init__(self):
        self.first = None # Nodo primero 
        self.last = None # Nodo final
        self.size = 0 # Variable para el tamaño de la lista

    # Metodo para verificar si la lista esta vacia
    def empty(self):
        return self.first == None  


    # Mostrar la cantidad de elementos de la lista
    def Size(self):
        return self.size

    # Mostrar en pantalla la lista
    def showList(self):
        aux = self.first
        while aux != None:
            print(aux.data, end=" ")
            aux = aux.nxt
        print("")


    # Insertar elemento al inicio de la lista
    def insertFirst(self, data):
        # Asignar memoria, rellenar, el campo de datos 
        newNode = Node(data)
        # Verificar si la lista esta vacia
        if self.empty():
            # Operacion insertar elemento en una lista vacia
            # Los punteros inicios y fin apuntan al nuevo elemento
            self.first = self.last = newNode
        else:
            # Operacion al insertar elemento al inicio de la lista
            # El puntero del nuevo elemnto apunta hacia el elemento
            newNode.nxt = self.first
            self.first = newNode

        # Actualizar el tamaño
        self.size += 1

    # Insertar elemento al final de la lista
    def insertLast(self, data):
        # Asignar memoria y rellenar el campo de datos
        newNode = Node(data)
        if self.empty():
            # Operacion insertar elemento en una lista vacia
            self.first = self.last = newNode
        else:
            # Operacion insertar un elemento al final de una lista
            # El puntero siguiente
            self.last.nxt = newNode
            # El puntero fin apunta hacia el nuevo elemento
            self.last = newNode
        
        # Actualizar el tamaño
        self.size += 1

    def insert(self, data, position = None):
        # Asignar memoria y rellenar el cmapo de datos
        newNode = Node(data)
        # Bandera para verificar si se encuentra la posicion
        coincidence = False

        # Verificar si la lista esta vacia
        if self.empty():
            # Operacion de insertar elemento en una lsita vacia
            self.first = self.last = newNode
            self.size += 1
            coincidence = True
        
        elif position == None:
            self.insertLast(data)
            coincidence = True
        
        # Operacion insertar elemento en cualquier parte de la lista
        else:
            # Elegir la posicion de la lista (la insercion se realizara despues de la posicion)
            # Buscar la posicion
            aux = self.first
            while aux != None:
                if aux.data == position:
                    coincidence = True
                    break
                aux = aux.nxt

            if coincidence:
                aux = self.first
                while aux.data != position:
                    aux = aux.nxt
                # Punto 4 del algoritmo
                newNode.nxt = aux.nxt 
                # Punto 5 del algoritmo
                aux.nxt = newNode
                #Verificar si el nuevo nodo quedo como ultimo
                if not newNode:
                    self.last = newNode

                # El tamaño se actualiza
                self.size += 1
                coincidence = True

        # Validar si no hubo posicion existente
        if not coincidence: # Es lo mismo que if coincidence == False
            print("Error - La posicion ingresada no existe en la lista o no se especificó.")


    
    def deleteFirst(self):
        # Verificar si la lista esta vacia
        if self.empty():
            print("Error: No es posible eliminar un elemento de una lista vacia.")
        # Verificar si queda un solo elemento en la lista
        elif self.first == self.last:
            self.first = self.last = None
            # Actualizar el tamaño de la lista
            self.size -= 1
        # Operacion eliminar elemento al inicio de la lista
        else:
            self.first = self.first.nxt
            self.size -=  1

    def deleteLast(self):
        # Verificar si la lista esta vacia
        if self.empty():
            print("Error: No es posible eliminar un elemento de una lista vacia.")
        # Verificar si queda un solo elemento en la lista
        elif self.first == self.last:
            self.first = self.last = None
            # Actualizar el tamaño de la lista
            self.size -= 1
        # Operacion eliminar elemento al final de la lista
        else:
            aux = self.first
            while aux.nxt != self.last:
                aux = aux.nxt
            aux.nxt = None
            self.last = aux
            self.size -= 1

    # Operacion eleiminar elemento en cualquier parte de la lista
    def delete(self, data):
        # Bandera para verificar si el dato existe en la lista
        coincidence = False
        # Verificar si la lista está vacia
        if self.empty():
            print("Error: No es posible eliminar un elemento de una lista vacia")
            coincidence = True
        # Verificar si queda un solo elemento en la lista
        elif self.first == self.last and self.last.data == data:
            self.first = self.last = None
            # Actualizar el tamaño de la lista
            self.size -= 1
            coincidence = True
        # Verificar si el elemento que se eliminará es el primero de la lista
        elif data == self.first.data:
            self.deleteFirst
            coincidence = True
        # Operacion eliminar elemento en cualquier parte de la lista
        else:
            # Verificar si el dato que se va a eliminar existe en la lista => Operación Buscar ó Look
            aux = self.first.nxt
            while aux != None:
                if aux.data == data:
                    coincidence = True
                    break
                aux = aux.nxt
            # Si se encuentra el dato realizar la operación
            if coincidence:

                # Paso 1 en la operación eliminar elemento en cualquier parte
                aux = self.first
                while aux.nxt.data != data:
                    aux = aux.nxt
                # Paso 2 en al opración eliminar elemento en cualquier parte de la lista
                aux.nxt = aux.nxt.nxt
                # Si el elemento actual es el ultimo elemento de la lista
                if aux.nxt == None:
                    self.last = aux
                # Actualizar el tamaño de la lista
                self.size -= 1

            # Validar si el elemento que se desea eliminar no se encuentra en la lista
            if not coincidence:
                print("Error: El elemento que desea eliminar no existe en la lista")