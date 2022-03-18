from nodes import Node


# Crear la clase pila
class Stack():

    # Crear el constructor de la pila
    def __init__(self):
        self.first = None # Primer elemento de la pila
        self.top = None # Ultimo elemento de la pila (self.top en pilas simplemente enlazadas)
        self.size = 0 # Cantidad de elementos de la pila

    # Operación pila vacia
    def Empty(self):
        return self.first == None

    # Insertar elemento al final de la pila
    def Push(self, data):
        # Asignar memoria y rellenar el campo de datos
        newNode = Node(data)
        if self.Empty():
            # Operacion insertar elemento en una pila vacia
            self.first = self.top = newNode
        else:
            # Operacion insertar un elemento al final de una pila
            # El puntero siguiente
            self.top.nxt = newNode
            # El puntero fin apunta hacia el nuevo elemento
            self.top = newNode
        
        # Actualizar el tamaño
        self.size += 1

    # Operación apilar o ingresar elemento al final de la pila
    def Pop(self):
        # Verificar si la pila esta vacia
        if self.Empty():
            print("Error: No es posible eliminar un elemento de una pila vacia.")
        # Verificar si queda un solo elemento en la pila
        elif self.first == self.top:
            self.first = self.top = None
            # Actualizar el tamaño de la pila
            self.size -= 1
        # Operacion eliminar elemento al final de la pila
        else:
            aux = self.first
            while aux.nxt != self.top:
                aux = aux.nxt
            aux.nxt = None
            self.top = aux
            self.size -= 1

    # Devolver el elemento que está en la cima
    def Top(self):
        return self.top.data

    # Operación la cantidad de elementos de la pila
    def Size(self):
        return self.size

    # Mostrar en pantalla la pila
    def Show(self):
        aux = self.first
        while aux != None:
            print(aux.data)
            aux = aux.nxt