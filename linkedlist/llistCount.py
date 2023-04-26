#Find Length of a Linked List Iterative 

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

    def getCount(self):
        temp = self.head
        count=0
        while(temp):
            count+=1
            temp = temp.next

        return count 


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
      
    # Function call
    print("Count of nodes is :", llist.getCount())


