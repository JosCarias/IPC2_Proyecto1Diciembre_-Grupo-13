import random
from nodo import Nodo

class ListaDoble:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.Cursor = None
        self.bandera = True


    def insertarNodo(self, node):
        if self.primero is None:
            self.primero = self.ultimo = self.Cursor = Nodo(node)
            # self.Cursor.node.CantidadReproducciones = 1 # Cuenta la primera cancion que se repoduce
        else: 
            actual = self.ultimo
            self.ultimo = actual.siguiente = Nodo(node)
            self.ultimo.anterior = actual
        self .__unir_nodos()

    # Verifica la existencia de elemntos en una lista
    def verificador(self):
        actual = self.primero
        if self.primero != None:
            return True
        else:
            return False
        
    def recorrer(self):
        actual = self.primero
        if self.primero != None:
            while actual:
                print('Cancion: ' + actual.node.nombre)
                print('Artista: ' + actual.node.artista)
                print('Album: ' + actual.node.album)
                print('Imagen: ' + actual.node.imagen)
                print('Ruta: ' + actual.node.ruta)
                print('\n') 
                actual = actual.siguiente
                if actual == self.primero:
                    break
        else:
            print('La lista está vacía\n')
    

    def recorrer_playlist(self):
        actual = self.primero
        salida=""
        while actual:
            print('Nombre de playlist: ' + actual.node.nombre)
            print('Canciones: ')
            aux = actual.node.canciones.primero
            salida+="-"+str(actual.node.nombre)+"\n"
            while aux:
                print(aux.node.nombre)
                aux = aux.siguiente
                salida+=str(aux.node.nombre)+"\n"
                if aux == actual.node.canciones.primero:
                    break
            actual = actual.siguiente
            print('\n') 
            if actual == self.primero:
                break
        return salida

    
    # Esta funcion sirve para la función aleatorio
    def BuscaNodo(self, indice):
        contador = 0
        aux = self.primero
        if aux != None:
            while aux != None:
                if contador == indice:
                    return aux
                else:
                    aux = aux.siguiente
                    contador = contador + 1
                    if aux == self.primero:
                        return None
        return None
    
    def siguienteCancion(self):
        if self.bandera:
            self.Cursor = self.Cursor.siguiente
            cancion = self.Cursor.node
        else:
            indice = random.randint(0, int(self.cantidadElementos())-1)
            self.Cursor = self.BuscaNodo(indice)
            cancion = self.Cursor.node
        cancion.CantidadReproducciones = int(cancion.CantidadReproducciones)+1 # Contador de número de reproducciones
        return cancion

    def anteriorCancion(self):
        if self.bandera:
            self.Cursor = self.Cursor.anterior
            cancion = self.Cursor.node
        else:
            indice = random.randint(0, int(self.cantidadElementos())-1)
            self.Cursor = self.BuscaNodo(indice)
            cancion = self.Cursor.node
        cancion.CantidadReproducciones = int(cancion.CantidadReproducciones)+1 # Contador de número de reproducciones
        return cancion

    def aleatorioCancion(self):
        if self.bandera:
            self.bandera = False
            print('Entre en aleatorio')
        else:
            self.bandera = True
            print('He salido de aleatorio')
        return 
        
        
    def cantidadElementos(self):
        contador = 0
        aux = self.primero
        if aux != None:
            while aux != None:
                contador = contador + 1
                aux = aux.siguiente
                if aux == self.primero:
                    return contador

    def BuscarPorIndice(self, indice):
        contador = 0
        aux = self.primero
        while aux and contador != indice:
            aux = aux.siguiente
            contador += 1
        return aux.node if aux else None
    
    def BuscarPorAlbum(self, album):
        aux = self.primero
        if aux != None:
            while aux != None:
                if aux.node.album == album:
                    return True
                else:
                    aux = aux.siguiente
                    if aux == self.primero:
                        return False
        return False
    
    def BuscarPorArtista(self, artista):
        aux = self.primero
        if aux != None:
            while aux != None:
                if aux.node.artista == artista:
                    return True
                else:
                    aux = aux.siguiente
                    if aux == self.primero:
                        return False
        return False
    
    def buscar_por_nombre(self, nombre):
        if self.primero is None:  # Verificar si la lista está vacía
            return None
    
        actual = self.primero  # Empezar desde el primer nodo
        while actual:
            if actual.node.nombre == nombre:  # Verificar si el nombre coincide
                return actual.node  # Devolver el nodo si se encuentra el nombre
    
            actual = actual.siguiente  # Moverse al siguiente nodo
            if actual == self.primero:  # Si volvemos al inicio, hemos recorrido toda la lista
                break  # Romper el bucle para evitar un bucle infinito si no se encuentra el nombre
            
        return None

    def __unir_nodos(self):
        if self.primero!=None:
            self.primero.anterior=self.ultimo
            self.ultimo.siguiente=self.primero

    