# How does Level Order Traversal work?

# The main idea of level order traversal is to traverse all the nodes of a lower level before moving to any of the nodes of a higher level. This can be done in any of the following ways: 

#     the naive one (finding the height of the tree and traversing each level and printing the nodes of that level)
#     efficiently using a queue.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)


def printCurrentLevel(root, level):
    if root is None:
        return None
    if level==1:
        print(root.data, end="")
    elif level>1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    print("Level order traversal of binary tree is -")
    printLevelOrder(root)
 
#  Level Order traversal of binary tree is 
# 1 2 3 4 5 

# Time Complexity: O(N2), where N is the number of nodes in the skewed tree.
# Auxiliary Space: O(1) If the recursion stack is considered the space used is O(N).


#using queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelOrder(root):
    if root is None:
        return None

    queue = []

    queue.append(root)

    while(len(queue) > 0):
        print(queue[0].data, end=" ")

        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    print("Level Order Traversal of binary tree is -")
    printLevelOrder(root)


# Level Order traversal of binary tree is 
# 1 2 3 4 5 

# Time Complexity: O(N) where N is the number of nodes in the binary tree.
# Auxiliary Space: O(N) where N is the number of nodes in the binary tree.