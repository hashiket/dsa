#Intersection of two Sorted Linked Lists

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

def intersection(ll1, ll2):
    new = LinkedList()

    while ll1.head and ll2.head:
        if ll1.head.data == ll2.head.data:
            new.push(ll1.head.data)
            ll1.head = ll1.head.next
            ll2.head = ll2.head.next

        elif ll1.head.data <ll2.head.data:
            ll1.head = ll1.head.next
        else:
            ll2.head = ll2.head.next

    return new



first = LinkedList()
second = LinkedList()
first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(7)
 
second.push(4)
second.push(9)
second.push(7)
 
ans = intersection(first, second)
 
print("Intersection is : ", end=' ')
ans.printll()
