from arboles_binarios import BinarySearchTree
abb = BinarySearchTree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(35)
abb.insert(89)
abb.insert(70)
abb.transversal()
abb.transversal("Pre orden")
abb.transversal("Post orden")
res = abb.search(1)
print(f"el resultado es: { res }")
abb.remove(35)
abb.transversal()