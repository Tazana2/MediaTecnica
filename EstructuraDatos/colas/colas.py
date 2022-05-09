from nodes import Node

# Crear la clase cola
class Queue():

    # Crear el constructor de la cola
    def __init__(self):
        self.front = None # Primer elemento de la cola
        self.rear = None # Ultimo elemento de la cola (self.top en colas simplemente enlazadas)
        self.size = 0 # Cantidad de elementos de la cola

    # Operación cola vacia
    def Empty(self):
        return self.front == None

    # Insertar elemento al final de la cola
    def Enqueue(self, data):
        # Asignar memoria y rellenar el campo de datos
        newNode = Node(data)
        if self.Empty():
            # Operacion insertar elemento en una cola vacia
            self.front = self.rear = newNode
        else:
            # Operacion insertar un elemento al final de una cola
            # El puntero siguiente
            self.rear.nxt = newNode
            # El puntero fin apunta hacia el nuevo elemento
            self.rear = newNode
        
        # Actualizar el tamaño
        self.size += 1


    # Operación acolar o ingresar elemento al final de la cola
    def Dequeue(self):
        # Verificar si la cola esta vacia
        if self.Empty():
            print("Error: No es posible eliminar un elemento en una cola vacia.")
        # Verificar si queda un elemento en la cola
        elif self.front == self.rear:
            self.front = self.rear = None
            # Actualizar el tamaño
            self.size -= 1
        # Operacion dequeue
        else:
            self.front = self.front.nxt
            # Actualizar el tamaño de la cola
            self.size -= 1

    # Primer elemento de la cola
    def Front(self):
        if self.Empty:
            return None
        else:
            return self.front.data


    # Operación la cantidad de productos de la pila
    def Size(self):
        return self.size

    # Mostrar en pantalla la pila
    def Show(self):
        aux = self.front
        while aux != None:
            print(aux.data)
            aux = aux.nxt


    # Buscar un elemento en la cola
    def Look(self, data):
        aux = self.front
        while aux != None:
            if aux.data == data:
                return True
            aux = aux.nxt
        return False