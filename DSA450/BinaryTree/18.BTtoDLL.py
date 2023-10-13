#Convert Binary Tree to Doubly Linked List by keeping track of visited node


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

prev = None

def BinaryTree2DublyLinkedList(root):
    if root is None:
        return root


    head = BinaryTree2DublyLinkedList(root.left)

    global prev

    if prev is None:
        head = root
    else:
        root.left = prev
        prev.right = root

    prev = root

    BinaryTree2DublyLinkedList(root.right)

    return head


def print_dll(head):
    while head is  not None:
        print(head.data, end="")
        head = head.right



if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
      
    head = BinaryTree2DoubleLinkedList(root)
      
    # Print the converted list
    print_dll(head)
      

# 25 12 30 10 36 15 

# Note: The use of static variables like above is not a recommended practice, here static is used for simplicity. Imagine if the same function is called for two or more trees. The old value of prev would be used in the next call for a different tree. To avoid such problems, we can use a double-pointer or a reference to a pointer.

# Time Complexity: O(N), The above program does a simple inorder traversal, so time complexity is O(N) where N is the number of nodes in a given Binary tree.
# Auxiliary Space: O(N), For recursion call stack.