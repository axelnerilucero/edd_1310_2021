from lista import DoubleLinkedList

list = DoubleLinkedList()
print(f"¿l esta vacia? {list.is_empty()}")
list.append(1)
list.append(2)
list.append(3)
list.append(1)
list.append(2)
list.append(3)
#list.remove_from_head(3)
#list.remove_from_tail(2)
print(f"El tamaño de la lista es de {list.get_size()} elementos")
list.transversal()
#print(list.get(0))
# NOTE: No se porque no los muestra pero si estan, ya que en el metodo de get_size me los muestra
