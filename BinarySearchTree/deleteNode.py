
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def insert(root, key):
    if root is None :
        return Node(key)

    if root.data < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)

    return root

def minValue(root):
    current = root
    while(current.left is not None):
        current = current.left
    return current
def delete(root, key):
    if root is None:
        return root

    if root.data < key:
        root.right = delete(root.right, key)
    elif(key<root.data):
        root.left = delete(root.left, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValue(root.right)


        root.data = temp.data

        root.left = delete(root.left, root.data)

    return root


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
 
print("Inorder traversal of the given tree")
inorder(root)
 
print("\nDelete 20")
root = delete(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)
 
print("\nDelete 30")
root = delete(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)
 
print("\nDelete 50")
root = delete(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)
