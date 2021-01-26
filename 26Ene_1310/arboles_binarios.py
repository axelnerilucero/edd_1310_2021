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
        if self.__root == None:
            print("Nada que eliminar")
        else:
            self.__remove( None, None, self.__root, value)

    def __remove(self, padre_hi, padre_hd, actual, value):
        if actual == None:
            print("Caso base")
            return None
        elif actual.data == value:
            print("Encontrado: ", actual.data)
            #Caso 1: hoja
            if actual.left == None and actual.right == None:
                if padre_hi != None:
                    padre_hi.left = None
                else:
                    padre_hd.right = None
            #Caso 2: con un hijo
            if (actual.left != None and actual.right == None) or (actual.left == None and actual.right != None):
                print("Es un nodo con un hijo: ", actual.data)
                if actual.left != None:
                    actual.data = actual.left.data
                    actual.left = None
                else:
                    actual.data = actual.right.data
                    actual.right = None
            #Caso 3: con dos hijos
            #·················El mas pequeño de la izquierda sube

            #Return actual
        elif value < actual.data:
            print("Buscar a la izquierda")
            self.__remove(actual, None, actual.left, value)
        else:
            print("Buscar a la derecha")
            self.__remove(None, actual, actual.right, value)



"""
arb = BinarySearchTree()
numeros = [3,4,1,2,5,6,7,8,9]
for num in numeros:
    arb.insert(num)
"""
