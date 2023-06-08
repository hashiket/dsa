#reverse LinkedList


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
            temp=temp.next

    def reverse(self):
        current = self.head
        prev=None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev 

             

ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)
ll.push(50)
ll.printll()
ll.reverse()
ll.printll()