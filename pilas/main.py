from lists import Stack
from os import system

# Crear la instancia de la clase Stack
stackDeshacer = Stack()
stackRehacer = Stack()


while True:

    system("cls")

    print("Acciones realizadas: ")
    stackDeshacer.Show()

    print("Ultima acción realizada: ", stackDeshacer.Top())

    print("\n\n","."*25)
    print("Menú de opciones:\n1. Ingresar una nueva acción\n2. Ctrl + Z\n3. Ctrl + Y\n4. Mostrar la pila de acciones para rehacer\n5. Salir")
    opcion = input("Digite la opción seleccionada: ")


    if opcion == "1":
        accionNueva = input("\nEscriba una acción nueva: ")
        stackDeshacer.Push(accionNueva)
    elif opcion == "2":
        if stackDeshacer.Empty():
            print("\nError: No hay acciones para deshacer")
            op = input("\n\nDigite cualquier tecla para continuar....")
        else:
            stackRehacer.Push(stackDeshacer.Top())
            stackDeshacer.Pop()
    elif opcion == "3":
        if stackRehacer.Empty():
            print("\nError: No hay acciones para deshacer")
            op = input("\n\nDigite cualquier tecla para continuar....")
        else:
            stackDeshacer.Push(stackRehacer.Top())
            stackDeshacer.Pop()
    elif opcion == "4":
        print("\nAcciones para rehacer")
        stackRehacer.Show()
        op = input("\n\nDigite cualquier tecla para continuar....")
    elif opcion == "5":
        break

print("\n\n","."*25)
print("Programa terminado")
