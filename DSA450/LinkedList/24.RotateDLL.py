#Rotate DoublyLinked list by N nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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


    def rotate(self, key):
        if self.head == None or self.head.next == None:
            return 

        current = self.head
        ct=1
        while ct<key and current != None:
            ct+=1
            current = current.next

        if current == None:
            return

        nthNode = current 

        while current.next!=None:
            current = current.next

        current.next = self.head

        self.head.prev = current

        self.head = nthNode.next

        self.head.prev = None
        
        nthNode.next = None




ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)
ll.push(50)
ll.push(60)


ll.printLL()
                
ll.rotate(2)

print("##############")

ll.printLL()


