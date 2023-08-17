class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head

        if self.head != None:
            self.head.prev = node
        self.head = node 

    def printLL(self):
        temp = self.head

        while temp != None:
            print(temp.data)

            temp = temp.next

    def triplet(self, key):
        ptr = self.head
        ptr1 = None
        ptr2 = None
        ct = 0
        while ptr!=None:
            ptr1 = ptr.next
            while ptr1 != None:
                ptr2 = ptr1.next
                while ptr2 != None:
                    if((ptr.data + ptr1.data + ptr2.data) == key):
                        print(ptr.data,ptr1.data, ptr2.data)
                        ct += 1
                    ptr2 = ptr2.next

                ptr1 = ptr1.next
            ptr = ptr.next
        print(ct)
ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)
ll.push(50)

ll.printLL()
                
ll.triplet(60)
