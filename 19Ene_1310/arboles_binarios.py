class NodoArbol:
    def __init__( self, value, left=None, right=None ):
        self.data = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__( self ):
        self.__root = None

    def insert( self, value ):
        #regla 1
        if self.__root is None:
            self.__root = NodoArbol(value, None, None)
        #regla 2
        else:
            self.__insert__(self.__root, value)

    def __insert__(self, nodo, value):
        if nodo.data == value:
            print("El dato ya existe, no se ingresa nada chamaco baboso")
        elif value < nodo.data:
            #regla 1
            if nodo.left == None:
                nodo.left = NodoArbol(value , None, None)
            #regla 2
            else:
                self.__insert__( nodo.left,value)
        else:
            #regla 1
            if nodo.right == None:
                nodo.right = NodoArbol(value , None, None)
            #regla 2
            else:
                self.__insert__( nodo.right,value)


    def __recorrido_in(self,nodo):
        if nodo != None:
            self.__recorrido_in(nodo.left)
            print(nodo.data,end=', ')
            self.__recorrido_in(nodo.right)

    def transversal( self, format="In orden"):
        if format == "In orden":
            self.__recorrido_in(self.__root)
        elif format =="Pre orden":
            print("Recorrido en pre")
        elif format == "Post orden":
            print("Post orden")
        else:
            print("Error, ese formato no existe")
        print("")

"""
arb = BinarySearchTree()
numeros = [3,4,1,2,5,6,7,8,9]
for num in numeros:
    arb.insert(num)
"""
