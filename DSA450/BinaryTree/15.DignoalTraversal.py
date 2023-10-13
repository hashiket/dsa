#Diagonal Traversal of Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def  diagonalPrintUtil(root, d, diagonalPrintMap):
    if root is None:
        return 
    try:
        diagonalPrintMap[d].append(root.data)
    except KeyError:
        diagonalPrintMap[d] = [root.data]

    diagonalPrintUtil(root.left, d+1, diagonalPrintMap)

    diagonalPrintUtil(root.right, d, diagonalPrintMap)


def diagonalPrint(root):
    if root is None:
        return

    diagonalPrintMap = dict()

    diagonalPrintUtil(root, 0,  diagonalPrintMap)

    for i in diagonalPrintMap:
        for j in diagonalPrintMap[i]:
            print(j, end=" ")
        print()


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
 
diagonalPrint(root)

# Diagonal Traversal of binary tree : 
# 8 10 14 
# 3 6 7 13 
# 1 4 

# Time complexity: O( N logN )
# Auxiliary Space: O( N )


# from collections import deque

# # A binary tree node


# class Node:

# 	# Constructor to create a
# 	# new binary tree node
# 	def __init__(self, data):
# 		self.data = data
# 		self.left = None
# 		self.right = None


# def diagonal(root):
# 	out = []
# 	node = root

# 	# queue to store left nodes
# 	left_q = deque()
# 	while node:

# 		# append data to output array
# 		out.append(node.data)

# 		# if left available add it to the queue
# 		if node.left:
# 			left_q.appendleft(node.left)

# 		# if right is available change the node
# 		if node.right:
# 			node = node.right
# 		else:

# 			# else pop the left_q
# 			if len(left_q) >= 1:
# 				node = left_q.pop()
# 			else:
# 				node = None
# 	return out


# # Driver Code
# root = Node(8)
# root.left = Node(3)
# root.right = Node(10)
# root.left.left = Node(1)
# root.left.right = Node(6)
# root.right.right = Node(14)
# root.right.right.left = Node(13)
# root.left.right.left = Node(4)
# root.left.right.right = Node(7)

# print(diagonal(root))
