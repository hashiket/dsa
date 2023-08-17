#Flatten a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.down = None
        self.right = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, head_ref, data):
        node = Node(data)
        node.down = head_ref

        head_ref = node

        return head_ref

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.down

    def merge(self, a, b):
        if a==None:
            return b 

        if b==None:
            return a 

        result =  None
        if a.data < b.data:
            result = a 
            result.down = self.merge(a.down, b)
        else:
            result = b 
            result.down = self.merge(a, b.down)
        result.right = None
        return result
        
    

    def flatten(self, root):
        if root== None or root.right==None:
            return root


        root.right = self.flatten(root.right)

        root = self.merge(root, root.right)

        return root

if __name__ == "__main__":
    L = LinkedList()

    L.head = L.push(L.head, 30)
    L.head = L.push(L.head, 8)
    L.head = L.push(L.head, 7)
    L.head = L.push(L.head, 5)

    L.head.right = L.push(L.head.right, 20)
    L.head.right = L.push(L.head.right, 10)
 
    L.head.right.right = L.push(L.head.right.right, 50)
    L.head.right.right = L.push(L.head.right.right, 22)
    L.head.right.right = L.push(L.head.right.right, 19)
 
    L.head.right.right.right = L.push(L.head.right.right.right, 45)
    L.head.right.right.right = L.push(L.head.right.right.right, 40)
    L.head.right.right.right = L.push(L.head.right.right.right, 35)
    L.head.right.right.right = L.push(L.head.right.right.right, 20)
 
    # Function call
    L.head = L.flatten(L.head)
 
    L.printLL()