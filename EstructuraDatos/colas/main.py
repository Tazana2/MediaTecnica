import colas

cola = colas.Queue()

cola.Enqueue("Jara")

print("Personas que están en la cola: ")
cola.Show()

print("\nMás personas que están en la cola: ")
cola.Enqueue("André")
cola.Enqueue("Nicky")
cola.Enqueue("Santana")
cola.Enqueue("Valeria")
cola.Enqueue("Carlos")
cola.Show()

print("\nMás personas que están en la cola:")

