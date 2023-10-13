#Left View of a tree
##recursive
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def leftViewUtil(root, level, max_level):
#     if root is None:
#         return

#     if (max_level[0] < level):
#         print(root.data, end=" ")
#         max_level[0] = level

#     leftViewUtil(root.left, level+1, max_level)
#     leftViewUtil(root.right, level+1, max_level)


# def leftView(root):
#     max_level = [0]
#     leftViewUtil(root, 1, max_level)



# if __name__ == '__main__':
#     root = Node(10)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(7)
#     root.left.right = Node(8)
#     root.right.right = Node(15)
#     root.right.left = Node(12)
#     root.right.right.left = Node(14)
     
#     leftView(root)


# 10 2 7 14 

# Time Complexity: O(N), The function does a simple traversal of the tree, so the complexity is O(n). 
# Auxiliary Space: O(h),

#Print Left View of a Binary Tree Using Level Order Traversal: 
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftView(root):
    if root is None:
        return

    q = []
    q.append(root)

    while len(q):
        
        n = len(q)

        for i in range(1, n+1):
            temp = q.pop(0)

            if i==1:
                print(temp.data, end=" ")

            if temp.left:
                q.append(temp.left)

            if temp.right:
                q.append(temp.right)


if __name__ == '__main__':
 
    root = newNode(10)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(8)
    root.right.right = newNode(15)
    root.right.left = newNode(12)
    root.right.right.left = newNode(14)
    leftView(root)