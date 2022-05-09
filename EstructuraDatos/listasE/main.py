from listasE.lists import SimplyLinkedList

# Crear una isntancia para la lista simplemente enlazada
lst = SimplyLinkedList()

# Ingresar un dato a la lista
lst.insertFirst(2)

# Ingresar mas datos al inicio de la lista
lst.insertFirst(3)
lst.insertFirst(1)


print("Lista con nuevos elementos al inicio:")
lst.showList()

print("\nCantidad de elementos en la lista:", lst.Size())

# Insertar elementos al final de la lista
lst.insertLast(5)
lst.insertLast("The_End")


print("\nLista con nuevos elementos al final:")
lst.showList()

# Insertar elementos en cuaquier parte de la lista
# lst.insert(2022, 1)

print("\nLista con nuevo elemento en cualquier parte: ")
lst.showList()


# lst.deleteFirst()

#print("\nLista con el primer elemento eliminado: ")
#lst.showList()


# lst.deleteLast()

# print("\nLista con el ultimo elemento eliminado: ")
#lst.showList()


lst.delete(22)
lst.showList()

print("\nElemento en la ultima posicion: ", lst.last)