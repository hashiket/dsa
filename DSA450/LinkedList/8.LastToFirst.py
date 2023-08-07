#Move last element to front of a given Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printll(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def move(self):
        temp = self.head
        secl = None
        while temp.next != None:
            secl= temp
            temp = temp.next

        secl.next = None

        temp.next = self.head
        self.head = temp


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(1)
ll.push(4)
ll.push(5)
ll.push(4)

ll.printll()

ll.move()
print("####*****")

ll.printll()

            
