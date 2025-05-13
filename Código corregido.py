class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y

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

        if balance > 1 and value < node.left.value:
            return rotate_right(node)
        if balance < -1 and value > node.right.value:
            return rotate_left(node)
        if balance > 1 and value > node.left.value:
            node.left = rotate_left(node.left)
            return rotate_right(node)
        if balance < -1 and value < node.right.value:
            node.right = rotate_right(node.right)
            return rotate_left(node)

        return node

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._get_min(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)

        updateHeight(node)
        balance = getBalance(node)

        if balance > 1 and getBalance(node.left) >= 0:
            return rotate_right(node)
        if balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            return rotate_right(node)
        if balance < -1 and getBalance(node.right) <= 0:
            return rotate_left(node)
        if balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            return rotate_left(node)

        return node

    def _get_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if not node:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)

    def print_tree(self, node=None, level=0, prefix="Root: "):
        node = node if node else self.root
        if node:
            print(" " * (level * 4) + prefix + f"{node.value} (h={node.height}, bf={getBalance(node)})")
            if node.left:
                self.print_tree(node.left, level + 1, "L--- ")
            if node.right:
                self.print_tree(node.right, level + 1, "R--- ")
