class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)

    if key<root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

def iterativeSearch(root, key):
    while root != None:
        

        if key< root.data:
            root = root.left

        elif key > root.data:
            root = root.right
        else:
            return True
    return False

root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)
if iterativeSearch(root, 60):
    print("Yes")
else:
    print("No")