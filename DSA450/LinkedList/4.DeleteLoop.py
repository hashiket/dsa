#delete the loop in ll

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data ):
        node = Node(5)
        node.next = self.head
        self.head = node

    def deleteLoop(self):
        slow = self.head
        fast = self.head 
        if self.head is None:
            return 

        if self.head.next is None:
            return

        while slow and fast and fast.next :
            slow = slow.next
            fast = fast.next.next

            if slow.next == fast.next:
                slow = self.head
                while slow.next != fast.next:
                    slow = slow.next
                    fast = fast.next
                fast.next = None
    
    def printll(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next


llist = LinkedList()
# ll.push(1)
# ll.push(2)
# ll.push(3)
# ll.push(4)
# ll.push(5)
llist.head = Node(50)
llist.head.next = Node(20)
llist.head.next.next = Node(15)
llist.head.next.next.next = Node(4)
llist.head.next.next.next.next = Node(10)

llist.head.next.next.next.next.next = llist.head.next.next
llist.deleteLoop()
llist.printll()