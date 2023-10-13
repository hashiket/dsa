#Diameter of a Binary Tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0

    return 1+max(height(node.left),height(node.right))


def diameter(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(lheight+rheight+1,max(ldiameter,rdiameter))

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    # Function Call
    print(diameter(root))

# Diameter of the given binary tree is 4

# Time Complexity: O(N2)
# Auxiliary Space: O(N) for call stack



# Python3 code to implement the above approach that uses the
# morris traversal algorithm

# A tree node
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.left = None
# 		self.right = None

# # Create a new node
# def newNode(data):
# 	node = Node(data)
# 	return node

# # Morris traversal to find the diameter of the binary tree
# def findDiameter(root):
# 	ans = 0
# 	curr = root

# 	while curr is not None:
# 		if curr.left is None:
# 			curr = curr.right
# 		else:
# 			pre = curr.left
# 			while pre.right is not None and pre.right != curr:
# 				pre = pre.right
# 			if pre.right is None:
# 				pre.right = curr
# 				curr = curr.left
# 			else:
# 				pre.right = None
# 				leftHeight = 0
# 				rightHeight = 0
# 				temp = curr.left
# 				while temp is not None:
# 					leftHeight += 1
# 					temp = temp.right
# 				temp = curr.right
# 				while temp is not None:
# 					rightHeight += 1
# 					temp = temp.left
# 				ans = max(ans, leftHeight + rightHeight + 1)
# 				curr = curr.right
# 	return ans


# # Driver code
# if __name__ == '__main__':
# 	# Create the given binary tree
# 	root = newNode(1)
# 	root.left = newNode(2)
# 	root.right = newNode(3)
# 	root.left.left = newNode(4)
# 	root.left.right = newNode(5)

# 	# Find the diameter of the binary tree using Morris
# 	# traversal
# 	diameter = findDiameter(root)

# 	# Print the diameter of the binary tree
# 	print("The diameter of given binary tree is", diameter)
