#Postorder Traversal of a tree both using recursion and Iteration
from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#recursion
# def postorder(root):
#     if root is None:
#         return 


#     postorder(root.left)
#     postorder(root.right)
#     print(root.data, end=" ")




def postorder(root):
    if root is None:
        return

    stack = deque()

    stack.append(root)

    out = deque()

    while stack:

        curr = stack.pop()

        out.append(curr.data)

        if curr.left:
            stack.append(curr.left)

        if curr.right:
            stack.append(curr.right)

    while out:
        print(out.pop(), end=" ")










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
 
    postorder(root)