#remove duplicate from sorted ll


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

    def removeDuplicate(self):
        temp = self.head  
        if temp is None:
            return None         
        while temp.next is not None:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp=temp.next
        return self.head

    def deleteKey(self, key):
        temp = self.head
        prev=None
        curr = temp
        while curr:
            if curr.data == key:
                break
            prev= curr
            curr = curr.next

        prev.next = curr.next

            


ll = LinkedList()
ll.push(10)
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)
ll.push(50)

ll.printll()

ll.removeDuplicate()
ll.printll()

ll.deleteKey(40)
ll.printll()