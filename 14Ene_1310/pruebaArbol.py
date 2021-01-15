class NodoArbol:
    def __init__( self, value, left=None, rigth=None ):
        self.data = value
        self.left = left
        self.rigth = rigth

arbol = NodoArbol("R", NodoArbol("C",None,None), NodoArbol("H",None,None))
print(arbol.left.data)
print(arbol.data)


arbol2 = NodoArbol(4,NodoArbol(3,NodoArbol(2,NodoArbol(1,None,None),None),None),NodoArbol(5,None,None))
print(arbol2.rigth.data)

arbol3 = NodoArbol()
