from nodes import Node
from os import system

# Crear la clase pila
class Queue():

    # Crear el constructor de la pila
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    # Operación pila vacia
    def Empty(self):
        return self.front == None

    # Insertar el producto al final de la pila
    def Enqueue(self, data, data2):
        # Asignar memoria y rellenar el campo de datos con todos los datos registrados
        newNode = Node(data, data2)
        if self.Empty():
            # Operacion insertar producto en una pila vacia
            self.front = self.rear = newNode
        else:
            # Operacion insertar un producto al final de una pila
            self.rear.nxt = newNode
            self.rear = newNode
        
        # Actualizar el tamaño
        self.size += 1
        # Retorna el valor del producto multiplicado por la cantidad de este mismo



    # Operación apilar o ingresar productos al final de la pila
    def Dequeue(self):
        # Verificar si la pila esta vacia aunque sea redundante pues en el main ya se hace esta verificación
        if self.Empty():
            print("Error: No es posible eliminar un elemento de una pila vacia.")
        elif self.front == self.rear:
            self.front = self.rear = None
            self.size -= 1
        # Operacion eliminar elemento al final de la pila
        else:
            self.front = self.front.nxt
            self.size -=  1

        # Retorna el valor y la cantidad que estaban almacenadas en el ultimo nodo
        

    # Devolver el producto que está en la cima
    def Front(self):
        return self.rear.data, self.rear.data2

    # Operación la cantidad de productos de la pila
    def Size(self):
        return self.size

    # Mostrar en pantalla la pila
    def Show(self):
        aux = self.front
        while aux != None:
            print(aux.data)
            aux = aux.nxt

    def Look(self,data):
        aux = self.front
        while aux != None:
            if data == aux.data:
                return True
            aux = aux.nxt
        return False


# Crear la clase para mostrar el menú
class GUI():
    def __init__(self):
        self.lst1 = Queue()
        self.lst2 = Queue()
        self.lst3 = Queue()
        self.lst4 = Queue()
        self.lst5 = Queue()
        self.lst6 = Queue()
        self.lst7 = Queue()
        self.lst8 = Queue()
        self.lst9 = Queue()
        self.lst10 = Queue()

    # Ingresar la opción
    def Choose():
        system("clear")
        option = input("Ingrese su nombre y el número de la taquilla a la que se dirige: ").split("-")
        return option

    # Verificar la opción de taquilla y agregar la persona a dicha taquilla
    def Add(self,op):
        if op[1] == '1':
            self.lst1.Enqueue(op[0],op[1])
        elif op[1] == '2':
            self.lst2.Enqueue(op[0],op[1])
        elif op[1] == '3':
            self.lst3.Enqueue(op[0],op[1])
        elif op[1] == '4':
            self.lst4.Enqueue(op[0],op[1])
        elif op[1] == '5':
            self.lst5.Enqueue(op[0],op[1])
        elif op[1] == '6':
            self.lst6.Enqueue(op[0],op[1])
        elif op[1] == '7':
            self.lst7.Enqueue(op[0],op[1])
        elif op[1] == '8':
            self.lst8.Enqueue(op[0],op[1])
        elif op[1] == '9':
            self.lst9.Enqueue(op[0],op[1])
        elif op[1] == '10':
            self.lst10.Enqueue(op[0],op[1])

    # Eliminar a una persona de la cola
    def Delete(self,op):
        if op == '1':
            self.lst1.Dequeue()
        elif op == '2':
                self.lst2.Dequeue()
        elif op == '3':
                self.lst3.Dequeue()
        elif op == '4':
                self.lst4.Dequeue()
        elif op == '5':
                self.lst5.Dequeue()
        elif op == '6':
                self.lst6.Dequeue()
        elif op == '7':
                self.lst7.Dequeue()
        elif op == '8':
                self.lst8.Dequeue()
        elif op == '9':
                self.lst9.Dequeue()
        elif op == '10':
                self.lst10.Dequeue()

    # Inicio del programa
    def Start(self):
        system("clear")
        for i in range(int(input("Ingrese la cantidad de personas que se van a ir a una taquilla: "))):
            thing = GUI.Choose()
            # Verificar si es un número
            if thing[0].isdigit():
                GUI.Delete(self,thing[0])
            else:   
                GUI.Add(self,thing)
        GUI.Checkout(self)
    

    # Mostrar las colas al final
    def Checkout(self):
        system("clear")
        option = input("\nIngrese la cola de la cual desea ver cuantas personas quedaron: ")
        if option == '1':
            self.lst1.Show()
            print("Total personas restantes: ", self.lst1.size)
        elif option == '2':
            self.lst2.Show()
            print("Total personas restantes: ", self.lst2.size)
        elif option == '3':
            self.lst3.Show()
            print("Total personas restantes: ", self.lst3.size)
        elif option == '4':
            self.lst4.Show()
            print("Total personas restantes: ", self.lst4.size)
        elif option == '5':
            self.lst5.Show()
            print("Total personas restantes: ", self.lst5.size)
        elif option == '6':
            self.lst6.Show()
            print("Total personas restantes: ", self.lst6.size)
        elif option == '7':
            self.lst7.Show()
            print("Total personas restantes: ", self.lst7.size)
        elif option == '8':
            self.lst8.Show()
            print("Total personas restantes: ", self.lst8.size)
        elif option == '9':
            self.lst9.Show()
            print("Total personas restantes: ", self.lst9.size)
        elif option == '10':
            self.lst10.Show()
            print("Total personas restantes: ", self.lst10.size)