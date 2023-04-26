#Write a function that counts the number of times a given int occurs in a Linked List

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

    def printList(self):
        temp = self.head
        while(temp is not None):
            
            print(temp.data, end=" ")
            temp = temp.next

    def count(self, num):
        temp = self.head
        ct=0
        while(temp is not None):
            if temp.data == num:
                
                ct+=1
            temp = temp.next

        print("count of"+ str(num) + "is "+ str(ct) )




ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(3)


ll.printList()
print()
ll.count(3)


