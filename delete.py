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
        

    def countK(self, key):
        temp = self.head 
        ct=0
        while temp:
            if temp.data == key:
                ct+=1
            temp = temp.next
        return ct

    def delete(self, key):
        temp = self.head

        if self.head.data == key:
            self.head = self.head.next
        prev = temp
        while temp:
            if temp.data==key:
                break
            prev = temp
            temp = temp.next  

        prev.next = temp.next

    def search(self,head, key):
        temp = head 
        while temp:                
            if temp.data == key:
                return True
            temp = temp.next
        else:
            return False
        return self.search(head.next,key)



ll = LinkedList()
ll.push(10)
ll.push(2)
ll.push(4)
ll.push(2)
ll.push(2)

ll.printll()

print(ll.countK(2))

ll.delete(2)
ll.printll()
print(ll.search(ll.head, 3))
