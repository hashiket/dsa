#Construct Binary Tree from String with bracket representation

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root):
    if root:
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)

def findIndex(Str, si, ei):
    if(si<ei):
        return -1

    s = []
    for i in range(si, se+1):
        if Str[i] == '(':
            s.append(Str[i])

        elif (Str[i] == ')'):
            if (s[-1] == '('):
                s.pop(-1)
 
                # if stack is empty, this is
                # the required index
                if len(s) == 0:
                    return i
    return -1 


def treeFromString(Str, si, ei):
    if si>ei:
        return 

    root = Node(ord(Str[si])- ord('0'))
    index =-1

    if (si+1 <= ei and Str[si+1] == '('):
        index = findIndex(Str, si+1, ei)

    if (index != -1):
 
        # call for left subtree
        root.left = treeFromString(Str, si + 2,
                                   index - 1)
 
        # call for right subtree
        root.right = treeFromString(Str, index + 2,
                                    ei - 1)
    return root


if __name__ == '__main__':
    Str = "4(2(3)(1))(6(5))"
    root = treeFromString(Str, 0, len(Str) - 1)
    preOrder(root)