class Nodo:
    def __init__( self , value , siguiente = None):
        self.data = value #No estan encapsuladas
        self.siguiente = siguiente

class Linkedlist:
    def __init__( self ): #
        self.__head = None

    def is_empty( self ):
         return self.__head == None

    def append( self , value ):
        nuevo = Nodo( value )
        if self.__head == None: #self.is_empty
            self.__head = nuevo
        else:
            curr_node = self.__head
            while curr_node.siguiente != None: #Verifica que esta en el nodo final
                curr_node = curr_node.siguiente
            curr_node.siguiente = nuevo

    def transversal( self ): #Este es para recorrerlo
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} -> ", end="")
            curr_node = curr_node.siguiente
        print("")

    def remove( self , value ):
        curr_node = self.__head
        if self.__head.data == value:
            self.__head = self.__head.siguiente
        else:
            anterior = None
            while curr_node.data != value and curr_node.siguiente != None:
                anterior = curr_node
                curr_node = curr_node.siguiente
            if curr_node.data == value:
                anterior.siguiente = curr_node.siguiente
            else:
                print(f"El dato no existe en la lista")

    def preppend( self , value):
        nuevo = Nodo( value , self.__head)
        self.head = nuevo

    def tail( self ): #Este es para recorrerlo
        curr_node = self.__head
        while curr_node.siguiente != None:
            curr_node = curr_node.siguiente
        return curr_node

    def get( self , posicion = None): #por defecto regresa el ultimo
        contador = 0
        dato = None
        if posicion == None:
            dato = self.tail().data
        else:
            curr_node = self.__head
            while curr_node != None and contador != posicion:
                curr_node =curr_node.siguiente
                contador = contador + 1
            if contador == posicion:
                dato = curr_node.data
        return dato

class NodoDoble:
    def __init__( self , valor , anterior = None, siguiente = None):
        self.data = value
        self.next = siguiente
        self.prev = anterior

class DoubleLinkedList:
    def __init__( self ):
        self.__head = NodoDoble( None )
        self.__tail = NodoDoble( None )
        self.__size = 0

    def get_size( self ) :
        return self.__size

    def is_empty( self ):
        return self.__size ==0

    def append(self, value):
        if self.is_empty():
            nuevo = NodoDoble( value )
            self.__head = nuevo
            self.__tail = nuevo
        else:
            nuevo = NodoDoble(value , None , self.__tail)
            self.__tail.next = nuevo
            self.__tail = nuevo
        self.__size +=1

    def transversal( self ):
        curr_node = self.__head
        while curr_node != None:
            print(f" <-- { curr_node.data } -->" , end="")
            curr_node = curr_node.next
        print("")

    def reverse_transversal( self ):
        curr_node = self.__tail
        while curr_node != None:
            print(f" <-- { curr_node.data } -->" , end="")
            curr_node = curr_node.prev
        print("")

    def remove_from_head( self , value)    :
        curr_node = self.__head
        if self__head.data = value:
            self.__head = self.__head.next
            self.__head.prev = None
            self.__taill = self.__tail
        while curr_node.data != value anda curr_node != None:
            curr_node = curr_node.next
        if curr_node.data == value:
            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev
        curr_node.next = None
        curr_node.prev = None
        self.__size -= 1
