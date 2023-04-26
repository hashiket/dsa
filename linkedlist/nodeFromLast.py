#Program for Nth node from the end of a Linked List

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


    def printNthFromLast(self, n):
        temp = self.head
        length = 0
        while(temp is not None):
            temp = temp.next
            length+=1
        print(length)
        if n>length:
            print("location is greater than linklist")
            return 

        temp = self.head
        for i in range(0,length-n):
            temp = temp.next
        print(temp.data)

if __name__=="__main__":
    ll = LinkedList()
    ll.push(35)
    ll.push(30)
    ll.push(67)
    ll.push(89)

    ll.printNthFromLast(1)

