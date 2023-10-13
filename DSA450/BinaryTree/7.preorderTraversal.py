#Preorder Traversal of a tree both using recursion and Iteration
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#recursion
# def preorder(root):
#     if root is None:
#         return

#     print(root.data, end=" ")
#     preorder(root.left)
#     preorder(root.right)


#Iteration
def preorder(root):
    if root is None :
        return

    stack = deque()

    stack.append(root)

    while stack:
        curr = stack.pop()
        print(curr.data, end=" ")
        if curr.right:
            stack.append(curr.right)

        if curr.left:
            stack.append(curr.left)


#Iteration optimize
# def preorderIterative(root):
 
#     # return if the tree is empty
#     if root is None:
#         return
 
#     # create an empty stack and push the root node
#     stack = deque()
#     stack.append(root)
 
#     # start from the root node (set current node to the root node)
#     curr = root
 
#     # loop till stack is empty
#     while stack:
 
#         # if the current node exists, print it and push its right child
#         # to the stack before moving to its left child
#         if curr:
#             print(curr.data, end=' ')
 
#             if curr.right:
#                 stack.append(curr.right)
 
#             curr = curr.left
#         # if the current node is None, pop a node from the stack
#         # set the current node to the popped node
#         else:
#             curr = stack.pop()
 









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
 
    preorder(root)