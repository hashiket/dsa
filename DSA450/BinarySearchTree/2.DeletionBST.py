#Deletion in Binary Search Tree (BST)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return None

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def insert(root, data):
    if root is None:
        return Node(data)

    if root.data < data:
        root.right = insert(root.right, data)
    elif root.data > data:
        root.left = insert(root.left, data)

    return root


def delete(root, data):
    if root is None:
        return root

    if root.data < data:
        root.left = delete(root.left, data)
        return root
    elif root.data > data:
        root.right = delete(root.right, data)
        return root

    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp
    else:
        succParent = root

        succ = root.right
        while succ.left is not None:
            succParent = root
            succ = succ.left

        if succParent!=root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right

        root.data = succ.data
        del succ
        return root

if __name__ == '__main__':
    # Let us create following BST
    #          50
    #       /     \
    #      30      70
    #     /  \    /  \
    #   20   40  60   80
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
 
    print("Original BST: ", end='')
    inorder(root)
 
    print("\n\nDelete a Leaf Node: 20")
    root = delete(root, 20)
    print("Modified BST tree after deleting Leaf Node:")
    inorder(root)
 
    print("\n\nDelete Node with single child: 70")
    root = delete(root, 70)
    print("Modified BST tree after deleting single child Node:")
    inorder(root)
 
    print("\n\nDelete Node with both child: 50")
    root = delete(root, 50)
    print("Modified BST tree after deleting both child Node:")
    inorder(root)

        


    
# Original BST: 20 30 40 50 60 70 

# Delete a Leaf Node: 20
# Modified BST tree after deleting Leaf Node:
# 30 40 50 60 70 

# Delete Node with single child: 70
# Modified BST tree after deleting single child No...

# Time Complexity: O(h), where h is the height of the BST. 
# Auxiliary Space: O(n).