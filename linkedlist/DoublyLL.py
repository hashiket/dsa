class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head 
        if self.head != None:
            self.head.prev = node
        self.head = node

    def printLL(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def insert(self, prev, data):
        if prev is None:
            return None

        node = Node(data)
        node.next = prev.next
        prev.next = node
        node.prev = prev
        if node.next != None:
            node.next.prev = node

        

ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)

ll.insert(ll.head.next, 50)

ll.printLL()

