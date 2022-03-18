# Creacion de la clase (o el objeto) Nodo 
class Node():
    
    # Definir el constructor de la clase    
    def __init__(self, data, data2, data3, nxt = None):
        self.data = data # Data que pertenece al nodo 
        self.data2 = data2
        self.data3 = data3
        self.nxt = nxt # Puntero que pertence al nodo
    
    # Formato de salida por pantalla para el nodo
    def __str__(self):
        return str(self.data)