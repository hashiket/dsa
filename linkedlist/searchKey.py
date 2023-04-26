class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, key):
        temp = Node(key)
        temp.next = self.head
        self.head = temp
    
    def find(self, key):
        temp = self.head
        while(temp):
            if temp.data == key:
                print("Found")
                return
            temp=temp.next
        print("Not Found")
        

ll = LinkedList()
ll.push(4)
ll.push(5)
ll.push(6)
ll.push(7)
ll.push(8)

ll.find(12)

