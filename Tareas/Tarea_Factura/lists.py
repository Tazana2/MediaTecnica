from nodes import Node
from os import system


# Crear la clase pila
class Stack():

    # Crear el constructor de la pila
    def __init__(self):
        self.first = None
        self.top = None
        self.size = 0

    # Operación pila vacia
    def Empty(self):
        return self.first == None

    # Insertar el producto al final de la pila
    def Push(self, data, data2, data3):
        # Hacer que newNode sea global para poder utilizar sus datos en otras funciones
        global newNode 
        # Asignar memoria y rellenar el campo de datos con todos los datos registrados
        newNode = Node(data, data2, data3)
        if self.Empty():
            # Operacion insertar producto en una pila vacia
            self.first = self.top = newNode
        else:
            # Operacion insertar un producto al final de una pila
            self.top.nxt = newNode
            self.top = newNode
        
        # Actualizar el tamaño
        self.size += 1
        # Retorna el valor del producto multiplicado por la cantidad de este mismo
        return int(data2) * int(data3)


    # Operación apilar o ingresar productos al final de la pila
    def Pop(self):
        # Verificar si la pila esta vacia aunque sea redundante pues en el main ya se hace esta verificación
        if self.Empty():
            print("Error: No es posible eliminar un elemento de una pila vacia.")
        elif self.first == self.top:
            self.first = self.top = None
            self.size -= 1
        # Operacion eliminar elemento al final de la pila
        else:
            aux = self.first
            while aux.nxt != self.top:
                aux = aux.nxt
            aux.nxt = None
            self.top = aux
            self.size -= 1

        # Retorna el valor y la cantidad que estaban almacenadas en el ultimo nodo
        return int(newNode.data2) *int(newNode.data3)
        

    # Devolver el producto que está en la cima
    def Top(self):
        return self.top.data, self.top.data2, self.top.data3

    # Operación la cantidad de productos de la pila
    def Size(self):
        return self.size

    # Mostrar en pantalla la pila
    def Show(self):
        aux = self.first
        while aux != None:
            print(" -  Nombre:",aux.data, "/ Precio:",aux.data2, "/ Cantidad:", aux.data3)
            aux = aux.nxt



class GUI():

    # Crear el constructor de la UI
    def __init__(self):
        # Instancias de la clase Stack
        self.purchases = Stack()
        self.facture = Stack()
        # Variable para guardar periodicamente el subtotal
        self.subtotal = 0

    # Operación para empezar el proceso
    def Start(self):
        while True:

            system("clear") # EN WINDOWS UTILIZAR: system("cls")
            print("Lista de compra:")

            self.purchases.Show()

            print("\n"+"-"*30)
            print("Menú de opciones:\n1. Ingresar producto con todos sus datos\n2. Eliminar ultimo producto junto con sus datos\n3. Modificar el último elemento\n4. Finalizar compra")
            opcion = input("Digite la opción que desee seleccionar: ")

            if opcion == "1":
                name = input("\nIngrese el nombre de su producto: ")
                value = input("\nIngrese el valor por unidad del producto: ")
                # Verificar que el valor del producto sea un número
                if value.isdigit():
                    # Verificar que la cantidad sea un número
                    quantity = input("\nIngrese la cantidad: ")
                    if quantity.isdigit():
                        self.purchases.Push(name, value, quantity)
                        # Al subtotal se le da el valor que retorna el Push (Ver en funcion Push)
                        self.subtotal += self.facture.Push(name, value, quantity)
                    else:
                        print("\nError: La cantidad debe ser un número")
                        op = input("\nPulse cualquier tecla para continuar....")
                else:
                    print("\nError: El valor debe ser un número")
                    op = input("\nPulse cualquier tecla para continuar....")

            elif opcion == "2":
                if self.purchases.Empty():
                    print("\nError: No hay productos en el carrito de compra - No se puede borrar lo que no está")
                    op = input("\nPulse cualquier tecla para continuar....")
                else:
                    self.purchases.Pop()
                    # Al subtotal se le quita el valor que retorna el Pop (Ver en funcion Pop)
                    self.subtotal -= self.facture.Pop()

            elif opcion == "3":
                if self.purchases.Empty():
                    print("\nError: No hay productos en el carrito de compra - No se puede modificar lo que no está")
                    op = input("\nPulse cualquier tecla para continuar....")
                else:
                    name = input("\nIngrese el nombre de su producto: ")
                    value = input("\nIngrese el valor por unidad del producto: ")
                    self.purchases.Pop()
                    # Al subtotal se le quita el valor que retorna el Pop (Ver en funcion Pop)
                    self.subtotal -= self.facture.Pop()
                    # Verificar que el valor del producto sea un número
                    if value.isdigit():
                        # Verificar que la cantidad sea un número
                        quantity = input("\nIngrese la cantidad: ")
                        if quantity.isdigit():
                            self.purchases.Push(name, value, quantity)
                            # Al subtotal se le da el valor que retorna el Push (Ver en funcion Push)
                            self.subtotal += self.facture.Push(name, value, quantity)
                        else:
                            print("\nError: La cantidad debe ser un número")
                            op = input("\nPulse cualquier tecla para continuar....")
                    else:
                        print("\nError: El valor debe ser un número")
                        op = input("\nPulse cualquier tecla para continuar....")
                
            elif opcion == "4":
                self.Facturation()
                break

    # Operación para mostrar la factura
    def Facturation(self):
        system("clear") # EN WINDOWS UTILIZAR: system("cls")

        print("\nProductos comprados: \n")
        self.facture.Show()

        print("\nSubtotal: ",str(self.subtotal)+"$", "/ IVA: ", str(self.subtotal*0.19)+"$")
        print("-"*30)
        print("Total: ", str(self.subtotal+(self.subtotal*0.19))+"$", "\nTotal Sin IVA: ", str(self.subtotal)+"$")
        
        print("\n\nTerminando proceso...Muchas gracias por comprar en Tiendas XYZ. Vuelva pronto!")


