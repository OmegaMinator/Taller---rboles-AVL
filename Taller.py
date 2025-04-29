import sys 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 
#ok

def getHeight(node):
    if not node:
        return 0
    return node.height
#ok
def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right) #Corregido queda [getHeight(node.right) - getHeight(node.left)]
#ok ya que aunque las diapositivas dicen derecha menos izquierda realmente no importa el orden, porque tomamos si es 1 o -1
def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))
#correcto
def rotate_right(y):
    x = y.left 
    T2 = x.right
    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x
#esta rotación está mal planteada
def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y
#en estas rotaciones falta el balance; logramos cuadrarlas correctamente como se ve en el paint pero falta el último paso;
#le falta colocar: x.right = T2 y x.left =
class AVLTree:  
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node 
        
        updateHeight(node)
        
        balance = getBalance(node)

        if balance > 1 and getBalance(node.left) >= 0:
             rotate_right(node) 
        elif balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            rotate_right(node) 
        elif balance < -1 and getBalance(node.right) <= 0:
            rotate_left(node)
        elif balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            rotate_left(node) 
        
        return node 
    


avl = AVLTree()
values_to_insert = [10, 20, 30, 40, 50, 25]

print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)

print("\n--- Después de inserciones ---")
