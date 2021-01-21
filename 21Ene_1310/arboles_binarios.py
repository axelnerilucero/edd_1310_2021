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

    def __recorrido_pre(self,nodo):
        if nodo:
            print(nodo.data,end=", ")
            self.__recorrido_pre(nodo.left)
            self.__recorrido_pre(nodo.right)

    def  __recorrido_pos(self,nodo):
        if nodo:
            self.__recorrido_pos(nodo.left)
            self.__recorrido_pos(nodo.right)
            print(nodo.data,end=", ")

    def transversal( self, format="In orden"):
        if format == "In orden":
            self.__recorrido_in(self.__root)
        elif format =="Pre orden":
            print("Recorrido en pre")
            self.__recorrido_pre(self.__root)
        elif format == "Post orden":
            print("Post orden")
            self.__recorrido_pos(self.__root)
        else:
            print("Error, ese formato no existe")
        print("")

    def search(self, value):
        if self.__root == None:
            return None
        else:
            return self.__search(self.__root, value)

    def __search(self, nodo, value):
        if nodo == None: #¿Esta vacio?
            print("caso base")
            return None
        elif nodo.data == value:   #Caso base de recursividad
            print("Encontrado")
            return nodo
        elif value < nodo.data:
            print("Buscar a la izquierda")
            return self.__search(nodo.left, value)
        else:
            print("Buscar a la derecha")
            return self.__search(nodo.right, value)

    def remove( self , value):
        #implementar search dentro de remove HAZ
        if encontrado.left == None and encontrado.right == None:
            print("Eliminando", encontrado.data)
            encontrado = None
        #Caso 2
        elif (encontrado.left != None and encontrado.right == None) or \
             (encontrado.left == None and encontrado.right != None):
             print(f"A eliminar: {encontrado.data}")



"""
arb = BinarySearchTree()
numeros = [3,4,1,2,5,6,7,8,9]
for num in numeros:
    arb.insert(num)
"""
