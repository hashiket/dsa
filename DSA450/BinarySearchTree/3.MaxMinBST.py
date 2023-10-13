#Find maximum (or minimum) in Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def findMax(root):
    if root is None:
        return float('-inf')

    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)

    if lres > res:
        res = lres
    elif rres > res:
        res = rres

    return res

def findMin(root):
    if root is None:
        return float('-inf')

    res = root.data
    lres = findMin(root.left)
    rres = findMin(root.right)

    if lres <res:
        res = lres
    elif rres < res:
        res = rres
    return res

if __name__ == '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)
 
    # Function call
    print("Maximum element is",
          findMax(root))
        
    print("Maximum element is",
          findMin(root))