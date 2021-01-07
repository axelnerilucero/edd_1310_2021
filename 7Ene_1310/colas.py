from Queue import Queue, BoundedPriorityQueue
"""
q1 = Queue()
q1.enqueue(1)
q1.is_empty()
q1.enqueue(3)
q1.enqueue(12)
print(q1.to_string())

print ("Prueba 2 de Queue")
c1 = { "id":1,  "nombre":"Mario",  "balance": 20.5 }
c3 = { "id":2,  "nombre":"Diana",  "balance": 23320.5 }
c2 = { "id":3,  "nombre":"Bartolo",  "balance": 342314320.5 }

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
siguiente = atencion.dequeue(0)
print(f"Bienvenido sr. {siguiente['nombre']}, ¿en que podemos ayudarle?")
"""
print("Pruebas de las colas con prioridad acotada")
maestres = {"prioridad":4, "descripcion":"maestre",  "personas":["juan p", "diego h"] }
niños = {"prioridad":2, "descripcion":"niños",  "personas":["Santi h", "Angel h"] }
mecanicos = {"prioridad":4, "descripcion":"mecanicos",  "personas":["Diana T", "Maria Z"] }

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'] , maestres)
cpa.enqueue(niños['prioridad'] , niños)
cpa.enqueue(mecanicos['prioridad'] , mecanicos)
cpa.to_string()
