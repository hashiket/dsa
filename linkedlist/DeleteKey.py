
class Node:
    def __init__(self, data):
        self.data =data
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def push(self, key):
        temp = Node(key)
        temp.next = self.root
        self.root = temp

    def delete(self, key):
        temp = self.root

        if self.root.data == key:
                self.root = self.root.next
                return 

        prev = temp
        while(temp):
           
            
            if temp.data == key:
                break
            prev=temp
            temp=temp.next

            
        prev.next=temp.next

    def printll(self):
        temp = self.root
        while(temp):
            print(temp.data)
            temp=temp.next


ll = LinkedList()
ll.push(3)
ll.push(2)
ll.push(6)
ll.push(7)
ll.push(2)
ll.push(5)

ll.delete(2)
ll.printll()