##Check if a linked list is a circular linked list.

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
        while temp != None:
            print(temp.data)
            temp= temp.next


    def isCircular(self):
        temp = self.head
        s = set()

        while temp!=None:
            if temp in s:
                return True
            
            s.add(temp)
            temp = temp.next

        return False

ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)
ll.push(50)
ll.head.next.next.next.next.next = ll.head

#ll.printLL()

print(ll.isCircular())
