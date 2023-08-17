#Deletion from a Circular Linked List.

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
        while temp != None:
            print(temp.data)
            temp= temp.next

    def deleteNode(self, key):
        temp = self.head 

        if temp is None:
            return None

        if temp.data==key and temp.next ==temp:
            return None

        if temp.data == key:
            
            while temp!=None:
                temp=temp.next

            temp.next = self.head.next

            self.head = temp.next

        while temp.next!=None and temp.next.data!=key:
            temp=temp.next

        if(temp.next.data==key):
            temp.next = temp.next.next
        else:
            print("no such keyfound")
      
ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)

ll.head.next.next.next.next = ll.head

#ll.printLL()

ll.deleteNode(30)

ll.printLL()