#O(h)timeComplexity-SapceComplexityO(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end="")
        inorder(root.right)

def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)

    else:
        root.right = insert(root.right, key)

    return root

def delete(root, key):
    if root is None:
        return root
    
    if key < root.data:
        root.left = delete(root.left, key)
        return root
    elif key > root.data:
        root.right = delete(root.right, key)
        return root

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        succParent =root
        succ = root.right

        while succ.left!=None:
            succParent = succ
            succ = succ.left

        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right

        root.data = succ.data

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
 
print("\n\nDelete 20")
root = delete(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)
 
print("\n\nDelete 30")
root = delete(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)
 
print("\n\nDelete 50")
root = delete(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)


