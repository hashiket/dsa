#Find the Maximum Depth or Height of given Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxHeigth(root):
    if root is None:
        return 0
    else:
        lheight = maxHeigth(root.left)
        rheight = maxHeigth(root.right)

        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
 
print("Height of tree is %d" % (maxHeigth(root)))

# Height of tree is 3

# Time Complexity: O(N) (Please see the post on Tree Traversal for details)
# Auxiliary Space: O(N) due to recursive stack.



#Find the Maximum Depth or Height of given Binary Tree
#https://www.geeksforgeeks.org/find-the-maximum-depth-or-height-of-a-tree/
# class Node:
 
#     def __init__(self):
#         self.key = 0
#         self.left, self.right = None, None
 
# # Utility function to create a new node
 
 
# def newNode(key):
 
#     temp = Node()
#     temp.key = key
#     temp.left, temp.right = None, None
#     return temp
 
 
# # Function to find the height(depth) of the tree
# def height(root):
 
#     # Initialising a variable to count the
#     # height of tree
#     depth = 0
 
#     q = []
 
#     # appending first level element along with None
#     q.append(root)
#     q.append(None)
#     while(len(q) > 0):
#         temp = q[0]
#         q = q[1:]
 
#         # When None encountered, increment the value
#         if(temp == None):
#             depth += 1
 
#         # If None not encountered, keep moving
#         if(temp != None):
#             if(temp.left):
#                 q.append(temp.left)
 
#             if(temp.right):
#                 q.append(temp.right)
 
#         # If queue still have elements left,
#         # append None again to the queue.
#         elif(len(q) > 0):
#             q.append(None)
#     return depth
 
# # Driver program
 
 
# # Let us create Binary Tree shown in above example
# root = newNode(1)
# root.left = newNode(2)
# root.right = newNode(3)
 
# root.left.left = newNode(4)
# root.left.right = newNode(5)
 
# print(f"Height(Depth) of tree is: {height(root)}")
 
 
# # This code is contributed by shinjanpatra
# Output

# Height(Depth) of tree is: 3

# Time Complexity: O(N)
# Auxiliary Space: O(N)