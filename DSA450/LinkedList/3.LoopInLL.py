#Detect Loop in LL

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
            temp= temp.next

    def loop(self):
        temp = self.head
        s=set()
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp=temp.next
        return False

    

ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.head.next.next.next.next = ll.head
print(ll.loop())
#ll.printll()

