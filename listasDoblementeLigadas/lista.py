class NodoDoble:
    def __init__( self , value ):
        self.data = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__( self ):
        self.__head = None
        self.__tail = None
        self.__size = 0


    def get_size( self ):
        return self.__size

    def is_empty( self ):
        return self.__head == None

    def append( self , value ):
        nuevo = NodoDoble(value)
        if self.__head == None:
            self.head = nuevo
        else:
            curr_node = self.__head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = nuevo
        self.__size += 1

    def transversal( self ):
        pibote = self.__head
        while pibote != None:
            print(f"{pibote.data} -->", end="")
            pibote = pibote.next
        print("")

    def reverse_transversal( self ):
        pibote = self.__tail
        while pibote != None:
            print(f"{pibote.data}")
            pibote = pibote.prev
        print("")

    """def remove_from_head( self , value ):
        pibote = self.__head
        if self.head.__data == value:
            self.__head = self.__head.next
        else:
            anterior = None
            while pibote.data != value and pibote.next != None:
                anterior = pibote
                anterior = pibote.next
            if pibote.data == value:
                anterior.next = pibote.next
            else:
                print (f"El dato no existe en la lista")"""


    """def remove_from_tail( self , value ):
        pibote = self.__tail
        if self.__tail.data == value:
            self.__tail = self.__tail.prev
        else:
            anterior = None
            while pibote.data != value and pibote.prev != None:
                anterior = pibote
                anterior = pibote.prev
            if pibote.data == value:
                anterior.prev = pibote.prev
            else:
                print (f"El dato no existe en la lista")"""

    """def finf_from_tail( self , posicion = None): #por defecto regresa el ultimo
        NodoDoble(value)
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
        return dato"""
