#A program to check if a Binary Tree is BST or not

INT_MAX = 4294967296
INT_MIN = -4294967296

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root):
    return isBSTUtil(root, INT_MIN, INT_MAX)

def isBSTUtil(root, mini, maxi):
    if root is None:
        return True

    if root.data < mini or root.data > maxi:
        return False

    return (isBSTUtil(root.left, mini, root.data-1) and isBSTUtil(root.right, root.data+1, maxi))
if __name__ == "__main__":
  root = Node(4)
  root.left = Node(2)
  root.right = Node(5)
  root.left.left = Node(1)
  root.left.right = Node(3)
 
  # Function call
  if (isBST(root)):
      print("Is BST")
  else:
      print("Not a BST")
    

# Is BST

# Time Complexity: O(N), Where N is the number of nodes in the tree
# Auxiliary Space: O(1), if Function Call Stack size is not considered, otherwise O(H) where H is the height of the tree
