#Find a value in a BST

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right =  insert(root.right, data)

    return root

def search(root, data):
    if root is None or root.data==data:
        return root

    if root.data < data:
        return search(root.right, data)

    return search(root.left, data)

if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
 
    # Key to be found
    key = 6
 
    # Searching in a BST
    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")
 
    key = 60
 
    # Searching in a BST
    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")