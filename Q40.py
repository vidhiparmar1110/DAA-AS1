class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    if root is not None:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

root = Node('A')

root.left = Node('B')
root.right = Node('C')

root.left.left = Node('D')
root.left.right = Node('E')

root.right.left = Node('F')
root.right.right = Node('G')

print("Preorder:")
preorder(root)

print("\n\nInorder:")
inorder(root)

print("\n\nPostorder:")
postorder(root)
