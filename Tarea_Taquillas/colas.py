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
        system("cls")
        option = input().split("-")
        return option

    def LastChoose():
        system("cls")
        print("-"*35)
        option = input("\n1. Agregar\n2. Eliminar\n3. Ver las colas\n4. Terminar proceso\n\n¿Que desea hacer?: ")
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
        else:
            print("\n- ERROR: No existe esa taquilla")

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
        else:
            print("\n- ERROR: No existe esa taquilla")

    # Mostrar la cantidad de personas restantes en la cola que el usuario elija
    def Checkout(self):
        system("cls")
        option = input("\nIngrese la taquilla de la cual desea ver cuantas personas quedaron: ")
        if option == '1':
            self.lst1.Show()
            print("-"*35,"\nTotal personas restantes: ", self.lst1.size)
        elif option == '2':
            self.lst2.Show()
            print("-"*35,"\nTotal personas restantes: ", self.lst2.size)
        elif option == '3':
            self.lst3.Show()
            print("-"*35,"\nTotal personas restantes: ", self.lst3.size)
        elif option == '4':
            self.lst4.Show()
            print("-"*35,"\nTotal personas restantes: ", self.lst4.size)
        elif option == '5':
            self.lst5.Show()
            print("-"*35,"\nTotal personas restantes: ", self.lst5.size)
        elif option == '6':
            self.lst6.Show()
            print("-"*35,"\nTotal personas restantes: ", self.lst6.size)
        elif option == '7':
            self.lst7.Show()
            print("-"*35,"\nTotal personas restantes: ", self.lst7.size)
        elif option == '8':
            self.lst8.Show()
            print("-"*35,"\nTotal personas restantes: ", self.lst8.size)
        elif option == '9':
            self.lst9.Show()
            print("-"*35,"\nTotal personas restantes: ", self.lst9.size)
        elif option == '10':
            self.lst10.Show()
            print("-"*35,"\nTotal personas restantes: ", self.lst10.size)
        else:
            print("\n- ERROR: No existe esa taquilla")

        abc = input("Pulse cualquier tecla para continuar...")

    def LastAdd(self):
        system("cls")
        name = input("Ingrese su nombre: ")
        op = input("\n1. Adquisición teléfono nuevo\n2. Cambio de plan\n3. Cancelación de plan\n4. Solución de problema técnico\n5. Pago de facturas vencidas\n\nIngrese el nombre del servicio para el cual viene: ")
        if op == '1':
            if self.lst1.size < 15:
                self.lst1.Enqueue(name, '1')
            else:
                if self.lst2.size < 15:
                    self.lst2.Enqueue(name, '2')
                    abc = input("\nUsted fue puesto en la segunda taquilla para el servicio seleccionado\n\nPresione cualquier tecla para continuar...")
                else:
                    abc = input("\nAmbas taquillas están llenas, lo sentimos.\n\nPresione cualquier tecla para continuar...")
                    
        elif op == '2':
            if self.lst3.size < 15:
                self.lst3.Enqueue(name, '3')
            else:
                if self.lst4.size < 15:
                    self.lst4.Enqueue(name, '4')
                    abc = input("\nUsted fue puesto en la segunda taquilla para el servicio seleccionado\n\nPresione cualquier tecla para continuar...")
                else:
                    abc = input("\nAmbas taquillas están llenas, lo sentimos.\n\nPresione cualquier tecla para continuar...")
        elif op == '3':
            if self.lst5.size < 15:
                self.lst5.Enqueue(name, '5')
            else:
                if self.lst6.size < 15:
                    self.lst6.Enqueue(name, '6')
                    abc = input("\nUsted fue puesto en la segunda taquilla para el servicio seleccionado\n\nPresione cualquier tecla para continuar...")
                else:
                    abc = input("\nAmbas taquillas están llenas, lo sentimos.\n\nPresione cualquier tecla para continuar...")
        elif op == '4':
            if self.lst7.size < 15:
                self.lst7.Enqueue(name, '7')
            else:
                if self.lst8.size < 15:
                    self.lst8.Enqueue(name, '8')
                    abc = input("\nUsted fue puesto en la segunda taquilla para el servicio seleccionado\n\nPresione cualquier tecla para continuar...")
                else:
                    abc = input("\nAmbas taquillas están llenas, lo sentimos.\n\nPresione cualquier tecla para continuar...")
        elif op == '5':
            if self.lst9.size < 15:
                self.lst9.Enqueue(name, '9')
            else:
                if self.lst10.size < 15:
                    self.lst10.Enqueue(name, '10')
                    abc = input("\nUsted fue puesto en la segunda taquilla para el servicio seleccionado\n\nPresione cualquier tecla para continuar...")
                else:
                    abc = input("\nAmbas taquillas están llenas, lo sentimos.\n\nPresione cualquier tecla para continuar...")
        
        else:
            print("\n- ERROR: No existe una taquilla con el servicio deseado.")

    def LastDelete(self):
        system("cls")
        op = input("Ingrese el número de la taquilla de la cual desea eliminar a la primer persona: ")
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
        else:
            print("\n- ERROR: No existe esa taquilla")



    # Inicio del programa
    def Start(self):
        system("cls")
        for i in range(int(input("Ingrese la cantidad de personas que se van a ir a una taquilla: "))):
            thing = GUI.Choose()
            # Verificar si es un número
            if thing[0].isdigit():
                GUI.Delete(self,thing[0])
            else:   
                GUI.Add(self,thing)
        GUI.End(self)

    def End(self):
        # Menú final de opciones
        while True:
            thing = GUI.LastChoose()
            if thing == '1':
                GUI.LastAdd(self)
            elif thing == '2':
                GUI.LastDelete(self)
            elif thing == '3':
                GUI.Checkout(self)
            elif thing == '4':
                print("Gracias! Que tenga un buen día")
                break
            else:
                print("- ERROR: No existe dicha opción")
                abc = input("Presione cualquier tecla para continuar...")
