
def cuenta_regresiva(numero):
    if numero >= 0:
        print(numero)
        return cuenta_regresiva(numero-1)


cuenta_regresiva(10)

print("\n""\n""\n")

class Stack:
    def __init__( self ):
        self.__data = list()


    def is_empty( self ):
        return len(self.__data) == 0

    def length( self ):
        return len(self.__data)

    def pop( self ):
        if self.is_empty():
            print("Pila vacia")
        else:
            return self.__data.pop()

    def push( self , value ):
        self.__data.append(value)

    def peek( self ):
        return self.__data[len(self.__data)- 1]

    def to_string( self ):
        for value in self.__data[::-1]:
            print(f" │ {value} │ ")
            print(" -----")

duracell = Stack()
duracell.push(4)
duracell.push(3)
duracell.push(2)
duracell.push(1)
aux = list()
duracell.to_string()
def mitadPila(pila,tam):
    if tam != mitad(pila,tam):
        aux.append(pila.pop())
        print(aux)

        return mitadPila(pila,tam-1)

def mitad(pila,tam):
    mitad = (pila.length()/2)
    return mitad

mitadPila(duracell, duracell.length())
