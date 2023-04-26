#middle key of LL

class Node:
    def __init__(self, data):
        self.data = data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printList(self):
        temp = self.head 
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def middle(self):
        temp = self.head
        count=0
        while(temp is not None):
            temp=temp.next
            count+=1
        temp = self.head
        mid=count//2
        while(mid!=0):
            temp = temp.next
            mid-=1

        print("middle element " + str(temp.data))

ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)

ll.printList()
print()
ll.middle()