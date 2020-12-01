class Nodo:
    def __init__( self , value , next = None):
        self.data = value
        self.next = next


class CircularList:
    def __init__( self ):
        self.__ref = None
        #self.__primero = self.__ref.next
        self.__size = 0

    def size( self ):
        return self.__size

    def is_empty( self ):
        return self.__ref == None

    def insertar( self , value ):
        #nuevo = Nodo( value )
        if (self.is_empty()):
            self.__ref = Nodo(value)
            self.__ref.next = self.__ref
        elif (int(value) > self.__ref.data):
            curr_node = self.__ref
            while curr_node.next != self.__ref:
                curr_node = curr_node.next
            self.__ref = Nodo(value, curr_node.next.next)
            curr_node.next.next = self.__ref
        elif (int(value) < self.__ref.data):
            curr_node = self.__ref
            while curr_node.next != self.__ref:
                curr_node = curr_node.next
            self.__ref = Nodo(value, curr_node.next)
            curr_node.next = self.__ref
        else:
            pass
        self.__size += 1


    def transversal( self ):
        curr_node = self.__ref
        while curr_node.next != self.__ref:
            print(f"{curr_node.data} --> ", end="")
            curr_node = curr_node.next
        print(f"{curr_node.data} --> ", end="")
        print("")

    def search(self, value):
        curr_node = self.__ref
        if self.__ref.data == value:
            self.__ref = self.__ref.next
        else:
            anterior = None
            while curr_node.data != value and curr_node.next != self.__ref:
                anterior = curr_node
                curr_node = curr_node.next
            if curr_node.data == value:
                print("Este dato ya existe")
            else:
                print(f"El dato se puede agregar a la lista")


    def remove(self, value):
        curr_node = self.__ref
        if self.__ref.data == value:
            self.__ref = self.__ref.next
        else:
            anterior = None
            while curr_node.data != value and curr_node.next != self.__ref:
                anterior = curr_node
                curr_node = curr_node.next
            if curr_node.data == value:
                anterior.next = curr_node.next
            else:
                print(f"El dato no existe en la lista")
        self.__size -= 1
