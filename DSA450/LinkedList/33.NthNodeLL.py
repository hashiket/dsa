#Nth node from end of linked list

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

    def printLL(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    def printNthNode(self, k):
        temp = self.head

        l = 0

        while temp:
            l+=1
            temp=temp.next
        
        temp = self.head
        if k>l:
            print("Please enter valid location")
            return

        for i in range(l-k):
            temp = temp.next

        print(temp.data)


ll  = LinkedList()

ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(6)
ll.push(7)
ll.push(8)
ll.push(9)
ll.push(10)


ll.printLL()

ll.printNthNode(8)        