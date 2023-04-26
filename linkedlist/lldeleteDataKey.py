#Delete a Linked List node at a given position

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

    def deleteNodeAtGivenPosition(self, position):
        if self.head is None:
            return 
        index = 0
        current = self.head
        while(current.next and index<position):
            previous = current
            current  = current.next
            index+=1

        if index < position:
            print("Position is out of ll")
        elif index==0:
            self.head = self.head.next.next
        else:
            previous.next = current.next

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp=temp.next




llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)
  
print("Created Linked List: ")
llist.printList()
llist.deleteNodeAtGivenPosition(4)
print("\nLinked List after Deletion at position 4: ")
llist.printList()
        
