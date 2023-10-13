#Inorder Traversal of a tree both using recursion and Iteration
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Recursive Implementation
# def inorder(root):
#     if root is None:
#         return root

#     inorder(root.left)
#     print(root.data, end=" ")
#     inorder(root.right)

#Iteration
def inorder(root):
    stack = deque()

    curr = root

    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.data, end=" ")
            curr = curr.right

if __name__ == '__main__':
 
    ''' Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    inorder(root)
 