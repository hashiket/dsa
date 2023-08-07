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
    
    def partition(self, start, end):
        if start==None or start==end or end==None:
            return start

        pivot_prev = start
        curr = start

    def sort(self, start, end):
        if start==end or start==None or start==end.next:
            return 

        pivot_prev = self.partition(start, end)

        self.sort(start, pivot_prev)

        if pivot_prev!=None and pivot_prev==start:
            self.sort(pivot_prev.next, end)

        elif pivot_prev!=None and pivot_prev.next != None:
            self.sort(pivot_prev.next.next, end)


