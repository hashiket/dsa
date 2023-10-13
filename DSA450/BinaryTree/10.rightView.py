#Right View of a Binary Tree using Recursion:

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# def rightUtilLevel(root, level, max_level):
#     if root is None:
#         return

#     if max_level[0] <level:
#         print(root.data, end=" ")
#         max_level[0]=level

#     rightUtilLevel(root.right, level+1, max_level)
#     rightUtilLevel(root.left, level+1, max_level)


# def rightView(root):
#     max_level = [0]
#     rightUtilLevel(root, 1, max_level)




# 1    3    7    8    

# Time Complexity: O(N), Traversing the Tree having N nodes
# Auxiliary Space: O(N), 


from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def rightView(root):
    if root is None:
        return

    q = deque()

    q.append(q)

    while q:

        n=len(q)

        while n>0:
            n-=1

            node = q.popleft()

            if n==0:
                print(root.data, end=" ")

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
 
rightView(root)

# 1 3 7 8 

# Time Complexity: O(N), where N is the number of nodes in the binary tree.
# Auxiliary Space: O(N) since using auxiliary space for queue