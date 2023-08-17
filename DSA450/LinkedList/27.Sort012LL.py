#Sort a LL of 0's, 1's and 2's

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


    def sortll(self):
        temp = self.head

        count = [0, 0, 0]

        while temp!=None:
            count[temp.data] +=1
            temp= temp.next

        temp = self.head
        i=0
        while temp!=None:
            if count[i]==0:
                i+=1
            else:
                temp.data = i 
                count[i]-=1
                temp = temp.next


ll  = LinkedList()

ll.push(1)
ll.push(0)
ll.push(1)
ll.push(0)
ll.push(2)
ll.push(0)
ll.push(2)

ll.printLL()

ll.sortll()

ll.printLL()

