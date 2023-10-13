#Inorder predecessor and successor for a given key in BST

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)

    if root.data < data:
        root.right = insert(root.right, data)
    elif root.data > data:
        root.left = insert(root.left, data)

    return root

def findPreSuc(root, key):
    if root is None:
        return 

    if root.data == key:
        if root.left is not None:
            tmp = root.left
            while tmp.right:
                tmp = tmp.right
            findPreSuc.pre = tmp

        if root.right is not None:
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            findPreSuc.suc = tmp
        return

    if root.data > key:
        findPreSuc.suc = root
        findPreSuc(root.left, key)
    else:
        findPreSuc.pre = root
        findPreSuc(root.right, key)


key = 65 #Key to be searched in BST
  
""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80
"""
root = None
root = insert(root, 50)
insert(root, 30);
insert(root, 20);
insert(root, 40);
insert(root, 70);
insert(root, 60);
insert(root, 80);
 
# Static variables of the function findPreSuc
findPreSuc.pre = None
findPreSuc.suc = None
 
findPreSuc(root, key)
 
if findPreSuc.pre is not None:
    print("Predecessor is", findPreSuc.pre.data)
 
else:
    print("No Predecessor")
 
if findPreSuc.suc is not None:
    print("Successor is", findPreSuc.suc.data)
else:
    print("No Successor")