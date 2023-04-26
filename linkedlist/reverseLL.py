#reverse LinkList

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

    def reverse(self):
        prev = None
        current = self.head

        while(current is not None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev


    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp=temp.next

ll = LinkedList()
ll.push(30)
ll.push(67)
ll.push(34)
ll.push(45)
ll.printList()
ll.reverse()
print()
ll.printList()