#Check if a tree is balanced or not


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0

    return max(height(root.left), height(root.right))+ 1

def isBalanced(root):
    if root is None:
        return True

    lh = height(root.left)
    rh = height(root.right)

    if (abs(lh-rh) <= 1) and isBalanced(root.left) is True and isBalanced(root.right) is True:
        return True

    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
if isBalanced(root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")

# Tree is not balanced

# Time Complexity: O(n^2) in case of full binary tree.
# Auxiliary Space: O(n) space for call stack since using recursion



"""
Python3 program to check if a tree is height-balanced
"""
# A binary tree Node


class Node:

	# Constructor to create a new Node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Function to check if tree is height-balanced or not


def isBalanced(root):

	# Base condition
	if root is None:
		return True

	# Compute height of left subtree
	lh = isBalanced(root.left)

	# If left subtree is not balanced,
	# return 0
	if lh == 0:
		return 0

	# Do same thing for the right subtree
	rh = isBalanced(root.right)
	if rh == 0:
		return 0

	# Allowed values for (lh - rh) are 1, -1, 0
	if (abs(lh - rh) > 1):
		return 0

	# If we reach here means tree is
	# height-balanced tree, return height
	# in this case
	else:
		return max(lh, rh) + 1


# Driver code
if __name__ == '__main__':
	root = Node(10)
	root.left = Node(5)
	root.right = Node(30)
	root.right.left = Node(15)
	root.right.right = Node(20)
	if (isBalanced(root) == 0):
		print("Not Balanced")
	else:
		print("Balanced")

# This code is contributed by Shweta Singh
