#https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0


def topView(root):
    if root is None:
        return 

    q = []

    m = dict()
    hd =0
    root.hd = hd

    q.append(root)

    while len(q):
        root = q[0]
        hd = root.hd

        if hd not in m:
            m[hd] = root.data

        if root.left:
            root.left.hd = hd-1
            q.append(root.left)

        if root.right:
            root.right.hd = hd+1
            q.append(root.right)

        q.pop(0)
    for i in sorted(m):
        print(m[i], end=" ")


if __name__ == '__main__':
 
    """ Create following Binary Tree
         1
        / \
       2   3
        \
          4
           \
            5
              \
               6
    """
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.right = newNode(4)
    root.left.right.right = newNode(5)
    root.left.right.right.right = newNode(6)
    print("The  top view of the tree is: ")
    topView(root)

# The top view of the tree is : 
# 2 1 3 6 

# Time complexity: O(N * log(N)), where N is the number of nodes in the given tree.
# Auxiliary Space: O(N), As we store nodes in the map and queue.


#Above approach using HashMap for Java
# Python code for the above approach
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.left = None
# 		self.right = None

# class QueueObj:
# 	def __init__(self, node, hd):
# 		self.node = node
# 		self.hd = hd

# def topView(root):
# 	if root is None:
# 		return

# 	q = []
# 	mp = {}
# 	mn = 0
# 	mx = 0
# 	# Level Order Traversal
# 	q.append(QueueObj(root, 0))
# 	while len(q) != 0:
# 		curr = q.pop(0)

# 		# only include in map if this is the
# 		# first node of this specific
# 		# horizontal distance
# 		if curr.hd not in mp:
# 			mp[curr.hd] = curr.node.data

# 		if curr.node.left is not None:
# 			# min can be found only in left side due to
# 			# "-1" minimum horizontal distance of any
# 			# node from root
# 			mn = min(mn, curr.hd-1)
# 			q.append(QueueObj(curr.node.left, curr.hd-1))

# 		if curr.node.right is not None:
# 			# max can be found only in right side due to
# 			# "+1" maximum horizontal distance of any
# 			# node from root
# 			mx = max(mx, curr.hd+1)
# 			q.append(QueueObj(curr.node.right, curr.hd+1))

# 	# traversal of (horizontal distance from rooo)
# 	# minimum to maximum
# 	for hd in range(mn, mx+1):
# 		print(mp[hd],end=" ")

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.right = Node(4)
# root.left.right.right = Node(5)
# root.left.right.right.right = Node(6)
# print("Following are nodes in top view of Binary Tree")
# topView(root)

# Following are nodes in top view of Binary Tree
# 2 1 3 6 

# Time Complexity: O(N), Since we only perform level-order traversal and print some part of the N nodes which at max will be 2N in case of skew tree
# Auxiliary Space: O(N), Since we store the nodes in the map and queue.