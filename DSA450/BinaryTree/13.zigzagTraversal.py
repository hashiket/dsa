#ZigZag Tree Traversal
#https://www.geeksforgeeks.org/zigzag-tree-traversal/

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def zigzag(root):
    if root is None:
        return 

    currentlevel = []
    nextlevel = []

    ltr = True

    currentlevel.append(root)

    while len(currentlevel)>0:
        curr = currentlevel.pop(-1)

        print(curr.data, end=" ")

        if ltr:
            if curr.left:
                nextlevel.append(curr.left)

            if curr.right:
                nextlevel.append(curr.right)

        else:

            if curr.right:
                nextlevel.append(curr.right)
            if curr.left:
                nextlevel.append(curr.left)

        if len(currentlevel)==0:
            ltr = not ltr

            currentlevel, nextlevel = nextlevel, currentlevel

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
print("Zigzag Order traversal of binary tree is")
zigzag(root)
 
#  ZigZag Order traversal of binary tree is 
# 1 3 2 7 6 5 4 

# Time Complexity: O(n) 
# Space Complexity: O(n)+(n)=O(n)