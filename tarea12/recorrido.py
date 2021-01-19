class NodoArbol:
    def __init__( self, value, left=None, rigth=None ):
        self.data = value
        self.left = left
        self.rigth = rigth

arbol = NodoArbol("+", NodoArbol("-",NodoArbol(5,None,None),NodoArbol(4,None,None)), NodoArbol("*",NodoArbol(3,None,None),NodoArbol(2,None,None)))
print(f"Arbol 1 con raiz: {arbol.data}")
print("RECORRIDOS ARBOL 1")
print("In orden \n(5,-,4,+,3*2)")
print("Pre orden \n(+,-,5,4,*,3,2)")
print("Post orden \n(5,4,-,3,2,*,+)")
arbol2 = NodoArbol(40, NodoArbol(30,NodoArbol(25,None,None),NodoArbol(35,None,None)), NodoArbol(50,NodoArbol(45,None,None),NodoArbol(60,None,None)))
print("\n\n\n")
print(f"Arbol 2 con raiz: {arbol2.data}")
print("RECORRIDOS ARBOL 2")
print("In orden \n(23,30,35,40,45,50,60)")
print("Pre orden \n(40,30,25,35,50,45,60)")
print("Post orden \n(25,35,30,45,60,50,40)")
