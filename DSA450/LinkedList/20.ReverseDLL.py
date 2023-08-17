# Reverse the doubly linked list

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

        node.next =  self.head
        node.prev = None

        if self.head != None:
            self.head.prev = node

        self.head = node 

    def reverse(self):
        if self.head == None and self.head.next == None:
            return self.head

        curr = self.head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            curr.prev = temp
            prev = curr
            curr = temp
        self.head =  prev
            


    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp =  temp.next

        
ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)

ll.printLL()

ll.reverse()
print("************")
ll.printLL()