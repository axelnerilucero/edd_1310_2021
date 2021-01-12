class Priorityqueue:
    def __init__( self ):
        prioridad = list()
        nombre = list()
        self.__data = list(zip(prioridad,nombre))


    def is_empty( self ):
        return len(self.__data) == 0

    def length( self ):
        return "Quedan " + str(len(self.__data)) + " personas"

    def enqueue( self, elem ):
        self.__data.append(elem)

    def dequeue( self ):
        self.__data.sort()
        if not self.is_empty():
            return self.__data.pop(0)
        else:
            print("Se ha despejado la nave")

    def to_string( self ):
        self.__data.sort()
        for elem in self.__data:
            if elem[0] == 1:
                print (f"prioridad: {elem[0]}, descripcion: ninas, nombre: {elem[1]} ")
            elif elem[0] == 2:
                print (f"prioridad: {elem[0]}, descripcion: ninos, nombre: {elem[1]} ")
            elif elem[0] == 3:
                print (f"prioridad: {elem[0]}, descripcion: mujeres u hombre, nombre: {elem[1]} ")
            elif elem[0] == 4:
                print (f"prioridad: {elem[0]}, descripcion: vigia, timonel o mecanico, nombre: {elem[1]} ")
            elif elem[0] == 5:
                print (f"prioridad: {elem[0]}, descripcion: capitan, nombre: {elem[1]} ")
            else:
                print(f"{elem[1]} no abandona el barco")
